# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 09:37:03 2015

@author: Robert Smith
"""

from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean, create_engine
from sqlalchemy.orm import relationship, sessionmaker



## Mixins


class CodeMixin(object):

    code = Column(String(50), nullable=False, unique=True)


class NameMixin(object):

    name = Column(String(255), nullable=False)


class PathMixin(object):

    path = Column(Text, default=None, unique=True)


class DescriptionMixin(object):

    description = Column(Text, default=None)


class DomainMixin(object):

    @declared_attr
    def domain_id(cls):
        return Column('domain_id', ForeignKey('etl.domains.id'), nullable=False)

    @declared_attr
    def domain(cls):
        return relationship('Domain', primaryjoin= lambda: cls.domain_id==Domain.id, uselist=False)


class ScriptMixin(object):

    @declared_attr
    def script_id(cls):
        return Column('script_id', ForeignKey('etl.scripts.id'), nullable=False)

    @declared_attr
    def script(cls):
        return relationship('Script', primaryjoin= lambda: cls.script_id==Script.id)


class TableMixin(object):

    @declared_attr
    def table_id(cls):
        return Column('table_id', ForeignKey('etl.tables.id'), nullable=False)

    @declared_attr
    def table(cls):
        return relationship('Table', primaryjoin= lambda: cls.table_id==Table.id, uselist=False)


class FieldMixin(object):

    @declared_attr
    def field_id(cls):
        return Column('field_id', ForeignKey('etl.fields.id'), nullable=False)

    @declared_attr
    def field(cls):
        return relationship('Field', primaryjoin= lambda: cls.field_id == Field.id, uselist=False)


class TableFieldMixin(object):

    @declared_attr
    def table_field_id(cls):
        return Column('table_field_id', ForeignKey('etl.table_field.id'), nullable=False)

    @declared_attr
    def table_field(cls):
        return relationship('TableField', primaryjoin= lambda: cls.table_field_id==TableField.id, uselist=False)


class SchemaBase(object):

    __table_args__ = {'schema': 'etl'}




### Table Definitions


ETL_Base = declarative_base(name='ETL_Base', cls = SchemaBase)



class Domain(PathMixin, DescriptionMixin, CodeMixin, ETL_Base):

    __tablename__ = 'domains'

    id = Column(Integer, primary_key=True, autoincrement=True)

    def __init__(self, code, path=None, description=None):
        self.code = code
        self.path = path
        self.description = description


class Script(PathMixin, DescriptionMixin, DomainMixin, CodeMixin, ETL_Base):

    __tablename__ = 'scripts'

    id = Column(Integer, primary_key=True, autoincrement=True)

    def __init__(self, domain, code, path, description=None):
        self.domain = domain
        self.code = code
        self.path = path
        self.description = description


class Table(DescriptionMixin, NameMixin, ETL_Base):

    __tablename__ = 'tables'

    id = Column(Integer, primary_key=True, autoincrement=True)

    def __init__(self, name, description=None):
        self.name = name
        self.description = description


class Field(DescriptionMixin, NameMixin, ETL_Base):

    __tablename__ = 'fields'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sql_type = Column(String(100), nullable=False)
    size = Column(Integer, default=None)
    precision = Column(Integer, default=None)

    local_field_id = Column(Integer, ForeignKey('etl.fields.id'), default=None)
    local_field = relationship('Field', remote_side=id)

    def __init__(self, name, sql_type, size=None, precision=None, description=None):
        self.name = name
        self.sql_type = sql_type
        self.size = size
        self.precision = precision
        self.description = description

class ScriptTable(ScriptMixin, TableMixin, ETL_Base):

    __tablename__ = 'script_tables'

    id = Column(Integer, primary_key=True, autoincrement=True)
    header_ind = Column(Boolean, default=None)

    def __init__(self, script, table, header_ind=False):
        self.script = script
        self.table = table
        self.header_ind = header_ind


class TableField(DescriptionMixin, TableMixin, FieldMixin, ETL_Base):

    __tablename__ = 'table_fields'

    id = Column(Integer, primary_key=True, autoincrement=True)
    key_field = Column(Boolean, default=False)
    sequence_id = Column(Integer, default=None)

    def __init__(self, table, field, position, key_field=False, description=None):
        self.table = table
        self.field = field
        self.position = position
        self.key_field = key_field
        self.description = description


class TableAssociation(ETL_Base):

    __tablename__ = 'table_associations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    foreign_table_id = Column(Integer, ForeignKey('etl.tables.id'), nullable=False)
    local_table_id = Column(Integer, ForeignKey('etl.tables.id'), nullable=False)

    foreign_table = relationship('Table', primaryjoin= foreign_table_id==Table.id, uselist=False)
    local_table = relationship('Table', primaryjoin= local_table_id==Table.id, uselist=False)

    def __init__(self, foreign_table, local_table):
        self.foreign_table = foreign_table
        self.local_table = local_table


class FieldAssociation(ETL_Base):

    __tablename__ = 'field_associations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    foreign_field_id = Column(Integer, ForeignKey('etl.fields.id'), nullable=False)
    local_field_id = Column(Integer, ForeignKey('etl.fields.id'), nullable=False)

    foreign_field = relationship('Field', primaryjoin= foreign_field_id==Field.id, uselist=False)
    local_field = relationship('Field', primaryjoin= local_field_id==Field.id, uselist=False)

    def __init__(self, foreign_field, local_field):
        self.foreign_field = foreign_field
        self.local_field = local_field







#if __name__ == '__main__':
#    import yaml
#    import os
#    import csv
#    cfg_path = "C:/users/a421356/desktop/test.yml"
#    engine = create_engine('sqlite://')

#    engine = create_engine('postgresql+psycopg2://rws:rws@localhost:5432/central', echo=True)
#    ETL_Base.metadata.drop_all(engine)

#    ETL_Base.metadata.create_all(engine)

#    Session = sessionmaker(bind=engine)
#    session = Session()
#
#    data_root = "C:/users/a421356/python/package/etl/data/"
#
#    inputs = None
#    with open(os.path.join(data_root, 'domain.txt'), mode='r') as fl:
#        inputs = []
#        wr = csv.DictReader(fl, dialect='excel-tab')
#        for val in wr:
#            inputs.append(Domain(**val))
#        session.add_all(inputs)
#
#    inputs = None
#    with open(os.path.join(data_root, 'script.txt'), mode='r') as fl:
#        inputs = []
#        wr = csv.DictReader(fl, dialect='excel-tab')
#        for val in wr:
#            val['domain'] = session.query(Domain).filter(Domain.code == val['domain']).first()
#            inputs.append(Script(**val))
#        session.add_all(inputs)
#
#    inputs = None
#    with open(os.path.join(data_root, 'table.txt'), mode='r') as fl:
#        inputs = []
#        wr = csv.DictReader(fl, dialect='excel-tab')
#        for val in wr:
#            inputs.append(Table(**val))
#        session.add_all(inputs)
#
#    inputs = None
#    with open(os.path.join(data_root, 'field.txt'), mode='r') as fl:
#        inputs = []
#        wr = csv.DictReader(fl, dialect='excel-tab')
#        for val in wr:
#            val['size'] = int(val['size'])
#            if val['precision'] == '' or val['precision'] is None:
#                val['precision'] = None
#            else:
#                val['precision'] = int(val['precision'])
#            inputs.append(Field(**val))
#        session.add_all(inputs)
#
#    inputs = None
#    with open(os.path.join(data_root, 'table_fields.txt'), mode='r') as fl:
#        inputs = []
#        wr = csv.DictReader(fl, dialect='excel-tab')
#        for val in wr:
#            val['table'] = session.query(Table).filter(val['table'] == Table.name).first()
#            val['field'] = session.query(Field).filter(val['field'] == Field.name).first()
#            val['position'] = int(val['position'])
#            val['key_field'] = val['key_field'] == 'X'
#            inputs.append(TableField(**val))
#        session.add_all(inputs)
#
#    inputs = None
#    with open(os.path.join(data_root, 'association_table.txt'), mode='r') as fl:
#        inputs = []
#        wr = csv.DictReader(fl, dialect='excel-tab')
#        for val in wr:
#            val['foreign_table'] = session.query(Table).filter(val['foreign_table'] == Table.name).first()
#            val['local_table'] = session.query(Table).filter(val['local_table'] == Table.name).first()
#            inputs.append(TableAssociation(**val))
#        session.add_all(inputs)
#
#    inputs = None
#    with open(os.path.join(data_root, 'association_field.txt'), mode='r') as fl:
#        inputs = []
#        wr = csv.DictReader(fl, dialect='excel-tab')
#        for val in wr:
#            val['foreign_field'] = session.query(Field).filter(val['foreign_field'] == Field.name).first()
#            val['local_field'] = session.query(Field).filter(val['local_field'] == Field.name).first()
#            inputs.append(FieldAssociation(**val))
#        session.add_all(inputs)
#
#    session.commit()
#
#    session.close()


