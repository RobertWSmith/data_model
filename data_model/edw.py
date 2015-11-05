# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 10:49:47 2015

@author: Robert Smith
"""

import architect

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, synonym

from sqlalchemy import (Column, Date, Integer, Numeric, String, Text,
                        PickleType, Time, create_engine, event)

import subprocess as sp
import yaml


__all__ = ['EDW_Base',
           'Calendar', 'Material',
           'Facility', 'Customer', 'UnitsAtRisk', 'OpenDeliveryDoc',
           'OpenSalesDoc', 'DeliveryDetails', 'OrderDetails'
           ]


engine_url = 'postgresql+psycopg2://rws:rws@localhost:5432/central'
#engine_url = 'postgresql+psycopg2://rws:rws@10.76.26.161:5432/central'


class SchemaBase(object):

    __table_args__ = {'schema': 'edw'}


EDW_Base = declarative_base(name='EDW_Base', cls=SchemaBase)


class Calendar(EDW_Base):
    """\
    Sourced from GDYR_BI_VWS.GDYR_CAL
    """
    yaml_tag = "!Calendar"

    __tablename__ = 'calendar'

    day_date = Column(Date, primary_key=True)
    month_dt = Column(Date)
    ttl_days_in_mnth = Column(Integer)
    day_of_week = Column(Integer)
    day_of_week_name_abbrev = Column(String(3))
    day_of_week_name_desc = Column(String(9))
    weekday_in_month_occurence = Column(Integer)
    day_of_month = Column(Integer)
    day_of_qtr = Column(Integer)
    day_of_year = Column(Integer)
    cal_last_day_mo_ind = Column(String(1))
    cal_last_day_yr_ind = Column(String(1))
    cal_wk = Column(Integer)
    cal_mth = Column(Integer)
    cal_yr = Column(Integer)


#register yaml constructor
yaml.add_constructor('!Calendar', lambda loader, node: Calendar)


class Material(EDW_Base):
     """\
     Sourced from GDYR_BI_VWS.NAT_MATL_HIER_DESCR_EN_CURR
     """

     __tablename__ = 'materials'

     matl_id = Column(String(18), primary_key=True)
     descr = Column(String(40))
     global_part_nbr = Column(String(35))
     global_prod_grp_nbr = Column(String(4))
     global_cmnt_txt = Column(String(240))
     matl_id_trim = Column(String(18))
     matl_no_8 = Column(String(8))
     tic_cd = Column(String(10))
     tic_version_cd = Column(String(20))
     hva_txt = Column(String(3))
     hmc_txt = Column(String(3))
     sal_ind = Column(String(1))
     pal_ind = Column(String(1))
     matl_prty = Column(String(2))
     ext_matl_grp_id = Column(String(18))
     stk_class_id = Column(String(2))
     stk_class_dt = Column(Date)
     matl_sta_id = Column(String(2))
     matl_sta_dt = Column(Date)
     tire_sz_text = Column(String(40))
     brand_id = Column(String(3))
     brand_name = Column(String(20))
     assoc_brand_id = Column(String(3))
     assoc_brand_name = Column(String(20))
     super_brand_id = Column(String(3))
     super_brand_name = Column(String(20))
     pbu_nbr = Column(String(2))
     pbu_name = Column(String(50))
     mkt_area_nbr = Column(String(2))
     mkt_area_name = Column(String(50))
     mkt_grp_nbr = Column(String(4))
     mkt_grp_name = Column(String(50))
     prod_grp_nbr = Column(String(4))
     prod_grp_name = Column(String(50))
     prod_line_nbr = Column(String(6))
     prod_line_name = Column(String(50))
     mkt_ctgy_mkt_area_nbr = Column(String(2))
     mkt_ctgy_mkt_area_name = Column(String(50))
     mkt_ctgy_mkt_grp_nbr = Column(String(4))
     mkt_ctgy_mkt_grp_name = Column(String(50))
     mkt_ctgy_prod_grp_nbr = Column(String(4))
     mkt_ctgy_prod_grp_name = Column(String(50))
     mkt_ctgy_prod_line_nbr = Column(String(6))
     mkt_ctgy_prod_line_name = Column(String(50))
     vol_meas_id = Column(String(3))
     unit_vol = Column(Numeric(15,3,3))
     compression_ratio = Column(Numeric(15,3,3))
     unit_compressed_vol = Column(Numeric(15,3,3))
     wt_meas_id = Column(String(3))
     unit_wt = Column(Numeric(15,3,3))
     base_uom = Column(String(3))
     tier = Column(String(40))
     prty_src_facl_id = Column(String(4))
     prty_src_facl_nm = Column(String(40))


#register yaml constructor
yaml.add_constructor('!Material', lambda loader, node: Material)


class Facility(EDW_Base):
    """\
    Sourced from GDYR_BI_VWS.NAT_FACILITY_EN_CURR
    """

    __tablename__ = 'facilities'

    facility_id = Column(String(4), primary_key=True)
    facility_name = Column(String(40))
    val_area_id = Column(String(4))
    int_cust_id = Column(String(10))
    vendor_cust_id = Column(String(10))
    purch_org_id = Column(String(18))
    sales_org_cd = Column(String(4))
    distr_chan_cd = Column(String(2))
    div_cd = Column(String(2))
    cntry_id = Column(String(3))
    terr_id = Column(String(3))
    district_id = Column(String(35))
    city_id = Column(String(35))


#register yaml constructor
yaml.add_constructor('!Facility', lambda loader, node: Facility)



class Customer(EDW_Base):
    """\
    Sourced from GDYR_BI_VWS.NAT_CUST_HIER_DESCR_EN_CURR
    """

    __tablename__ = 'customers'

    ship_to_cust_id = Column(String(10), primary_key=True)
    cust_name = Column(String(35))
    own_cust_id = Column(String(10))
    own_cust_name = Column(String(35))
    co_cd = Column(String(4))
    co_desc = Column(String(25))
    sales_org_cd = Column(String(4))
    sales_org_name = Column(String(20))
    distr_chan_cd = Column(String(2))
    distr_chan_name = Column(String(20))
    div_cd = Column(String(2))
    cust_grp_id = Column(String(2))
    cust_grp_name = Column(String(20))
    prim_ship_facility_id = Column(String(4))
    deliv_prty_cd = Column(String(2))
    ship_cond_id = Column(String(2))
    cust_grp2_cd = Column(String(3))
    cntry_name_cd = Column(String(3))
    terr_name = Column(String(35))
    district_name = Column(String(35))
    city_name = Column(String(35))
    postal_cd = Column(String(10))
    oe_repl_ind = Column(String(1))
    oe_repl_desc = Column(String(25))

    cust_id = synonym('ship_to_cust_id')


#register yaml constructor
yaml.add_constructor('!Customer', lambda loader, node: Customer)


@architect.install('partition', type='range', subtype='date', constraint='month', column='snapshot_dt', db=engine_url)
class UnitsAtRisk(EDW_Base):
    """\
    Sourced from queries agsinst NA_BI_VWS.ORDER_DETAIL,
    NA_BI_VWS.OPEN_ORDER_SCHDLN, NA_BI_VWS.ORDER_DETAIL_CURR,
    NA_BI_VWS.OPEN_ORDER_SCHDLN_CURR, NA_BI_VWS.DELIVERY_DETIAL_CURR

    Shows open confirmed qty by snapshot date, and shipped units as a comparison.
    """

    __tablename__ = 'units_at_risk'

    snapshot_dt = Column(Date, primary_key=True)
    sold_to_cust_id = Column(String(10), primary_key=True)
    snap_facility_id = Column(String(4), primary_key=True)
    curr_facility_id = Column(String(4), primary_key=True)
    matl_id = Column(String(18), primary_key=True)
    snap_itm_deliv_blk_cd = Column(String(2), primary_key=True)
    qty_unit_meas_id = Column(String(3), primary_key=True)

    snap_order_qty = Column(Numeric(15,3,3))
    curr_order_qty = Column(Numeric(15,3,3))
    snap_cm_working_open_cnfrm_qty = Column(Numeric(15,3,3))
    snap_fm_open_cnfrm_qty = Column(Numeric(15,3,3))
    snap_uncnfrm_qty = Column(Numeric(15,3,3))
    snap_wait_list_qty = Column(Numeric(15,3,3))
    curr_cm_working_open_cnfrm_qty = Column(Numeric(15,3,3))
    curr_fm_open_cnfrm_qty = Column(Numeric(15,3,3))
    curr_uncnfrm_qty = Column(Numeric(15,3,3))
    curr_wait_list_qty = Column(Numeric(15,3,3))
    tot_dn_qty = Column(Numeric(15,3,3))
    cancel_qty = Column(Numeric(15,3,3))
    curr_in_proc_qty = Column(Numeric(15,3,3))
    agid_in_mnth_qty = Column(Numeric(15,3,3))

    material = relationship(Material, primaryjoin= matl_id==Material.matl_id, uselist=False)
    snapshot_facility = relationship(Facility, primaryjoin= snap_facility_id==Facility.facility_id, uselist=False)
    current_facility = relationship(Facility, primaryjoin= curr_facility_id==Facility.facility_id, uselist=False)
    customer = relationship(Customer, primaryjoin= sold_to_cust_id==Customer.cust_id, uselist=False)
    calendar = relationship(Calendar, primaryjoin= snapshot_dt==Calendar.day_date, uselist=False)

    cust_id = synonym('sold_to_cust_id')


@event.listens_for(UnitsAtRisk.__table__, "before_drop")
def drop_units_at_risk_child_tables(target, connection, **kw):
    """
    Look up all triggers, functions and partitioned sub-tables of `edw.units_at_risk`
    and drop each in order to ensure a clean removal.
    """
    schema = UnitsAtRisk.__table_args__.get('schema')
    tablename = UnitsAtRisk.__tablename__
    like_partition_table = ''.join((tablename, '_y%%'))
    like_tablename = ''.join(('%%', tablename, '%%'))

    triggers = connection.execute("""
        select
            trigger_name
        from information_schema.triggers
        where
            trigger_catalog = 'central'
            and trigger_schema = '{schema}'
            and trigger_name like '{like_tablename}'
    """.format(schema=schema, like_tablename=like_partition_table))

    for val in triggers:
        trigger_name = val[0]
        trigger_sql_str = "DROP TRIGGER IF EXISTS {trigger_name} ON {schema}.{tablename} CASCADE".format(trigger_name=trigger_name, schema=schema, tablename=tablename)
        trans = connection.begin()
        connection.execute(trigger_sql_str)
        trans.commit()

    functions = connection.execute("""
        select
            routine_schema as schema
            , routine_name as routine_name
        from information_schema.routines
        where
            routine_catalog = 'central'
            and routine_schema = '{schema}'
            and routine_name like '{like_tablename}'
            """.format(schema=schema, like_tablename=like_tablename))

    for val in functions:
        function_name = val[1]
        function_sql_str = "DROP FUNCTION IF EXISTS {function_name}() CASCADE".format(function_name=function_name)
        trans = connection.begin()
        connection.execute(function_sql_str)
        trans.commit()

    tbls = connection.execute("""
        select
            table_schema as schema
            , table_name as table_name
        from information_schema.tables
        where
            table_catalog = 'central'
            and table_type = 'BASE TABLE'
            and table_schema = '{schema}'
            and table_name like '{like_tablename}'
            and table_name <> '{tablename}'
        """.format(schema=schema, like_tablename=like_partition_table, tablename=tablename))

    for val in tbls:
        child_tablename = val[1]
        sql_str = "DROP TABLE IF EXISTS {schema}.{tablename}".format(schema=schema, tablename=child_tablename)
        trans = connection.begin()
        connection.execute(sql_str)
        trans.commit()


#register yaml constructor
yaml.add_constructor('!UnitsAtRisk', lambda loader, node: UnitsAtRisk)


class UnitsAtRiskModel(EDW_Base):
    """\
    Stores pickled linear models based on UnitsAtRisk
    """

    __tablename__  = 'units_at_risk_models'

    id = Column(Integer, primary_key=True)
    begin_date = Column(Date)
    end_date = Column(Date)
    cust_id = Column(String(10))
    matl_id = Column(String(18))
    formula = Column(Text)
    model = Column(PickleType)


#register yaml constructor
yaml.add_constructor('!UnitsAtRiskModel', lambda loader, node: UnitsAtRiskModel)


class OpenDeliveryDoc(EDW_Base):
    """\
    Stores data from 'order book' query.
    """

    __tablename__ = 'delivery_doc_open'

    deliv_fiscal_yr = Column(String(4), primary_key=True)
    deliv_id = Column(String(10), primary_key=True)
    deliv_line_nbr = Column(Integer, primary_key=True)

    order_fiscal_yr = Column(String(4))
    order_id = Column(String(10))
    order_line_nbr = Column(Integer)

    intra_cmpny_flg = Column(String(1))
    sls_qty_unit_meas_id = Column(String(3))
    qty_to_ship = Column(Numeric(15,3,3))
    rpt_qty_unit_meas_id = Column(String(3))
    rpt_qty_to_ship = Column(Numeric(15,3,3))


#register yaml constructor
yaml.add_constructor('!OpenDeliveryDoc', lambda loader, node: OpenDeliveryDoc)


class OpenSalesDoc(EDW_Base):

    __tablename__ = 'sales_doc_open'

    order_fiscal_yr = Column(String(4), primary_key=True)
    order_id = Column(String(10), primary_key=True)
    order_line_nbr = Column(Integer, primary_key=True)
    sched_line_nbr = Column(Integer, primary_key=True)
    status_cd = Column(String(1), primary_key=True)

    sls_qty_unit_meas_id = Column(String(3))
    open_qty = Column(Numeric(15,3,3))

    order_cat_id = Column(String(1))
    order_type_id = Column(String(4))
    pln_goods_iss_dt = Column(Date)
    pln_deliv_dt = Column(Date)
    ship_to_cust_id = Column(String(10))
    matl_id = Column(String(18))
    facility_id = Column(String(4))


#register yaml constructor
yaml.add_constructor('!OpenSalesDoc', lambda loader, node: OpenSalesDoc)


class DeliveryDetails(EDW_Base):
    """\
    Stores data from `na_bi_vws.delivery_detail_curr` view.
    """

    __tablename__ = 'delivery_details'

    deliv_fiscal_yr = Column(String(4), primary_key=True)
    deliv_id = Column(String(10), primary_key=True)
    deliv_line_nbr = Column(Integer, primary_key=True)

    bill_lading_id = Column(String(35))
    goods_iss_ind = Column(String(1))
    outbound_deliv_ind = Column(String(1))

    orig_deliv_line_nbr = Column(Integer)
    rtg_id = Column(String(6))
    terms_id = Column(String(3))
    unld_pt_cd = Column(String(25))
    spcl_proc_id = Column(String(4))

    order_fiscal_yr = Column(String(4))
    order_id = Column(String(10))
    order_line_nbr = Column(Integer)
    sd_doc_ctgy_cd = Column(String(1))

    sales_org_cd = Column(String(4))
    distr_chan_Cd = Column(String(2))
    cust_grp_id = Column(String(2))
    sold_to_cust_id = Column(String(10))
    ship_to_cust_id = Column(String(10))
    bill_to_cust_id = Column(String(10))
    payor_cust_id = Column(String(10))

    deliv_prty_id = Column(String(2))
    ship_cond_id = Column(String(2))
    cust_grp2_cd = Column(String(3))

    facility_id = Column(String(4))
    deliv_line_facility_id = Column(String(4))
    ship_pt_id = Column(String(4))

    deliv_note_crea_dt = Column(Date)
    deliv_line_crea_dt = Column(Date)
    pln_goods_mvt_dt = Column(Date)
    actl_goods_iss_dt = Column(Date)
    deliv_dt = Column(Date)

    deliv_type_id = Column(String(4))
    deliv_cat_id = Column(String(1))
    item_cat_id = Column(String(4))

    matl_id = Column(String(18))
    cust_part_nbr = Column(String(35))
    batch_nbr = Column(String(10))

    qty_unit_meas_id = Column(String(3))
    deliv_qty = Column(Numeric(15,3,3))
    rpt_qty_unit_meas_id = Column(String(3))
    rpt_deliv_qty = Column(Numeric(15,3,3))
    vol_unit_meas_id = Column(String(3))
    vol = Column(Numeric(15,3,3))
    wt_unit_meas_id = Column(String(3))
    gross_wt = Column(Numeric(15,3,3))
    net_wt = Column(Numeric(15,3,3))

    src_crt_usr_id = Column(String(8))
    deliv_blk_cd = Column(String(2))
    goods_rcpt_post_dt = Column(Date)


#register yaml constructor
yaml.add_constructor('!DeliveryDetails', lambda loader, node: DeliveryDetails)


class OrderDetails(EDW_Base):
    """
    sourced from 'na_bi_vws.order_detail_curr'
    """

    __tablename__ = 'order_details'

    order_fiscal_yr = Column(String(4), primary_key=True)
    order_id = Column(String(10), primary_key=True)
    order_line_nbr = Column(Integer, primary_key=True)
    sched_line_nbr = Column(Integer, primary_key=True)

    orig_order_line_nbr = Column(Integer)

    order_cat_id = Column(String(1))
    order_type_id = Column(String(4))
    item_cat_id = Column(String(4))
    schd_ln_ctgy_cd = Column(String(2))

    cust_po_nbr = Column(String(20))
    cust_po_itm_nbr = Column(String(6))
    po_type_id = Column(String(4))
    ro_po_type_ind = Column(String(1))

    cancel_dt = Column(Date)
    rej_reas_id = Column(String(2))
    rej_reas_desc = Column(String(40))

    co_cd = Column(String(4))
    sales_org_cd = Column(String(4))
    distr_chan_cd = Column(String(2))
    cust_grp_id = Column(String(2))
    sold_to_cust_id = Column(String(10))
    ship_to_cust_id = Column(String(10))
    bill_to_cust_id = Column(String(10))
    payor_cust_id = Column(String(10))

    cust_grp2_cd = Column(String(3))
    ship_cond_id = Column(String(2))
    route_id = Column(String(6))
    deliv_grp_cd = Column(String(3))

    deliv_prty_id = Column(String(2))
    order_reas_cd = Column(String(3))
    spcl_proc_id = Column(String(4))
    wait_list_cd = Column(String(1))
    cancel_ind = Column(String(1))
    return_ind = Column(String(1))

    deliv_blk_ind = Column(String(1))
    deliv_blk_cd = Column(String(2))
    deliv_blk_desc = Column(String(20))
    order_deliv_blk_cd = Column(String(2))
    order_deliv_blk_desc = Column(String(20))

    facility_id = Column(String(4))
    ship_pt_id = Column(String(4))

    matl_id = Column(String(18))
    cust_part_nbr = Column(String(35))
    batch_nbr = Column(String(10))
    prod_allct_determ_proc_id = Column(String(18))
    avail_chk_grp_cd = Column(String(3))

    order_dt = Column(Date)
    order_crt_tm = Column(Time)
    order_ln_crt_dt = Column(Date)
    order_ln_crt_tm = Column(Time)
    pln_matl_avl_dt = Column(Date)
    pln_load_dt = Column(Date)
    pln_goods_iss_dt = Column(Date)
    pln_deliv_dt = Column(Date)
    fnl_accept_dt = Column(Date)
    cust_rdd = Column(Date)
    frst_matl_avl_dt = Column(Date)
    frst_pln_goods_iss_dt = Column(Date)
    frst_rdd = Column(Date)
    fc_matl_avl_dt = Column(Date)
    fc_pln_goods_iss_dt = Column(Date)
    frst_prom_deliv_dt = Column(Date)

    prc_dt = Column(Date)
    crncy_id = Column(String(3))
    price = Column(Numeric(14,2,2))
    grp_crncy_id = Column(String(3))
    price_grp_amt = Column(Numeric(14,2,2))

    qty_unit_meas_id = Column(String(3))
    src_ord_qty = Column(Numeric(15,3,3))
    order_qty = Column(Numeric(15,3,3))
    cnfrm_qty = Column(Numeric(15,3,3))
    sls_qty_unit_meas_id = Column(String(3))
    sls_order_qty = Column(Numeric(15,3,3))
    rpt_qty_unit_meas_id = Column(String(3))
    rpt_order_qty = Column(Numeric(15,3,3))
    rpt_cnfrm_qty = Column(Numeric(15,3,3))
    wt_unit_meas_id = Column(String(3))
    gross_wt = Column(Numeric(15,3,3))
    net_wt = Column(Numeric(15,3,3))
    vol_unit_meas_id = Column(String(3))
    vol = Column(Numeric(15,3,3))

    order_creator = Column(String(12))


#register yaml constructor
yaml.add_constructor('!OrderDetails', lambda loader, node: OrderDetails)



class TruckloadMaster(EDW_Base):
    """\
    sourced from 'na_bi_vws.tl_mstr_curr'
    """

    __tablename__ = 'truckload_master'

    cust_id = Column(String(10))
    deliv_grp_cd = Column(String(3), primary_key=True)
    fiscal_yr = Column(String(4), primary_key=True)
    sls_doc_id = Column(String(10), primary_key=True)
    sls_doc_itm_id = Column(Integer, primary_key=True)
    facility_id = Column(String(4))
    ship_rcve_pt_cd = Column(String(4))
    matl_id = Column(String(18))
    itm_qty = Column(Numeric(15,3,3))
    deliv_dt = Column(Date)
    matl_avl_dt = Column(Date)
    gross_wt_qty = Column(Numeric(15,3,3))
    vol_qty = Column(Numeric(15,3,3))
    tl_pln_cd = Column(String(1))
    acctng_doc_create_dt = Column(Date)
    acctng_doc_create_tm = Column(Time)
    src_crt_usr_id = Column(String(12))
    sap_trans_cd = Column(String(20))


#register yaml constructor
yaml.add_constructor('!TruckloadMaster', lambda loader, node: TruckloadMaster)



class TruckloadCapacity(EDW_Base):
    """\
    sourced from 'na_bi_vws.tl_cap_deliv_schd_curr'
    """

    __tablename__ = 'truckload_capacity'

    cust_id = Column(String(10), primary_key=True)
    deliv_dt = Column(Date, primary_key=True)
    tl_seq_id = Column(Integer, primary_key=True)
    deliv_grp_cd = Column(String(3))
    trlr_typ_id = Column(String(3))
    min_wt_qty = Column(Numeric(15,3,3))
    tl_pln_cd = Column(String(1))
    rpt_tl_seq_id = Column(Integer)


#register yaml constructor
yaml.add_constructor('!TruckloadCapacity', lambda loader, node: TruckloadCapacity)


class TrailerType(EDW_Base):
    """
    sourced from 'na_bi_vws.order_detail_curr'
    """

    __tablename__ = 'trailer_type'

    trlr_typ_id = Column(String(3), primary_key=True)
    trlr_type_desc = Column(String(40))
    min_wt_qty = Column(Numeric(18,3,3))
    max_wt_qty = Column(Numeric(18,3,3))
    vol_qty = Column(Numeric(18,3,3))


#register yaml constructor
yaml.add_constructor('!TrailerType', lambda loader, node: TrailerType)



def drop_all(engine):
    EDW_Base.metadata.drop_all(engine)

def create_all(engine):
    EDW_Base.metadata.create_all(engine)

def partition():
    output = sp.call(['architect', 'partition', '--module', 'data_model.edw'])
    return output

def rebuild(engine_url, drop_all_ind=False):
    eng = create_engine(engine_url, echo=True)
    if drop_all:
        drop_all(eng)
    create_all(eng)
    partition()


if __name__ == '__main__':
    rebuild(engine_url, drop_all_ind=True)
#    eng = create_engine(engine_url, echo=True)
#    drop_all(eng)

