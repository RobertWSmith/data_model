# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 21:55:04 2015

@author: Robert Smith
"""

from os.path import dirname, join, normpath, split, splitext
#import datetime
#import yaml
#from db_utils import Access
#from sqlalchemy import create_engine
#import sqlalchemy_access

#import pyodbc

basepath = normpath(dirname(__file__))
config_name = '.'.join((splitext(split(__file__)[1])[0], 'yml'))

config_path = normpath(join(basepath, 'config'))
schema_path = normpath(join(basepath, "etl/schema"))

db = normpath("C:/Users/A421356/WinShuttle/Query/Results/WinshuttleOutput.accdb")
#a = Access(db)

config_file = normpath(join(config_path, config_name))


sql = {
    'tables': """
SELECT
    SAP_Tablename as sap_table_name
    , SAP_Description as sap_table_description
    , Synonym as table_synonym

FROM Tbl_SAP_Table_Synonyms

ORDER BY
    SAP_Tablename
""",
    'TableField': """\
SELECT
    DD03M.TABNAME AS sap_table_name
    , DD03M.FIELDNAME AS sap_field_name
    , DD03M.DOMNAME AS sap_domain
    , DD03M.FIELD_POSITION AS field_position
    , DD03M.CHECKTABLE AS check_table
    , DD03M.KEYFLAG AS key_ind
    , DD03M.MANDATORY AS mandatory_ind
    , DD03L.NOTNULL AS not_null_ind
    , DD03M.DATATYPE AS data_type
    , DD03M.LENG AS length
    , DD03M.DECIMALS AS decimals
    , Tbl_SAP_Field_Synonyms.SYNONYM AS sap_field_synonym
    , Tbl_SAP_Field_Synonyms.SAP_Type AS sap_type
    , Tbl_SAP_Field_Synonyms.SAP_Length AS sap_length
    , Tbl_SAP_Field_Synonyms.SAP_Decimals AS sap_decimals
    , DD03M.DDTEXT AS sap_table_field_desc
FROM (
    DD03M
INNER JOIN DD03L
    ON (DD03M.FIELDNAME = DD03L.FIELDNAME)
        AND (DD03M.TABNAME = DD03L.TABNAME)
    )
LEFT JOIN Tbl_SAP_Field_Synonyms
        ON (DD03M.FIELDNAME = Tbl_SAP_Field_Synonyms.SAP_Field)
WHERE
    DD03M.TABNAME = ?

ORDER BY
    DD03M.FIELD_POSITION;
"""
}


def data_type_str(**row):
    if row.get('sap_domain', '') in ('XFELD', 'X'):
        return 'Boolean'
    elif row.get('sap_type', '') in ('SSTRING', 'STRING'):
        return 'Text'
    elif row.get('sap_type', '') == 'DATS':
        return "Date"
    elif row.get('sap_type', '') == 'TIMS':
        return "Time"
    elif row.get('sap_type', '') in ('QUAN', 'DEC', 'CURR'):
        return 'Numeric(15,3,3)'
    elif row.get('sap_type', '') == 'FLTP':
        return 'Float'
    elif row.get('sap_type', '') in ('INT1', 'INT2', 'INT4'):
        return 'Integer'
    else:
        return 'String(' + str(int(row.get('length'))) + ')'

def primary_key_str(**row):
    if row.get('key_ind') == 'X':
        return 'primary_key = True'
    else:
        return 'default=None'

def doc_str(**row):
    table_field = '-'.join([row.get('sap_table_name', ''), row.get('sap_field_name', '')])
    desc = row.get('sap_table_field_desc')
    fmt = '''doc="""Sourced from {0}'''.format(table_field)
    if desc is not None:
        descr = " // {0}".format(str(desc).replace('"', "'"))
    else:
        descr = ""
    return fmt + descr + '"""'


def field_str(**row):
    if data_type_str(**row) is None:
        return None

    fmt_dict = {
        'sap_field_name': row.get('sap_field_name'),
        'data_type': data_type_str(**row),
        'kwargs': ', '.join([primary_key_str(**row), doc_str(**row)])
        }

    # pass on fields that have certain key characters in the field name
    for val in ('/', '.'):
        if fmt_dict['sap_field_name'].count(val) > 0:
            return None

    output_fmt = """    {sap_field_name} = Column('{sap_field_name}', {data_type}, {kwargs})"""

    return output_fmt.format(**fmt_dict)

def synonym_str(**row):
    if row.get('sap_field_synonym') is not None:
        return "    {0} = synonym('{1}')".format(row.get('sap_field_synonym'), row.get('sap_field_name'))
    else:
        return None


def table_str(**row):
    output_fmt = """

################################################################################

class {table_synonym}(SAP_Base):
    \"\"\"\\
    Table sourced from: {sap_table_name}
    Description: {sap_table_description}
    \"\"\"

    __tablename__ = "{sap_table_name}"

{fields}

{synonyms}


################################################################################

"""
    fmt_dict = {
        'table_synonym': row.get('table_synonym'),
        'sap_table_name': row.get('sap_table_name'),
        'sap_table_description': row.get('sap_table_description'),
        'fields': '\n'.join([f for f in row.get('fields')]),
        'synonyms': '\n'.join([s for s in row.get('synonyms')])
        }
    return output_fmt.format(**fmt_dict)


def file_str(tables):
    import datetime
    output_fmt = '''
__doc__ = \"\"\"
file generated: {timestamp}
\"\"\"

from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, Numeric, Text, Time, Float
from sqlalchemy.orm import relationship, synonym
#from .custom_type import CoerceDate, CoerceTime, CoerceBoolean, CoerceNumeric, CoerceInteger

class SchemaBase(object):

    @declared_attr
    def __table_args__(cls):
        return {{'schema': '{schema}'}}

SAP_Base = declarative_base(name="SAP_Base", cls=SchemaBase)


### Begin table definitions

{table_defs}


if __name__ == '__main__':
    engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/central', echo=True)

#    SAP_Base.metadata.drop_all(engine)
    SAP_Base.metadata.create_all(engine)


'''
    fmt_dict = {
        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'schema': 'sap',
        'table_defs': '\n'.join([table_str(**t) for t in tables])
    }
    return output_fmt.format(**fmt_dict)





if __name__ == "__main__":
    import pyodbc

    a = pyodbc.connect(dbq=db, driver="Microsoft Access Driver (*.mdb, *.accdb)")
    final_output = {}
    table_classes  = []
    tables = []

    with a.cursor().execute(sql['tables']) as tables_qry:
        tbl = None
        keys = tuple((v[0] for v in tables_qry.description))

        for val in tables_qry:
            vals = dict(zip(keys, val))
            vals['fields'] = []
            vals['synonyms'] = []
            table_classes.append(vals)

    for val in table_classes:
        crsr = a.cursor()
        with crsr.execute(sql['TableField'], val['sap_table_name']) as table_field_qry:
            keys = tuple((v[0] for v in table_field_qry.description))
            for row in table_field_qry:
                vals = dict(zip(keys, row))

                fs = field_str(**vals)
                if fs is not None:
                    val['fields'].append(fs)
                    ss = synonym_str(**vals)
                    if ss is not None:
                        val['synonyms'].append(ss)


    for val in table_classes:
        print(table_str(**val))

    with open(normpath(join(schema_path, 'sap.py')), mode='w', newline='') as fl:
        fl.write(file_str(table_classes))






