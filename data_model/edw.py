# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 10:49:47 2015

@author: Robert Smith
"""


from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, Date, Integer, Numeric, Boolean, String
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, synonym

import yaml


class SchemaBase(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __table_args__ = {'schema': 'edw'}


EDW_Base = declarative_base(name='EDW_Base', cls=SchemaBase)


class Calendar(EDW_Base):
    """\
    Sourced from GDYR_BI_VWS.GDYR_CAL
    """
    yaml_tag = "!Calendar"

    __tablename__ = 'calendar'

    day_date = Column(Date, primary_key=True)
    month_dt = Column(Date, index=True)
    ttl_days_in_mnth = Column(Integer)
    day_of_week = Column(Integer)
    day_of_week_name_abbrev = Column(String(3))
    day_of_week_name_desc = Column(String(9))
    weekday_in_month_occurence = Column(Integer)
    day_of_month = Column(Integer)
    day_of_qtr = Column(Integer)
    day_of_year = Column(Integer)
    cal_last_day_mo_ind = Column(Boolean)
    cal_last_day_yr_ind = Column(Boolean)
    cal_wk = Column(Integer)
    cal_mth = Column(Integer)
    cal_yr = Column(Integer)


#register yaml constructor
yaml.add_constructor('!CalendarTable', lambda loader, node: Calendar)


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
     sal_ind = Column(Boolean)
     pal_ind = Column(Boolean)
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
     pbu_nbr = Column(String(2), index=True)
     pbu_name = Column(String(50))
     mkt_area_nbr = Column(String(2), index=True)
     mkt_area_name = Column(String(50))
     mkt_grp_nbr = Column(String(4), index=True)
     mkt_grp_name = Column(String(50))
     prod_grp_nbr = Column(String(4))
     prod_grp_name = Column(String(50))
     prod_line_nbr = Column(String(6), index=True)
     prod_line_name = Column(String(50))
     mkt_ctgy_mkt_area_nbr = Column(String(2), index=True)
     mkt_ctgy_mkt_area_name = Column(String(50))
     mkt_ctgy_mkt_grp_nbr = Column(String(4))
     mkt_ctgy_mkt_grp_name = Column(String(50))
     mkt_ctgy_prod_grp_nbr = Column(String(4))
     mkt_ctgy_prod_grp_name = Column(String(50))
     mkt_ctgy_prod_line_nbr = Column(String(6), index=True)
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
yaml.add_constructor('!MaterialTable', lambda loader, node: Material)


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
    purch_org_id = Column(String(4))
    sales_org_cd = Column(String(4), index=True)
    distr_chan_cd = Column(String(2), index=True)
    div_cd = Column(String(2))
    cntry_id = Column(String(3))
    terr_id = Column(String(3))
    district_id = Column(String(35))
    city_id = Column(String(35))


#register yaml constructor
yaml.add_constructor('!FacilityTable', lambda loader, node: Facility)



class Customer(EDW_Base):
    """\
    Sourced from GDYR_BI_VWS.NAT_CUST_HIER_DESCR_EN_CURR
    """

    __tablename__ = 'customers'

    ship_to_cust_id = Column(String(10), primary_key=True)
    cust_name = Column(String(35))
    own_cust_id = Column(String(10), index=True)
    own_cust_name = Column(String(35))
    co_cd = Column(String(4), index=True)
    co_desc = Column(String(25))
    sales_org_cd = Column(String(4), index=True)
    sales_org_name = Column(String(20))
    distr_chan_cd = Column(String(2), index=True)
    distr_chan_name = Column(String(20))
    div_cd = Column(String(2))
    cust_grp_id = Column(String(2), index=True)
    cust_grp_name = Column(String(20))
    prim_ship_facility_id = Column(String(4), index=True)
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
yaml.add_constructor('!CustomerTable', lambda loader, node: Customer)


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


#register yaml constructor
yaml.add_constructor('!UnitsAtRiskTable', lambda loader, node: UnitsAtRisk)



__all__ = ['EDW_Base', 'Calendar', 'Material', 'Facility', 'Customer', 'UnitsAtRisk']


if __name__ == '__main__':
    eng_url = 'postgresql+psycopg2://rws:rws@10.76.26.161:5432/central'
    eng = create_engine(eng_url, echo=True)
    EDW_Base.metadata.create_all(eng)


