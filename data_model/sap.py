
__doc__ = """
file generated: 2015-08-31 17:09:12
"""

from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, Numeric, Text, Time, Float
from sqlalchemy.orm import relationship, synonym
#from .custom_type import CoerceDate, CoerceTime, CoerceBoolean, CoerceNumeric, CoerceInteger

class SchemaBase(object):

    @declared_attr
    def __table_args__(cls):
        return {'schema': 'sap'}

SAP_Base = declarative_base(name="SAP_Base", cls=SchemaBase)


### Begin table definitions



################################################################################

class ChangeHdr(SAP_Base):
    """\
    Table sourced from: CDHDR
    Description: Change document header
    """

    __tablename__ = "CDHDR"

    OBJECTCLAS = Column('OBJECTCLAS', String(15), primary_key = True, doc="""Sourced from CDHDR-OBJECTCLAS // Object class""")
    OBJECTID = Column('OBJECTID', String(90), primary_key = True, doc="""Sourced from CDHDR-OBJECTID // Object value""")
    CHANGENR = Column('CHANGENR', String(10), primary_key = True, doc="""Sourced from CDHDR-CHANGENR // Document change number""")
    USERNAME = Column('USERNAME', String(12), default=None, doc="""Sourced from CDHDR-USERNAME // User name of the person responsible in change document""")
    UDATE = Column('UDATE', String(8), default=None, doc="""Sourced from CDHDR-UDATE // Creation date of the change document""")
    UTIME = Column('UTIME', String(6), default=None, doc="""Sourced from CDHDR-UTIME // Time changed""")
    TCODE = Column('TCODE', String(20), default=None, doc="""Sourced from CDHDR-TCODE // Transaction in which a change was made""")
    PLANCHNGNR = Column('PLANCHNGNR', String(12), default=None, doc="""Sourced from CDHDR-PLANCHNGNR // Planned change number""")
    ACT_CHNGNO = Column('ACT_CHNGNO', String(10), default=None, doc="""Sourced from CDHDR-ACT_CHNGNO // Change number of the document created by this change""")
    WAS_PLANND = Column('WAS_PLANND', String(1), default=None, doc="""Sourced from CDHDR-WAS_PLANND // Flag that changes were generated from planned changes""")
    CHANGE_IND = Column('CHANGE_IND', String(1), default=None, doc="""Sourced from CDHDR-CHANGE_IND // Application object change type (U, I, E, D)""")
    LANGU = Column('LANGU', String(1), default=None, doc="""Sourced from CDHDR-LANGU // Language Key""")
    VERSION = Column('VERSION', String(3), default=None, doc="""Sourced from CDHDR-VERSION // 3-Byte field""")




################################################################################




################################################################################

class ChangeItem(SAP_Base):
    """\
    Table sourced from: CDPOS
    Description: Change document items
    """

    __tablename__ = "CDPOS"

    OBJECTCLAS = Column('OBJECTCLAS', String(15), primary_key = True, doc="""Sourced from CDPOS-OBJECTCLAS // Object class""")
    OBJECTID = Column('OBJECTID', String(90), primary_key = True, doc="""Sourced from CDPOS-OBJECTID // Object value""")
    CHANGENR = Column('CHANGENR', String(10), primary_key = True, doc="""Sourced from CDPOS-CHANGENR // Document change number""")
    TABNAME = Column('TABNAME', String(30), primary_key = True, doc="""Sourced from CDPOS-TABNAME // Table Name""")
    TABKEY = Column('TABKEY', String(70), primary_key = True, doc="""Sourced from CDPOS-TABKEY // Changed table record key""")
    FNAME = Column('FNAME', String(30), primary_key = True, doc="""Sourced from CDPOS-FNAME // Field Name""")
    CHNGIND = Column('CHNGIND', String(1), primary_key = True, doc="""Sourced from CDPOS-CHNGIND // Change Type (U, I, S, D)""")
    TEXT_CASE = Column('TEXT_CASE', Boolean, default=None, doc="""Sourced from CDPOS-TEXT_CASE // Flag: X=Text change""")
    UNIT_OLD = Column('UNIT_OLD', String(3), default=None, doc="""Sourced from CDPOS-UNIT_OLD // Change documents, unit referenced""")
    UNIT_NEW = Column('UNIT_NEW', String(3), default=None, doc="""Sourced from CDPOS-UNIT_NEW // Change documents, unit referenced""")
    CUKY_OLD = Column('CUKY_OLD', String(5), default=None, doc="""Sourced from CDPOS-CUKY_OLD // Change documents, referenced currency""")
    CUKY_NEW = Column('CUKY_NEW', String(5), default=None, doc="""Sourced from CDPOS-CUKY_NEW // Change documents, referenced currency""")
    VALUE_NEW = Column('VALUE_NEW', String(254), default=None, doc="""Sourced from CDPOS-VALUE_NEW // New contents of changed field""")
    VALUE_OLD = Column('VALUE_OLD', String(254), default=None, doc="""Sourced from CDPOS-VALUE_OLD // Old contents of changed field""")




################################################################################




################################################################################

class PurchReq(SAP_Base):
    """\
    Table sourced from: EBAN
    Description: Purchase Requisition
    """

    __tablename__ = "EBAN"

    BANFN = Column('BANFN', String(10), primary_key = True, doc="""Sourced from EBAN-BANFN // Purchase Requisition Number""")
    BNFPO = Column('BNFPO', String(5), primary_key = True, doc="""Sourced from EBAN-BNFPO // Item Number of Purchase Requisition""")
    BSART = Column('BSART', String(4), default=None, doc="""Sourced from EBAN-BSART // Purchase Requisition Document Type""")
    BSTYP = Column('BSTYP', String(1), default=None, doc="""Sourced from EBAN-BSTYP // Purchasing Document Category""")
    BSAKZ = Column('BSAKZ', String(1), default=None, doc="""Sourced from EBAN-BSAKZ // Control indicator for purchasing document type""")
    LOEKZ = Column('LOEKZ', String(1), default=None, doc="""Sourced from EBAN-LOEKZ // Deletion Indicator in Purchasing Document""")
    STATU = Column('STATU', String(1), default=None, doc="""Sourced from EBAN-STATU // Processing status of purchase requisition""")
    ESTKZ = Column('ESTKZ', String(1), default=None, doc="""Sourced from EBAN-ESTKZ // Creation Indicator (Purchase Requisition/Schedule Lines)""")
    FRGKZ = Column('FRGKZ', String(1), default=None, doc="""Sourced from EBAN-FRGKZ // Release Indicator""")
    FRGZU = Column('FRGZU', String(8), default=None, doc="""Sourced from EBAN-FRGZU // Release status""")
    FRGST = Column('FRGST', String(2), default=None, doc="""Sourced from EBAN-FRGST // Release Strategy in Purchase Requisition""")
    EKGRP = Column('EKGRP', String(3), default=None, doc="""Sourced from EBAN-EKGRP // Purchasing Group""")
    ERNAM = Column('ERNAM', String(12), default=None, doc="""Sourced from EBAN-ERNAM // Name of Person who Created the Object""")
    ERDAT = Column('ERDAT', Date, default=None, doc="""Sourced from EBAN-ERDAT // Changed On""")
    AFNAM = Column('AFNAM', String(12), default=None, doc="""Sourced from EBAN-AFNAM // Name of Requisitioner/Requester""")
    TXZ01 = Column('TXZ01', String(40), default=None, doc="""Sourced from EBAN-TXZ01 // Short Text""")
    MATNR = Column('MATNR', String(18), default=None, doc="""Sourced from EBAN-MATNR // Material Number""")
    EMATN = Column('EMATN', String(18), default=None, doc="""Sourced from EBAN-EMATN // Material Number Corresponding to Manufacturer Part Number""")
    WERKS = Column('WERKS', String(4), default=None, doc="""Sourced from EBAN-WERKS // Plant""")
    LGORT = Column('LGORT', String(4), default=None, doc="""Sourced from EBAN-LGORT // Storage Location""")
    BEDNR = Column('BEDNR', String(10), default=None, doc="""Sourced from EBAN-BEDNR // Requirement Tracking Number""")
    MATKL = Column('MATKL', String(9), default=None, doc="""Sourced from EBAN-MATKL // Material Group""")
    RESWK = Column('RESWK', String(4), default=None, doc="""Sourced from EBAN-RESWK // Supplying (Issuing) Plant in Stock Transport Order""")
    MENGE = Column('MENGE', String(13), default=None, doc="""Sourced from EBAN-MENGE // Purchase Requisition Quantity""")
    MEINS = Column('MEINS', String(3), default=None, doc="""Sourced from EBAN-MEINS // Purchase Requisition Unit of Measure""")
    BUMNG = Column('BUMNG', String(13), default=None, doc="""Sourced from EBAN-BUMNG // Shortage (stock undercoverage) quantity""")
    BADAT = Column('BADAT', String(8), default=None, doc="""Sourced from EBAN-BADAT // Requisition (Request) Date""")
    LPEIN = Column('LPEIN', String(1), default=None, doc="""Sourced from EBAN-LPEIN // Category of Delivery Date""")
    LFDAT = Column('LFDAT', Date, default=None, doc="""Sourced from EBAN-LFDAT // Item Delivery Date""")
    FRGDT = Column('FRGDT', String(8), default=None, doc="""Sourced from EBAN-FRGDT // Purchase Requisition Release Date""")
    WEBAZ = Column('WEBAZ', Numeric(15,3,3), default=None, doc="""Sourced from EBAN-WEBAZ // Goods Receipt Processing Time in Days""")
    PREIS = Column('PREIS', String(11), default=None, doc="""Sourced from EBAN-PREIS // Price in Purchase Requisition""")
    PEINH = Column('PEINH', Numeric(15,3,3), default=None, doc="""Sourced from EBAN-PEINH // Price Unit""")
    PSTYP = Column('PSTYP', String(1), default=None, doc="""Sourced from EBAN-PSTYP // Item Category in Purchasing Document""")
    KNTTP = Column('KNTTP', String(1), default=None, doc="""Sourced from EBAN-KNTTP // Account Assignment Category""")
    KZVBR = Column('KZVBR', String(1), default=None, doc="""Sourced from EBAN-KZVBR // Consumption Posting""")
    KFLAG = Column('KFLAG', Boolean, default=None, doc="""Sourced from EBAN-KFLAG // Acct.asst.changeable""")
    VRTKZ = Column('VRTKZ', String(1), default=None, doc="""Sourced from EBAN-VRTKZ // Distribution indicator for multiple account assignment""")
    TWRKZ = Column('TWRKZ', String(1), default=None, doc="""Sourced from EBAN-TWRKZ // Partial Invoice Indicator""")
    WEPOS = Column('WEPOS', Boolean, default=None, doc="""Sourced from EBAN-WEPOS // Goods Receipt Indicator""")
    WEUNB = Column('WEUNB', Boolean, default=None, doc="""Sourced from EBAN-WEUNB // Goods Receipt, Non-Valuated""")
    REPOS = Column('REPOS', Boolean, default=None, doc="""Sourced from EBAN-REPOS // Invoice Receipt Indicator""")
    LIFNR = Column('LIFNR', String(10), default=None, doc="""Sourced from EBAN-LIFNR // Desired Vendor""")
    FLIEF = Column('FLIEF', String(10), default=None, doc="""Sourced from EBAN-FLIEF // Fixed Vendor""")
    EKORG = Column('EKORG', String(4), default=None, doc="""Sourced from EBAN-EKORG // Purchasing Organization""")
    VRTYP = Column('VRTYP', String(1), default=None, doc="""Sourced from EBAN-VRTYP // Purchasing Document Category""")
    KONNR = Column('KONNR', String(10), default=None, doc="""Sourced from EBAN-KONNR // Number of Principal Purchase Agreement""")
    KTPNR = Column('KTPNR', String(5), default=None, doc="""Sourced from EBAN-KTPNR // Item Number of Principal Purchase Agreement""")
    INFNR = Column('INFNR', String(10), default=None, doc="""Sourced from EBAN-INFNR // Number of Purchasing Info Record""")
    ZUGBA = Column('ZUGBA', Boolean, default=None, doc="""Sourced from EBAN-ZUGBA // Assigned Source of Supply""")
    QUNUM = Column('QUNUM', String(10), default=None, doc="""Sourced from EBAN-QUNUM // Number of Quota Arrangement""")
    QUPOS = Column('QUPOS', String(3), default=None, doc="""Sourced from EBAN-QUPOS // Quota Arrangement Item""")
    DISPO = Column('DISPO', String(3), default=None, doc="""Sourced from EBAN-DISPO // MRP Controller (Materials Planner)""")
    SERNR = Column('SERNR', String(8), default=None, doc="""Sourced from EBAN-SERNR // BOM explosion number""")
    BVDAT = Column('BVDAT', String(8), default=None, doc="""Sourced from EBAN-BVDAT // Date of last resubmission""")
    BATOL = Column('BATOL', String(3), default=None, doc="""Sourced from EBAN-BATOL // Resubmission Interval of Purchase Requisition""")
    BVDRK = Column('BVDRK', String(7), default=None, doc="""Sourced from EBAN-BVDRK // Number of resubmissions""")
    EBELN = Column('EBELN', String(10), default=None, doc="""Sourced from EBAN-EBELN // Purchase Order Number""")
    EBELP = Column('EBELP', String(5), default=None, doc="""Sourced from EBAN-EBELP // Purchase Order Item Number""")
    BEDAT = Column('BEDAT', Date, default=None, doc="""Sourced from EBAN-BEDAT // Purchase Order Date""")
    BSMNG = Column('BSMNG', String(13), default=None, doc="""Sourced from EBAN-BSMNG // Quantity Ordered Against this Purchase Requisition""")
    LBLNI = Column('LBLNI', String(10), default=None, doc="""Sourced from EBAN-LBLNI // Entry Sheet Number""")
    BWTAR = Column('BWTAR', String(10), default=None, doc="""Sourced from EBAN-BWTAR // Valuation Type""")
    XOBLR = Column('XOBLR', Boolean, default=None, doc="""Sourced from EBAN-XOBLR // Item affects commitments""")
    EBAKZ = Column('EBAKZ', Boolean, default=None, doc="""Sourced from EBAN-EBAKZ // Purchase Requisition Closed""")
    RSNUM = Column('RSNUM', String(10), default=None, doc="""Sourced from EBAN-RSNUM // Number of Reservation/Dependent Requirement""")
    SOBKZ = Column('SOBKZ', String(1), default=None, doc="""Sourced from EBAN-SOBKZ // Special Stock Indicator""")
    ARSNR = Column('ARSNR', String(10), default=None, doc="""Sourced from EBAN-ARSNR // Settlement reservation number""")
    ARSPS = Column('ARSPS', String(4), default=None, doc="""Sourced from EBAN-ARSPS // Item number of the settlement reservation""")
    FIXKZ = Column('FIXKZ', Boolean, default=None, doc="""Sourced from EBAN-FIXKZ // Purchase Requisition is Fixed""")
    BMEIN = Column('BMEIN', String(3), default=None, doc="""Sourced from EBAN-BMEIN // Purchase Order Unit of Measure""")
    REVLV = Column('REVLV', String(2), default=None, doc="""Sourced from EBAN-REVLV // Revision Level""")
    VORAB = Column('VORAB', Boolean, default=None, doc="""Sourced from EBAN-VORAB // Advance procurement: project stock""")
    PACKNO = Column('PACKNO', String(10), default=None, doc="""Sourced from EBAN-PACKNO // Package number""")
    KANBA = Column('KANBA', String(1), default=None, doc="""Sourced from EBAN-KANBA // Kanban Indicator""")
    BPUEB = Column('BPUEB', String(1), default=None, doc="""Sourced from EBAN-BPUEB // Adopt Requisition Price in Purchase Order""")
    CUOBJ = Column('CUOBJ', String(18), default=None, doc="""Sourced from EBAN-CUOBJ // Configuration (internal object number)""")
    FRGGR = Column('FRGGR', String(2), default=None, doc="""Sourced from EBAN-FRGGR // Release group""")
    FRGRL = Column('FRGRL', Boolean, default=None, doc="""Sourced from EBAN-FRGRL // Release Not Yet Completely Effected""")
    AKTNR = Column('AKTNR', String(10), default=None, doc="""Sourced from EBAN-AKTNR // Promotion""")
    CHARG = Column('CHARG', String(10), default=None, doc="""Sourced from EBAN-CHARG // Batch Number""")
    UMSOK = Column('UMSOK', String(1), default=None, doc="""Sourced from EBAN-UMSOK // Special Stock Indicator for Physical Stock Transfer""")
    VERID = Column('VERID', String(4), default=None, doc="""Sourced from EBAN-VERID // Production Version""")
    FIPOS = Column('FIPOS', String(14), default=None, doc="""Sourced from EBAN-FIPOS // Commitment Item""")
    FISTL = Column('FISTL', String(16), default=None, doc="""Sourced from EBAN-FISTL // Funds Center""")
    GEBER = Column('GEBER', String(10), default=None, doc="""Sourced from EBAN-GEBER // Fund""")
    KZKFG = Column('KZKFG', String(1), default=None, doc="""Sourced from EBAN-KZKFG // Origin of Configuration""")
    SATNR = Column('SATNR', String(18), default=None, doc="""Sourced from EBAN-SATNR // Cross-Plant Configurable Material""")
    MNG02 = Column('MNG02', String(13), default=None, doc="""Sourced from EBAN-MNG02 // Committed Quantity""")
    DAT01 = Column('DAT01', String(8), default=None, doc="""Sourced from EBAN-DAT01 // Committed Date""")
    ATTYP = Column('ATTYP', String(2), default=None, doc="""Sourced from EBAN-ATTYP // Material Category""")
    ADRNR = Column('ADRNR', String(10), default=None, doc="""Sourced from EBAN-ADRNR // Manual address number in purchasing document item""")
    ADRN2 = Column('ADRN2', String(10), default=None, doc="""Sourced from EBAN-ADRN2 // Number of delivery address""")
    KUNNR = Column('KUNNR', String(10), default=None, doc="""Sourced from EBAN-KUNNR // Customer""")
    EMLIF = Column('EMLIF', String(10), default=None, doc="""Sourced from EBAN-EMLIF // Vendor to be supplied/who is to receive delivery""")
    LBLKZ = Column('LBLKZ', Boolean, default=None, doc="""Sourced from EBAN-LBLKZ // Subcontracting vendor""")
    KZBWS = Column('KZBWS', String(1), default=None, doc="""Sourced from EBAN-KZBWS // Valuation of Special Stock""")
    WAERS = Column('WAERS', String(5), default=None, doc="""Sourced from EBAN-WAERS // Currency Key""")
    IDNLF = Column('IDNLF', String(35), default=None, doc="""Sourced from EBAN-IDNLF // Material Number Used by Vendor""")
    GSFRG = Column('GSFRG', Boolean, default=None, doc="""Sourced from EBAN-GSFRG // Overall release of purchase requisitions""")
    MPROF = Column('MPROF', String(4), default=None, doc="""Sourced from EBAN-MPROF // Manufacturer Part Profile""")
    KZFME = Column('KZFME', String(1), default=None, doc="""Sourced from EBAN-KZFME // Units of measure usage""")
    SPRAS = Column('SPRAS', String(1), default=None, doc="""Sourced from EBAN-SPRAS // Language Key""")
    TECHS = Column('TECHS', String(12), default=None, doc="""Sourced from EBAN-TECHS // Parameter Variant/Standard Variant""")
    MFRPN = Column('MFRPN', String(40), default=None, doc="""Sourced from EBAN-MFRPN // Manufacturer Part Number""")
    MFRNR = Column('MFRNR', String(10), default=None, doc="""Sourced from EBAN-MFRNR // Number of a Manufacturer""")
    EMNFR = Column('EMNFR', String(10), default=None, doc="""Sourced from EBAN-EMNFR // External manufacturer code name or number""")
    FORDN = Column('FORDN', String(10), default=None, doc="""Sourced from EBAN-FORDN // Framework Order""")
    FORDP = Column('FORDP', String(5), default=None, doc="""Sourced from EBAN-FORDP // Item of framework order""")
    PLIFZ = Column('PLIFZ', Numeric(15,3,3), default=None, doc="""Sourced from EBAN-PLIFZ // Planned Delivery Time in Days""")
    BERID = Column('BERID', String(10), default=None, doc="""Sourced from EBAN-BERID // MRP Area""")
    UZEIT = Column('UZEIT', String(6), default=None, doc="""Sourced from EBAN-UZEIT // Delivery Date Time-Spot""")
    FKBER = Column('FKBER', String(16), default=None, doc="""Sourced from EBAN-FKBER // Functional Area""")
    GRANT_NBR = Column('GRANT_NBR', String(20), default=None, doc="""Sourced from EBAN-GRANT_NBR // Grant""")
    MEMORY = Column('MEMORY', Boolean, default=None, doc="""Sourced from EBAN-MEMORY // Purchase Requisition not yet Complete""")
    BANPR = Column('BANPR', String(2), default=None, doc="""Sourced from EBAN-BANPR // Requisition Processing State""")
    RLWRT = Column('RLWRT', Numeric(15,3,3), default=None, doc="""Sourced from EBAN-RLWRT // Total value at time of release""")
    BLCKD = Column('BLCKD', String(1), default=None, doc="""Sourced from EBAN-BLCKD // Purchase Requisition Blocked""")
    REVNO = Column('REVNO', String(8), default=None, doc="""Sourced from EBAN-REVNO // Version number in Purchasing""")
    BLCKT = Column('BLCKT', String(60), default=None, doc="""Sourced from EBAN-BLCKT // Reason for Item Block""")
    BESWK = Column('BESWK', String(4), default=None, doc="""Sourced from EBAN-BESWK // Procuring Plant""")
    EPROFILE = Column('EPROFILE', String(2), default=None, doc="""Sourced from EBAN-EPROFILE // External Procurement Profile""")
    EPREFDOC = Column('EPREFDOC', String(10), default=None, doc="""Sourced from EBAN-EPREFDOC // External Procurement Reference Document""")
    EPREFITM = Column('EPREFITM', String(5), default=None, doc="""Sourced from EBAN-EPREFITM // External Procurement Reference Item""")
    GMMNG = Column('GMMNG', String(13), default=None, doc="""Sourced from EBAN-GMMNG // PO Quantity of Purchase Requisition in POs on Hold""")
    WRTKZ = Column('WRTKZ', Boolean, default=None, doc="""Sourced from EBAN-WRTKZ // Value-Based Commitment Reduction for Service Purchase Reqs""")
    RESLO = Column('RESLO', String(4), default=None, doc="""Sourced from EBAN-RESLO // Issuing Storage Location for Stock Transport Order""")
    KBLNR = Column('KBLNR', String(10), default=None, doc="""Sourced from EBAN-KBLNR // Document Number for Earmarked Funds""")
    KBLPOS = Column('KBLPOS', String(3), default=None, doc="""Sourced from EBAN-KBLPOS // Earmarked Funds: Document Item""")
    PRIO_URG = Column('PRIO_URG', String(2), default=None, doc="""Sourced from EBAN-PRIO_URG // Requirement Urgency""")
    PRIO_REQ = Column('PRIO_REQ', String(3), default=None, doc="""Sourced from EBAN-PRIO_REQ // Requirement Priority""")
    MEMORYTYPE = Column('MEMORYTYPE', String(1), default=None, doc="""Sourced from EBAN-MEMORYTYPE // Category of Incompleteness""")
    ANZSN = Column('ANZSN', Integer, default=None, doc="""Sourced from EBAN-ANZSN // Number of serial numbers""")
    MHDRZ = Column('MHDRZ', Numeric(15,3,3), default=None, doc="""Sourced from EBAN-MHDRZ // Minimum Remaining Shelf Life""")
    IPRKZ = Column('IPRKZ', String(1), default=None, doc="""Sourced from EBAN-IPRKZ // Period Indicator for Shelf Life Expiration Date""")
    NODISP = Column('NODISP', Boolean, default=None, doc="""Sourced from EBAN-NODISP // Ind: Reserv. not applicable to MRP;Purc. req. not created""")
    SRM_CONTRACT_ID = Column('SRM_CONTRACT_ID', String(10), default=None, doc="""Sourced from EBAN-SRM_CONTRACT_ID // Central Contract""")
    SRM_CONTRACT_ITM = Column('SRM_CONTRACT_ITM', String(10), default=None, doc="""Sourced from EBAN-SRM_CONTRACT_ITM // Central Contract Item Number""")
    BUDGET_PD = Column('BUDGET_PD', String(10), default=None, doc="""Sourced from EBAN-BUDGET_PD // FM: Budget Period""")
    ZZSC_ID = Column('ZZSC_ID', String(10), default=None, doc="""Sourced from EBAN-ZZSC_ID // Shopping Cart ID""")
    ZZSC_STATUS = Column('ZZSC_STATUS', String(30), default=None, doc="""Sourced from EBAN-ZZSC_STATUS // Status of Shopping Cart""")
    YRREQ = Column('YRREQ', String(10), default=None, doc="""Sourced from EBAN-YRREQ // Reference Requisition  Number""")
    FMFGUS_KEY = Column('FMFGUS_KEY', String(22), default=None, doc="""Sourced from EBAN-FMFGUS_KEY // United States Federal Government Fields""")
    ADVCODE = Column('ADVCODE', String(2), default=None, doc="""Sourced from EBAN-ADVCODE // Advice Code""")
    STACODE = Column('STACODE', String(2), default=None, doc="""Sourced from EBAN-STACODE // Status Code""")
    BANFN_CS = Column('BANFN_CS', String(10), default=None, doc="""Sourced from EBAN-BANFN_CS // Cross-System PReq Number""")
    BNFPO_CS = Column('BNFPO_CS', String(5), default=None, doc="""Sourced from EBAN-BNFPO_CS // Cross-System PReq Item""")
    ITEM_CS = Column('ITEM_CS', String(1), default=None, doc="""Sourced from EBAN-ITEM_CS // Cross-System Item Category""")
    BSMNG_SND = Column('BSMNG_SND', String(13), default=None, doc="""Sourced from EBAN-BSMNG_SND // PO Quantity Sender""")
    IUID_RELEVANT = Column('IUID_RELEVANT', String(1), default=None, doc="""Sourced from EBAN-IUID_RELEVANT // IUID-Relevant""")
    SGT_SCAT = Column('SGT_SCAT', String(16), default=None, doc="""Sourced from EBAN-SGT_SCAT // Stock Segment""")
    SGT_RCAT = Column('SGT_RCAT', String(16), default=None, doc="""Sourced from EBAN-SGT_RCAT // Requirement Segment""")

    prch_req_id = synonym('BANFN')
    prch_req_item_id = synonym('BNFPO')
    prch_ord_type_cd = synonym('BSART')
    prch_doc_ctgy_cd = synonym('BSTYP')
    prch_doc_type_cntrl_cd = synonym('BSAKZ')
    release_status_cd = synonym('FRGZU')
    prch_grp_cd = synonym('EKGRP')
    doc_create_user_id = synonym('ERNAM')
    doc_create_dt = synonym('ERDAT')
    material_id = synonym('MATNR')
    mfg_part_nbr_matl_id = synonym('EMATN')
    material_group_cd = synonym('MATKL')
    sto_source_facility_id = synonym('RESWK')
    uom_cd = synonym('MEINS')
    delivery_dt = synonym('LFDAT')
    price_uom_cd = synonym('PEINH')
    prch_doc_item_ctgy_cd = synonym('PSTYP')
    goods_receipt_ind = synonym('WEPOS')
    prch_org_cd = synonym('EKORG')
    mrp_controller_cd = synonym('DISPO')
    prch_doc_id = synonym('EBELN')
    prch_doc_item_id = synonym('EBELP')
    prch_ord_dt = synonym('BEDAT')
    special_stock_cd = synonym('SOBKZ')
    release_grp_cd = synonym('FRGGR')
    incomplete_release_ind = synonym('FRGRL')
    configurable_material_ind = synonym('KZKFG')
    matl_ctgy_id = synonym('ATTYP')
    addr_id = synonym('ADRNR')
    addr_nbr = synonym('ADRN2')
    customer_id = synonym('KUNNR')
    receiving_vendor_id = synonym('EMLIF')
    special_stock_valuation_Cd = synonym('KZBWS')
    currency_cd = synonym('WAERS')
    vendor_material_nbr = synonym('IDNLF')
    language_cd = synonym('SPRAS')
    mfg_part_nbr = synonym('MFRPN')
    ext_mfg_cd = synonym('EMNFR')
    mrp_area_id = synonym('BERID')
    sto_source_stor_loc_id = synonym('RESLO')
    incompleteness_ctgy_cd = synonym('MEMORYTYPE')


################################################################################




################################################################################

class PurchInfo(SAP_Base):
    """\
    Table sourced from: EINA
    Description: Purchasing Info Record: General Data
    """

    __tablename__ = "EINA"

    INFNR = Column('INFNR', String(10), primary_key = True, doc="""Sourced from EINA-INFNR // Number of Purchasing Info Record""")
    MATNR = Column('MATNR', String(18), default=None, doc="""Sourced from EINA-MATNR // Material Number""")
    MATKL = Column('MATKL', String(9), default=None, doc="""Sourced from EINA-MATKL // Material Group""")
    LIFNR = Column('LIFNR', String(10), default=None, doc="""Sourced from EINA-LIFNR // Vendor Account Number""")
    LOEKZ = Column('LOEKZ', Boolean, default=None, doc="""Sourced from EINA-LOEKZ // Purchasing info: General data flagged for deletion""")
    ERDAT = Column('ERDAT', Date, default=None, doc="""Sourced from EINA-ERDAT // Date on Which Record Was Created""")
    ERNAM = Column('ERNAM', String(12), default=None, doc="""Sourced from EINA-ERNAM // Name of Person who Created the Object""")
    TXZ01 = Column('TXZ01', String(40), default=None, doc="""Sourced from EINA-TXZ01 // Short Text for Purchasing Info Record""")
    SORTL = Column('SORTL', String(10), default=None, doc="""Sourced from EINA-SORTL // Sort Term for Non-Stock Info Records""")
    MEINS = Column('MEINS', String(3), default=None, doc="""Sourced from EINA-MEINS // Purchase Order Unit of Measure""")
    UMREZ = Column('UMREZ', Numeric(15,3,3), default=None, doc="""Sourced from EINA-UMREZ // Numerator for Conversion of Order Unit to Base Unit""")
    UMREN = Column('UMREN', Numeric(15,3,3), default=None, doc="""Sourced from EINA-UMREN // Denominator for Conversion of Order Unit to Base Unit""")
    IDNLF = Column('IDNLF', String(35), default=None, doc="""Sourced from EINA-IDNLF // Material Number Used by Vendor""")
    VERKF = Column('VERKF', String(30), default=None, doc="""Sourced from EINA-VERKF // Salesperson Responsible in the Event of Queries""")
    TELF1 = Column('TELF1', String(16), default=None, doc="""Sourced from EINA-TELF1 // Vendor's Telephone Number""")
    MAHN1 = Column('MAHN1', Numeric(15,3,3), default=None, doc="""Sourced from EINA-MAHN1 // Number of Days for First Reminder/Expediter""")
    MAHN2 = Column('MAHN2', Numeric(15,3,3), default=None, doc="""Sourced from EINA-MAHN2 // Number of Days for Second Reminder/Expediter""")
    MAHN3 = Column('MAHN3', Numeric(15,3,3), default=None, doc="""Sourced from EINA-MAHN3 // Number of Days for Third Reminder/Expediter""")
    URZNR = Column('URZNR', String(10), default=None, doc="""Sourced from EINA-URZNR // Certificate Number""")
    URZDT = Column('URZDT', String(8), default=None, doc="""Sourced from EINA-URZDT // Certificate of Origin Valid Until""")
    URZLA = Column('URZLA', String(3), default=None, doc="""Sourced from EINA-URZLA // Country of Issue of Certificate of Origin""")
    URZTP = Column('URZTP', String(1), default=None, doc="""Sourced from EINA-URZTP // Certificate Category""")
    URZZT = Column('URZZT', String(16), default=None, doc="""Sourced from EINA-URZZT // Number""")
    LMEIN = Column('LMEIN', String(3), default=None, doc="""Sourced from EINA-LMEIN // Base Unit of Measure""")
    REGIO = Column('REGIO', String(3), default=None, doc="""Sourced from EINA-REGIO // Region (State, Province, County)""")
    VABME = Column('VABME', String(1), default=None, doc="""Sourced from EINA-VABME // Variable Purchase Order Unit Active""")
    LTSNR = Column('LTSNR', String(6), default=None, doc="""Sourced from EINA-LTSNR // Vendor Subrange""")
    LTSSF = Column('LTSSF', String(5), default=None, doc="""Sourced from EINA-LTSSF // Sort Sequence Number""")
    WGLIF = Column('WGLIF', String(18), default=None, doc="""Sourced from EINA-WGLIF // Vendor Material Group""")
    RUECK = Column('RUECK', String(2), default=None, doc="""Sourced from EINA-RUECK // Return Agreement""")
    LIFAB = Column('LIFAB', String(8), default=None, doc="""Sourced from EINA-LIFAB // Available (Deliverable) From""")
    LIFBI = Column('LIFBI', String(8), default=None, doc="""Sourced from EINA-LIFBI // Available (Deliverable) Until""")
    KOLIF = Column('KOLIF', String(10), default=None, doc="""Sourced from EINA-KOLIF // Prior Vendor""")
    ANZPU = Column('ANZPU', Numeric(15,3,3), default=None, doc="""Sourced from EINA-ANZPU // Number of Points""")
    PUNEI = Column('PUNEI', String(3), default=None, doc="""Sourced from EINA-PUNEI // Points unit""")
    RELIF = Column('RELIF', Boolean, default=None, doc="""Sourced from EINA-RELIF // Regular Vendor""")
    MFRNR = Column('MFRNR', String(10), default=None, doc="""Sourced from EINA-MFRNR // Manufacturer""")

    material_id = synonym('MATNR')
    material_group_cd = synonym('MATKL')
    doc_create_dt = synonym('ERDAT')
    doc_create_user_id = synonym('ERNAM')
    uom_cd = synonym('MEINS')
    base_uom_conversin_num = synonym('UMREZ')
    base_uom_conversion_denom = synonym('UMREN')
    vendor_material_nbr = synonym('IDNLF')
    region = synonym('REGIO')


################################################################################




################################################################################

class PurchDocHist(SAP_Base):
    """\
    Table sourced from: EKBE
    Description: History per Purchasing Document
    """

    __tablename__ = "EKBE"

    EBELN = Column('EBELN', String(10), primary_key = True, doc="""Sourced from EKBE-EBELN // Purchasing Document Number""")
    EBELP = Column('EBELP', String(5), primary_key = True, doc="""Sourced from EKBE-EBELP // Item Number of Purchasing Document""")
    ZEKKN = Column('ZEKKN', String(2), primary_key = True, doc="""Sourced from EKBE-ZEKKN // Sequential Number of Account Assignment""")
    VGABE = Column('VGABE', String(1), primary_key = True, doc="""Sourced from EKBE-VGABE // Transaction/event type, purchase order history""")
    GJAHR = Column('GJAHR', String(4), primary_key = True, doc="""Sourced from EKBE-GJAHR // Material Document Year""")
    BELNR = Column('BELNR', String(10), primary_key = True, doc="""Sourced from EKBE-BELNR // Number of Material Document""")
    BUZEI = Column('BUZEI', String(4), primary_key = True, doc="""Sourced from EKBE-BUZEI // Item in Material Document""")
    BEWTP = Column('BEWTP', String(1), default=None, doc="""Sourced from EKBE-BEWTP // Purchase Order History Category""")
    BWART = Column('BWART', String(3), default=None, doc="""Sourced from EKBE-BWART // Movement Type (Inventory Management)""")
    BUDAT = Column('BUDAT', Date, default=None, doc="""Sourced from EKBE-BUDAT // Posting Date in the Document""")
    MENGE = Column('MENGE', String(13), default=None, doc="""Sourced from EKBE-MENGE // Quantity""")
    BPMNG = Column('BPMNG', Numeric(15,3,3), default=None, doc="""Sourced from EKBE-BPMNG // Quantity in purchase order price unit""")
    DMBTR = Column('DMBTR', Numeric(15,3,3), default=None, doc="""Sourced from EKBE-DMBTR // Amount in Local Currency""")
    WRBTR = Column('WRBTR', Numeric(15,3,3), default=None, doc="""Sourced from EKBE-WRBTR // Amount in Document Currency""")
    WAERS = Column('WAERS', String(5), default=None, doc="""Sourced from EKBE-WAERS // Currency Key""")
    AREWR = Column('AREWR', Numeric(15,3,3), default=None, doc="""Sourced from EKBE-AREWR // GR/IR account clearing value in local currency""")
    WESBS = Column('WESBS', Numeric(15,3,3), default=None, doc="""Sourced from EKBE-WESBS // Goods Receipt Blocked Stock in Order Unit""")
    BPWES = Column('BPWES', Numeric(15,3,3), default=None, doc="""Sourced from EKBE-BPWES // Quantity in GR blocked stock in order price unit""")
    SHKZG = Column('SHKZG', String(1), default=None, doc="""Sourced from EKBE-SHKZG // Debit/Credit Indicator""")
    BWTAR = Column('BWTAR', String(10), default=None, doc="""Sourced from EKBE-BWTAR // Valuation Type""")
    ELIKZ = Column('ELIKZ', Boolean, default=None, doc="""Sourced from EKBE-ELIKZ // 'Delivery Completed' Indicator""")
    XBLNR = Column('XBLNR', String(16), default=None, doc="""Sourced from EKBE-XBLNR // Reference Document Number""")
    LFGJA = Column('LFGJA', String(4), default=None, doc="""Sourced from EKBE-LFGJA // Fiscal Year of a Reference Document""")
    LFBNR = Column('LFBNR', String(10), default=None, doc="""Sourced from EKBE-LFBNR // Document No. of a Reference Document""")
    LFPOS = Column('LFPOS', String(4), default=None, doc="""Sourced from EKBE-LFPOS // Item of a Reference Document""")
    GRUND = Column('GRUND', String(4), default=None, doc="""Sourced from EKBE-GRUND // Reason for Movement""")
    CPUDT = Column('CPUDT', Date, default=None, doc="""Sourced from EKBE-CPUDT // Day On Which Accounting Document Was Entered""")
    CPUTM = Column('CPUTM', Time, default=None, doc="""Sourced from EKBE-CPUTM // Time of Entry""")
    REEWR = Column('REEWR', Numeric(15,3,3), default=None, doc="""Sourced from EKBE-REEWR // Invoice Value Entered (in Local Currency)""")
    EVERE = Column('EVERE', String(2), default=None, doc="""Sourced from EKBE-EVERE // Compliance with Shipping Instructions""")
    REFWR = Column('REFWR', Numeric(15,3,3), default=None, doc="""Sourced from EKBE-REFWR // Invoice Value in Foreign Currency""")
    MATNR = Column('MATNR', String(18), default=None, doc="""Sourced from EKBE-MATNR // Material Number""")
    WERKS = Column('WERKS', String(4), default=None, doc="""Sourced from EKBE-WERKS // Plant""")
    XWSBR = Column('XWSBR', Boolean, default=None, doc="""Sourced from EKBE-XWSBR // Reversal of GR allowed for GR-based IV despite invoice""")
    ETENS = Column('ETENS', String(4), default=None, doc="""Sourced from EKBE-ETENS // Sequential Number of Vendor Confirmation""")
    KNUMV = Column('KNUMV', String(10), default=None, doc="""Sourced from EKBE-KNUMV // Number of the document condition""")
    MWSKZ = Column('MWSKZ', String(2), default=None, doc="""Sourced from EKBE-MWSKZ // Tax on sales/purchases code""")
    LSMNG = Column('LSMNG', Numeric(15,3,3), default=None, doc="""Sourced from EKBE-LSMNG // Quantity in Unit of Measure from Delivery Note""")
    LSMEH = Column('LSMEH', String(3), default=None, doc="""Sourced from EKBE-LSMEH // Unit of Measure From Delivery Note""")
    EMATN = Column('EMATN', String(18), default=None, doc="""Sourced from EKBE-EMATN // Material Number""")
    AREWW = Column('AREWW', Numeric(15,3,3), default=None, doc="""Sourced from EKBE-AREWW // Clearing value on GR/IR clearing account (transac. currency)""")
    HSWAE = Column('HSWAE', String(5), default=None, doc="""Sourced from EKBE-HSWAE // Local currency key""")
    BAMNG = Column('BAMNG', Numeric(15,3,3), default=None, doc="""Sourced from EKBE-BAMNG // Quantity""")
    CHARG = Column('CHARG', String(10), default=None, doc="""Sourced from EKBE-CHARG // Batch Number""")
    BLDAT = Column('BLDAT', Date, default=None, doc="""Sourced from EKBE-BLDAT // Document Date in Document""")
    XWOFF = Column('XWOFF', Boolean, default=None, doc="""Sourced from EKBE-XWOFF // Calculation of val. open""")
    XUNPL = Column('XUNPL', Boolean, default=None, doc="""Sourced from EKBE-XUNPL // Unplanned Account Assignment from Invoice Verification""")
    ERNAM = Column('ERNAM', String(12), default=None, doc="""Sourced from EKBE-ERNAM // Name of Person who Created the Object""")
    SRVPOS = Column('SRVPOS', String(18), default=None, doc="""Sourced from EKBE-SRVPOS // Service number""")
    PACKNO = Column('PACKNO', String(10), default=None, doc="""Sourced from EKBE-PACKNO // Package Number of Service""")
    INTROW = Column('INTROW', String(10), default=None, doc="""Sourced from EKBE-INTROW // Line Number of Service""")
    BEKKN = Column('BEKKN', String(2), default=None, doc="""Sourced from EKBE-BEKKN // Number of PO Account Assignment""")
    LEMIN = Column('LEMIN', Boolean, default=None, doc="""Sourced from EKBE-LEMIN // Returns Indicator""")
    AREWB = Column('AREWB', Numeric(15,3,3), default=None, doc="""Sourced from EKBE-AREWB // Clearing Value on GR/IR Account in PO Currency""")
    REWRB = Column('REWRB', Numeric(15,3,3), default=None, doc="""Sourced from EKBE-REWRB // Invoice Amount in PO Currency""")
    SAPRL = Column('SAPRL', String(4), default=None, doc="""Sourced from EKBE-SAPRL // SAP Release""")
    MENGE_POP = Column('MENGE_POP', String(13), default=None, doc="""Sourced from EKBE-MENGE_POP // Quantity""")
    BPMNG_POP = Column('BPMNG_POP', String(13), default=None, doc="""Sourced from EKBE-BPMNG_POP // Quantity in purchase order price unit""")
    DMBTR_POP = Column('DMBTR_POP', String(13), default=None, doc="""Sourced from EKBE-DMBTR_POP // Amount in Local Currency""")
    WRBTR_POP = Column('WRBTR_POP', String(13), default=None, doc="""Sourced from EKBE-WRBTR_POP // Amount in Document Currency""")
    WESBB = Column('WESBB', Numeric(15,3,3), default=None, doc="""Sourced from EKBE-WESBB // Valuated Goods Receipt Blocked Stock in Order Unit""")
    BPWEB = Column('BPWEB', Numeric(15,3,3), default=None, doc="""Sourced from EKBE-BPWEB // Quantity in Valuated GR Blocked Stock in Order Price Unit""")
    WEORA = Column('WEORA', Boolean, default=None, doc="""Sourced from EKBE-WEORA // Acceptance At Origin""")
    AREWR_POP = Column('AREWR_POP', String(13), default=None, doc="""Sourced from EKBE-AREWR_POP // GR/IR account clearing value in local currency""")
    KUDIF = Column('KUDIF', Numeric(15,3,3), default=None, doc="""Sourced from EKBE-KUDIF // Exchange Rate Difference Amount""")
    RETAMT_FC = Column('RETAMT_FC', String(13), default=None, doc="""Sourced from EKBE-RETAMT_FC // Retention Amount in Document Currency""")
    RETAMT_LC = Column('RETAMT_LC', String(13), default=None, doc="""Sourced from EKBE-RETAMT_LC // Retention Amount in Company Code Currency""")
    RETAMTP_FC = Column('RETAMTP_FC', String(13), default=None, doc="""Sourced from EKBE-RETAMTP_FC // Posted Retention Amount in Document Currency""")
    RETAMTP_LC = Column('RETAMTP_LC', String(13), default=None, doc="""Sourced from EKBE-RETAMTP_LC // Posted Security Retention Amount in Company Code Currency""")
    XMACC = Column('XMACC', String(1), default=None, doc="""Sourced from EKBE-XMACC // Multiple Account Assignment""")
    WKURS = Column('WKURS', Numeric(15,3,3), default=None, doc="""Sourced from EKBE-WKURS // Exchange Rate""")
    INV_ITEM_ORIGIN = Column('INV_ITEM_ORIGIN', String(1), default=None, doc="""Sourced from EKBE-INV_ITEM_ORIGIN // Origin of an Invoice Item""")
    VBELN_ST = Column('VBELN_ST', String(10), default=None, doc="""Sourced from EKBE-VBELN_ST // Delivery""")
    VBELP_ST = Column('VBELP_ST', String(6), default=None, doc="""Sourced from EKBE-VBELP_ST // Delivery Item""")
    SGT_SCAT = Column('SGT_SCAT', String(16), default=None, doc="""Sourced from EKBE-SGT_SCAT // Stock Segment""")
    ET_UPD = Column('ET_UPD', String(1), default=None, doc="""Sourced from EKBE-ET_UPD // Procedure for Updating the Schedule Line Quantity""")
    J_SC_DIE_COMP_F = Column('J_SC_DIE_COMP_F', String(1), default=None, doc="""Sourced from EKBE-J_SC_DIE_COMP_F // Depreciation completion flag""")

    prch_doc_id = synonym('EBELN')
    prch_doc_item_id = synonym('EBELP')
    fiscal_year = synonym('GJAHR')
    prch_ord_hist_ctgy_cd = synonym('BEWTP')
    im_matl_mvmnt_type_cd = synonym('BWART')
    doc_post_dt = synonym('BUDAT')
    prch_ord_price_unit_qty = synonym('BPMNG')
    currency_cd = synonym('WAERS')
    delivery_complete_ind = synonym('ELIKZ')
    ref_doc_id = synonym('LFBNR')
    ref_doc_item_id = synonym('LFPOS')
    acctng_doc_create_dt = synonym('CPUDT')
    acctng_doc_create_tm = synonym('CPUTM')
    material_id = synonym('MATNR')
    delivery_note_uom_qty = synonym('LSMNG')
    mfg_part_nbr_matl_id = synonym('EMATN')
    local_currency_cd = synonym('HSWAE')
    prch_req_qty = synonym('BAMNG')
    doc_create_user_id = synonym('ERNAM')


################################################################################




################################################################################

class SA_SchedLine(SAP_Base):
    """\
    Table sourced from: EKET
    Description: Scheduling Agreement Schedule Lines
    """

    __tablename__ = "EKET"

    EBELN = Column('EBELN', String(10), primary_key = True, doc="""Sourced from EKET-EBELN // Purchasing Document Number""")
    EBELP = Column('EBELP', String(5), primary_key = True, doc="""Sourced from EKET-EBELP // Item Number of Purchasing Document""")
    ETENR = Column('ETENR', String(4), primary_key = True, doc="""Sourced from EKET-ETENR // Delivery Schedule Line Counter""")
    EINDT = Column('EINDT', String(8), default=None, doc="""Sourced from EKET-EINDT // Item Delivery Date""")
    SLFDT = Column('SLFDT', String(8), default=None, doc="""Sourced from EKET-SLFDT // Statistics-Relevant Delivery Date""")
    LPEIN = Column('LPEIN', String(1), default=None, doc="""Sourced from EKET-LPEIN // Category of Delivery Date""")
    MENGE = Column('MENGE', String(13), default=None, doc="""Sourced from EKET-MENGE // Scheduled Quantity""")
    AMENG = Column('AMENG', String(13), default=None, doc="""Sourced from EKET-AMENG // Previous Quantity (Delivery Schedule Lines)""")
    WEMNG = Column('WEMNG', String(13), default=None, doc="""Sourced from EKET-WEMNG // Quantity of Goods Received""")
    WAMNG = Column('WAMNG', String(13), default=None, doc="""Sourced from EKET-WAMNG // Issued Quantity""")
    UZEIT = Column('UZEIT', String(6), default=None, doc="""Sourced from EKET-UZEIT // Delivery Date Time-Spot""")
    BANFN = Column('BANFN', String(10), default=None, doc="""Sourced from EKET-BANFN // Purchase Requisition Number""")
    BNFPO = Column('BNFPO', String(5), default=None, doc="""Sourced from EKET-BNFPO // Item Number of Purchase Requisition""")
    ESTKZ = Column('ESTKZ', String(1), default=None, doc="""Sourced from EKET-ESTKZ // Creation Indicator (Purchase Requisition/Schedule Lines)""")
    QUNUM = Column('QUNUM', String(10), default=None, doc="""Sourced from EKET-QUNUM // Number of Quota Arrangement""")
    QUPOS = Column('QUPOS', String(3), default=None, doc="""Sourced from EKET-QUPOS // Quota Arrangement Item""")
    MAHNZ = Column('MAHNZ', Numeric(15,3,3), default=None, doc="""Sourced from EKET-MAHNZ // No. of Reminders/Expediters for Schedule Line""")
    BEDAT = Column('BEDAT', Date, default=None, doc="""Sourced from EKET-BEDAT // Order date of schedule line""")
    RSNUM = Column('RSNUM', String(10), default=None, doc="""Sourced from EKET-RSNUM // Number of Reservation/Dependent Requirement""")
    SERNR = Column('SERNR', String(8), default=None, doc="""Sourced from EKET-SERNR // BOM explosion number""")
    FIXKZ = Column('FIXKZ', Boolean, default=None, doc="""Sourced from EKET-FIXKZ // Schedule Line is 'Fixed'""")
    GLMNG = Column('GLMNG', String(13), default=None, doc="""Sourced from EKET-GLMNG // Quantity Delivered (Stock Transfer)""")
    DABMG = Column('DABMG', String(13), default=None, doc="""Sourced from EKET-DABMG // Quantity Reduced (MRP)""")
    CHARG = Column('CHARG', String(10), default=None, doc="""Sourced from EKET-CHARG // Batch Number""")
    LICHA = Column('LICHA', String(15), default=None, doc="""Sourced from EKET-LICHA // Vendor Batch Number""")
    CHKOM = Column('CHKOM', Boolean, default=None, doc="""Sourced from EKET-CHKOM // Components""")
    VERID = Column('VERID', String(4), default=None, doc="""Sourced from EKET-VERID // Production Version""")
    ABART = Column('ABART', String(1), default=None, doc="""Sourced from EKET-ABART // Scheduling agreement release type""")
    MNG02 = Column('MNG02', String(13), default=None, doc="""Sourced from EKET-MNG02 // Committed Quantity""")
    DAT01 = Column('DAT01', String(8), default=None, doc="""Sourced from EKET-DAT01 // Committed Date""")
    ALTDT = Column('ALTDT', String(8), default=None, doc="""Sourced from EKET-ALTDT // Previous delivery date""")
    AULWE = Column('AULWE', String(10), default=None, doc="""Sourced from EKET-AULWE // Route Schedule""")
    MBDAT = Column('MBDAT', Date, default=None, doc="""Sourced from EKET-MBDAT // Material Staging/Availability Date""")
    MBUHR = Column('MBUHR', Time, default=None, doc="""Sourced from EKET-MBUHR // Material Staging Time (Local, Relating to a Plant)""")
    LDDAT = Column('LDDAT', Date, default=None, doc="""Sourced from EKET-LDDAT // Loading Date""")
    LDUHR = Column('LDUHR', Time, default=None, doc="""Sourced from EKET-LDUHR // Loading Time (Local Time Relating to a Shipping Point)""")
    TDDAT = Column('TDDAT', String(8), default=None, doc="""Sourced from EKET-TDDAT // Transportation Planning Date""")
    TDUHR = Column('TDUHR', Time, default=None, doc="""Sourced from EKET-TDUHR // Transp. Planning Time (Local, Relating to a Shipping Point)""")
    WADAT = Column('WADAT', Date, default=None, doc="""Sourced from EKET-WADAT // Goods Issue Date""")
    WAUHR = Column('WAUHR', Time, default=None, doc="""Sourced from EKET-WAUHR // Time of Goods Issue (Local, Relating to a Plant)""")
    ELDAT = Column('ELDAT', String(8), default=None, doc="""Sourced from EKET-ELDAT // Goods Receipt End Date""")
    ELUHR = Column('ELUHR', String(6), default=None, doc="""Sourced from EKET-ELUHR // Goods Receipt End Time (Local, Relating to a Plant)""")
    ANZSN = Column('ANZSN', Integer, default=None, doc="""Sourced from EKET-ANZSN // Number of serial numbers""")
    NODISP = Column('NODISP', Boolean, default=None, doc="""Sourced from EKET-NODISP // Ind: Reserv. not applicable to MRP;Purc. req. not created""")
    GEO_ROUTE = Column('GEO_ROUTE', String(10), default=None, doc="""Sourced from EKET-GEO_ROUTE // Description of a Geographical Route""")
    ROUTE_GTS = Column('ROUTE_GTS', String(10), default=None, doc="""Sourced from EKET-ROUTE_GTS // Route Code for SAP Global Trade Services""")
    GTS_IND = Column('GTS_IND', String(2), default=None, doc="""Sourced from EKET-GTS_IND // Goods Traffic Type""")
    TSP = Column('TSP', String(10), default=None, doc="""Sourced from EKET-TSP // Forwarding agent""")
    CD_LOCNO = Column('CD_LOCNO', String(20), default=None, doc="""Sourced from EKET-CD_LOCNO // Location number in APO""")
    CD_LOCTYPE = Column('CD_LOCTYPE', String(4), default=None, doc="""Sourced from EKET-CD_LOCTYPE // APO location type""")
    HANDOVERDATE = Column('HANDOVERDATE', String(8), default=None, doc="""Sourced from EKET-HANDOVERDATE // Handover Date at the Handover Location""")
    HANDOVERTIME = Column('HANDOVERTIME', String(6), default=None, doc="""Sourced from EKET-HANDOVERTIME // Handover time at the handover location""")
    KEY_ID = Column('KEY_ID', String(16), default=None, doc="""Sourced from EKET-KEY_ID // Unique Number of Budget""")
    OTB_VALUE = Column('OTB_VALUE', String(17), default=None, doc="""Sourced from EKET-OTB_VALUE // Required Budget""")
    OTB_CURR = Column('OTB_CURR', String(5), default=None, doc="""Sourced from EKET-OTB_CURR // OTB Currency""")
    OTB_RES_VALUE = Column('OTB_RES_VALUE', String(17), default=None, doc="""Sourced from EKET-OTB_RES_VALUE // Reserved Budget for OTB-Relevant Purchasing Document""")
    OTB_SPEC_VALUE = Column('OTB_SPEC_VALUE', String(17), default=None, doc="""Sourced from EKET-OTB_SPEC_VALUE // Special Release Budget""")
    SPR_RSN_PROFILE = Column('SPR_RSN_PROFILE', String(4), default=None, doc="""Sourced from EKET-SPR_RSN_PROFILE // Reason Profile for OTB Special Release""")
    BUDG_TYPE = Column('BUDG_TYPE', String(2), default=None, doc="""Sourced from EKET-BUDG_TYPE // Budget Type""")
    OTB_STATUS = Column('OTB_STATUS', String(1), default=None, doc="""Sourced from EKET-OTB_STATUS // OTB Check Status""")
    OTB_REASON = Column('OTB_REASON', String(3), default=None, doc="""Sourced from EKET-OTB_REASON // Reason Indicator for OTB Check Status""")
    CHECK_TYPE = Column('CHECK_TYPE', String(1), default=None, doc="""Sourced from EKET-CHECK_TYPE // Type of OTB Check""")
    DL_ID = Column('DL_ID', String(22), default=None, doc="""Sourced from EKET-DL_ID // Date Line ID (GUID)""")
    HANDOVER_DATE = Column('HANDOVER_DATE', String(8), default=None, doc="""Sourced from EKET-HANDOVER_DATE // Transfer Date""")
    NO_SCEM = Column('NO_SCEM', String(1), default=None, doc="""Sourced from EKET-NO_SCEM // Purchase Order Not Transferred to SCEM""")
    DNG_DATE = Column('DNG_DATE', String(8), default=None, doc="""Sourced from EKET-DNG_DATE // Creation Date of Reminder Message Record""")
    DNG_TIME = Column('DNG_TIME', String(6), default=None, doc="""Sourced from EKET-DNG_TIME // Creation Time of Reminder Message Record""")
    CNCL_ANCMNT_DONE = Column('CNCL_ANCMNT_DONE', String(1), default=None, doc="""Sourced from EKET-CNCL_ANCMNT_DONE // Cancellation Threat Made""")
    DATESHIFT_NUMBER = Column('DATESHIFT_NUMBER', String(3), default=None, doc="""Sourced from EKET-DATESHIFT_NUMBER // Number of Current Date Shifts""")

    prch_doc_id = synonym('EBELN')
    prch_doc_item_id = synonym('EBELP')
    deliv_schd_ln_id = synonym('ETENR')
    prch_req_id = synonym('BANFN')
    prch_req_item_id = synonym('BNFPO')
    prch_ord_dt = synonym('BEDAT')
    route_schd_id = synonym('AULWE')
    material_availability_dt = synonym('MBDAT')
    material_staging_tm = synonym('MBUHR')
    loading_dt = synonym('LDDAT')
    loading_tm = synonym('LDUHR')
    goods_issue_dt = synonym('WADAT')
    goods_issue_tm = synonym('WAUHR')


################################################################################




################################################################################

class PurchHdr(SAP_Base):
    """\
    Table sourced from: EKKO
    Description: Purchasing Document Header
    """

    __tablename__ = "EKKO"

    EBELN = Column('EBELN', String(10), primary_key = True, doc="""Sourced from EKKO-EBELN // Purchasing Document Number""")
    BUKRS = Column('BUKRS', String(4), default=None, doc="""Sourced from EKKO-BUKRS // Company Code""")
    BSTYP = Column('BSTYP', String(1), default=None, doc="""Sourced from EKKO-BSTYP // Purchasing Document Category""")
    BSART = Column('BSART', String(4), default=None, doc="""Sourced from EKKO-BSART // Purchasing Document Type""")
    BSAKZ = Column('BSAKZ', String(1), default=None, doc="""Sourced from EKKO-BSAKZ // Control indicator for purchasing document type""")
    LOEKZ = Column('LOEKZ', String(1), default=None, doc="""Sourced from EKKO-LOEKZ // Deletion Indicator in Purchasing Document""")
    STATU = Column('STATU', String(1), default=None, doc="""Sourced from EKKO-STATU // Status of Purchasing Document""")
    AEDAT = Column('AEDAT', Date, default=None, doc="""Sourced from EKKO-AEDAT // Date on Which Record Was Created""")
    ERNAM = Column('ERNAM', String(12), default=None, doc="""Sourced from EKKO-ERNAM // Name of Person who Created the Object""")
    PINCR = Column('PINCR', String(5), default=None, doc="""Sourced from EKKO-PINCR // Item Number Interval""")
    LPONR = Column('LPONR', String(5), default=None, doc="""Sourced from EKKO-LPONR // Last Item Number""")
    LIFNR = Column('LIFNR', String(10), default=None, doc="""Sourced from EKKO-LIFNR // Vendor Account Number""")
    SPRAS = Column('SPRAS', String(1), default=None, doc="""Sourced from EKKO-SPRAS // Language Key""")
    ZTERM = Column('ZTERM', String(4), default=None, doc="""Sourced from EKKO-ZTERM // Terms of Payment Key""")
    ZBD1T = Column('ZBD1T', String(3), default=None, doc="""Sourced from EKKO-ZBD1T // Cash (Prompt Payment) Discount Days""")
    ZBD2T = Column('ZBD2T', String(3), default=None, doc="""Sourced from EKKO-ZBD2T // Cash (Prompt Payment) Discount Days""")
    ZBD3T = Column('ZBD3T', String(3), default=None, doc="""Sourced from EKKO-ZBD3T // Cash (Prompt Payment) Discount Days""")
    ZBD1P = Column('ZBD1P', String(5), default=None, doc="""Sourced from EKKO-ZBD1P // Cash Discount Percentage 1""")
    ZBD2P = Column('ZBD2P', String(5), default=None, doc="""Sourced from EKKO-ZBD2P // Cash Discount Percentage 2""")
    EKORG = Column('EKORG', String(4), default=None, doc="""Sourced from EKKO-EKORG // Purchasing Organization""")
    EKGRP = Column('EKGRP', String(3), default=None, doc="""Sourced from EKKO-EKGRP // Purchasing Group""")
    WAERS = Column('WAERS', String(5), default=None, doc="""Sourced from EKKO-WAERS // Currency Key""")
    WKURS = Column('WKURS', Numeric(15,3,3), default=None, doc="""Sourced from EKKO-WKURS // Exchange Rate""")
    KUFIX = Column('KUFIX', Boolean, default=None, doc="""Sourced from EKKO-KUFIX // Indicator: Fixing of Exchange Rate""")
    BEDAT = Column('BEDAT', Date, default=None, doc="""Sourced from EKKO-BEDAT // Purchasing Document Date""")
    KDATB = Column('KDATB', Date, default=None, doc="""Sourced from EKKO-KDATB // Start of Validity Period""")
    KDATE = Column('KDATE', Date, default=None, doc="""Sourced from EKKO-KDATE // End of Validity Period""")
    BWBDT = Column('BWBDT', Date, default=None, doc="""Sourced from EKKO-BWBDT // Closing Date for Applications""")
    ANGDT = Column('ANGDT', Date, default=None, doc="""Sourced from EKKO-ANGDT // Deadline for Submission of Bid/Quotation""")
    BNDDT = Column('BNDDT', Date, default=None, doc="""Sourced from EKKO-BNDDT // Binding Period for Quotation""")
    GWLDT = Column('GWLDT', Date, default=None, doc="""Sourced from EKKO-GWLDT // Warranty Date""")
    AUSNR = Column('AUSNR', String(10), default=None, doc="""Sourced from EKKO-AUSNR // Bid invitation number""")
    ANGNR = Column('ANGNR', String(10), default=None, doc="""Sourced from EKKO-ANGNR // Quotation Number""")
    IHRAN = Column('IHRAN', Date, default=None, doc="""Sourced from EKKO-IHRAN // Quotation Submission Date""")
    IHREZ = Column('IHREZ', String(12), default=None, doc="""Sourced from EKKO-IHREZ // Your Reference""")
    VERKF = Column('VERKF', String(30), default=None, doc="""Sourced from EKKO-VERKF // Responsible Salesperson at Vendor's Office""")
    TELF1 = Column('TELF1', String(16), default=None, doc="""Sourced from EKKO-TELF1 // Vendor's Telephone Number""")
    LLIEF = Column('LLIEF', String(10), default=None, doc="""Sourced from EKKO-LLIEF // Supplying Vendor""")
    KUNNR = Column('KUNNR', String(10), default=None, doc="""Sourced from EKKO-KUNNR // Customer Number""")
    KONNR = Column('KONNR', String(10), default=None, doc="""Sourced from EKKO-KONNR // Number of Principal Purchase Agreement""")
    ABGRU = Column('ABGRU', String(2), default=None, doc="""Sourced from EKKO-ABGRU // Field Not Used""")
    AUTLF = Column('AUTLF', Boolean, default=None, doc="""Sourced from EKKO-AUTLF // Complete Delivery Stipulated for Each Purchase Order""")
    WEAKT = Column('WEAKT', Boolean, default=None, doc="""Sourced from EKKO-WEAKT // Indicator: Goods Receipt Message""")
    RESWK = Column('RESWK', String(4), default=None, doc="""Sourced from EKKO-RESWK // Supplying (Issuing) Plant in Stock Transport Order""")
    LBLIF = Column('LBLIF', String(10), default=None, doc="""Sourced from EKKO-LBLIF // Field not used""")
    INCO1 = Column('INCO1', String(3), default=None, doc="""Sourced from EKKO-INCO1 // Incoterms (Part 1)""")
    INCO2 = Column('INCO2', String(28), default=None, doc="""Sourced from EKKO-INCO2 // Incoterms (Part 2)""")
    KTWRT = Column('KTWRT', Numeric(15,3,3), default=None, doc="""Sourced from EKKO-KTWRT // Target Value for Header Area per Distribution""")
    SUBMI = Column('SUBMI', String(10), default=None, doc="""Sourced from EKKO-SUBMI // Collective Number""")
    KNUMV = Column('KNUMV', String(10), default=None, doc="""Sourced from EKKO-KNUMV // Number of the document condition""")
    KALSM = Column('KALSM', String(6), default=None, doc="""Sourced from EKKO-KALSM // Procedure (Pricing, Output Control, Acct. Det., Costing,...)""")
    STAFO = Column('STAFO', String(6), default=None, doc="""Sourced from EKKO-STAFO // Update group for statistics update""")
    LIFRE = Column('LIFRE', String(10), default=None, doc="""Sourced from EKKO-LIFRE // Different Invoicing Party""")
    EXNUM = Column('EXNUM', String(10), default=None, doc="""Sourced from EKKO-EXNUM // Number of foreign trade data in MM and SD documents""")
    UNSEZ = Column('UNSEZ', String(12), default=None, doc="""Sourced from EKKO-UNSEZ // Our Reference""")
    LOGSY = Column('LOGSY', String(10), default=None, doc="""Sourced from EKKO-LOGSY // Logical System""")
    UPINC = Column('UPINC', String(5), default=None, doc="""Sourced from EKKO-UPINC // Item Number Interval for Subitems""")
    STAKO = Column('STAKO', Boolean, default=None, doc="""Sourced from EKKO-STAKO // Document with time-dependent conditions""")
    FRGGR = Column('FRGGR', String(2), default=None, doc="""Sourced from EKKO-FRGGR // Release group""")
    FRGSX = Column('FRGSX', String(2), default=None, doc="""Sourced from EKKO-FRGSX // Release Strategy""")
    FRGKE = Column('FRGKE', String(1), default=None, doc="""Sourced from EKKO-FRGKE // Release Indicator: Purchasing Document""")
    FRGZU = Column('FRGZU', String(8), default=None, doc="""Sourced from EKKO-FRGZU // Release status""")
    FRGRL = Column('FRGRL', Boolean, default=None, doc="""Sourced from EKKO-FRGRL // Release Not Yet Completely Effected""")
    LANDS = Column('LANDS', String(3), default=None, doc="""Sourced from EKKO-LANDS // Country for Tax Return""")
    LPHIS = Column('LPHIS', Boolean, default=None, doc="""Sourced from EKKO-LPHIS // Indicator for scheduling agreement release documentation""")
    ADRNR = Column('ADRNR', String(10), default=None, doc="""Sourced from EKKO-ADRNR // Address number""")
    STCEG_L = Column('STCEG_L', String(3), default=None, doc="""Sourced from EKKO-STCEG_L // Country of Sales Tax ID Number""")
    STCEG = Column('STCEG', String(20), default=None, doc="""Sourced from EKKO-STCEG // VAT Registration Number""")
    ABSGR = Column('ABSGR', String(2), default=None, doc="""Sourced from EKKO-ABSGR // Reason for Cancellation""")
    ADDNR = Column('ADDNR', String(10), default=None, doc="""Sourced from EKKO-ADDNR // Document number for additional""")
    KORNR = Column('KORNR', String(1), default=None, doc="""Sourced from EKKO-KORNR // Correction of miscellaneous provisions""")
    MEMORY = Column('MEMORY', Boolean, default=None, doc="""Sourced from EKKO-MEMORY // Purchase order not yet complete""")
    PROCSTAT = Column('PROCSTAT', String(2), default=None, doc="""Sourced from EKKO-PROCSTAT // Purchasing document processing state""")
    RLWRT = Column('RLWRT', Numeric(15,3,3), default=None, doc="""Sourced from EKKO-RLWRT // Total value at time of release""")
    REVNO = Column('REVNO', String(8), default=None, doc="""Sourced from EKKO-REVNO // Version number in Purchasing""")
    SCMPROC = Column('SCMPROC', String(1), default=None, doc="""Sourced from EKKO-SCMPROC // SCM Process That Created the Purchase Order""")
    REASON_CODE = Column('REASON_CODE', String(4), default=None, doc="""Sourced from EKKO-REASON_CODE // Goods Receipt Reason Code""")
    MEMORYTYPE = Column('MEMORYTYPE', String(1), default=None, doc="""Sourced from EKKO-MEMORYTYPE // Category of Incompleteness""")
    RETTP = Column('RETTP', String(1), default=None, doc="""Sourced from EKKO-RETTP // Retention Indicator""")
    RETPC = Column('RETPC', String(5), default=None, doc="""Sourced from EKKO-RETPC // Retention in Percent""")
    DPTYP = Column('DPTYP', String(4), default=None, doc="""Sourced from EKKO-DPTYP // Down Payment Indicator""")
    DPPCT = Column('DPPCT', String(5), default=None, doc="""Sourced from EKKO-DPPCT // Down Payment Percentage""")
    DPAMT = Column('DPAMT', Numeric(15,3,3), default=None, doc="""Sourced from EKKO-DPAMT // Down Payment Amount in Document Currency""")
    DPDAT = Column('DPDAT', String(8), default=None, doc="""Sourced from EKKO-DPDAT // Due Date for Down Payment""")
    MSR_ID = Column('MSR_ID', String(10), default=None, doc="""Sourced from EKKO-MSR_ID // Process Identification Number""")
    HIERARCHY_EXISTS = Column('HIERARCHY_EXISTS', Boolean, default=None, doc="""Sourced from EKKO-HIERARCHY_EXISTS // Part of a Contract Hierarchy""")
    THRESHOLD_EXISTS = Column('THRESHOLD_EXISTS', Boolean, default=None, doc="""Sourced from EKKO-THRESHOLD_EXISTS // Threshold Value for Exchange Rates Exists""")
    LEGAL_CONTRACT = Column('LEGAL_CONTRACT', String(40), default=None, doc="""Sourced from EKKO-LEGAL_CONTRACT // Legal Contract Number""")
    DESCRIPTION = Column('DESCRIPTION', String(40), default=None, doc="""Sourced from EKKO-DESCRIPTION // Contract Name""")
    RELEASE_DATE = Column('RELEASE_DATE', Date, default=None, doc="""Sourced from EKKO-RELEASE_DATE // Release Date of Contract""")
    VSART = Column('VSART', String(2), default=None, doc="""Sourced from EKKO-VSART // Shipping type""")
    HANDOVERLOC = Column('HANDOVERLOC', String(10), default=None, doc="""Sourced from EKKO-HANDOVERLOC // Location for a physical handover of goods""")
    SHIPCOND = Column('SHIPCOND', String(2), default=None, doc="""Sourced from EKKO-SHIPCOND // Shipping Conditions""")
    FORCE_ID = Column('FORCE_ID', String(32), default=None, doc="""Sourced from EKKO-FORCE_ID // Internal Key for Force Element""")
    FORCE_CNT = Column('FORCE_CNT', String(6), default=None, doc="""Sourced from EKKO-FORCE_CNT // Internal (Version) Counter""")
    RELOC_ID = Column('RELOC_ID', String(10), default=None, doc="""Sourced from EKKO-RELOC_ID // Relocation ID""")
    RELOC_SEQ_ID = Column('RELOC_SEQ_ID', String(4), default=None, doc="""Sourced from EKKO-RELOC_SEQ_ID // Relocation Step ID""")
    ZZPORNUM = Column('ZZPORNUM', String(10), default=None, doc="""Sourced from EKKO-ZZPORNUM // PO response from SRM""")
    ZZBUYER = Column('ZZBUYER', String(12), default=None, doc="""Sourced from EKKO-ZZBUYER // P2P Old - Do not use anymore""")
    ZZLEASING_COMP = Column('ZZLEASING_COMP', String(10), default=None, doc="""Sourced from EKKO-ZZLEASING_COMP // Account Number of Vendor or Creditor""")
    POHF_TYPE = Column('POHF_TYPE', String(1), default=None, doc="""Sourced from EKKO-POHF_TYPE // Document for Seasonal Purchase Order Processing""")
    EQ_EINDT = Column('EQ_EINDT', String(8), default=None, doc="""Sourced from EKKO-EQ_EINDT // Delivery Date Header: All Items Have Same Delivery Date""")
    EQ_WERKS = Column('EQ_WERKS', String(4), default=None, doc="""Sourced from EKKO-EQ_WERKS // Plant Header: All Items Have Same Receiving Plant""")
    FIXPO = Column('FIXPO', String(1), default=None, doc="""Sourced from EKKO-FIXPO // Firm Deal Indicator""")
    EKGRP_ALLOW = Column('EKGRP_ALLOW', String(1), default=None, doc="""Sourced from EKKO-EKGRP_ALLOW // Take Account of Purch. Group""")
    WERKS_ALLOW = Column('WERKS_ALLOW', String(1), default=None, doc="""Sourced from EKKO-WERKS_ALLOW // Take Account of Plants""")
    CONTRACT_ALLOW = Column('CONTRACT_ALLOW', String(1), default=None, doc="""Sourced from EKKO-CONTRACT_ALLOW // Take Account of Contracts""")
    PSTYP_ALLOW = Column('PSTYP_ALLOW', String(1), default=None, doc="""Sourced from EKKO-PSTYP_ALLOW // Take Account of Item Categories""")
    FIXPO_ALLOW = Column('FIXPO_ALLOW', String(1), default=None, doc="""Sourced from EKKO-FIXPO_ALLOW // Take Account of Fixed-Date Purchases Indicator""")
    KEY_ID_ALLOW = Column('KEY_ID_ALLOW', String(1), default=None, doc="""Sourced from EKKO-KEY_ID_ALLOW // Consider Budget""")
    AUREL_ALLOW = Column('AUREL_ALLOW', String(1), default=None, doc="""Sourced from EKKO-AUREL_ALLOW // Take Account of Alloc. Table Relevance""")
    DELPER_ALLOW = Column('DELPER_ALLOW', String(1), default=None, doc="""Sourced from EKKO-DELPER_ALLOW // Take Account of Dlvy Period""")
    EINDT_ALLOW = Column('EINDT_ALLOW', String(1), default=None, doc="""Sourced from EKKO-EINDT_ALLOW // Take Account of Delivery Date""")
    OTB_LEVEL = Column('OTB_LEVEL', String(1), default=None, doc="""Sourced from EKKO-OTB_LEVEL // OTB Check Level""")
    OTB_COND_TYPE = Column('OTB_COND_TYPE', String(4), default=None, doc="""Sourced from EKKO-OTB_COND_TYPE // OTB Condition Type""")
    KEY_ID = Column('KEY_ID', String(16), default=None, doc="""Sourced from EKKO-KEY_ID // Unique Number of Budget""")
    OTB_VALUE = Column('OTB_VALUE', String(17), default=None, doc="""Sourced from EKKO-OTB_VALUE // Required Budget""")
    OTB_CURR = Column('OTB_CURR', String(5), default=None, doc="""Sourced from EKKO-OTB_CURR // OTB Currency""")
    OTB_RES_VALUE = Column('OTB_RES_VALUE', String(17), default=None, doc="""Sourced from EKKO-OTB_RES_VALUE // Reserved Budget for OTB-Relevant Purchasing Document""")
    OTB_SPEC_VALUE = Column('OTB_SPEC_VALUE', String(17), default=None, doc="""Sourced from EKKO-OTB_SPEC_VALUE // Special Release Budget""")
    SPR_RSN_PROFILE = Column('SPR_RSN_PROFILE', String(4), default=None, doc="""Sourced from EKKO-SPR_RSN_PROFILE // Reason Profile for OTB Special Release""")
    BUDG_TYPE = Column('BUDG_TYPE', String(2), default=None, doc="""Sourced from EKKO-BUDG_TYPE // Budget Type""")
    OTB_STATUS = Column('OTB_STATUS', String(1), default=None, doc="""Sourced from EKKO-OTB_STATUS // OTB Check Status""")
    OTB_REASON = Column('OTB_REASON', String(3), default=None, doc="""Sourced from EKKO-OTB_REASON // Reason Indicator for OTB Check Status""")
    CHECK_TYPE = Column('CHECK_TYPE', String(1), default=None, doc="""Sourced from EKKO-CHECK_TYPE // Type of OTB Check""")
    CON_OTB_REQ = Column('CON_OTB_REQ', String(1), default=None, doc="""Sourced from EKKO-CON_OTB_REQ // OTB-Relevant Contract""")
    CON_PREBOOK_LEV = Column('CON_PREBOOK_LEV', String(1), default=None, doc="""Sourced from EKKO-CON_PREBOOK_LEV // OTB Indicator Level for Contracts""")
    CON_DISTR_LEV = Column('CON_DISTR_LEV', String(1), default=None, doc="""Sourced from EKKO-CON_DISTR_LEV // Distribution Using Target Value or Item Data""")

    prch_doc_id = synonym('EBELN')
    company_cd = synonym('BUKRS')
    prch_doc_ctgy_cd = synonym('BSTYP')
    prch_ord_type_cd = synonym('BSART')
    prch_doc_type_cntrl_cd = synonym('BSAKZ')
    update_dt = synonym('AEDAT')
    doc_create_user_id = synonym('ERNAM')
    language_cd = synonym('SPRAS')
    prch_org_cd = synonym('EKORG')
    prch_grp_cd = synonym('EKGRP')
    currency_cd = synonym('WAERS')
    prch_ord_dt = synonym('BEDAT')
    validity_period_start_dt = synonym('KDATB')
    validity_period_end_dt = synonym('KDATE')
    quote_validity_dt = synonym('ANGDT')
    quote_valid_to_dt = synonym('BNDDT')
    guarantee_dt = synonym('GWLDT')
    quote_id = synonym('ANGNR')
    quote_submission_dt = synonym('IHRAN')
    customer_id = synonym('KUNNR')
    rej_reas_id = synonym('ABGRU')
    sto_source_facility_id = synonym('RESWK')
    incoterms_cd = synonym('INCO1')
    incoterms_desc = synonym('INCO2')
    release_grp_cd = synonym('FRGGR')
    release_strategy_cd = synonym('FRGSX')
    prch_doc_release_cd = synonym('FRGKE')
    release_status_cd = synonym('FRGZU')
    incomplete_release_ind = synonym('FRGRL')
    issuing_country_cd = synonym('LANDS')
    addr_id = synonym('ADRNR')
    incompleteness_ctgy_cd = synonym('MEMORYTYPE')


################################################################################




################################################################################

class PurchItem(SAP_Base):
    """\
    Table sourced from: EKPO
    Description: Purchasing Document Item
    """

    __tablename__ = "EKPO"

    EBELN = Column('EBELN', String(10), primary_key = True, doc="""Sourced from EKPO-EBELN // Purchasing Document Number""")
    EBELP = Column('EBELP', String(5), primary_key = True, doc="""Sourced from EKPO-EBELP // Item Number of Purchasing Document""")
    LOEKZ = Column('LOEKZ', String(1), default=None, doc="""Sourced from EKPO-LOEKZ // Deletion Indicator in Purchasing Document""")
    STATU = Column('STATU', String(1), default=None, doc="""Sourced from EKPO-STATU // RFQ status""")
    AEDAT = Column('AEDAT', Date, default=None, doc="""Sourced from EKPO-AEDAT // Purchasing Document Item Change Date""")
    TXZ01 = Column('TXZ01', String(40), default=None, doc="""Sourced from EKPO-TXZ01 // Short Text""")
    MATNR = Column('MATNR', String(18), default=None, doc="""Sourced from EKPO-MATNR // Material Number""")
    EMATN = Column('EMATN', String(18), default=None, doc="""Sourced from EKPO-EMATN // Material Number""")
    BUKRS = Column('BUKRS', String(4), default=None, doc="""Sourced from EKPO-BUKRS // Company Code""")
    WERKS = Column('WERKS', String(4), default=None, doc="""Sourced from EKPO-WERKS // Plant""")
    LGORT = Column('LGORT', String(4), default=None, doc="""Sourced from EKPO-LGORT // Storage Location""")
    BEDNR = Column('BEDNR', String(10), default=None, doc="""Sourced from EKPO-BEDNR // Requirement Tracking Number""")
    MATKL = Column('MATKL', String(9), default=None, doc="""Sourced from EKPO-MATKL // Material Group""")
    INFNR = Column('INFNR', String(10), default=None, doc="""Sourced from EKPO-INFNR // Number of Purchasing Info Record""")
    IDNLF = Column('IDNLF', String(35), default=None, doc="""Sourced from EKPO-IDNLF // Material Number Used by Vendor""")
    KTMNG = Column('KTMNG', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-KTMNG // Target Quantity""")
    MENGE = Column('MENGE', String(13), default=None, doc="""Sourced from EKPO-MENGE // Purchase Order Quantity""")
    MEINS = Column('MEINS', String(3), default=None, doc="""Sourced from EKPO-MEINS // Purchase Order Unit of Measure""")
    BPRME = Column('BPRME', String(3), default=None, doc="""Sourced from EKPO-BPRME // Order Price Unit (Purchasing)""")
    BPUMZ = Column('BPUMZ', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-BPUMZ // Numerator for Conversion of Order Price Unit into Order Unit""")
    BPUMN = Column('BPUMN', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-BPUMN // Denominator for Conv. of Order Price Unit into Order Unit""")
    UMREZ = Column('UMREZ', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-UMREZ // Numerator for Conversion of Order Unit to Base Unit""")
    UMREN = Column('UMREN', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-UMREN // Denominator for Conversion of Order Unit to Base Unit""")
    NETPR = Column('NETPR', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-NETPR // Net Price in Purchasing Document (in Document Currency)""")
    PEINH = Column('PEINH', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-PEINH // Price Unit""")
    NETWR = Column('NETWR', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-NETWR // Net Order Value in PO Currency""")
    BRTWR = Column('BRTWR', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-BRTWR // Gross order value in PO currency""")
    AGDAT = Column('AGDAT', String(8), default=None, doc="""Sourced from EKPO-AGDAT // Deadline for Submission of Bid/Quotation""")
    WEBAZ = Column('WEBAZ', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-WEBAZ // Goods Receipt Processing Time in Days""")
    MWSKZ = Column('MWSKZ', String(2), default=None, doc="""Sourced from EKPO-MWSKZ // Tax on sales/purchases code""")
    BONUS = Column('BONUS', String(2), default=None, doc="""Sourced from EKPO-BONUS // Settlement Group 1 (Purchasing)""")
    INSMK = Column('INSMK', String(1), default=None, doc="""Sourced from EKPO-INSMK // Stock Type""")
    SPINF = Column('SPINF', String(1), default=None, doc="""Sourced from EKPO-SPINF // Indicator: Update Info Record""")
    PRSDR = Column('PRSDR', Boolean, default=None, doc="""Sourced from EKPO-PRSDR // Price Printout""")
    SCHPR = Column('SCHPR', Boolean, default=None, doc="""Sourced from EKPO-SCHPR // Indicator: Estimated Price""")
    MAHNZ = Column('MAHNZ', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-MAHNZ // Number of Reminders/Expediters""")
    MAHN1 = Column('MAHN1', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-MAHN1 // Number of Days for First Reminder/Expediter""")
    MAHN2 = Column('MAHN2', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-MAHN2 // Number of Days for Second Reminder/Expediter""")
    MAHN3 = Column('MAHN3', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-MAHN3 // Number of Days for Third Reminder/Expediter""")
    UEBTO = Column('UEBTO', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-UEBTO // Overdelivery Tolerance Limit""")
    UEBTK = Column('UEBTK', Boolean, default=None, doc="""Sourced from EKPO-UEBTK // Indicator: Unlimited Overdelivery Allowed""")
    UNTTO = Column('UNTTO', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-UNTTO // Underdelivery Tolerance Limit""")
    BWTAR = Column('BWTAR', String(10), default=None, doc="""Sourced from EKPO-BWTAR // Valuation Type""")
    BWTTY = Column('BWTTY', String(1), default=None, doc="""Sourced from EKPO-BWTTY // Valuation Category""")
    ABSKZ = Column('ABSKZ', Boolean, default=None, doc="""Sourced from EKPO-ABSKZ // Rejection Indicator""")
    AGMEM = Column('AGMEM', String(3), default=None, doc="""Sourced from EKPO-AGMEM // Internal Comment on Quotation""")
    ELIKZ = Column('ELIKZ', Boolean, default=None, doc="""Sourced from EKPO-ELIKZ // 'Delivery Completed' Indicator""")
    EREKZ = Column('EREKZ', Boolean, default=None, doc="""Sourced from EKPO-EREKZ // Final Invoice Indicator""")
    PSTYP = Column('PSTYP', String(1), default=None, doc="""Sourced from EKPO-PSTYP // Item Category in Purchasing Document""")
    KNTTP = Column('KNTTP', String(1), default=None, doc="""Sourced from EKPO-KNTTP // Account Assignment Category""")
    KZVBR = Column('KZVBR', String(1), default=None, doc="""Sourced from EKPO-KZVBR // Consumption Posting""")
    VRTKZ = Column('VRTKZ', String(1), default=None, doc="""Sourced from EKPO-VRTKZ // Distribution indicator for multiple account assignment""")
    TWRKZ = Column('TWRKZ', String(1), default=None, doc="""Sourced from EKPO-TWRKZ // Partial Invoice Indicator""")
    WEPOS = Column('WEPOS', Boolean, default=None, doc="""Sourced from EKPO-WEPOS // Goods Receipt Indicator""")
    WEUNB = Column('WEUNB', Boolean, default=None, doc="""Sourced from EKPO-WEUNB // Goods Receipt, Non-Valuated""")
    REPOS = Column('REPOS', Boolean, default=None, doc="""Sourced from EKPO-REPOS // Invoice Receipt Indicator""")
    WEBRE = Column('WEBRE', Boolean, default=None, doc="""Sourced from EKPO-WEBRE // Indicator: GR-Based Invoice Verification""")
    KZABS = Column('KZABS', Boolean, default=None, doc="""Sourced from EKPO-KZABS // Order Acknowledgment Requirement""")
    LABNR = Column('LABNR', String(20), default=None, doc="""Sourced from EKPO-LABNR // Order Acknowledgment Number""")
    KONNR = Column('KONNR', String(10), default=None, doc="""Sourced from EKPO-KONNR // Number of Principal Purchase Agreement""")
    KTPNR = Column('KTPNR', String(5), default=None, doc="""Sourced from EKPO-KTPNR // Item Number of Principal Purchase Agreement""")
    ABDAT = Column('ABDAT', Date, default=None, doc="""Sourced from EKPO-ABDAT // Reconciliation Date for Agreed Cumulative Quantity""")
    ABFTZ = Column('ABFTZ', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-ABFTZ // Agreed Cumulative Quantity""")
    ETFZ1 = Column('ETFZ1', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-ETFZ1 // Firm Zone (Go-Ahead for Production)""")
    ETFZ2 = Column('ETFZ2', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-ETFZ2 // Trade-Off Zone (Go-Ahead for Materials Procurement)""")
    KZSTU = Column('KZSTU', String(1), default=None, doc="""Sourced from EKPO-KZSTU // Firm/Trade-Off Zones Binding with Regard to Mat. Planning""")
    NOTKZ = Column('NOTKZ', Boolean, default=None, doc="""Sourced from EKPO-NOTKZ // Exclusion in Outline Agreement Item with Material Class""")
    LMEIN = Column('LMEIN', String(3), default=None, doc="""Sourced from EKPO-LMEIN // Base Unit of Measure""")
    EVERS = Column('EVERS', String(2), default=None, doc="""Sourced from EKPO-EVERS // Shipping Instructions""")
    ZWERT = Column('ZWERT', String(13), default=None, doc="""Sourced from EKPO-ZWERT // Target Value for Outline Agreement in Document Currency""")
    NAVNW = Column('NAVNW', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-NAVNW // Non-deductible input tax""")
    ABMNG = Column('ABMNG', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-ABMNG // Standard release order quantity""")
    PRDAT = Column('PRDAT', Date, default=None, doc="""Sourced from EKPO-PRDAT // Date of Price Determination""")
    BSTYP = Column('BSTYP', String(1), default=None, doc="""Sourced from EKPO-BSTYP // Purchasing Document Category""")
    EFFWR = Column('EFFWR', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-EFFWR // Effective value of item""")
    XOBLR = Column('XOBLR', Boolean, default=None, doc="""Sourced from EKPO-XOBLR // Item affects commitments""")
    KUNNR = Column('KUNNR', String(10), default=None, doc="""Sourced from EKPO-KUNNR // Customer""")
    ADRNR = Column('ADRNR', String(10), default=None, doc="""Sourced from EKPO-ADRNR // Manual address number in purchasing document item""")
    EKKOL = Column('EKKOL', String(4), default=None, doc="""Sourced from EKPO-EKKOL // Condition Group with Vendor""")
    SKTOF = Column('SKTOF', Boolean, default=None, doc="""Sourced from EKPO-SKTOF // Item Does Not Qualify for Cash Discount""")
    STAFO = Column('STAFO', String(6), default=None, doc="""Sourced from EKPO-STAFO // Update group for statistics update""")
    PLIFZ = Column('PLIFZ', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-PLIFZ // Planned Delivery Time in Days""")
    NTGEW = Column('NTGEW', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-NTGEW // Net Weight""")
    GEWEI = Column('GEWEI', String(3), default=None, doc="""Sourced from EKPO-GEWEI // Unit of Weight""")
    TXJCD = Column('TXJCD', String(15), default=None, doc="""Sourced from EKPO-TXJCD // Tax Jurisdiction""")
    ETDRK = Column('ETDRK', String(1), default=None, doc="""Sourced from EKPO-ETDRK // Indicator: Print-relevant schedule lines exist""")
    SOBKZ = Column('SOBKZ', String(1), default=None, doc="""Sourced from EKPO-SOBKZ // Special Stock Indicator""")
    ARSNR = Column('ARSNR', String(10), default=None, doc="""Sourced from EKPO-ARSNR // Settlement reservation number""")
    ARSPS = Column('ARSPS', String(4), default=None, doc="""Sourced from EKPO-ARSPS // Item number of the settlement reservation""")
    INSNC = Column('INSNC', Boolean, default=None, doc="""Sourced from EKPO-INSNC // Quality inspection indicator cannot be changed""")
    SSQSS = Column('SSQSS', String(8), default=None, doc="""Sourced from EKPO-SSQSS // Control Key for Quality Management in Procurement""")
    ZGTYP = Column('ZGTYP', String(4), default=None, doc="""Sourced from EKPO-ZGTYP // Certificate Type""")
    EAN11 = Column('EAN11', String(18), default=None, doc="""Sourced from EKPO-EAN11 // International Article Number (EAN/UPC)""")
    BSTAE = Column('BSTAE', String(4), default=None, doc="""Sourced from EKPO-BSTAE // Confirmation Control Key""")
    REVLV = Column('REVLV', String(2), default=None, doc="""Sourced from EKPO-REVLV // Revision Level""")
    GEBER = Column('GEBER', String(10), default=None, doc="""Sourced from EKPO-GEBER // Fund""")
    FISTL = Column('FISTL', String(16), default=None, doc="""Sourced from EKPO-FISTL // Funds Center""")
    FIPOS = Column('FIPOS', String(14), default=None, doc="""Sourced from EKPO-FIPOS // Commitment Item""")
    KO_GSBER = Column('KO_GSBER', String(4), default=None, doc="""Sourced from EKPO-KO_GSBER // Business area reported to the partner""")
    KO_PARGB = Column('KO_PARGB', String(4), default=None, doc="""Sourced from EKPO-KO_PARGB // assumed business area of the business partner""")
    KO_PRCTR = Column('KO_PRCTR', String(10), default=None, doc="""Sourced from EKPO-KO_PRCTR // Profit Center""")
    KO_PPRCTR = Column('KO_PPRCTR', String(10), default=None, doc="""Sourced from EKPO-KO_PPRCTR // Partner Profit Center""")
    MEPRF = Column('MEPRF', String(1), default=None, doc="""Sourced from EKPO-MEPRF // Price Determination (Pricing) Date Control""")
    BRGEW = Column('BRGEW', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-BRGEW // Gross Weight""")
    VOLUM = Column('VOLUM', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-VOLUM // Volume""")
    VOLEH = Column('VOLEH', String(3), default=None, doc="""Sourced from EKPO-VOLEH // Volume unit""")
    INCO1 = Column('INCO1', String(3), default=None, doc="""Sourced from EKPO-INCO1 // Incoterms (Part 1)""")
    INCO2 = Column('INCO2', String(28), default=None, doc="""Sourced from EKPO-INCO2 // Incoterms (Part 2)""")
    VORAB = Column('VORAB', Boolean, default=None, doc="""Sourced from EKPO-VORAB // Advance procurement: project stock""")
    KOLIF = Column('KOLIF', String(10), default=None, doc="""Sourced from EKPO-KOLIF // Prior Vendor""")
    LTSNR = Column('LTSNR', String(6), default=None, doc="""Sourced from EKPO-LTSNR // Vendor Subrange""")
    PACKNO = Column('PACKNO', String(10), default=None, doc="""Sourced from EKPO-PACKNO // Package number""")
    FPLNR = Column('FPLNR', String(10), default=None, doc="""Sourced from EKPO-FPLNR // Invoicing plan number""")
    GNETWR = Column('GNETWR', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-GNETWR // Currently not used""")
    STAPO = Column('STAPO', Boolean, default=None, doc="""Sourced from EKPO-STAPO // Item is statistical""")
    UEBPO = Column('UEBPO', String(5), default=None, doc="""Sourced from EKPO-UEBPO // Higher-Level Item in Purchasing Documents""")
    LEWED = Column('LEWED', Date, default=None, doc="""Sourced from EKPO-LEWED // Latest Possible Goods Receipt""")
    EMLIF = Column('EMLIF', String(10), default=None, doc="""Sourced from EKPO-EMLIF // Vendor to be supplied/who is to receive delivery""")
    LBLKZ = Column('LBLKZ', Boolean, default=None, doc="""Sourced from EKPO-LBLKZ // Subcontracting vendor""")
    SATNR = Column('SATNR', String(18), default=None, doc="""Sourced from EKPO-SATNR // Cross-Plant Configurable Material""")
    ATTYP = Column('ATTYP', String(2), default=None, doc="""Sourced from EKPO-ATTYP // Material Category""")
    VSART = Column('VSART', String(2), default=None, doc="""Sourced from EKPO-VSART // Shipping type""")
    HANDOVERLOC = Column('HANDOVERLOC', String(10), default=None, doc="""Sourced from EKPO-HANDOVERLOC // Location for a physical handover of goods""")
    KANBA = Column('KANBA', String(1), default=None, doc="""Sourced from EKPO-KANBA // Kanban Indicator""")
    ADRN2 = Column('ADRN2', String(10), default=None, doc="""Sourced from EKPO-ADRN2 // Number of delivery address""")
    CUOBJ = Column('CUOBJ', String(18), default=None, doc="""Sourced from EKPO-CUOBJ // Configuration (internal object number)""")
    XERSY = Column('XERSY', Boolean, default=None, doc="""Sourced from EKPO-XERSY // Evaluated Receipt Settlement (ERS)""")
    EILDT = Column('EILDT', Date, default=None, doc="""Sourced from EKPO-EILDT // Start Date for GR-Based Settlement""")
    DRDAT = Column('DRDAT', Date, default=None, doc="""Sourced from EKPO-DRDAT // Last Transmission""")
    DRUHR = Column('DRUHR', Time, default=None, doc="""Sourced from EKPO-DRUHR // Time""")
    DRUNR = Column('DRUNR', String(4), default=None, doc="""Sourced from EKPO-DRUNR // Sequential Number""")
    AKTNR = Column('AKTNR', String(10), default=None, doc="""Sourced from EKPO-AKTNR // Promotion""")
    ABELN = Column('ABELN', String(10), default=None, doc="""Sourced from EKPO-ABELN // Allocation Table Number""")
    ABELP = Column('ABELP', String(5), default=None, doc="""Sourced from EKPO-ABELP // Item number of allocation table""")
    ANZPU = Column('ANZPU', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-ANZPU // Number of Points""")
    PUNEI = Column('PUNEI', String(3), default=None, doc="""Sourced from EKPO-PUNEI // Points unit""")
    SAISO = Column('SAISO', String(4), default=None, doc="""Sourced from EKPO-SAISO // Season Category""")
    SAISJ = Column('SAISJ', String(4), default=None, doc="""Sourced from EKPO-SAISJ // Season Year""")
    EBON2 = Column('EBON2', String(2), default=None, doc="""Sourced from EKPO-EBON2 // Settlement Group 2 (Rebate Settlement, Purchasing)""")
    EBON3 = Column('EBON3', String(2), default=None, doc="""Sourced from EKPO-EBON3 // Settlement Group 3 (Rebate Settlement, Purchasing)""")
    EBONF = Column('EBONF', Boolean, default=None, doc="""Sourced from EKPO-EBONF // Item Relevant to Subsequent (Period-End Rebate) Settlement""")
    MLMAA = Column('MLMAA', Boolean, default=None, doc="""Sourced from EKPO-MLMAA // Material ledger activated at material level""")
    MHDRZ = Column('MHDRZ', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-MHDRZ // Minimum Remaining Shelf Life""")
    ANFNR = Column('ANFNR', String(10), default=None, doc="""Sourced from EKPO-ANFNR // RFQ Number""")
    ANFPS = Column('ANFPS', String(5), default=None, doc="""Sourced from EKPO-ANFPS // Item Number of RFQ""")
    KZKFG = Column('KZKFG', String(1), default=None, doc="""Sourced from EKPO-KZKFG // Origin of Configuration""")
    USEQU = Column('USEQU', String(1), default=None, doc="""Sourced from EKPO-USEQU // Quota arrangement usage""")
    UMSOK = Column('UMSOK', String(1), default=None, doc="""Sourced from EKPO-UMSOK // Special Stock Indicator for Physical Stock Transfer""")
    BANFN = Column('BANFN', String(10), default=None, doc="""Sourced from EKPO-BANFN // Purchase Requisition Number""")
    BNFPO = Column('BNFPO', String(5), default=None, doc="""Sourced from EKPO-BNFPO // Item Number of Purchase Requisition""")
    MTART = Column('MTART', String(4), default=None, doc="""Sourced from EKPO-MTART // Material Type""")
    UPTYP = Column('UPTYP', String(1), default=None, doc="""Sourced from EKPO-UPTYP // Subitem Category, Purchasing Document""")
    UPVOR = Column('UPVOR', String(1), default=None, doc="""Sourced from EKPO-UPVOR // Subitems Exist""")
    KZWI1 = Column('KZWI1', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-KZWI1 // Subtotal 1 from pricing procedure for condition""")
    KZWI2 = Column('KZWI2', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-KZWI2 // Subtotal 2 from pricing procedure for condition""")
    KZWI3 = Column('KZWI3', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-KZWI3 // Subtotal 3 from pricing procedure for condition""")
    KZWI4 = Column('KZWI4', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-KZWI4 // Subtotal 4 from pricing procedure for condition""")
    KZWI5 = Column('KZWI5', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-KZWI5 // Subtotal 5 from pricing procedure for condition""")
    KZWI6 = Column('KZWI6', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-KZWI6 // Subtotal 6 from pricing procedure for condition""")
    SIKGR = Column('SIKGR', String(3), default=None, doc="""Sourced from EKPO-SIKGR // Processing key for sub-items""")
    MFZHI = Column('MFZHI', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-MFZHI // Maximum Cumulative Material Go-Ahead Quantity""")
    FFZHI = Column('FFZHI', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-FFZHI // Maximum Cumulative Production Go-Ahead Quantity""")
    RETPO = Column('RETPO', Boolean, default=None, doc="""Sourced from EKPO-RETPO // Returns Item""")
    AUREL = Column('AUREL', String(1), default=None, doc="""Sourced from EKPO-AUREL // Relevant to Allocation Table""")
    BSGRU = Column('BSGRU', String(3), default=None, doc="""Sourced from EKPO-BSGRU // Reason for Ordering""")
    LFRET = Column('LFRET', String(4), default=None, doc="""Sourced from EKPO-LFRET // Delivery Type for Returns to Vendors""")
    MFRGR = Column('MFRGR', String(8), default=None, doc="""Sourced from EKPO-MFRGR // Material freight group""")
    NRFHG = Column('NRFHG', String(1), default=None, doc="""Sourced from EKPO-NRFHG // Material qualifies for discount in kind""")
    J_1BNBM = Column('J_1BNBM', String(16), default=None, doc="""Sourced from EKPO-J_1BNBM // Brazilian NCM Code""")
    J_1BMATUSE = Column('J_1BMATUSE', String(1), default=None, doc="""Sourced from EKPO-J_1BMATUSE // Usage of the material""")
    J_1BMATORG = Column('J_1BMATORG', String(1), default=None, doc="""Sourced from EKPO-J_1BMATORG // Origin of the material""")
    J_1BOWNPRO = Column('J_1BOWNPRO', Boolean, default=None, doc="""Sourced from EKPO-J_1BOWNPRO // Produced in-house""")
    J_1BINDUST = Column('J_1BINDUST', String(2), default=None, doc="""Sourced from EKPO-J_1BINDUST // Material CFOP category""")
    ABUEB = Column('ABUEB', String(4), default=None, doc="""Sourced from EKPO-ABUEB // Release Creation Profile""")
    NLABD = Column('NLABD', Date, default=None, doc="""Sourced from EKPO-NLABD // Next Forecast Delivery Schedule Transmission""")
    NFABD = Column('NFABD', Date, default=None, doc="""Sourced from EKPO-NFABD // Next JIT Delivery Schedule Transmission""")
    KZBWS = Column('KZBWS', String(1), default=None, doc="""Sourced from EKPO-KZBWS // Valuation of Special Stock""")
    BONBA = Column('BONBA', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-BONBA // Rebate basis 1""")
    FABKZ = Column('FABKZ', String(1), default=None, doc="""Sourced from EKPO-FABKZ // Indicator: Item Relevant to JIT Delivery Schedules""")
    J_1AINDXP = Column('J_1AINDXP', String(5), default=None, doc="""Sourced from EKPO-J_1AINDXP // Inflation Index""")
    J_1AIDATEP = Column('J_1AIDATEP', Date, default=None, doc="""Sourced from EKPO-J_1AIDATEP // Inflation Index Date""")
    MPROF = Column('MPROF', String(4), default=None, doc="""Sourced from EKPO-MPROF // Manufacturer Part Profile""")
    EGLKZ = Column('EGLKZ', Boolean, default=None, doc="""Sourced from EKPO-EGLKZ // 'Outward Delivery Completed' Indicator""")
    KZTLF = Column('KZTLF', String(1), default=None, doc="""Sourced from EKPO-KZTLF // Partial Delivery at Item Level (Stock Transfer)""")
    KZFME = Column('KZFME', String(1), default=None, doc="""Sourced from EKPO-KZFME // Units of measure usage""")
    RDPRF = Column('RDPRF', String(4), default=None, doc="""Sourced from EKPO-RDPRF // Rounding Profile""")
    TECHS = Column('TECHS', String(12), default=None, doc="""Sourced from EKPO-TECHS // Parameter Variant/Standard Variant""")
    CHG_SRV = Column('CHG_SRV', Boolean, default=None, doc="""Sourced from EKPO-CHG_SRV // Configuration changed""")
    CHG_FPLNR = Column('CHG_FPLNR', Boolean, default=None, doc="""Sourced from EKPO-CHG_FPLNR // No invoice for this item although not free of charge""")
    MFRPN = Column('MFRPN', String(40), default=None, doc="""Sourced from EKPO-MFRPN // Manufacturer Part Number""")
    MFRNR = Column('MFRNR', String(10), default=None, doc="""Sourced from EKPO-MFRNR // Number of a Manufacturer""")
    EMNFR = Column('EMNFR', String(10), default=None, doc="""Sourced from EKPO-EMNFR // External manufacturer code name or number""")
    NOVET = Column('NOVET', Boolean, default=None, doc="""Sourced from EKPO-NOVET // Item blocked for SD delivery""")
    AFNAM = Column('AFNAM', String(12), default=None, doc="""Sourced from EKPO-AFNAM // Name of Requisitioner/Requester""")
    TZONRC = Column('TZONRC', String(6), default=None, doc="""Sourced from EKPO-TZONRC // Time zone of recipient location""")
    IPRKZ = Column('IPRKZ', String(1), default=None, doc="""Sourced from EKPO-IPRKZ // Period Indicator for Shelf Life Expiration Date""")
    LEBRE = Column('LEBRE', Boolean, default=None, doc="""Sourced from EKPO-LEBRE // Indicator for Service-Based Invoice Verification""")
    BERID = Column('BERID', String(10), default=None, doc="""Sourced from EKPO-BERID // MRP Area""")
    XCONDITIONS = Column('XCONDITIONS', String(1), default=None, doc="""Sourced from EKPO-XCONDITIONS // Conditions for item although no invoice""")
    APOMS = Column('APOMS', String(1), default=None, doc="""Sourced from EKPO-APOMS // APO as Planning System""")
    CCOMP = Column('CCOMP', String(1), default=None, doc="""Sourced from EKPO-CCOMP // Posting Logic in the Case of Stock Transfers""")
    GRANT_NBR = Column('GRANT_NBR', String(20), default=None, doc="""Sourced from EKPO-GRANT_NBR // Grant""")
    FKBER = Column('FKBER', String(16), default=None, doc="""Sourced from EKPO-FKBER // Functional Area""")
    STATUS = Column('STATUS', String(1), default=None, doc="""Sourced from EKPO-STATUS // Status of Purchasing Document Item""")
    RESLO = Column('RESLO', String(4), default=None, doc="""Sourced from EKPO-RESLO // Issuing Storage Location for Stock Transport Order""")
    KBLNR = Column('KBLNR', String(10), default=None, doc="""Sourced from EKPO-KBLNR // Document Number for Earmarked Funds""")
    KBLPOS = Column('KBLPOS', String(3), default=None, doc="""Sourced from EKPO-KBLPOS // Earmarked Funds: Document Item""")
    WEORA = Column('WEORA', Boolean, default=None, doc="""Sourced from EKPO-WEORA // Acceptance At Origin""")
    SRV_BAS_COM = Column('SRV_BAS_COM', Boolean, default=None, doc="""Sourced from EKPO-SRV_BAS_COM // Service-Based Commitment""")
    PRIO_URG = Column('PRIO_URG', String(2), default=None, doc="""Sourced from EKPO-PRIO_URG // Requirement Urgency""")
    PRIO_REQ = Column('PRIO_REQ', String(3), default=None, doc="""Sourced from EKPO-PRIO_REQ // Requirement Priority""")
    EMPST = Column('EMPST', String(25), default=None, doc="""Sourced from EKPO-EMPST // Receiving point""")
    DIFF_INVOICE = Column('DIFF_INVOICE', String(2), default=None, doc="""Sourced from EKPO-DIFF_INVOICE // Differential Invoicing""")
    TRMRISK_RELEVANT = Column('TRMRISK_RELEVANT', String(2), default=None, doc="""Sourced from EKPO-TRMRISK_RELEVANT // Risk Relevancy in Purchasing""")
    SPE_ABGRU = Column('SPE_ABGRU', String(2), default=None, doc="""Sourced from EKPO-SPE_ABGRU // Reason for rejection of quotations and sales orders""")
    SPE_CRM_SO = Column('SPE_CRM_SO', String(10), default=None, doc="""Sourced from EKPO-SPE_CRM_SO // CRM Sales Order Number for TPOP Process""")
    SPE_CRM_SO_ITEM = Column('SPE_CRM_SO_ITEM', String(6), default=None, doc="""Sourced from EKPO-SPE_CRM_SO_ITEM // CRM Sales Order Item Number in TPOP Process""")
    SPE_CRM_REF_SO = Column('SPE_CRM_REF_SO', String(35), default=None, doc="""Sourced from EKPO-SPE_CRM_REF_SO // CRM Reference Order Number for TPOP Process""")
    SPE_CRM_REF_ITEM = Column('SPE_CRM_REF_ITEM', String(6), default=None, doc="""Sourced from EKPO-SPE_CRM_REF_ITEM // CRM Reference Sales Order Item Number in TPOP Process""")
    SPE_CRM_FKREL = Column('SPE_CRM_FKREL', String(1), default=None, doc="""Sourced from EKPO-SPE_CRM_FKREL // Billing Relevance CRM""")
    SPE_CHNG_SYS = Column('SPE_CHNG_SYS', String(1), default=None, doc="""Sourced from EKPO-SPE_CHNG_SYS // Last Changer's System Type""")
    SPE_INSMK_SRC = Column('SPE_INSMK_SRC', String(1), default=None, doc="""Sourced from EKPO-SPE_INSMK_SRC // Stock Type of Source Storage Location in STO""")
    SPE_CQ_CTRLTYPE = Column('SPE_CQ_CTRLTYPE', String(1), default=None, doc="""Sourced from EKPO-SPE_CQ_CTRLTYPE // CQ Control Type""")
    SPE_CQ_NOCQ = Column('SPE_CQ_NOCQ', Boolean, default=None, doc="""Sourced from EKPO-SPE_CQ_NOCQ // No Transmission of Cumulative Quantities in SA Release""")
    REASON_CODE = Column('REASON_CODE', String(4), default=None, doc="""Sourced from EKPO-REASON_CODE // Goods Receipt Reason Code""")
    CQU_SAR = Column('CQU_SAR', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-CQU_SAR // Cumulative Goods Receipts from Redirected Purchase Orders""")
    ANZSN = Column('ANZSN', Integer, default=None, doc="""Sourced from EKPO-ANZSN // Number of serial numbers""")
    SPE_EWM_DTC = Column('SPE_EWM_DTC', Boolean, default=None, doc="""Sourced from EKPO-SPE_EWM_DTC // EWM Delivery Based Tolerance Check""")
    EXLIN = Column('EXLIN', String(40), default=None, doc="""Sourced from EKPO-EXLIN // Item Number Length""")
    EXSNR = Column('EXSNR', String(5), default=None, doc="""Sourced from EKPO-EXSNR // External Sorting""")
    EHTYP = Column('EHTYP', String(4), default=None, doc="""Sourced from EKPO-EHTYP // External Hierarchy Category""")
    RETPC = Column('RETPC', String(5), default=None, doc="""Sourced from EKPO-RETPC // Retention in Percent""")
    DPTYP = Column('DPTYP', String(4), default=None, doc="""Sourced from EKPO-DPTYP // Down Payment Indicator""")
    DPPCT = Column('DPPCT', String(5), default=None, doc="""Sourced from EKPO-DPPCT // Down Payment Percentage""")
    DPAMT = Column('DPAMT', Numeric(15,3,3), default=None, doc="""Sourced from EKPO-DPAMT // Down Payment Amount in Document Currency""")
    DPDAT = Column('DPDAT', String(8), default=None, doc="""Sourced from EKPO-DPDAT // Due Date for Down Payment""")
    FLS_RSTO = Column('FLS_RSTO', Boolean, default=None, doc="""Sourced from EKPO-FLS_RSTO // Store Return with Inbound and Outbound Delivery""")
    EXT_RFX_NUMBER = Column('EXT_RFX_NUMBER', String(35), default=None, doc="""Sourced from EKPO-EXT_RFX_NUMBER // Document Number of External Document""")
    EXT_RFX_ITEM = Column('EXT_RFX_ITEM', String(10), default=None, doc="""Sourced from EKPO-EXT_RFX_ITEM // Item Number of External Document""")
    EXT_RFX_SYSTEM = Column('EXT_RFX_SYSTEM', String(10), default=None, doc="""Sourced from EKPO-EXT_RFX_SYSTEM // Logical System""")
    SRM_CONTRACT_ID = Column('SRM_CONTRACT_ID', String(10), default=None, doc="""Sourced from EKPO-SRM_CONTRACT_ID // Central Contract""")
    SRM_CONTRACT_ITM = Column('SRM_CONTRACT_ITM', String(10), default=None, doc="""Sourced from EKPO-SRM_CONTRACT_ITM // Central Contract Item Number""")
    BLK_REASON_ID = Column('BLK_REASON_ID', String(4), default=None, doc="""Sourced from EKPO-BLK_REASON_ID // Blocking Reason - ID""")
    BLK_REASON_TXT = Column('BLK_REASON_TXT', String(40), default=None, doc="""Sourced from EKPO-BLK_REASON_TXT // Blocking Reason - Text""")
    ITCONS = Column('ITCONS', Boolean, default=None, doc="""Sourced from EKPO-ITCONS // Real-Time Consumption Posting of Subcontracting Components""")
    FIXMG = Column('FIXMG', String(1), default=None, doc="""Sourced from EKPO-FIXMG // Delivery Date and Quantity Fixed""")
    WABWE = Column('WABWE', Boolean, default=None, doc="""Sourced from EKPO-WABWE // Indicator for GI-based goods receipt""")
    TC_AUT_DET = Column('TC_AUT_DET', String(2), default=None, doc="""Sourced from EKPO-TC_AUT_DET // Tax Code Automatically Determined""")
    MANUAL_TC_REASON = Column('MANUAL_TC_REASON', String(2), default=None, doc="""Sourced from EKPO-MANUAL_TC_REASON // Manual Tax Code Reason""")
    FISCAL_INCENTIVE = Column('FISCAL_INCENTIVE', String(4), default=None, doc="""Sourced from EKPO-FISCAL_INCENTIVE // Tax Incentive Type""")
    TAX_SUBJECT_ST = Column('TAX_SUBJECT_ST', String(1), default=None, doc="""Sourced from EKPO-TAX_SUBJECT_ST // Tax Subject to Substituição Tributária""")
    FISCAL_INCENTIVE_ID = Column('FISCAL_INCENTIVE_ID', String(4), default=None, doc="""Sourced from EKPO-FISCAL_INCENTIVE_ID // Incentive ID""")
    SF_TXJCD = Column('SF_TXJCD', String(15), default=None, doc="""Sourced from EKPO-SF_TXJCD // Jurisdiction Code of the Point of Origin""")
    ADVCODE = Column('ADVCODE', String(2), default=None, doc="""Sourced from EKPO-ADVCODE // Advice Code""")
    BUDGET_PD = Column('BUDGET_PD', String(10), default=None, doc="""Sourced from EKPO-BUDGET_PD // FM: Budget Period""")
    EXCPE = Column('EXCPE', String(2), default=None, doc="""Sourced from EKPO-EXCPE // Acceptance Period""")
    FMFGUS_KEY = Column('FMFGUS_KEY', String(22), default=None, doc="""Sourced from EKPO-FMFGUS_KEY // United States Federal Government Fields""")
    IUID_RELEVANT = Column('IUID_RELEVANT', String(1), default=None, doc="""Sourced from EKPO-IUID_RELEVANT // IUID-Relevant""")
    MRPIND = Column('MRPIND', String(1), default=None, doc="""Sourced from EKPO-MRPIND // Max. Retail Price Relevant""")
    SGT_SCAT = Column('SGT_SCAT', String(16), default=None, doc="""Sourced from EKPO-SGT_SCAT // Stock Segment""")
    SGT_RCAT = Column('SGT_RCAT', String(16), default=None, doc="""Sourced from EKPO-SGT_RCAT // Requirement Segment""")
    REFSITE = Column('REFSITE', String(4), default=None, doc="""Sourced from EKPO-REFSITE // Reference Site For Purchasing""")
    REF_ITEM = Column('REF_ITEM', String(5), default=None, doc="""Sourced from EKPO-REF_ITEM // Reference Item for Remaining Qty Cancellation""")
    SOURCE_ID = Column('SOURCE_ID', String(3), default=None, doc="""Sourced from EKPO-SOURCE_ID // Origin Profile""")
    SOURCE_KEY = Column('SOURCE_KEY', String(32), default=None, doc="""Sourced from EKPO-SOURCE_KEY // Key in Source System""")
    PUT_BACK = Column('PUT_BACK', Boolean, default=None, doc="""Sourced from EKPO-PUT_BACK // Indicator for Putting Back from Grouped PO Document""")
    POL_ID = Column('POL_ID', String(10), default=None, doc="""Sourced from EKPO-POL_ID // Order List Item Number""")
    CONS_ORDER = Column('CONS_ORDER', String(1), default=None, doc="""Sourced from EKPO-CONS_ORDER // Purchase Order for Consignment""")

    prch_doc_id = synonym('EBELN')
    prch_doc_item_id = synonym('EBELP')
    update_dt = synonym('AEDAT')
    material_id = synonym('MATNR')
    mfg_part_nbr_matl_id = synonym('EMATN')
    company_cd = synonym('BUKRS')
    material_group_cd = synonym('MATKL')
    vendor_material_nbr = synonym('IDNLF')
    uom_cd = synonym('MEINS')
    prch_order_price_uom_cd = synonym('BPRME')
    price_uom_to_order_uom_conv_num = synonym('BPUMZ')
    price_uom_to_order_uom_conv_denom = synonym('BPUMN')
    base_uom_conversin_num = synonym('UMREZ')
    base_uom_conversion_denom = synonym('UMREN')
    net_price_qty = synonym('NETPR')
    price_uom_cd = synonym('PEINH')
    doc_currency_net_value_qty = synonym('NETWR')
    gross_value = synonym('BRTWR')
    volume_rebate_grp_id = synonym('BONUS')
    stock_type_cd = synonym('INSMK')
    rejected_ind = synonym('ABSKZ')
    delivery_complete_ind = synonym('ELIKZ')
    final_invoice_ind = synonym('EREKZ')
    prch_doc_item_ctgy_cd = synonym('PSTYP')
    goods_receipt_ind = synonym('WEPOS')
    bom_explosion_ind = synonym('KZSTU')
    prch_doc_ctgy_cd = synonym('BSTYP')
    item_effective_value_qty = synonym('EFFWR')
    customer_id = synonym('KUNNR')
    addr_id = synonym('ADRNR')
    net_wt = synonym('NTGEW')
    weight_uom_cd = synonym('GEWEI')
    special_stock_cd = synonym('SOBKZ')
    cnfrm_cntrl_cd = synonym('BSTAE')
    price_determ_date_control_cd = synonym('MEPRF')
    gross_wt = synonym('BRGEW')
    vol = synonym('VOLUM')
    volume_uom_cd = synonym('VOLEH')
    incoterms_cd = synonym('INCO1')
    incoterms_desc = synonym('INCO2')
    receiving_vendor_id = synonym('EMLIF')
    matl_ctgy_id = synonym('ATTYP')
    addr_nbr = synonym('ADRN2')
    last_transmission_dt = synonym('DRDAT')
    last_transmission_tm = synonym('DRUHR')
    configurable_material_ind = synonym('KZKFG')
    prch_req_id = synonym('BANFN')
    prch_req_item_id = synonym('BNFPO')
    material_type_id = synonym('MTART')
    returns_item_ind = synonym('RETPO')
    order_reas_cd = synonym('BSGRU')
    special_stock_valuation_Cd = synonym('KZBWS')
    jit_deliv_schedule_rlvnt_ind = synonym('FABKZ')
    outward_delivery_complete_ind = synonym('EGLKZ')
    item_partial_delivery_cd = synonym('KZTLF')
    mfg_part_nbr = synonym('MFRPN')
    ext_mfg_cd = synonym('EMNFR')
    sd_item_delivery_block_ind = synonym('NOVET')
    mrp_area_id = synonym('BERID')
    sto_source_stor_loc_id = synonym('RESLO')
    receiving_point_cd = synonym('EMPST')
    external_hierarchy_ctgy_cd = synonym('EHTYP')
    deliv_dt_and_qty_fixed_ind = synonym('FIXMG')


################################################################################




################################################################################

class STO_ShipData(SAP_Base):
    """\
    Table sourced from: EKPV
    Description: Shipping Data For Stock Transfer of Purchasing Document Item
    """

    __tablename__ = "EKPV"

    EBELN = Column('EBELN', String(10), primary_key = True, doc="""Sourced from EKPV-EBELN // Purchasing Document Number""")
    EBELP = Column('EBELP', String(5), primary_key = True, doc="""Sourced from EKPV-EBELP // Item Number of Purchasing Document""")
    VSTEL = Column('VSTEL', String(4), default=None, doc="""Sourced from EKPV-VSTEL // Shipping Point/Receiving Point""")
    LPRIO = Column('LPRIO', String(2), default=None, doc="""Sourced from EKPV-LPRIO // Delivery Priority""")
    ROUTE = Column('ROUTE', String(6), default=None, doc="""Sourced from EKPV-ROUTE // Route""")
    KUNNR = Column('KUNNR', String(10), default=None, doc="""Sourced from EKPV-KUNNR // Customer Number""")
    KUNAG = Column('KUNAG', String(10), default=None, doc="""Sourced from EKPV-KUNAG // Sold-to party""")
    SPDNR = Column('SPDNR', String(10), default=None, doc="""Sourced from EKPV-SPDNR // Forwarding agent""")
    VKORG = Column('VKORG', String(4), default=None, doc="""Sourced from EKPV-VKORG // Sales Organization""")
    VTWEG = Column('VTWEG', String(2), default=None, doc="""Sourced from EKPV-VTWEG // Distribution Channel""")
    SPART = Column('SPART', String(2), default=None, doc="""Sourced from EKPV-SPART // Division""")
    LEDAT = Column('LEDAT', Date, default=None, doc="""Sourced from EKPV-LEDAT // Delivery Creation Date""")
    PLIFZ = Column('PLIFZ', Numeric(15,3,3), default=None, doc="""Sourced from EKPV-PLIFZ // Planned Delivery Time in Days""")
    SPRAS = Column('SPRAS', String(1), default=None, doc="""Sourced from EKPV-SPRAS // Language Key""")
    VSBED = Column('VSBED', String(2), default=None, doc="""Sourced from EKPV-VSBED // Shipping Conditions""")
    LADGR = Column('LADGR', String(4), default=None, doc="""Sourced from EKPV-LADGR // Loading Group""")
    TRAGR = Column('TRAGR', String(4), default=None, doc="""Sourced from EKPV-TRAGR // Transportation Group""")
    ABLAD = Column('ABLAD', String(25), default=None, doc="""Sourced from EKPV-ABLAD // Unloading Point""")
    KZAZU = Column('KZAZU', Boolean, default=None, doc="""Sourced from EKPV-KZAZU // Order Combination Indicator""")
    TZONIS = Column('TZONIS', String(6), default=None, doc="""Sourced from EKPV-TZONIS // Time zone of delivering location""")
    SPE_AUTH_NUMBER = Column('SPE_AUTH_NUMBER', String(20), default=None, doc="""Sourced from EKPV-SPE_AUTH_NUMBER // Return Material Authorization Number""")
    SPE_SRC_DLV_NO = Column('SPE_SRC_DLV_NO', String(10), default=None, doc="""Sourced from EKPV-SPE_SRC_DLV_NO // Source delivery number""")
    SPE_SRC_EXIDV = Column('SPE_SRC_EXIDV', String(20), default=None, doc="""Sourced from EKPV-SPE_SRC_EXIDV // Source/Target handling unit (external ID)""")
    SPE_FOLLOW_UP = Column('SPE_FOLLOW_UP', String(4), default=None, doc="""Sourced from EKPV-SPE_FOLLOW_UP // Default Follow-Up Activity Code""")
    SPE_EXT_ID = Column('SPE_EXT_ID', String(10), default=None, doc="""Sourced from EKPV-SPE_EXT_ID // External Delivery Number""")
    SPE_EXT_ID_ITEM = Column('SPE_EXT_ID_ITEM', String(6), default=None, doc="""Sourced from EKPV-SPE_EXT_ID_ITEM // External Delivery Item Number""")

    prch_doc_id = synonym('EBELN')
    prch_doc_item_id = synonym('EBELP')
    shipping_receiving_point_cd = synonym('VSTEL')
    delivery_priority_cd = synonym('LPRIO')
    route_id = synonym('ROUTE')
    customer_id = synonym('KUNNR')
    sold_to_customer_id = synonym('KUNAG')
    sales_org_cd = synonym('VKORG')
    distr_chan_cd = synonym('VTWEG')
    div_cd = synonym('SPART')
    delivery_note_create_dt = synonym('LEDAT')
    language_cd = synonym('SPRAS')
    shipping_condition_cd = synonym('VSBED')
    loading_grp_id = synonym('LADGR')
    unloading_point = synonym('ABLAD')


################################################################################




################################################################################

class Customer(SAP_Base):
    """\
    Table sourced from: KNA1
    Description: General Data in Customer Master
    """

    __tablename__ = "KNA1"

    KUNNR = Column('KUNNR', String(10), primary_key = True, doc="""Sourced from KNA1-KUNNR // Customer Number""")
    LAND1 = Column('LAND1', String(3), default=None, doc="""Sourced from KNA1-LAND1 // Country Key""")
    NAME1 = Column('NAME1', String(35), default=None, doc="""Sourced from KNA1-NAME1 // Name 1""")
    NAME2 = Column('NAME2', String(35), default=None, doc="""Sourced from KNA1-NAME2 // Name 2""")
    ORT01 = Column('ORT01', String(35), default=None, doc="""Sourced from KNA1-ORT01 // City""")
    PSTLZ = Column('PSTLZ', String(10), default=None, doc="""Sourced from KNA1-PSTLZ // Postal Code""")
    REGIO = Column('REGIO', String(3), default=None, doc="""Sourced from KNA1-REGIO // Region (State, Province, County)""")
    SORTL = Column('SORTL', String(10), default=None, doc="""Sourced from KNA1-SORTL // Sort field""")
    STRAS = Column('STRAS', String(35), default=None, doc="""Sourced from KNA1-STRAS // House number and street""")
    TELF1 = Column('TELF1', String(16), default=None, doc="""Sourced from KNA1-TELF1 // First telephone number""")
    TELFX = Column('TELFX', String(31), default=None, doc="""Sourced from KNA1-TELFX // Fax Number""")
    XCPDK = Column('XCPDK', Boolean, default=None, doc="""Sourced from KNA1-XCPDK // Indicator: Is the account a one-time account?""")
    ADRNR = Column('ADRNR', String(10), default=None, doc="""Sourced from KNA1-ADRNR // Address""")
    MCOD1 = Column('MCOD1', String(25), default=None, doc="""Sourced from KNA1-MCOD1 // Search term for matchcode search""")
    MCOD2 = Column('MCOD2', String(25), default=None, doc="""Sourced from KNA1-MCOD2 // Search Term for Matchcode Search""")
    MCOD3 = Column('MCOD3', String(25), default=None, doc="""Sourced from KNA1-MCOD3 // Search term for matchcode search""")
    ANRED = Column('ANRED', String(15), default=None, doc="""Sourced from KNA1-ANRED // Title""")
    AUFSD = Column('AUFSD', String(2), default=None, doc="""Sourced from KNA1-AUFSD // Central order block for customer""")
    BAHNE = Column('BAHNE', String(25), default=None, doc="""Sourced from KNA1-BAHNE // Express train station""")
    BAHNS = Column('BAHNS', String(25), default=None, doc="""Sourced from KNA1-BAHNS // Train station""")
    BBBNR = Column('BBBNR', String(7), default=None, doc="""Sourced from KNA1-BBBNR // International location number  (part 1)""")
    BBSNR = Column('BBSNR', String(5), default=None, doc="""Sourced from KNA1-BBSNR // International location number (Part 2)""")
    BEGRU = Column('BEGRU', String(4), default=None, doc="""Sourced from KNA1-BEGRU // Authorization Group""")
    BRSCH = Column('BRSCH', String(4), default=None, doc="""Sourced from KNA1-BRSCH // Industry key""")
    BUBKZ = Column('BUBKZ', String(1), default=None, doc="""Sourced from KNA1-BUBKZ // Check digit for the international location number""")
    DATLT = Column('DATLT', String(14), default=None, doc="""Sourced from KNA1-DATLT // Data communication line no.""")
    ERDAT = Column('ERDAT', Date, default=None, doc="""Sourced from KNA1-ERDAT // Date on which the Record Was Created""")
    ERNAM = Column('ERNAM', String(12), default=None, doc="""Sourced from KNA1-ERNAM // Name of Person who Created the Object""")
    EXABL = Column('EXABL', Boolean, default=None, doc="""Sourced from KNA1-EXABL // Indicator: Unloading points exist""")
    FAKSD = Column('FAKSD', String(2), default=None, doc="""Sourced from KNA1-FAKSD // Central billing block for customer""")
    FISKN = Column('FISKN', String(10), default=None, doc="""Sourced from KNA1-FISKN // Account number of the master record with the fiscal address""")
    KNAZK = Column('KNAZK', String(2), default=None, doc="""Sourced from KNA1-KNAZK // Working Time Calendar""")
    KNRZA = Column('KNRZA', String(10), default=None, doc="""Sourced from KNA1-KNRZA // Account number of an alternative payer""")
    KONZS = Column('KONZS', String(10), default=None, doc="""Sourced from KNA1-KONZS // Group key""")
    KTOKD = Column('KTOKD', String(4), default=None, doc="""Sourced from KNA1-KTOKD // Customer Account Group""")
    KUKLA = Column('KUKLA', String(2), default=None, doc="""Sourced from KNA1-KUKLA // Customer classification""")
    LIFNR = Column('LIFNR', String(10), default=None, doc="""Sourced from KNA1-LIFNR // Account Number of Vendor or Creditor""")
    LIFSD = Column('LIFSD', String(2), default=None, doc="""Sourced from KNA1-LIFSD // Central delivery block for the customer""")
    LOCCO = Column('LOCCO', String(10), default=None, doc="""Sourced from KNA1-LOCCO // City Coordinates""")
    LOEVM = Column('LOEVM', Boolean, default=None, doc="""Sourced from KNA1-LOEVM // Central Deletion Flag for Master Record""")
    NAME3 = Column('NAME3', String(35), default=None, doc="""Sourced from KNA1-NAME3 // Name 3""")
    NAME4 = Column('NAME4', String(35), default=None, doc="""Sourced from KNA1-NAME4 // Name 4""")
    NIELS = Column('NIELS', String(2), default=None, doc="""Sourced from KNA1-NIELS // Nielsen ID""")
    ORT02 = Column('ORT02', String(35), default=None, doc="""Sourced from KNA1-ORT02 // District""")
    PFACH = Column('PFACH', String(10), default=None, doc="""Sourced from KNA1-PFACH // PO Box""")
    PSTL2 = Column('PSTL2', String(10), default=None, doc="""Sourced from KNA1-PSTL2 // P.O. Box Postal Code""")
    COUNC = Column('COUNC', String(3), default=None, doc="""Sourced from KNA1-COUNC // County Code""")
    CITYC = Column('CITYC', String(4), default=None, doc="""Sourced from KNA1-CITYC // City Code""")
    RPMKR = Column('RPMKR', String(5), default=None, doc="""Sourced from KNA1-RPMKR // Regional Market""")
    SPERR = Column('SPERR', Boolean, default=None, doc="""Sourced from KNA1-SPERR // Central posting block""")
    SPRAS = Column('SPRAS', String(1), default=None, doc="""Sourced from KNA1-SPRAS // Language Key""")
    STCD1 = Column('STCD1', String(16), default=None, doc="""Sourced from KNA1-STCD1 // Tax Number 1""")
    STCD2 = Column('STCD2', String(11), default=None, doc="""Sourced from KNA1-STCD2 // Tax Number 2""")
    STKZA = Column('STKZA', String(1), default=None, doc="""Sourced from KNA1-STKZA // Indicator: Business Partner Subject to Equalization Tax?""")
    STKZU = Column('STKZU', Boolean, default=None, doc="""Sourced from KNA1-STKZU // Liable for VAT""")
    TELBX = Column('TELBX', String(15), default=None, doc="""Sourced from KNA1-TELBX // Telebox number""")
    TELF2 = Column('TELF2', String(16), default=None, doc="""Sourced from KNA1-TELF2 // Second telephone number""")
    TELTX = Column('TELTX', String(30), default=None, doc="""Sourced from KNA1-TELTX // Teletex number""")
    TELX1 = Column('TELX1', String(30), default=None, doc="""Sourced from KNA1-TELX1 // Telex number""")
    LZONE = Column('LZONE', String(10), default=None, doc="""Sourced from KNA1-LZONE // Transportation zone to or from which the goods are delivered""")
    XZEMP = Column('XZEMP', Boolean, default=None, doc="""Sourced from KNA1-XZEMP // Indicator: Is an alternative payer allowed in document?""")
    VBUND = Column('VBUND', String(6), default=None, doc="""Sourced from KNA1-VBUND // Company ID of Trading Partner""")
    STCEG = Column('STCEG', String(20), default=None, doc="""Sourced from KNA1-STCEG // VAT Registration Number""")
    DEAR1 = Column('DEAR1', Boolean, default=None, doc="""Sourced from KNA1-DEAR1 // Indicator: Competitor""")
    DEAR2 = Column('DEAR2', Boolean, default=None, doc="""Sourced from KNA1-DEAR2 // Indicator: Sales partner""")
    DEAR3 = Column('DEAR3', String(1), default=None, doc="""Sourced from KNA1-DEAR3 // Indicator: Sales prospect""")
    DEAR4 = Column('DEAR4', Boolean, default=None, doc="""Sourced from KNA1-DEAR4 // Indicator for customer type 4""")
    DEAR5 = Column('DEAR5', Boolean, default=None, doc="""Sourced from KNA1-DEAR5 // ID for default sold-to party""")
    GFORM = Column('GFORM', String(2), default=None, doc="""Sourced from KNA1-GFORM // Legal status""")
    BRAN1 = Column('BRAN1', String(10), default=None, doc="""Sourced from KNA1-BRAN1 // Industry Code 1""")
    BRAN2 = Column('BRAN2', String(10), default=None, doc="""Sourced from KNA1-BRAN2 // Industry code 2""")
    BRAN3 = Column('BRAN3', String(10), default=None, doc="""Sourced from KNA1-BRAN3 // Industry code 3""")
    BRAN4 = Column('BRAN4', String(10), default=None, doc="""Sourced from KNA1-BRAN4 // Industry code 4""")
    BRAN5 = Column('BRAN5', String(10), default=None, doc="""Sourced from KNA1-BRAN5 // Industry code 5""")
    EKONT = Column('EKONT', String(10), default=None, doc="""Sourced from KNA1-EKONT // Initial contact""")
    UMSAT = Column('UMSAT', Numeric(15,3,3), default=None, doc="""Sourced from KNA1-UMSAT // Annual sales""")
    UMJAH = Column('UMJAH', String(4), default=None, doc="""Sourced from KNA1-UMJAH // Year For Which Sales are Given""")
    UWAER = Column('UWAER', String(5), default=None, doc="""Sourced from KNA1-UWAER // Currency of sales figure""")
    JMZAH = Column('JMZAH', String(6), default=None, doc="""Sourced from KNA1-JMZAH // Yearly number of employees""")
    JMJAH = Column('JMJAH', String(4), default=None, doc="""Sourced from KNA1-JMJAH // Year for which the number of employees is given""")
    KATR1 = Column('KATR1', String(2), default=None, doc="""Sourced from KNA1-KATR1 // Attribute 1""")
    KATR2 = Column('KATR2', String(2), default=None, doc="""Sourced from KNA1-KATR2 // Attribute 2""")
    KATR3 = Column('KATR3', String(2), default=None, doc="""Sourced from KNA1-KATR3 // Attribute 3""")
    KATR4 = Column('KATR4', String(2), default=None, doc="""Sourced from KNA1-KATR4 // Ship or Cancel""")
    KATR5 = Column('KATR5', String(2), default=None, doc="""Sourced from KNA1-KATR5 // Attribute 5""")
    KATR6 = Column('KATR6', String(3), default=None, doc="""Sourced from KNA1-KATR6 // Attribute 6""")
    KATR7 = Column('KATR7', String(3), default=None, doc="""Sourced from KNA1-KATR7 // Attribute 7""")
    KATR8 = Column('KATR8', String(3), default=None, doc="""Sourced from KNA1-KATR8 // Attribute 8""")
    KATR9 = Column('KATR9', String(3), default=None, doc="""Sourced from KNA1-KATR9 // Attribute 9""")
    KATR10 = Column('KATR10', String(3), default=None, doc="""Sourced from KNA1-KATR10 // Attribute 10""")
    STKZN = Column('STKZN', String(1), default=None, doc="""Sourced from KNA1-STKZN // Natural Person""")
    UMSA1 = Column('UMSA1', Numeric(15,3,3), default=None, doc="""Sourced from KNA1-UMSA1 // Annual sales""")
    TXJCD = Column('TXJCD', String(15), default=None, doc="""Sourced from KNA1-TXJCD // Tax Jurisdiction""")
    PERIV = Column('PERIV', String(2), default=None, doc="""Sourced from KNA1-PERIV // Fiscal Year Variant""")
    ABRVW = Column('ABRVW', String(3), default=None, doc="""Sourced from KNA1-ABRVW // Usage Indicator""")
    INSPBYDEBI = Column('INSPBYDEBI', String(1), default=None, doc="""Sourced from KNA1-INSPBYDEBI // Inspection Carried Out By Customer (No Inspection Lot)""")
    INSPATDEBI = Column('INSPATDEBI', String(1), default=None, doc="""Sourced from KNA1-INSPATDEBI // Inspection for a Delivery Note After Outbound Delivery""")
    KTOCD = Column('KTOCD', String(4), default=None, doc="""Sourced from KNA1-KTOCD // Reference Account Group for One-Time Account (Customer)""")
    PFORT = Column('PFORT', String(35), default=None, doc="""Sourced from KNA1-PFORT // PO Box city""")
    WERKS = Column('WERKS', String(4), default=None, doc="""Sourced from KNA1-WERKS // Plant""")
    DTAMS = Column('DTAMS', String(1), default=None, doc="""Sourced from KNA1-DTAMS // Indicator for Data Medium Exchange""")
    DTAWS = Column('DTAWS', String(2), default=None, doc="""Sourced from KNA1-DTAWS // Instruction key for data medium exchange""")
    DUEFL = Column('DUEFL', String(1), default=None, doc="""Sourced from KNA1-DUEFL // Status of Data Transfer into Subsequent Release""")
    HZUOR = Column('HZUOR', String(2), default=None, doc="""Sourced from KNA1-HZUOR // Assignment to Hierarchy""")
    SPERZ = Column('SPERZ', Boolean, default=None, doc="""Sourced from KNA1-SPERZ // Payment Block""")
    ETIKG = Column('ETIKG', String(10), default=None, doc="""Sourced from KNA1-ETIKG // IS-R Labeling: customer/plant group""")
    CIVVE = Column('CIVVE', Boolean, default=None, doc="""Sourced from KNA1-CIVVE // ID for mainly non-military use""")
    MILVE = Column('MILVE', Boolean, default=None, doc="""Sourced from KNA1-MILVE // ID for mainly military use""")
    KDKG1 = Column('KDKG1', String(2), default=None, doc="""Sourced from KNA1-KDKG1 // Customer condition group 1""")
    KDKG2 = Column('KDKG2', String(2), default=None, doc="""Sourced from KNA1-KDKG2 // Customer condition group 2""")
    KDKG3 = Column('KDKG3', String(2), default=None, doc="""Sourced from KNA1-KDKG3 // Customer condition group 3""")
    KDKG4 = Column('KDKG4', String(2), default=None, doc="""Sourced from KNA1-KDKG4 // Customer condition group 4""")
    KDKG5 = Column('KDKG5', String(2), default=None, doc="""Sourced from KNA1-KDKG5 // Customer condition group 5""")
    XKNZA = Column('XKNZA', Boolean, default=None, doc="""Sourced from KNA1-XKNZA // Indicator: Alternative payer using account number""")
    FITYP = Column('FITYP', String(2), default=None, doc="""Sourced from KNA1-FITYP // Tax type""")
    STCDT = Column('STCDT', String(2), default=None, doc="""Sourced from KNA1-STCDT // Tax Number Type""")
    STCD3 = Column('STCD3', String(18), default=None, doc="""Sourced from KNA1-STCD3 // Tax Number 3""")
    STCD4 = Column('STCD4', String(18), default=None, doc="""Sourced from KNA1-STCD4 // Tax Number 4""")
    STCD5 = Column('STCD5', String(60), default=None, doc="""Sourced from KNA1-STCD5 // Tax Number 5""")
    XICMS = Column('XICMS', Boolean, default=None, doc="""Sourced from KNA1-XICMS // Customer is ICMS-exempt""")
    XXIPI = Column('XXIPI', Boolean, default=None, doc="""Sourced from KNA1-XXIPI // Customer is IPI-exempt""")
    XSUBT = Column('XSUBT', String(3), default=None, doc="""Sourced from KNA1-XSUBT // Customer group for Substituiçao Tributária calculation""")
    CFOPC = Column('CFOPC', String(2), default=None, doc="""Sourced from KNA1-CFOPC // Customer's CFOP category""")
    TXLW1 = Column('TXLW1', String(3), default=None, doc="""Sourced from KNA1-TXLW1 // Tax law: ICMS""")
    TXLW2 = Column('TXLW2', String(3), default=None, doc="""Sourced from KNA1-TXLW2 // Tax law: IPI""")
    CCC01 = Column('CCC01', Boolean, default=None, doc="""Sourced from KNA1-CCC01 // Indicator for biochemical warfare for legal control""")
    CCC02 = Column('CCC02', Boolean, default=None, doc="""Sourced from KNA1-CCC02 // Indicator for nuclear nonproliferation for legal control""")
    CCC03 = Column('CCC03', Boolean, default=None, doc="""Sourced from KNA1-CCC03 // Indicator for national security for legal control""")
    CCC04 = Column('CCC04', Boolean, default=None, doc="""Sourced from KNA1-CCC04 // Indicator for missile technology for legal control""")
    CASSD = Column('CASSD', String(2), default=None, doc="""Sourced from KNA1-CASSD // Central sales block for customer""")
    KNURL = Column('KNURL', String(132), default=None, doc="""Sourced from KNA1-KNURL // Uniform Resource Locator""")
    J_1KFREPRE = Column('J_1KFREPRE', String(10), default=None, doc="""Sourced from KNA1-J_1KFREPRE // Name of Representative""")
    J_1KFTBUS = Column('J_1KFTBUS', String(30), default=None, doc="""Sourced from KNA1-J_1KFTBUS // Type of Business""")
    J_1KFTIND = Column('J_1KFTIND', String(30), default=None, doc="""Sourced from KNA1-J_1KFTIND // Type of Industry""")
    CONFS = Column('CONFS', String(1), default=None, doc="""Sourced from KNA1-CONFS // Status of Change Authorization (Central)""")
    UPDAT = Column('UPDAT', Date, default=None, doc="""Sourced from KNA1-UPDAT // Date on Which the Changes Were Confirmed""")
    UPTIM = Column('UPTIM', Time, default=None, doc="""Sourced from KNA1-UPTIM // Time of Last Change Confirmation""")
    NODEL = Column('NODEL', Boolean, default=None, doc="""Sourced from KNA1-NODEL // Central deletion block for master record""")
    DEAR6 = Column('DEAR6', Boolean, default=None, doc="""Sourced from KNA1-DEAR6 // Indicator: Consumer""")
    CVP_XBLCK = Column('CVP_XBLCK', String(1), default=None, doc="""Sourced from KNA1-CVP_XBLCK // Business Purpose Completed Flag""")
    SUFRAMA = Column('SUFRAMA', String(9), default=None, doc="""Sourced from KNA1-SUFRAMA // Suframa Code""")
    RG = Column('RG', String(11), default=None, doc="""Sourced from KNA1-RG // RG Number""")
    EXP = Column('EXP', String(3), default=None, doc="""Sourced from KNA1-EXP // Issued by""")
    UF = Column('UF', String(2), default=None, doc="""Sourced from KNA1-UF // State""")
    RGDATE = Column('RGDATE', String(8), default=None, doc="""Sourced from KNA1-RGDATE // RG Issue Date""")
    RIC = Column('RIC', String(11), default=None, doc="""Sourced from KNA1-RIC // RIC Number""")
    RNE = Column('RNE', String(10), default=None, doc="""Sourced from KNA1-RNE // Foreign National Registration""")
    RNEDATE = Column('RNEDATE', String(8), default=None, doc="""Sourced from KNA1-RNEDATE // RNE Issue Date""")
    CNAE = Column('CNAE', String(7), default=None, doc="""Sourced from KNA1-CNAE // CNAE""")
    LEGALNAT = Column('LEGALNAT', String(4), default=None, doc="""Sourced from KNA1-LEGALNAT // Legal Nature""")
    CRTN = Column('CRTN', String(1), default=None, doc="""Sourced from KNA1-CRTN // CRT Number""")
    ICMSTAXPAY = Column('ICMSTAXPAY', String(2), default=None, doc="""Sourced from KNA1-ICMSTAXPAY // ICMS Taxpayer""")
    INDTYP = Column('INDTYP', String(2), default=None, doc="""Sourced from KNA1-INDTYP // Industry Main Type""")
    TDT = Column('TDT', String(2), default=None, doc="""Sourced from KNA1-TDT // Tax Declaration Type""")
    COMSIZE = Column('COMSIZE', String(2), default=None, doc="""Sourced from KNA1-COMSIZE // Company Size""")
    DECREGPC = Column('DECREGPC', String(2), default=None, doc="""Sourced from KNA1-DECREGPC // Declaration Regimen for PIS/COFINS""")
    ALC = Column('ALC', String(8), default=None, doc="""Sourced from KNA1-ALC // Agency Location Code""")
    PMT_OFFICE = Column('PMT_OFFICE', String(5), default=None, doc="""Sourced from KNA1-PMT_OFFICE // Payment Office""")
    PSOFG = Column('PSOFG', String(10), default=None, doc="""Sourced from KNA1-PSOFG // Processor group""")
    PSOIS = Column('PSOIS', String(20), default=None, doc="""Sourced from KNA1-PSOIS // Subledger acct preprocessing procedure""")
    PSON1 = Column('PSON1', String(35), default=None, doc="""Sourced from KNA1-PSON1 // Name 1""")
    PSON2 = Column('PSON2', String(35), default=None, doc="""Sourced from KNA1-PSON2 // Name 2""")
    PSON3 = Column('PSON3', String(35), default=None, doc="""Sourced from KNA1-PSON3 // Name 3""")
    PSOVN = Column('PSOVN', String(35), default=None, doc="""Sourced from KNA1-PSOVN // First Name""")
    PSOTL = Column('PSOTL', String(20), default=None, doc="""Sourced from KNA1-PSOTL // Title""")
    PSOHS = Column('PSOHS', String(6), default=None, doc="""Sourced from KNA1-PSOHS // House number: is no longer used from Release 4.6B""")
    PSOST = Column('PSOST', String(28), default=None, doc="""Sourced from KNA1-PSOST // Street: No longer used from Release 4.6B""")
    PSOO1 = Column('PSOO1', String(50), default=None, doc="""Sourced from KNA1-PSOO1 // Description""")
    PSOO2 = Column('PSOO2', String(50), default=None, doc="""Sourced from KNA1-PSOO2 // Description""")
    PSOO3 = Column('PSOO3', String(50), default=None, doc="""Sourced from KNA1-PSOO3 // Description""")
    PSOO4 = Column('PSOO4', String(50), default=None, doc="""Sourced from KNA1-PSOO4 // Description""")
    PSOO5 = Column('PSOO5', String(50), default=None, doc="""Sourced from KNA1-PSOO5 // Description""")
    YYOOCID = Column('YYOOCID', Boolean, default=None, doc="""Sourced from KNA1-YYOOCID // Out of City Indicator""")

    customer_id = synonym('KUNNR')
    country_cd = synonym('LAND1')
    name = synonym('NAME1')
    name2 = synonym('NAME2')
    city = synonym('ORT01')
    region = synonym('REGIO')
    addr_id = synonym('ADRNR')
    cust_order_blk_cd = synonym('AUFSD')
    auth_grp_id = synonym('BEGRU')
    doc_create_dt = synonym('ERDAT')
    doc_create_user_id = synonym('ERNAM')
    unloading_points_exist_ind = synonym('EXABL')
    city_coordinates_id = synonym('LOCCO')
    deletion_ind = synonym('LOEVM')
    name4 = synonym('NAME4')
    district = synonym('ORT02')
    po_box = synonym('PFACH')
    county_cd = synonym('COUNC')
    city_cd = synonym('CITYC')
    language_cd = synonym('SPRAS')
    transportation_zone_cd = synonym('LZONE')
    competitor_ind = synonym('DEAR1')
    sales_partner_ind = synonym('DEAR2')
    sales_prospect_cd = synonym('DEAR3')
    default_sold_to_party_ind = synonym('DEAR5')
    initial_contact_id = synonym('EKONT')
    ship_or_cancel_cd = synonym('KATR4')
    hierarchy_assignment_cd = synonym('HZUOR')
    payment_block_ind = synonym('SPERZ')
    non_military_use_ind = synonym('CIVVE')
    military_use_ind = synonym('MILVE')
    last_update_dt = synonym('UPDAT')
    last_update_tm = synonym('UPTIM')
    customer_ind = synonym('DEAR6')
    industry_type_cd = synonym('INDTYP')


################################################################################




################################################################################

class CustomerCompany(SAP_Base):
    """\
    Table sourced from: KNB1
    Description: Customer Master (Company Code)
    """

    __tablename__ = "KNB1"

    KUNNR = Column('KUNNR', String(10), primary_key = True, doc="""Sourced from KNB1-KUNNR // Customer Number""")
    BUKRS = Column('BUKRS', String(4), primary_key = True, doc="""Sourced from KNB1-BUKRS // Company Code""")
    PERNR = Column('PERNR', String(8), default=None, doc="""Sourced from KNB1-PERNR // Personnel Number""")
    ERDAT = Column('ERDAT', Date, default=None, doc="""Sourced from KNB1-ERDAT // Date on which the Record Was Created""")
    ERNAM = Column('ERNAM', String(12), default=None, doc="""Sourced from KNB1-ERNAM // Name of Person who Created the Object""")
    SPERR = Column('SPERR', Boolean, default=None, doc="""Sourced from KNB1-SPERR // Posting block for company code""")
    LOEVM = Column('LOEVM', Boolean, default=None, doc="""Sourced from KNB1-LOEVM // Deletion Flag for Master Record (Company Code Level)""")
    ZUAWA = Column('ZUAWA', String(3), default=None, doc="""Sourced from KNB1-ZUAWA // Key for sorting according to assignment numbers""")
    BUSAB = Column('BUSAB', String(2), default=None, doc="""Sourced from KNB1-BUSAB // Accounting clerk""")
    AKONT = Column('AKONT', String(10), default=None, doc="""Sourced from KNB1-AKONT // Reconciliation Account in General Ledger""")
    BEGRU = Column('BEGRU', String(4), default=None, doc="""Sourced from KNB1-BEGRU // Authorization Group""")
    KNRZE = Column('KNRZE', String(10), default=None, doc="""Sourced from KNB1-KNRZE // Head office account number (in branch accounts)""")
    KNRZB = Column('KNRZB', String(10), default=None, doc="""Sourced from KNB1-KNRZB // Account number of an alternative payer""")
    ZAMIM = Column('ZAMIM', Boolean, default=None, doc="""Sourced from KNB1-ZAMIM // Indicator: Payment notice to customer (with cleared items)?""")
    ZAMIV = Column('ZAMIV', Boolean, default=None, doc="""Sourced from KNB1-ZAMIV // Indicator: payment notice to sales department?""")
    ZAMIR = Column('ZAMIR', Boolean, default=None, doc="""Sourced from KNB1-ZAMIR // Indicator: payment notice to legal department?""")
    ZAMIB = Column('ZAMIB', Boolean, default=None, doc="""Sourced from KNB1-ZAMIB // Indicator: Payment notice to the accounting department ?""")
    ZAMIO = Column('ZAMIO', Boolean, default=None, doc="""Sourced from KNB1-ZAMIO // Indicator: payment notice to customer (w/o cleared items)?""")
    ZWELS = Column('ZWELS', String(10), default=None, doc="""Sourced from KNB1-ZWELS // List of the Payment Methods to be Considered""")
    XVERR = Column('XVERR', Boolean, default=None, doc="""Sourced from KNB1-XVERR // Indicator: Clearing between customer and vendor ?""")
    ZAHLS = Column('ZAHLS', String(1), default=None, doc="""Sourced from KNB1-ZAHLS // Block Key for Payment""")
    ZTERM = Column('ZTERM', String(4), default=None, doc="""Sourced from KNB1-ZTERM // Terms of Payment Key""")
    WAKON = Column('WAKON', String(4), default=None, doc="""Sourced from KNB1-WAKON // Terms of payment key for bill of exchange charges""")
    VZSKZ = Column('VZSKZ', String(2), default=None, doc="""Sourced from KNB1-VZSKZ // Interest calculation indicator""")
    ZINDT = Column('ZINDT', String(8), default=None, doc="""Sourced from KNB1-ZINDT // Key date of the last interest calculation""")
    ZINRT = Column('ZINRT', String(2), default=None, doc="""Sourced from KNB1-ZINRT // Interest calculation frequency in months""")
    EIKTO = Column('EIKTO', String(12), default=None, doc="""Sourced from KNB1-EIKTO // Our account number at customer""")
    ZSABE = Column('ZSABE', String(15), default=None, doc="""Sourced from KNB1-ZSABE // User at customer""")
    KVERM = Column('KVERM', String(30), default=None, doc="""Sourced from KNB1-KVERM // Memo""")
    FDGRV = Column('FDGRV', String(10), default=None, doc="""Sourced from KNB1-FDGRV // Planning group""")
    VRBKZ = Column('VRBKZ', String(2), default=None, doc="""Sourced from KNB1-VRBKZ // Export credit insurance institution number""")
    VLIBB = Column('VLIBB', Numeric(15,3,3), default=None, doc="""Sourced from KNB1-VLIBB // Amount Insured""")
    VRSZL = Column('VRSZL', Numeric(15,3,3), default=None, doc="""Sourced from KNB1-VRSZL // Insurance lead months""")
    VRSPR = Column('VRSPR', Numeric(15,3,3), default=None, doc="""Sourced from KNB1-VRSPR // Deductible percentage rate""")
    VRSNR = Column('VRSNR', String(10), default=None, doc="""Sourced from KNB1-VRSNR // Insurance number""")
    VERDT = Column('VERDT', Date, default=None, doc="""Sourced from KNB1-VERDT // Insurance validity date""")
    PERKZ = Column('PERKZ', String(1), default=None, doc="""Sourced from KNB1-PERKZ // Collective invoice variant""")
    XDEZV = Column('XDEZV', Boolean, default=None, doc="""Sourced from KNB1-XDEZV // Indicator: Local processing?""")
    XAUSZ = Column('XAUSZ', String(1), default=None, doc="""Sourced from KNB1-XAUSZ // Indicator for periodic account statements""")
    WEBTR = Column('WEBTR', Numeric(15,3,3), default=None, doc="""Sourced from KNB1-WEBTR // Bill of exchange limit (in local currency)""")
    REMIT = Column('REMIT', String(10), default=None, doc="""Sourced from KNB1-REMIT // Next payee""")
    DATLZ = Column('DATLZ', Date, default=None, doc="""Sourced from KNB1-DATLZ // Date of the last interest calculation run""")
    XZVER = Column('XZVER', Boolean, default=None, doc="""Sourced from KNB1-XZVER // Indicator: Record Payment History ?""")
    TOGRU = Column('TOGRU', String(4), default=None, doc="""Sourced from KNB1-TOGRU // Tolerance group for the business partner/G/L account""")
    KULTG = Column('KULTG', Numeric(15,3,3), default=None, doc="""Sourced from KNB1-KULTG // Probable time until check is paid""")
    HBKID = Column('HBKID', String(5), default=None, doc="""Sourced from KNB1-HBKID // Short Key for a House Bank""")
    XPORE = Column('XPORE', Boolean, default=None, doc="""Sourced from KNB1-XPORE // Indicator: Pay all items separately ?""")
    BLNKZ = Column('BLNKZ', String(2), default=None, doc="""Sourced from KNB1-BLNKZ // Subsidy Indicator for Determining the Reduction Rates""")
    ALTKN = Column('ALTKN', String(10), default=None, doc="""Sourced from KNB1-ALTKN // Previous Master Record Number""")
    ZGRUP = Column('ZGRUP', String(2), default=None, doc="""Sourced from KNB1-ZGRUP // Key for Payment Grouping""")
    URLID = Column('URLID', String(4), default=None, doc="""Sourced from KNB1-URLID // Short Key for Known/Negotiated Leave""")
    MGRUP = Column('MGRUP', String(2), default=None, doc="""Sourced from KNB1-MGRUP // Key for dunning notice grouping""")
    LOCKB = Column('LOCKB', String(7), default=None, doc="""Sourced from KNB1-LOCKB // Key of the Lockbox to Which the Customer Is To Pay""")
    UZAWE = Column('UZAWE', String(2), default=None, doc="""Sourced from KNB1-UZAWE // Payment Method Supplement""")
    EKVBD = Column('EKVBD', String(10), default=None, doc="""Sourced from KNB1-EKVBD // Account Number of Buying Group""")
    SREGL = Column('SREGL', String(3), default=None, doc="""Sourced from KNB1-SREGL // Selection Rule for Payment Advices""")
    XEDIP = Column('XEDIP', Boolean, default=None, doc="""Sourced from KNB1-XEDIP // Indicator: Send Payment Advices by EDI""")
    FRGRP = Column('FRGRP', String(4), default=None, doc="""Sourced from KNB1-FRGRP // Release Approval Group""")
    VRSDG = Column('VRSDG', String(3), default=None, doc="""Sourced from KNB1-VRSDG // Reason Code Conversion Version""")
    TLFXS = Column('TLFXS', String(31), default=None, doc="""Sourced from KNB1-TLFXS // Accounting clerk's fax number at the customer/vendor""")
    INTAD = Column('INTAD', String(130), default=None, doc="""Sourced from KNB1-INTAD // Internet address of partner company clerk""")
    XKNZB = Column('XKNZB', Boolean, default=None, doc="""Sourced from KNB1-XKNZB // Indicator: Alternative payer using account number""")
    GUZTE = Column('GUZTE', String(4), default=None, doc="""Sourced from KNB1-GUZTE // Payment Terms Key for Credit Memos""")
    GRICD = Column('GRICD', String(2), default=None, doc="""Sourced from KNB1-GRICD // Activity Code for Gross Income Tax""")
    GRIDT = Column('GRIDT', String(2), default=None, doc="""Sourced from KNB1-GRIDT // Distribution Type for Employment Tax""")
    WBRSL = Column('WBRSL', String(2), default=None, doc="""Sourced from KNB1-WBRSL // Value Adjustment Key""")
    CONFS = Column('CONFS', String(1), default=None, doc="""Sourced from KNB1-CONFS // Status of Change Authorization (Company Code Level)""")
    UPDAT = Column('UPDAT', Date, default=None, doc="""Sourced from KNB1-UPDAT // Date on Which the Changes Were Confirmed""")
    UPTIM = Column('UPTIM', Time, default=None, doc="""Sourced from KNB1-UPTIM // Time of Last Change Confirmation""")
    NODEL = Column('NODEL', Boolean, default=None, doc="""Sourced from KNB1-NODEL // Deletion bock for master record (company code level)""")
    TLFNS = Column('TLFNS', String(30), default=None, doc="""Sourced from KNB1-TLFNS // Accounting clerk's telephone number at business partner""")
    CESSION_KZ = Column('CESSION_KZ', String(2), default=None, doc="""Sourced from KNB1-CESSION_KZ // Accounts Receivable Pledging Indicator""")
    AVSND = Column('AVSND', String(1), default=None, doc="""Sourced from KNB1-AVSND // Indicator: Send Payment Advice by XML""")
    AD_HASH = Column('AD_HASH', String(10), default=None, doc="""Sourced from KNB1-AD_HASH // E-Mail Address for Avis: Hash Value""")
    QLAND = Column('QLAND', String(3), default=None, doc="""Sourced from KNB1-QLAND // Withholding Tax Country Key""")
    CVP_XBLCK_B = Column('CVP_XBLCK_B', String(1), default=None, doc="""Sourced from KNB1-CVP_XBLCK_B // Business Purpose Completed Flag""")
    CIIUCODE = Column('CIIUCODE', String(4), default=None, doc="""Sourced from KNB1-CIIUCODE // Main economic activity""")
    GMVKZD = Column('GMVKZD', Boolean, default=None, doc="""Sourced from KNB1-GMVKZD // Customer is in execution""")
    ZZDATYP = Column('ZZDATYP', String(2), default=None, doc="""Sourced from KNB1-ZZDATYP // Planning Date Control""")

    customer_id = synonym('KUNNR')
    company_cd = synonym('BUKRS')
    doc_create_dt = synonym('ERDAT')
    doc_create_user_id = synonym('ERNAM')
    deletion_ind = synonym('LOEVM')
    acctng_clerk_cd = synonym('BUSAB')
    auth_grp_id = synonym('BEGRU')
    planning_grp_cd = synonym('FDGRV')
    release_approval_grp_cd = synonym('FRGRP')
    last_update_dt = synonym('UPDAT')
    last_update_tm = synonym('UPTIM')


################################################################################




################################################################################

class CustomerHierarchy(SAP_Base):
    """\
    Table sourced from: KNVH
    Description: Customer Hierarchies
    """

    __tablename__ = "KNVH"

    HITYP = Column('HITYP', String(1), primary_key = True, doc="""Sourced from KNVH-HITYP // Customer hierarchy type""")
    KUNNR = Column('KUNNR', String(10), primary_key = True, doc="""Sourced from KNVH-KUNNR // Customer""")
    VKORG = Column('VKORG', String(4), primary_key = True, doc="""Sourced from KNVH-VKORG // Sales Organization""")
    VTWEG = Column('VTWEG', String(2), primary_key = True, doc="""Sourced from KNVH-VTWEG // Distribution Channel""")
    SPART = Column('SPART', String(2), primary_key = True, doc="""Sourced from KNVH-SPART // Division""")
    DATAB = Column('DATAB', Date, primary_key = True, doc="""Sourced from KNVH-DATAB // Start of validity period for assignment""")
    DATBI = Column('DATBI', Date, default=None, doc="""Sourced from KNVH-DATBI // End of validity period for the assignment""")
    HKUNNR = Column('HKUNNR', String(10), default=None, doc="""Sourced from KNVH-HKUNNR // Customer number of the higher-level customer hierarchy""")
    HVKORG = Column('HVKORG', String(4), default=None, doc="""Sourced from KNVH-HVKORG // Higher-level sales organization""")
    HVTWEG = Column('HVTWEG', String(2), default=None, doc="""Sourced from KNVH-HVTWEG // Higher-level distribution channel""")
    HSPART = Column('HSPART', String(2), default=None, doc="""Sourced from KNVH-HSPART // Higher-level division""")
    GRPNO = Column('GRPNO', String(3), default=None, doc="""Sourced from KNVH-GRPNO // Number of the routine used for copying""")
    BOKRE = Column('BOKRE', Boolean, default=None, doc="""Sourced from KNVH-BOKRE // Indicator: Customer Is Rebate-Relevant""")
    PRFRE = Column('PRFRE', Boolean, default=None, doc="""Sourced from KNVH-PRFRE // Relevant for price determination ID""")
    HZUOR = Column('HZUOR', String(2), default=None, doc="""Sourced from KNVH-HZUOR // Assignment to Hierarchy""")

    customer_id = synonym('KUNNR')
    sales_org_cd = synonym('VKORG')
    distr_chan_cd = synonym('VTWEG')
    div_cd = synonym('SPART')
    valid_from_dt = synonym('DATAB')
    valid_to_dt = synonym('DATBI')
    higher_sales_org_cd = synonym('HVKORG')
    higher_distr_chan_cd = synonym('HVTWEG')
    higher_div_cd = synonym('HSPART')
    cust_rebate_rlvnt_ind = synonym('BOKRE')
    relevant_for_price_determ_ind = synonym('PRFRE')
    hierarchy_assignment_cd = synonym('HZUOR')


################################################################################




################################################################################

class CustomerPartner(SAP_Base):
    """\
    Table sourced from: KNVP
    Description: Customer Master Partner Functions
    """

    __tablename__ = "KNVP"

    KUNNR = Column('KUNNR', String(10), primary_key = True, doc="""Sourced from KNVP-KUNNR // Customer Number""")
    VKORG = Column('VKORG', String(4), primary_key = True, doc="""Sourced from KNVP-VKORG // Sales Organization""")
    VTWEG = Column('VTWEG', String(2), primary_key = True, doc="""Sourced from KNVP-VTWEG // Distribution Channel""")
    SPART = Column('SPART', String(2), primary_key = True, doc="""Sourced from KNVP-SPART // Division""")
    PARVW = Column('PARVW', String(2), primary_key = True, doc="""Sourced from KNVP-PARVW // Partner Function""")
    PARZA = Column('PARZA', String(3), primary_key = True, doc="""Sourced from KNVP-PARZA // Partner counter""")
    KUNN2 = Column('KUNN2', String(10), default=None, doc="""Sourced from KNVP-KUNN2 // Customer number of business partner""")
    LIFNR = Column('LIFNR', String(10), default=None, doc="""Sourced from KNVP-LIFNR // Account Number of Vendor or Creditor""")
    PERNR = Column('PERNR', String(8), default=None, doc="""Sourced from KNVP-PERNR // Personnel Number""")
    PARNR = Column('PARNR', String(10), default=None, doc="""Sourced from KNVP-PARNR // Number of contact person""")
    KNREF = Column('KNREF', String(30), default=None, doc="""Sourced from KNVP-KNREF // Customer description of partner (plant, storage location)""")
    DEFPA = Column('DEFPA', Boolean, default=None, doc="""Sourced from KNVP-DEFPA // Default Partner""")

    customer_id = synonym('KUNNR')
    sales_org_cd = synonym('VKORG')
    distr_chan_cd = synonym('VTWEG')
    div_cd = synonym('SPART')
    partner_function_cd = synonym('PARVW')
    business_partner_customer_id = synonym('KUNN2')
    default_partner_ind = synonym('DEFPA')


################################################################################




################################################################################

class CustomerShipping(SAP_Base):
    """\
    Table sourced from: KNVS
    Description: Customer Master Shipping Data
    """

    __tablename__ = "KNVS"

    KUNNR = Column('KUNNR', String(10), primary_key = True, doc="""Sourced from KNVS-KUNNR // Customer Number""")
    VSTEL = Column('VSTEL', String(4), primary_key = True, doc="""Sourced from KNVS-VSTEL // Shipping Point/Receiving Point""")
    TRANS = Column('TRANS', String(3), default=None, doc="""Sourced from KNVS-TRANS // Transit route (sequence of the countries for transportation)""")
    TOPLA = Column('TOPLA', String(1), default=None, doc="""Sourced from KNVS-TOPLA // Route planning indicator""")
    TOURN = Column('TOURN', String(4), default=None, doc="""Sourced from KNVS-TOURN // Outline tour""")
    ANFRF = Column('ANFRF', String(3), default=None, doc="""Sourced from KNVS-ANFRF // Itinerary for regular route""")
    SPDNR = Column('SPDNR', String(10), default=None, doc="""Sourced from KNVS-SPDNR // Forwarding agent""")

    customer_id = synonym('KUNNR')
    shipping_receiving_point_cd = synonym('VSTEL')


################################################################################




################################################################################

class CustomerSalesOrg(SAP_Base):
    """\
    Table sourced from: KNVV
    Description: Customer Master Sales Data
    """

    __tablename__ = "KNVV"

    KUNNR = Column('KUNNR', String(10), primary_key = True, doc="""Sourced from KNVV-KUNNR // Customer Number""")
    VKORG = Column('VKORG', String(4), primary_key = True, doc="""Sourced from KNVV-VKORG // Sales Organization""")
    VTWEG = Column('VTWEG', String(2), primary_key = True, doc="""Sourced from KNVV-VTWEG // Distribution Channel""")
    SPART = Column('SPART', String(2), primary_key = True, doc="""Sourced from KNVV-SPART // Division""")
    ERNAM = Column('ERNAM', String(12), default=None, doc="""Sourced from KNVV-ERNAM // Name of Person who Created the Object""")
    ERDAT = Column('ERDAT', Date, default=None, doc="""Sourced from KNVV-ERDAT // Date on Which Record Was Created""")
    BEGRU = Column('BEGRU', String(4), default=None, doc="""Sourced from KNVV-BEGRU // Authorization Group""")
    LOEVM = Column('LOEVM', Boolean, default=None, doc="""Sourced from KNVV-LOEVM // Deletion flag for customer (sales level)""")
    VERSG = Column('VERSG', String(1), default=None, doc="""Sourced from KNVV-VERSG // Customer Statistics Group""")
    AUFSD = Column('AUFSD', String(2), default=None, doc="""Sourced from KNVV-AUFSD // Customer order block (sales area)""")
    KALKS = Column('KALKS', String(1), default=None, doc="""Sourced from KNVV-KALKS // Pricing procedure assigned to this customer""")
    KDGRP = Column('KDGRP', String(2), default=None, doc="""Sourced from KNVV-KDGRP // Customer group""")
    BZIRK = Column('BZIRK', String(6), default=None, doc="""Sourced from KNVV-BZIRK // Sales district""")
    KONDA = Column('KONDA', String(2), default=None, doc="""Sourced from KNVV-KONDA // Price group (customer)""")
    PLTYP = Column('PLTYP', String(2), default=None, doc="""Sourced from KNVV-PLTYP // Price list type""")
    AWAHR = Column('AWAHR', String(3), default=None, doc="""Sourced from KNVV-AWAHR // Order probability of the item""")
    INCO1 = Column('INCO1', String(3), default=None, doc="""Sourced from KNVV-INCO1 // Incoterms (Part 1)""")
    INCO2 = Column('INCO2', String(28), default=None, doc="""Sourced from KNVV-INCO2 // Incoterms (Part 2)""")
    LIFSD = Column('LIFSD', String(2), default=None, doc="""Sourced from KNVV-LIFSD // Customer delivery block (sales area)""")
    AUTLF = Column('AUTLF', Boolean, default=None, doc="""Sourced from KNVV-AUTLF // Complete delivery defined for each sales order?""")
    ANTLF = Column('ANTLF', Numeric(15,3,3), default=None, doc="""Sourced from KNVV-ANTLF // Maximum Number of Partial Deliveries Allowed Per Item""")
    KZTLF = Column('KZTLF', String(1), default=None, doc="""Sourced from KNVV-KZTLF // Partial delivery at item level""")
    KZAZU = Column('KZAZU', Boolean, default=None, doc="""Sourced from KNVV-KZAZU // Order Combination Indicator""")
    CHSPL = Column('CHSPL', Boolean, default=None, doc="""Sourced from KNVV-CHSPL // Batch split allowed""")
    LPRIO = Column('LPRIO', String(2), default=None, doc="""Sourced from KNVV-LPRIO // Delivery Priority""")
    EIKTO = Column('EIKTO', String(12), default=None, doc="""Sourced from KNVV-EIKTO // Shipper's (Our) Account Number at the Customer or Vendor""")
    VSBED = Column('VSBED', String(2), default=None, doc="""Sourced from KNVV-VSBED // Shipping Conditions""")
    FAKSD = Column('FAKSD', String(2), default=None, doc="""Sourced from KNVV-FAKSD // Billing block for customer (sales and distribution)""")
    MRNKZ = Column('MRNKZ', Boolean, default=None, doc="""Sourced from KNVV-MRNKZ // Manual invoice maintenance""")
    PERFK = Column('PERFK', String(2), default=None, doc="""Sourced from KNVV-PERFK // Invoice dates (calendar identification)""")
    PERRL = Column('PERRL', String(2), default=None, doc="""Sourced from KNVV-PERRL // Invoice list schedule (calendar identification)""")
    KVAKZ = Column('KVAKZ', Boolean, default=None, doc="""Sourced from KNVV-KVAKZ // Cost estimate indicator (inactive)""")
    KVAWT = Column('KVAWT', Numeric(15,3,3), default=None, doc="""Sourced from KNVV-KVAWT // Value limit for cost estimate (inactive)""")
    WAERS = Column('WAERS', String(5), default=None, doc="""Sourced from KNVV-WAERS // Currency""")
    KLABC = Column('KLABC', String(2), default=None, doc="""Sourced from KNVV-KLABC // Customer classification (ABC analysis)""")
    KTGRD = Column('KTGRD', String(2), default=None, doc="""Sourced from KNVV-KTGRD // Account assignment group for this customer""")
    ZTERM = Column('ZTERM', String(4), default=None, doc="""Sourced from KNVV-ZTERM // Terms of Payment Key""")
    VWERK = Column('VWERK', String(4), default=None, doc="""Sourced from KNVV-VWERK // Delivering Plant (Own or External)""")
    VKGRP = Column('VKGRP', String(3), default=None, doc="""Sourced from KNVV-VKGRP // Sales Group""")
    VKBUR = Column('VKBUR', String(4), default=None, doc="""Sourced from KNVV-VKBUR // Sales Office""")
    VSORT = Column('VSORT', String(10), default=None, doc="""Sourced from KNVV-VSORT // Item proposal""")
    KVGR1 = Column('KVGR1', String(3), default=None, doc="""Sourced from KNVV-KVGR1 // Customer group 1""")
    KVGR2 = Column('KVGR2', String(3), default=None, doc="""Sourced from KNVV-KVGR2 // Customer group 2""")
    KVGR3 = Column('KVGR3', String(3), default=None, doc="""Sourced from KNVV-KVGR3 // Customer group 3""")
    KVGR4 = Column('KVGR4', String(3), default=None, doc="""Sourced from KNVV-KVGR4 // Customer group 4""")
    KVGR5 = Column('KVGR5', String(3), default=None, doc="""Sourced from KNVV-KVGR5 // Customer group 5""")
    BOKRE = Column('BOKRE', Boolean, default=None, doc="""Sourced from KNVV-BOKRE // Indicator: Customer Is Rebate-Relevant""")
    BOIDT = Column('BOIDT', Date, default=None, doc="""Sourced from KNVV-BOIDT // Start of validity per.for the rebate index for the customer""")
    KURST = Column('KURST', String(4), default=None, doc="""Sourced from KNVV-KURST // Exchange Rate Type""")
    PRFRE = Column('PRFRE', Boolean, default=None, doc="""Sourced from KNVV-PRFRE // Relevant for price determination ID""")
    PRAT1 = Column('PRAT1', String(1), default=None, doc="""Sourced from KNVV-PRAT1 // ID for product attribute 1""")
    PRAT2 = Column('PRAT2', String(1), default=None, doc="""Sourced from KNVV-PRAT2 // ID for product attribute 2""")
    PRAT3 = Column('PRAT3', String(1), default=None, doc="""Sourced from KNVV-PRAT3 // ID for product attribute 3""")
    PRAT4 = Column('PRAT4', String(1), default=None, doc="""Sourced from KNVV-PRAT4 // ID for product attribute 4""")
    PRAT5 = Column('PRAT5', String(1), default=None, doc="""Sourced from KNVV-PRAT5 // ID for product attribute 5""")
    PRAT6 = Column('PRAT6', String(1), default=None, doc="""Sourced from KNVV-PRAT6 // ID for product attribute 6""")
    PRAT7 = Column('PRAT7', String(1), default=None, doc="""Sourced from KNVV-PRAT7 // ID for product attribute 7""")
    PRAT8 = Column('PRAT8', String(1), default=None, doc="""Sourced from KNVV-PRAT8 // ID for product attribute 8""")
    PRAT9 = Column('PRAT9', String(1), default=None, doc="""Sourced from KNVV-PRAT9 // ID for product attribute 9""")
    PRATA = Column('PRATA', String(1), default=None, doc="""Sourced from KNVV-PRATA // ID for product attribute 10""")
    KABSS = Column('KABSS', String(4), default=None, doc="""Sourced from KNVV-KABSS // Customer payment guarantee procedure""")
    KKBER = Column('KKBER', String(4), default=None, doc="""Sourced from KNVV-KKBER // Credit Control Area""")
    CASSD = Column('CASSD', String(2), default=None, doc="""Sourced from KNVV-CASSD // Sales block for customer (sales area)""")
    RDOFF = Column('RDOFF', Boolean, default=None, doc="""Sourced from KNVV-RDOFF // Switch off rounding?""")
    AGREL = Column('AGREL', Boolean, default=None, doc="""Sourced from KNVV-AGREL // Indicator: Relevant for agency business""")
    MEGRU = Column('MEGRU', String(4), default=None, doc="""Sourced from KNVV-MEGRU // Unit of Measure Group""")
    UEBTO = Column('UEBTO', Numeric(15,3,3), default=None, doc="""Sourced from KNVV-UEBTO // Overdelivery Tolerance Limit""")
    UNTTO = Column('UNTTO', Numeric(15,3,3), default=None, doc="""Sourced from KNVV-UNTTO // Underdelivery Tolerance Limit""")
    UEBTK = Column('UEBTK', Boolean, default=None, doc="""Sourced from KNVV-UEBTK // Unlimited overdelivery allowed""")
    PVKSM = Column('PVKSM', String(2), default=None, doc="""Sourced from KNVV-PVKSM // Customer procedure for product proposal""")
    PODKZ = Column('PODKZ', Boolean, default=None, doc="""Sourced from KNVV-PODKZ // Relevant for POD processing""")
    PODTG = Column('PODTG', Numeric(15,3,3), default=None, doc="""Sourced from KNVV-PODTG // Timeframe for Confirmation of POD""")
    BLIND = Column('BLIND', Boolean, default=None, doc="""Sourced from KNVV-BLIND // Index Structure Active for Subsequent Settlement (in AB)""")
    CARRIER_NOTIF = Column('CARRIER_NOTIF', Boolean, default=None, doc="""Sourced from KNVV-CARRIER_NOTIF // Carrier is to be notified""")
    CVP_XBLCK_V = Column('CVP_XBLCK_V', String(1), default=None, doc="""Sourced from KNVV-CVP_XBLCK_V // Business Purpose Completed Flag""")

    customer_id = synonym('KUNNR')
    sales_org_cd = synonym('VKORG')
    distr_chan_cd = synonym('VTWEG')
    div_cd = synonym('SPART')
    doc_create_user_id = synonym('ERNAM')
    doc_create_dt = synonym('ERDAT')
    auth_grp_id = synonym('BEGRU')
    deletion_ind = synonym('LOEVM')
    cust_order_blk_cd = synonym('AUFSD')
    customer_pricing_procedure_cd = synonym('KALKS')
    customer_group_id = synonym('KDGRP')
    sales_district_id = synonym('BZIRK')
    customer_pricing_grp_cd = synonym('KONDA')
    incoterms_cd = synonym('INCO1')
    incoterms_desc = synonym('INCO2')
    max_nbr_partial_deliveries = synonym('ANTLF')
    item_partial_delivery_cd = synonym('KZTLF')
    batch_split_allowed_ind = synonym('CHSPL')
    delivery_priority_cd = synonym('LPRIO')
    shipping_condition_cd = synonym('VSBED')
    currency_cd = synonym('WAERS')
    from_facility_id = synonym('VWERK')
    sales_group_id = synonym('VKGRP')
    sales_office_id = synonym('VKBUR')
    freight_policy_cd = synonym('KVGR2')
    cust_rebate_rlvnt_ind = synonym('BOKRE')
    rebate_idx_valid_from_dt = synonym('BOIDT')
    relevant_for_price_determ_ind = synonym('PRFRE')
    credit_control_area_cd = synonym('KKBER')
    uom_group_cd = synonym('MEGRU')


################################################################################




################################################################################

class Vendor(SAP_Base):
    """\
    Table sourced from: LFA1
    Description: Vendor Master (General Section)
    """

    __tablename__ = "LFA1"

    LIFNR = Column('LIFNR', String(10), primary_key = True, doc="""Sourced from LFA1-LIFNR // Account Number of Vendor or Creditor""")
    LAND1 = Column('LAND1', String(3), default=None, doc="""Sourced from LFA1-LAND1 // Country Key""")
    NAME1 = Column('NAME1', String(35), default=None, doc="""Sourced from LFA1-NAME1 // Name 1""")
    NAME2 = Column('NAME2', String(35), default=None, doc="""Sourced from LFA1-NAME2 // Name 2""")
    NAME3 = Column('NAME3', String(35), default=None, doc="""Sourced from LFA1-NAME3 // Name 3""")
    NAME4 = Column('NAME4', String(35), default=None, doc="""Sourced from LFA1-NAME4 // Name 4""")
    ORT01 = Column('ORT01', String(35), default=None, doc="""Sourced from LFA1-ORT01 // City""")
    ORT02 = Column('ORT02', String(35), default=None, doc="""Sourced from LFA1-ORT02 // District""")
    PFACH = Column('PFACH', String(10), default=None, doc="""Sourced from LFA1-PFACH // PO Box""")
    PSTL2 = Column('PSTL2', String(10), default=None, doc="""Sourced from LFA1-PSTL2 // P.O. Box Postal Code""")
    PSTLZ = Column('PSTLZ', String(10), default=None, doc="""Sourced from LFA1-PSTLZ // Postal Code""")
    REGIO = Column('REGIO', String(3), default=None, doc="""Sourced from LFA1-REGIO // Region (State, Province, County)""")
    SORTL = Column('SORTL', String(10), default=None, doc="""Sourced from LFA1-SORTL // Sort field""")
    STRAS = Column('STRAS', String(35), default=None, doc="""Sourced from LFA1-STRAS // House number and street""")
    ADRNR = Column('ADRNR', String(10), default=None, doc="""Sourced from LFA1-ADRNR // Address""")
    MCOD1 = Column('MCOD1', String(25), default=None, doc="""Sourced from LFA1-MCOD1 // Search term for matchcode search""")
    MCOD2 = Column('MCOD2', String(25), default=None, doc="""Sourced from LFA1-MCOD2 // Search term for matchcode search""")
    MCOD3 = Column('MCOD3', String(25), default=None, doc="""Sourced from LFA1-MCOD3 // Search term for matchcode search""")
    ANRED = Column('ANRED', String(15), default=None, doc="""Sourced from LFA1-ANRED // Title""")
    BAHNS = Column('BAHNS', String(25), default=None, doc="""Sourced from LFA1-BAHNS // Train station""")
    BBBNR = Column('BBBNR', String(7), default=None, doc="""Sourced from LFA1-BBBNR // International location number  (part 1)""")
    BBSNR = Column('BBSNR', String(5), default=None, doc="""Sourced from LFA1-BBSNR // International location number (Part 2)""")
    BEGRU = Column('BEGRU', String(4), default=None, doc="""Sourced from LFA1-BEGRU // Authorization Group""")
    BRSCH = Column('BRSCH', String(4), default=None, doc="""Sourced from LFA1-BRSCH // Industry key""")
    BUBKZ = Column('BUBKZ', String(1), default=None, doc="""Sourced from LFA1-BUBKZ // Check digit for the international location number""")
    DATLT = Column('DATLT', String(14), default=None, doc="""Sourced from LFA1-DATLT // Data communication line no.""")
    DTAMS = Column('DTAMS', String(1), default=None, doc="""Sourced from LFA1-DTAMS // Indicator for Data Medium Exchange""")
    DTAWS = Column('DTAWS', String(2), default=None, doc="""Sourced from LFA1-DTAWS // Instruction key for data medium exchange""")
    ERDAT = Column('ERDAT', Date, default=None, doc="""Sourced from LFA1-ERDAT // Date on which the Record Was Created""")
    ERNAM = Column('ERNAM', String(12), default=None, doc="""Sourced from LFA1-ERNAM // Name of Person who Created the Object""")
    ESRNR = Column('ESRNR', String(11), default=None, doc="""Sourced from LFA1-ESRNR // ISR Subscriber Number""")
    KONZS = Column('KONZS', String(10), default=None, doc="""Sourced from LFA1-KONZS // Group key""")
    KTOKK = Column('KTOKK', String(4), default=None, doc="""Sourced from LFA1-KTOKK // Vendor account group""")
    KUNNR = Column('KUNNR', String(10), default=None, doc="""Sourced from LFA1-KUNNR // Customer Number""")
    LNRZA = Column('LNRZA', String(10), default=None, doc="""Sourced from LFA1-LNRZA // Account Number of the Alternative Payee""")
    LOEVM = Column('LOEVM', Boolean, default=None, doc="""Sourced from LFA1-LOEVM // Central Deletion Flag for Master Record""")
    SPERR = Column('SPERR', Boolean, default=None, doc="""Sourced from LFA1-SPERR // Central posting block""")
    SPERM = Column('SPERM', Boolean, default=None, doc="""Sourced from LFA1-SPERM // Centrally imposed purchasing block""")
    SPRAS = Column('SPRAS', String(1), default=None, doc="""Sourced from LFA1-SPRAS // Language Key""")
    STCD1 = Column('STCD1', String(16), default=None, doc="""Sourced from LFA1-STCD1 // Tax Number 1""")
    STCD2 = Column('STCD2', String(11), default=None, doc="""Sourced from LFA1-STCD2 // Tax Number 2""")
    STKZA = Column('STKZA', String(1), default=None, doc="""Sourced from LFA1-STKZA // Indicator: Business Partner Subject to Equalization Tax?""")
    STKZU = Column('STKZU', Boolean, default=None, doc="""Sourced from LFA1-STKZU // Liable for VAT""")
    TELBX = Column('TELBX', String(15), default=None, doc="""Sourced from LFA1-TELBX // Telebox number""")
    TELF1 = Column('TELF1', String(16), default=None, doc="""Sourced from LFA1-TELF1 // First telephone number""")
    TELF2 = Column('TELF2', String(16), default=None, doc="""Sourced from LFA1-TELF2 // Second telephone number""")
    TELFX = Column('TELFX', String(31), default=None, doc="""Sourced from LFA1-TELFX // Fax Number""")
    TELTX = Column('TELTX', String(30), default=None, doc="""Sourced from LFA1-TELTX // Teletex number""")
    TELX1 = Column('TELX1', String(30), default=None, doc="""Sourced from LFA1-TELX1 // Telex number""")
    XCPDK = Column('XCPDK', Boolean, default=None, doc="""Sourced from LFA1-XCPDK // Indicator: Is the account a one-time account?""")
    XZEMP = Column('XZEMP', Boolean, default=None, doc="""Sourced from LFA1-XZEMP // Indicator: Alternative payee in document allowed ?""")
    VBUND = Column('VBUND', String(6), default=None, doc="""Sourced from LFA1-VBUND // Company ID of Trading Partner""")
    FISKN = Column('FISKN', String(10), default=None, doc="""Sourced from LFA1-FISKN // Account number of the master record with fiscal address""")
    STCEG = Column('STCEG', String(20), default=None, doc="""Sourced from LFA1-STCEG // VAT Registration Number""")
    STKZN = Column('STKZN', String(1), default=None, doc="""Sourced from LFA1-STKZN // Natural Person""")
    SPERQ = Column('SPERQ', String(2), default=None, doc="""Sourced from LFA1-SPERQ // Function That Will Be Blocked""")
    GBORT = Column('GBORT', String(25), default=None, doc="""Sourced from LFA1-GBORT // Place of birth of the person subject to withholding tax""")
    GBDAT = Column('GBDAT', Date, default=None, doc="""Sourced from LFA1-GBDAT // Date of birth of the person subject to withholding tax""")
    SEXKZ = Column('SEXKZ', String(1), default=None, doc="""Sourced from LFA1-SEXKZ // Key for the Sex of the Person Subject to Withholding Tax""")
    KRAUS = Column('KRAUS', String(11), default=None, doc="""Sourced from LFA1-KRAUS // Credit information number""")
    REVDB = Column('REVDB', String(8), default=None, doc="""Sourced from LFA1-REVDB // Last review (external)""")
    QSSYS = Column('QSSYS', String(4), default=None, doc="""Sourced from LFA1-QSSYS // Vendor's QM system""")
    KTOCK = Column('KTOCK', String(4), default=None, doc="""Sourced from LFA1-KTOCK // Reference Account Group for One-Time Account (Vendor)""")
    PFORT = Column('PFORT', String(35), default=None, doc="""Sourced from LFA1-PFORT // PO Box city""")
    WERKS = Column('WERKS', String(4), default=None, doc="""Sourced from LFA1-WERKS // Plant (Own or External)""")
    LTSNA = Column('LTSNA', Boolean, default=None, doc="""Sourced from LFA1-LTSNA // Indicator: vendor sub-range relevant""")
    WERKR = Column('WERKR', Boolean, default=None, doc="""Sourced from LFA1-WERKR // Indicator: plant level relevant""")
    PLKAL = Column('PLKAL', String(2), default=None, doc="""Sourced from LFA1-PLKAL // Factory calendar key""")
    DUEFL = Column('DUEFL', String(1), default=None, doc="""Sourced from LFA1-DUEFL // Status of Data Transfer into Subsequent Release""")
    TXJCD = Column('TXJCD', String(15), default=None, doc="""Sourced from LFA1-TXJCD // Tax Jurisdiction""")
    SPERZ = Column('SPERZ', Boolean, default=None, doc="""Sourced from LFA1-SPERZ // Payment Block""")
    SCACD = Column('SCACD', String(4), default=None, doc="""Sourced from LFA1-SCACD // Standard carrier access code""")
    SFRGR = Column('SFRGR', String(4), default=None, doc="""Sourced from LFA1-SFRGR // Forwarding agent freight group""")
    LZONE = Column('LZONE', String(10), default=None, doc="""Sourced from LFA1-LZONE // Transportation zone to or from which the goods are delivered""")
    XLFZA = Column('XLFZA', Boolean, default=None, doc="""Sourced from LFA1-XLFZA // Indicator: Alternative payee using account number""")
    DLGRP = Column('DLGRP', String(4), default=None, doc="""Sourced from LFA1-DLGRP // Service agent procedure group""")
    FITYP = Column('FITYP', String(2), default=None, doc="""Sourced from LFA1-FITYP // Tax type""")
    STCDT = Column('STCDT', String(2), default=None, doc="""Sourced from LFA1-STCDT // Tax Number Type""")
    REGSS = Column('REGSS', Boolean, default=None, doc="""Sourced from LFA1-REGSS // Registered for Social Insurance""")
    ACTSS = Column('ACTSS', String(3), default=None, doc="""Sourced from LFA1-ACTSS // Activity Code for Social Insurance""")
    STCD3 = Column('STCD3', String(18), default=None, doc="""Sourced from LFA1-STCD3 // Tax Number 3""")
    STCD4 = Column('STCD4', String(18), default=None, doc="""Sourced from LFA1-STCD4 // Tax Number 4""")
    STCD5 = Column('STCD5', String(60), default=None, doc="""Sourced from LFA1-STCD5 // Tax Number 5""")
    IPISP = Column('IPISP', Boolean, default=None, doc="""Sourced from LFA1-IPISP // Tax Split""")
    TAXBS = Column('TAXBS', String(1), default=None, doc="""Sourced from LFA1-TAXBS // Tax Base in Percentage""")
    PROFS = Column('PROFS', String(30), default=None, doc="""Sourced from LFA1-PROFS // Profession""")
    STGDL = Column('STGDL', String(2), default=None, doc="""Sourced from LFA1-STGDL // Shipment: statistics group, transportation service agent""")
    EMNFR = Column('EMNFR', String(10), default=None, doc="""Sourced from LFA1-EMNFR // External manufacturer code name or number""")
    LFURL = Column('LFURL', String(132), default=None, doc="""Sourced from LFA1-LFURL // Uniform Resource Locator""")
    J_1KFREPRE = Column('J_1KFREPRE', String(10), default=None, doc="""Sourced from LFA1-J_1KFREPRE // Name of Representative""")
    J_1KFTBUS = Column('J_1KFTBUS', String(30), default=None, doc="""Sourced from LFA1-J_1KFTBUS // Type of Business""")
    J_1KFTIND = Column('J_1KFTIND', String(30), default=None, doc="""Sourced from LFA1-J_1KFTIND // Type of Industry""")
    CONFS = Column('CONFS', String(1), default=None, doc="""Sourced from LFA1-CONFS // Status of Change Authorization (Central)""")
    UPDAT = Column('UPDAT', Date, default=None, doc="""Sourced from LFA1-UPDAT // Date on Which the Changes Were Confirmed""")
    UPTIM = Column('UPTIM', Time, default=None, doc="""Sourced from LFA1-UPTIM // Time of Last Change Confirmation""")
    NODEL = Column('NODEL', Boolean, default=None, doc="""Sourced from LFA1-NODEL // Central deletion block for master record""")
    QSSYSDAT = Column('QSSYSDAT', String(8), default=None, doc="""Sourced from LFA1-QSSYSDAT // Validity date of certification""")
    PODKZB = Column('PODKZB', String(1), default=None, doc="""Sourced from LFA1-PODKZB // Vendor indicator relevant for proof of delivery""")
    FISKU = Column('FISKU', String(10), default=None, doc="""Sourced from LFA1-FISKU // Account Number of Master Record of Tax Office Responsible""")
    STENR = Column('STENR', String(18), default=None, doc="""Sourced from LFA1-STENR // Tax Number at Responsible Tax Authority""")
    CARRIER_CONF = Column('CARRIER_CONF', String(1), default=None, doc="""Sourced from LFA1-CARRIER_CONF // Carrier confirmation is expected""")
    MIN_COMP = Column('MIN_COMP', Boolean, default=None, doc="""Sourced from LFA1-MIN_COMP // Micro company indicator""")
    TERM_LI = Column('TERM_LI', Boolean, default=None, doc="""Sourced from LFA1-TERM_LI // Terms of Liability""")
    CRC_NUM = Column('CRC_NUM', String(25), default=None, doc="""Sourced from LFA1-CRC_NUM // CRC number""")
    CVP_XBLCK = Column('CVP_XBLCK', String(1), default=None, doc="""Sourced from LFA1-CVP_XBLCK // Business Purpose Completed Flag""")
    RG = Column('RG', String(11), default=None, doc="""Sourced from LFA1-RG // RG Number""")
    EXP = Column('EXP', String(3), default=None, doc="""Sourced from LFA1-EXP // Issued by""")
    UF = Column('UF', String(2), default=None, doc="""Sourced from LFA1-UF // State""")
    RGDATE = Column('RGDATE', String(8), default=None, doc="""Sourced from LFA1-RGDATE // RG Issue Date""")
    RIC = Column('RIC', String(11), default=None, doc="""Sourced from LFA1-RIC // RIC Number""")
    RNE = Column('RNE', String(10), default=None, doc="""Sourced from LFA1-RNE // Foreign National Registration""")
    RNEDATE = Column('RNEDATE', String(8), default=None, doc="""Sourced from LFA1-RNEDATE // RNE Issue Date""")
    CNAE = Column('CNAE', String(7), default=None, doc="""Sourced from LFA1-CNAE // CNAE""")
    LEGALNAT = Column('LEGALNAT', String(4), default=None, doc="""Sourced from LFA1-LEGALNAT // Legal Nature""")
    CRTN = Column('CRTN', String(1), default=None, doc="""Sourced from LFA1-CRTN // CRT Number""")
    ICMSTAXPAY = Column('ICMSTAXPAY', String(2), default=None, doc="""Sourced from LFA1-ICMSTAXPAY // ICMS Taxpayer""")
    INDTYP = Column('INDTYP', String(2), default=None, doc="""Sourced from LFA1-INDTYP // Industry Main Type""")
    TDT = Column('TDT', String(2), default=None, doc="""Sourced from LFA1-TDT // Tax Declaration Type""")
    COMSIZE = Column('COMSIZE', String(2), default=None, doc="""Sourced from LFA1-COMSIZE // Company Size""")
    DECREGPC = Column('DECREGPC', String(2), default=None, doc="""Sourced from LFA1-DECREGPC // Declaration Regimen for PIS/COFINS""")
    J_SC_CAPITAL = Column('J_SC_CAPITAL', String(15), default=None, doc="""Sourced from LFA1-J_SC_CAPITAL // Capital Amount""")
    J_SC_CURRENCY = Column('J_SC_CURRENCY', String(5), default=None, doc="""Sourced from LFA1-J_SC_CURRENCY // Currency""")
    ALC = Column('ALC', String(8), default=None, doc="""Sourced from LFA1-ALC // Agency Location Code""")
    PMT_OFFICE = Column('PMT_OFFICE', String(5), default=None, doc="""Sourced from LFA1-PMT_OFFICE // Payment Office""")
    PSOFG = Column('PSOFG', String(10), default=None, doc="""Sourced from LFA1-PSOFG // Processor group""")
    PSOIS = Column('PSOIS', String(20), default=None, doc="""Sourced from LFA1-PSOIS // Subledger acct preprocessing procedure""")
    PSON1 = Column('PSON1', String(35), default=None, doc="""Sourced from LFA1-PSON1 // Name 1""")
    PSON2 = Column('PSON2', String(35), default=None, doc="""Sourced from LFA1-PSON2 // Name 2""")
    PSON3 = Column('PSON3', String(35), default=None, doc="""Sourced from LFA1-PSON3 // Name 3""")
    PSOVN = Column('PSOVN', String(35), default=None, doc="""Sourced from LFA1-PSOVN // First Name""")
    PSOTL = Column('PSOTL', String(20), default=None, doc="""Sourced from LFA1-PSOTL // Title""")
    PSOHS = Column('PSOHS', String(6), default=None, doc="""Sourced from LFA1-PSOHS // House number: is no longer used from Release 4.6B""")
    PSOST = Column('PSOST', String(28), default=None, doc="""Sourced from LFA1-PSOST // Street: No longer used from Release 4.6B""")
    TRANSPORT_CHAIN = Column('TRANSPORT_CHAIN', String(10), default=None, doc="""Sourced from LFA1-TRANSPORT_CHAIN // Transportation Chain""")
    STAGING_TIME = Column('STAGING_TIME', String(3), default=None, doc="""Sourced from LFA1-STAGING_TIME // Staging Time in Days""")
    SCHEDULING_TYPE = Column('SCHEDULING_TYPE', String(1), default=None, doc="""Sourced from LFA1-SCHEDULING_TYPE // Scheduling Procedure""")
    SUBMI_RELEVANT = Column('SUBMI_RELEVANT', Boolean, default=None, doc="""Sourced from LFA1-SUBMI_RELEVANT // Cross Docking: Relevant for Collective Numbering""")
    ZPREF_ORD = Column('ZPREF_ORD', String(1), default=None, doc="""Sourced from LFA1-ZPREF_ORD // Preferred Ordering Method""")
    ZCHANGE_ORDER = Column('ZCHANGE_ORDER', String(1), default=None, doc="""Sourced from LFA1-ZCHANGE_ORDER // Change Order Restriction""")
    ZARIBA_ENABLED = Column('ZARIBA_ENABLED', String(1), default=None, doc="""Sourced from LFA1-ZARIBA_ENABLED // Ariba Enabled""")

    country_cd = synonym('LAND1')
    name = synonym('NAME1')
    name2 = synonym('NAME2')
    name4 = synonym('NAME4')
    city = synonym('ORT01')
    district = synonym('ORT02')
    po_box = synonym('PFACH')
    region = synonym('REGIO')
    addr_id = synonym('ADRNR')
    auth_grp_id = synonym('BEGRU')
    doc_create_dt = synonym('ERDAT')
    doc_create_user_id = synonym('ERNAM')
    customer_id = synonym('KUNNR')
    deletion_ind = synonym('LOEVM')
    language_cd = synonym('SPRAS')
    payment_block_ind = synonym('SPERZ')
    transportation_zone_cd = synonym('LZONE')
    ext_mfg_cd = synonym('EMNFR')
    last_update_dt = synonym('UPDAT')
    last_update_tm = synonym('UPTIM')
    industry_type_cd = synonym('INDTYP')


################################################################################




################################################################################

class VendorCompany(SAP_Base):
    """\
    Table sourced from: LFB1
    Description: Vendor Master (Company Code)
    """

    __tablename__ = "LFB1"

    LIFNR = Column('LIFNR', String(10), primary_key = True, doc="""Sourced from LFB1-LIFNR // Account Number of Vendor or Creditor""")
    BUKRS = Column('BUKRS', String(4), primary_key = True, doc="""Sourced from LFB1-BUKRS // Company Code""")
    PERNR = Column('PERNR', String(8), default=None, doc="""Sourced from LFB1-PERNR // Personnel Number""")
    ERDAT = Column('ERDAT', Date, default=None, doc="""Sourced from LFB1-ERDAT // Date on which the Record Was Created""")
    ERNAM = Column('ERNAM', String(12), default=None, doc="""Sourced from LFB1-ERNAM // Name of Person who Created the Object""")
    SPERR = Column('SPERR', Boolean, default=None, doc="""Sourced from LFB1-SPERR // Posting block for company code""")
    LOEVM = Column('LOEVM', Boolean, default=None, doc="""Sourced from LFB1-LOEVM // Deletion Flag for Master Record (Company Code Level)""")
    ZUAWA = Column('ZUAWA', String(3), default=None, doc="""Sourced from LFB1-ZUAWA // Key for sorting according to assignment numbers""")
    AKONT = Column('AKONT', String(10), default=None, doc="""Sourced from LFB1-AKONT // Reconciliation Account in General Ledger""")
    BEGRU = Column('BEGRU', String(4), default=None, doc="""Sourced from LFB1-BEGRU // Authorization Group""")
    VZSKZ = Column('VZSKZ', String(2), default=None, doc="""Sourced from LFB1-VZSKZ // Interest calculation indicator""")
    ZWELS = Column('ZWELS', String(10), default=None, doc="""Sourced from LFB1-ZWELS // List of the Payment Methods to be Considered""")
    XVERR = Column('XVERR', Boolean, default=None, doc="""Sourced from LFB1-XVERR // Indicator: Clearing between customer and vendor?""")
    ZAHLS = Column('ZAHLS', String(1), default=None, doc="""Sourced from LFB1-ZAHLS // Block Key for Payment""")
    ZTERM = Column('ZTERM', String(4), default=None, doc="""Sourced from LFB1-ZTERM // Terms of Payment Key""")
    EIKTO = Column('EIKTO', String(12), default=None, doc="""Sourced from LFB1-EIKTO // Our account number with the vendor""")
    ZSABE = Column('ZSABE', String(15), default=None, doc="""Sourced from LFB1-ZSABE // Clerk at vendor""")
    KVERM = Column('KVERM', String(30), default=None, doc="""Sourced from LFB1-KVERM // Memo""")
    FDGRV = Column('FDGRV', String(10), default=None, doc="""Sourced from LFB1-FDGRV // Planning group""")
    BUSAB = Column('BUSAB', String(2), default=None, doc="""Sourced from LFB1-BUSAB // Accounting clerk""")
    LNRZE = Column('LNRZE', String(10), default=None, doc="""Sourced from LFB1-LNRZE // Head office account number""")
    LNRZB = Column('LNRZB', String(10), default=None, doc="""Sourced from LFB1-LNRZB // Account number of the alternative payee""")
    ZINDT = Column('ZINDT', String(8), default=None, doc="""Sourced from LFB1-ZINDT // Key date of the last interest calculation""")
    ZINRT = Column('ZINRT', String(2), default=None, doc="""Sourced from LFB1-ZINRT // Interest calculation frequency in months""")
    DATLZ = Column('DATLZ', Date, default=None, doc="""Sourced from LFB1-DATLZ // Date of the last interest calculation run""")
    XDEZV = Column('XDEZV', Boolean, default=None, doc="""Sourced from LFB1-XDEZV // Indicator: Local processing?""")
    WEBTR = Column('WEBTR', Numeric(15,3,3), default=None, doc="""Sourced from LFB1-WEBTR // Bill of exchange limit (in local currency)""")
    KULTG = Column('KULTG', Numeric(15,3,3), default=None, doc="""Sourced from LFB1-KULTG // Probable time until check is paid""")
    REPRF = Column('REPRF', Boolean, default=None, doc="""Sourced from LFB1-REPRF // Check Flag for Double Invoices or Credit Memos""")
    TOGRU = Column('TOGRU', String(4), default=None, doc="""Sourced from LFB1-TOGRU // Tolerance group for the business partner/G/L account""")
    HBKID = Column('HBKID', String(5), default=None, doc="""Sourced from LFB1-HBKID // Short Key for a House Bank""")
    XPORE = Column('XPORE', Boolean, default=None, doc="""Sourced from LFB1-XPORE // Indicator: Pay all items separately ?""")
    QSZNR = Column('QSZNR', String(10), default=None, doc="""Sourced from LFB1-QSZNR // Certificate Number of the Withholding Tax Exemption""")
    QSZDT = Column('QSZDT', Date, default=None, doc="""Sourced from LFB1-QSZDT // Validity Date for Withholding Tax Exemption Certificate""")
    QSSKZ = Column('QSSKZ', String(2), default=None, doc="""Sourced from LFB1-QSSKZ // Withholding Tax Code""")
    BLNKZ = Column('BLNKZ', String(2), default=None, doc="""Sourced from LFB1-BLNKZ // Subsidy Indicator for Determining the Reduction Rates""")
    MINDK = Column('MINDK', String(3), default=None, doc="""Sourced from LFB1-MINDK // Minority Indicators""")
    ALTKN = Column('ALTKN', String(10), default=None, doc="""Sourced from LFB1-ALTKN // Previous Master Record Number""")
    ZGRUP = Column('ZGRUP', String(2), default=None, doc="""Sourced from LFB1-ZGRUP // Key for Payment Grouping""")
    MGRUP = Column('MGRUP', String(2), default=None, doc="""Sourced from LFB1-MGRUP // Key for dunning notice grouping""")
    UZAWE = Column('UZAWE', String(2), default=None, doc="""Sourced from LFB1-UZAWE // Payment Method Supplement""")
    QSREC = Column('QSREC', String(2), default=None, doc="""Sourced from LFB1-QSREC // Vendor Recipient Type""")
    QSBGR = Column('QSBGR', String(1), default=None, doc="""Sourced from LFB1-QSBGR // Authority for Exemption from Withholding Tax""")
    QLAND = Column('QLAND', String(3), default=None, doc="""Sourced from LFB1-QLAND // Withholding Tax Country Key""")
    XEDIP = Column('XEDIP', Boolean, default=None, doc="""Sourced from LFB1-XEDIP // Indicator: Send Payment Advices by EDI""")
    FRGRP = Column('FRGRP', String(4), default=None, doc="""Sourced from LFB1-FRGRP // Release Approval Group""")
    TOGRR = Column('TOGRR', String(4), default=None, doc="""Sourced from LFB1-TOGRR // Tolerance group; Invoice Verification""")
    TLFXS = Column('TLFXS', String(31), default=None, doc="""Sourced from LFB1-TLFXS // Accounting clerk's fax number at the customer/vendor""")
    INTAD = Column('INTAD', String(130), default=None, doc="""Sourced from LFB1-INTAD // Internet address of partner company clerk""")
    XLFZB = Column('XLFZB', Boolean, default=None, doc="""Sourced from LFB1-XLFZB // Indicator: Alternative payee using account number""")
    GUZTE = Column('GUZTE', String(4), default=None, doc="""Sourced from LFB1-GUZTE // Payment Terms Key for Credit Memos""")
    GRICD = Column('GRICD', String(2), default=None, doc="""Sourced from LFB1-GRICD // Activity Code for Gross Income Tax""")
    GRIDT = Column('GRIDT', String(2), default=None, doc="""Sourced from LFB1-GRIDT // Distribution Type for Employment Tax""")
    XAUSZ = Column('XAUSZ', String(1), default=None, doc="""Sourced from LFB1-XAUSZ // Indicator for periodic account statements""")
    CERDT = Column('CERDT', Date, default=None, doc="""Sourced from LFB1-CERDT // Certification date""")
    CONFS = Column('CONFS', String(1), default=None, doc="""Sourced from LFB1-CONFS // Status of Change Authorization (Company Code Level)""")
    UPDAT = Column('UPDAT', Date, default=None, doc="""Sourced from LFB1-UPDAT // Date on Which the Changes Were Confirmed""")
    UPTIM = Column('UPTIM', Time, default=None, doc="""Sourced from LFB1-UPTIM // Time of Last Change Confirmation""")
    NODEL = Column('NODEL', Boolean, default=None, doc="""Sourced from LFB1-NODEL // Deletion bock for master record (company code level)""")
    TLFNS = Column('TLFNS', String(30), default=None, doc="""Sourced from LFB1-TLFNS // Accounting clerk's telephone number at business partner""")
    AVSND = Column('AVSND', String(1), default=None, doc="""Sourced from LFB1-AVSND // Indicator: Send Payment Advice by XML""")
    AD_HASH = Column('AD_HASH', String(10), default=None, doc="""Sourced from LFB1-AD_HASH // E-Mail Address for Avis: Hash Value""")
    CVP_XBLCK_B = Column('CVP_XBLCK_B', String(1), default=None, doc="""Sourced from LFB1-CVP_XBLCK_B // Business Purpose Completed Flag""")
    CIIUCODE = Column('CIIUCODE', String(4), default=None, doc="""Sourced from LFB1-CIIUCODE // Main economic activity""")
    J_SC_SUBCONTYPE = Column('J_SC_SUBCONTYPE', String(1), default=None, doc="""Sourced from LFB1-J_SC_SUBCONTYPE // Subcontractor Type""")
    J_SC_COMPDATE = Column('J_SC_COMPDATE', String(3), default=None, doc="""Sourced from LFB1-J_SC_COMPDATE // Completion Date Of Inspection""")
    J_SC_OFFSM = Column('J_SC_OFFSM', String(1), default=None, doc="""Sourced from LFB1-J_SC_OFFSM // Offset Method""")
    J_SC_OFFSR = Column('J_SC_OFFSR', String(3), default=None, doc="""Sourced from LFB1-J_SC_OFFSR // Offset Percentage""")
    BASIS_PNT = Column('BASIS_PNT', String(6), default=None, doc="""Sourced from LFB1-BASIS_PNT // Average daily basis points for purchase cards""")
    GMVKZK = Column('GMVKZK', Boolean, default=None, doc="""Sourced from LFB1-GMVKZK // Vendor is in execution""")
    PREPAY_RELEVANT = Column('PREPAY_RELEVANT', String(1), default=None, doc="""Sourced from LFB1-PREPAY_RELEVANT // Prepayment Relevance (Vendor Master)""")
    ASSIGN_TEST = Column('ASSIGN_TEST', String(4), default=None, doc="""Sourced from LFB1-ASSIGN_TEST // Assignment Test Group""")
    YY1099_VENDOR = Column('YY1099_VENDOR', String(10), default=None, doc="""Sourced from LFB1-YY1099_VENDOR // 1099 Alternate Vendor""")
    YYKONZS = Column('YYKONZS', String(10), default=None, doc="""Sourced from LFB1-YYKONZS // Group key""")
    YYBRSCH = Column('YYBRSCH', String(4), default=None, doc="""Sourced from LFB1-YYBRSCH // Industry key""")
    YYINTAD = Column('YYINTAD', String(130), default=None, doc="""Sourced from LFB1-YYINTAD // Internet address of partner company clerk""")

    company_cd = synonym('BUKRS')
    doc_create_dt = synonym('ERDAT')
    doc_create_user_id = synonym('ERNAM')
    deletion_ind = synonym('LOEVM')
    auth_grp_id = synonym('BEGRU')
    planning_grp_cd = synonym('FDGRV')
    acctng_clerk_cd = synonym('BUSAB')
    release_approval_grp_cd = synonym('FRGRP')
    certification_dt = synonym('CERDT')
    last_update_dt = synonym('UPDAT')
    last_update_tm = synonym('UPTIM')


################################################################################




################################################################################

class VendorPurchOrg(SAP_Base):
    """\
    Table sourced from: LFM1
    Description: Vendor master record purchasing organization data
    """

    __tablename__ = "LFM1"

    LIFNR = Column('LIFNR', String(10), primary_key = True, doc="""Sourced from LFM1-LIFNR // Vendor Account Number""")
    EKORG = Column('EKORG', String(4), primary_key = True, doc="""Sourced from LFM1-EKORG // Purchasing Organization""")
    ERDAT = Column('ERDAT', Date, default=None, doc="""Sourced from LFM1-ERDAT // Date on Which Record Was Created""")
    ERNAM = Column('ERNAM', String(12), default=None, doc="""Sourced from LFM1-ERNAM // Name of Person who Created the Object""")
    SPERM = Column('SPERM', Boolean, default=None, doc="""Sourced from LFM1-SPERM // Purchasing block at purchasing organization level""")
    LOEVM = Column('LOEVM', Boolean, default=None, doc="""Sourced from LFM1-LOEVM // Delete flag for vendor at purchasing level""")
    LFABC = Column('LFABC', String(1), default=None, doc="""Sourced from LFM1-LFABC // ABC indicator""")
    WAERS = Column('WAERS', String(5), default=None, doc="""Sourced from LFM1-WAERS // Purchase order currency""")
    VERKF = Column('VERKF', String(30), default=None, doc="""Sourced from LFM1-VERKF // Responsible Salesperson at Vendor's Office""")
    TELF1 = Column('TELF1', String(16), default=None, doc="""Sourced from LFM1-TELF1 // Vendor's telephone number""")
    MINBW = Column('MINBW', Numeric(15,3,3), default=None, doc="""Sourced from LFM1-MINBW // Minimum order value""")
    ZTERM = Column('ZTERM', String(4), default=None, doc="""Sourced from LFM1-ZTERM // Terms of Payment Key""")
    INCO1 = Column('INCO1', String(3), default=None, doc="""Sourced from LFM1-INCO1 // Incoterms (Part 1)""")
    INCO2 = Column('INCO2', String(28), default=None, doc="""Sourced from LFM1-INCO2 // Incoterms (Part 2)""")
    WEBRE = Column('WEBRE', Boolean, default=None, doc="""Sourced from LFM1-WEBRE // Indicator: GR-Based Invoice Verification""")
    KZABS = Column('KZABS', Boolean, default=None, doc="""Sourced from LFM1-KZABS // Order Acknowledgment Requirement""")
    KALSK = Column('KALSK', String(2), default=None, doc="""Sourced from LFM1-KALSK // Group for Calculation Schema (Vendor)""")
    KZAUT = Column('KZAUT', Boolean, default=None, doc="""Sourced from LFM1-KZAUT // Automatic Generation of Purchase Order Allowed""")
    EXPVZ = Column('EXPVZ', String(1), default=None, doc="""Sourced from LFM1-EXPVZ // Mode of Transport for Foreign Trade""")
    ZOLLA = Column('ZOLLA', String(6), default=None, doc="""Sourced from LFM1-ZOLLA // Customs Office: Office of Exit/Entry for Foreign Trade""")
    MEPRF = Column('MEPRF', String(1), default=None, doc="""Sourced from LFM1-MEPRF // Price Determination (Pricing) Date Control""")
    EKGRP = Column('EKGRP', String(3), default=None, doc="""Sourced from LFM1-EKGRP // Purchasing Group""")
    XERSY = Column('XERSY', Boolean, default=None, doc="""Sourced from LFM1-XERSY // Evaluated Receipt Settlement (ERS)""")
    PLIFZ = Column('PLIFZ', Numeric(15,3,3), default=None, doc="""Sourced from LFM1-PLIFZ // Planned Delivery Time in Days""")
    MRPPP = Column('MRPPP', String(3), default=None, doc="""Sourced from LFM1-MRPPP // Planning calendar""")
    LFRHY = Column('LFRHY', String(3), default=None, doc="""Sourced from LFM1-LFRHY // Planning cycle""")
    LIBES = Column('LIBES', String(1), default=None, doc="""Sourced from LFM1-LIBES // Order entry by vendor""")
    LIPRE = Column('LIPRE', String(2), default=None, doc="""Sourced from LFM1-LIPRE // Price marking, vendor""")
    LISER = Column('LISER', String(1), default=None, doc="""Sourced from LFM1-LISER // Rack-jobbing: vendor""")
    PRFRE = Column('PRFRE', Boolean, default=None, doc="""Sourced from LFM1-PRFRE // Indicator: 'relev. to price determination (vend. hierarchy)""")
    NRGEW = Column('NRGEW', String(1), default=None, doc="""Sourced from LFM1-NRGEW // Indicator whether discount in kind granted""")
    BOIND = Column('BOIND', Boolean, default=None, doc="""Sourced from LFM1-BOIND // Indicator: index compilation for subseq. settlement active""")
    BLIND = Column('BLIND', Boolean, default=None, doc="""Sourced from LFM1-BLIND // Indicator: Doc. index compilation active for purchase orders""")
    KZRET = Column('KZRET', Boolean, default=None, doc="""Sourced from LFM1-KZRET // Indicates whether vendor is returns vendor""")
    SKRIT = Column('SKRIT', String(1), default=None, doc="""Sourced from LFM1-SKRIT // Vendor sort criterion for materials""")
    BSTAE = Column('BSTAE', String(4), default=None, doc="""Sourced from LFM1-BSTAE // Confirmation Control Key""")
    RDPRF = Column('RDPRF', String(4), default=None, doc="""Sourced from LFM1-RDPRF // Rounding Profile""")
    MEGRU = Column('MEGRU', String(4), default=None, doc="""Sourced from LFM1-MEGRU // Unit of Measure Group""")
    VENSL = Column('VENSL', Numeric(15,3,3), default=None, doc="""Sourced from LFM1-VENSL // Vendor service level""")
    BOPNR = Column('BOPNR', String(4), default=None, doc="""Sourced from LFM1-BOPNR // Restriction Profile for PO-Based Load Building""")
    XERSR = Column('XERSR', Boolean, default=None, doc="""Sourced from LFM1-XERSR // Automatic evaluated receipt settlement for return items""")
    EIKTO = Column('EIKTO', String(12), default=None, doc="""Sourced from LFM1-EIKTO // Our account number with the vendor""")
    ABUEB = Column('ABUEB', String(4), default=None, doc="""Sourced from LFM1-ABUEB // Release Creation Profile""")
    PAPRF = Column('PAPRF', String(4), default=None, doc="""Sourced from LFM1-PAPRF // Profile for transferring material data via IDoc PROACT""")
    AGREL = Column('AGREL', Boolean, default=None, doc="""Sourced from LFM1-AGREL // Indicator: Relevant for agency business""")
    XNBWY = Column('XNBWY', Boolean, default=None, doc="""Sourced from LFM1-XNBWY // Revaluation allowed""")
    VSBED = Column('VSBED', String(2), default=None, doc="""Sourced from LFM1-VSBED // Shipping Conditions""")
    LEBRE = Column('LEBRE', Boolean, default=None, doc="""Sourced from LFM1-LEBRE // Indicator for Service-Based Invoice Verification""")
    BOLRE = Column('BOLRE', Boolean, default=None, doc="""Sourced from LFM1-BOLRE // Indicator: vendor subject to subseq. settlement accounting""")
    UMSAE = Column('UMSAE', Boolean, default=None, doc="""Sourced from LFM1-UMSAE // Comparison/agreement of business volumes necessary""")
    VENDOR_RMA_REQ = Column('VENDOR_RMA_REQ', String(1), default=None, doc="""Sourced from LFM1-VENDOR_RMA_REQ // Vendor RMA Number Required""")
    ACTIVITY_PROFIL = Column('ACTIVITY_PROFIL', String(4), default=None, doc="""Sourced from LFM1-ACTIVITY_PROFIL // Activity Profile for PO Controlling""")
    TRANSPORT_CHAIN = Column('TRANSPORT_CHAIN', String(10), default=None, doc="""Sourced from LFM1-TRANSPORT_CHAIN // Transportation Chain""")
    STAGING_TIME = Column('STAGING_TIME', String(3), default=None, doc="""Sourced from LFM1-STAGING_TIME // Staging Time in Days""")
    YYVENCON = Column('YYVENCON', String(1), default=None, doc="""Sourced from LFM1-YYVENCON // User Access for Contracts Flag""")

    prch_org_cd = synonym('EKORG')
    doc_create_dt = synonym('ERDAT')
    doc_create_user_id = synonym('ERNAM')
    deletion_ind = synonym('LOEVM')
    currency_cd = synonym('WAERS')
    minimum_order_value_qty = synonym('MINBW')
    incoterms_cd = synonym('INCO1')
    incoterms_desc = synonym('INCO2')
    price_determ_date_control_cd = synonym('MEPRF')
    prch_grp_cd = synonym('EKGRP')
    relevant_for_price_determ_ind = synonym('PRFRE')
    cnfrm_cntrl_cd = synonym('BSTAE')
    uom_group_cd = synonym('MEGRU')
    shipping_condition_cd = synonym('VSBED')


################################################################################




################################################################################

class DeliveryHdr(SAP_Base):
    """\
    Table sourced from: LIKP
    Description: SD Document: Delivery Header Data
    """

    __tablename__ = "LIKP"

    VBELN = Column('VBELN', String(10), primary_key = True, doc="""Sourced from LIKP-VBELN // Delivery""")
    ERNAM = Column('ERNAM', String(12), default=None, doc="""Sourced from LIKP-ERNAM // Name of Person who Created the Object""")
    ERZET = Column('ERZET', Time, default=None, doc="""Sourced from LIKP-ERZET // Entry time""")
    ERDAT = Column('ERDAT', Date, default=None, doc="""Sourced from LIKP-ERDAT // Date on Which Record Was Created""")
    BZIRK = Column('BZIRK', String(6), default=None, doc="""Sourced from LIKP-BZIRK // Sales district""")
    VSTEL = Column('VSTEL', String(4), default=None, doc="""Sourced from LIKP-VSTEL // Shipping Point/Receiving Point""")
    VKORG = Column('VKORG', String(4), default=None, doc="""Sourced from LIKP-VKORG // Sales Organization""")
    LFART = Column('LFART', String(4), default=None, doc="""Sourced from LIKP-LFART // Delivery Type""")
    AUTLF = Column('AUTLF', Boolean, default=None, doc="""Sourced from LIKP-AUTLF // Complete delivery defined for each sales order?""")
    KZAZU = Column('KZAZU', Boolean, default=None, doc="""Sourced from LIKP-KZAZU // Order Combination Indicator""")
    WADAT = Column('WADAT', Date, default=None, doc="""Sourced from LIKP-WADAT // Planned goods movement date""")
    LDDAT = Column('LDDAT', Date, default=None, doc="""Sourced from LIKP-LDDAT // Loading Date""")
    TDDAT = Column('TDDAT', String(8), default=None, doc="""Sourced from LIKP-TDDAT // Transportation Planning Date""")
    LFDAT = Column('LFDAT', Date, default=None, doc="""Sourced from LIKP-LFDAT // Delivery Date""")
    KODAT = Column('KODAT', Date, default=None, doc="""Sourced from LIKP-KODAT // Picking Date""")
    ABLAD = Column('ABLAD', String(25), default=None, doc="""Sourced from LIKP-ABLAD // Unloading Point""")
    INCO1 = Column('INCO1', String(3), default=None, doc="""Sourced from LIKP-INCO1 // Incoterms (Part 1)""")
    INCO2 = Column('INCO2', String(28), default=None, doc="""Sourced from LIKP-INCO2 // Incoterms (Part 2)""")
    EXPKZ = Column('EXPKZ', String(1), default=None, doc="""Sourced from LIKP-EXPKZ // Export indicator""")
    ROUTE = Column('ROUTE', String(6), default=None, doc="""Sourced from LIKP-ROUTE // Route""")
    FAKSK = Column('FAKSK', String(2), default=None, doc="""Sourced from LIKP-FAKSK // Billing block in SD document""")
    LIFSK = Column('LIFSK', String(2), default=None, doc="""Sourced from LIKP-LIFSK // Delivery block (document header)""")
    VBTYP = Column('VBTYP', String(1), default=None, doc="""Sourced from LIKP-VBTYP // SD document category""")
    KNFAK = Column('KNFAK', String(2), default=None, doc="""Sourced from LIKP-KNFAK // Customer factory calendar""")
    TPQUA = Column('TPQUA', String(1), default=None, doc="""Sourced from LIKP-TPQUA // not currently in use""")
    TPGRP = Column('TPGRP', String(2), default=None, doc="""Sourced from LIKP-TPGRP // not currently in use""")
    LPRIO = Column('LPRIO', String(2), default=None, doc="""Sourced from LIKP-LPRIO // Delivery Priority""")
    VSBED = Column('VSBED', String(2), default=None, doc="""Sourced from LIKP-VSBED // Shipping Conditions""")
    KUNNR = Column('KUNNR', String(10), default=None, doc="""Sourced from LIKP-KUNNR // Ship-to party""")
    KUNAG = Column('KUNAG', String(10), default=None, doc="""Sourced from LIKP-KUNAG // Sold-to party""")
    KDGRP = Column('KDGRP', String(2), default=None, doc="""Sourced from LIKP-KDGRP // Customer group""")
    STZKL = Column('STZKL', Numeric(15,3,3), default=None, doc="""Sourced from LIKP-STZKL // Not Currently in Use""")
    STZZU = Column('STZZU', Numeric(15,3,3), default=None, doc="""Sourced from LIKP-STZZU // not currently in use""")
    BTGEW = Column('BTGEW', String(15), default=None, doc="""Sourced from LIKP-BTGEW // Total Weight""")
    NTGEW = Column('NTGEW', Numeric(15,3,3), default=None, doc="""Sourced from LIKP-NTGEW // Net weight""")
    GEWEI = Column('GEWEI', String(3), default=None, doc="""Sourced from LIKP-GEWEI // Weight Unit""")
    VOLUM = Column('VOLUM', Numeric(15,3,3), default=None, doc="""Sourced from LIKP-VOLUM // Volume""")
    VOLEH = Column('VOLEH', String(3), default=None, doc="""Sourced from LIKP-VOLEH // Volume unit""")
    ANZPK = Column('ANZPK', String(5), default=None, doc="""Sourced from LIKP-ANZPK // Total number of packages in delivery""")
    BEROT = Column('BEROT', String(20), default=None, doc="""Sourced from LIKP-BEROT // Picked items location""")
    LFUHR = Column('LFUHR', Time, default=None, doc="""Sourced from LIKP-LFUHR // Time of delivery""")
    GRULG = Column('GRULG', String(4), default=None, doc="""Sourced from LIKP-GRULG // Weight group for delivery (To group)""")
    LSTEL = Column('LSTEL', String(2), default=None, doc="""Sourced from LIKP-LSTEL // Loading Point""")
    TRAGR = Column('TRAGR', String(4), default=None, doc="""Sourced from LIKP-TRAGR // Transportation Group""")
    FKARV = Column('FKARV', String(4), default=None, doc="""Sourced from LIKP-FKARV // Proposed billing type for a delivery-related billing doc.""")
    FKDAT = Column('FKDAT', Date, default=None, doc="""Sourced from LIKP-FKDAT // Billing date for billing index and printout""")
    PERFK = Column('PERFK', String(2), default=None, doc="""Sourced from LIKP-PERFK // Invoice dates (calendar identification)""")
    ROUTA = Column('ROUTA', String(6), default=None, doc="""Sourced from LIKP-ROUTA // Route""")
    STAFO = Column('STAFO', String(6), default=None, doc="""Sourced from LIKP-STAFO // Update group for statistics update""")
    KALSM = Column('KALSM', String(6), default=None, doc="""Sourced from LIKP-KALSM // Procedure (Pricing, Output Control, Acct. Det., Costing,...)""")
    KNUMV = Column('KNUMV', String(10), default=None, doc="""Sourced from LIKP-KNUMV // Number of the document condition""")
    WAERK = Column('WAERK', String(5), default=None, doc="""Sourced from LIKP-WAERK // SD Document Currency""")
    VKBUR = Column('VKBUR', String(4), default=None, doc="""Sourced from LIKP-VKBUR // Sales Office""")
    VBEAK = Column('VBEAK', Numeric(15,3,3), default=None, doc="""Sourced from LIKP-VBEAK // Shipping processing time for the entire document""")
    ZUKRL = Column('ZUKRL', String(40), default=None, doc="""Sourced from LIKP-ZUKRL // Combination criteria for delivery""")
    VERUR = Column('VERUR', String(35), default=None, doc="""Sourced from LIKP-VERUR // Distribution delivery""")
    COMMN = Column('COMMN', String(5), default=None, doc="""Sourced from LIKP-COMMN // Communication number for Q-API interface""")
    STWAE = Column('STWAE', String(5), default=None, doc="""Sourced from LIKP-STWAE // Statistics currency""")
    STCUR = Column('STCUR', Numeric(15,3,3), default=None, doc="""Sourced from LIKP-STCUR // Exchange rate for statistics""")
    EXNUM = Column('EXNUM', String(10), default=None, doc="""Sourced from LIKP-EXNUM // Number of foreign trade data in MM and SD documents""")
    AENAM = Column('AENAM', String(12), default=None, doc="""Sourced from LIKP-AENAM // Name of Person Who Changed Object""")
    AEDAT = Column('AEDAT', Date, default=None, doc="""Sourced from LIKP-AEDAT // Changed On""")
    LGNUM = Column('LGNUM', String(3), default=None, doc="""Sourced from LIKP-LGNUM // Warehouse Number / Warehouse Complex""")
    LISPL = Column('LISPL', String(1), default=None, doc="""Sourced from LIKP-LISPL // Delivery within one warehouse""")
    VKOIV = Column('VKOIV', String(4), default=None, doc="""Sourced from LIKP-VKOIV // Sales organization for intercompany billing""")
    VTWIV = Column('VTWIV', String(2), default=None, doc="""Sourced from LIKP-VTWIV // Distribution channel for intercompany billing""")
    SPAIV = Column('SPAIV', String(2), default=None, doc="""Sourced from LIKP-SPAIV // Division for intercompany billing""")
    FKAIV = Column('FKAIV', String(4), default=None, doc="""Sourced from LIKP-FKAIV // Billing type for intercompany billing""")
    PIOIV = Column('PIOIV', String(2), default=None, doc="""Sourced from LIKP-PIOIV // Date for intercompany billing""")
    FKDIV = Column('FKDIV', Date, default=None, doc="""Sourced from LIKP-FKDIV // Billing date for intercompany billing""")
    KUNIV = Column('KUNIV', String(10), default=None, doc="""Sourced from LIKP-KUNIV // Customer number for intercompany billing""")
    KKBER = Column('KKBER', String(4), default=None, doc="""Sourced from LIKP-KKBER // Credit Control Area""")
    KNKLI = Column('KNKLI', String(10), default=None, doc="""Sourced from LIKP-KNKLI // Customer's account number with credit limit reference""")
    GRUPP = Column('GRUPP', String(4), default=None, doc="""Sourced from LIKP-GRUPP // Customer Credit Group""")
    SBGRP = Column('SBGRP', String(3), default=None, doc="""Sourced from LIKP-SBGRP // Credit representative group for credit management""")
    CTLPC = Column('CTLPC', String(3), default=None, doc="""Sourced from LIKP-CTLPC // Credit management: Risk category""")
    CMWAE = Column('CMWAE', String(5), default=None, doc="""Sourced from LIKP-CMWAE // Currency key of credit control area""")
    AMTBL = Column('AMTBL', String(15), default=None, doc="""Sourced from LIKP-AMTBL // Released credit value of the document""")
    BOLNR = Column('BOLNR', String(35), default=None, doc="""Sourced from LIKP-BOLNR // Bill of lading""")
    LIFNR = Column('LIFNR', String(10), default=None, doc="""Sourced from LIKP-LIFNR // Vendor Account Number""")
    TRATY = Column('TRATY', String(4), default=None, doc="""Sourced from LIKP-TRATY // Means-of-Transport Type""")
    TRAID = Column('TRAID', String(20), default=None, doc="""Sourced from LIKP-TRAID // Means of Transport ID""")
    CMFRE = Column('CMFRE', Date, default=None, doc="""Sourced from LIKP-CMFRE // Release date of the document determined by credit management""")
    CMNGV = Column('CMNGV', Date, default=None, doc="""Sourced from LIKP-CMNGV // Next date""")
    XABLN = Column('XABLN', String(10), default=None, doc="""Sourced from LIKP-XABLN // Goods Receipt/Issue Slip Number""")
    BLDAT = Column('BLDAT', Date, default=None, doc="""Sourced from LIKP-BLDAT // Document Date in Document""")
    WADAT_IST = Column('WADAT_IST', Date, default=None, doc="""Sourced from LIKP-WADAT_IST // Actual Goods Movement Date""")
    TRSPG = Column('TRSPG', String(2), default=None, doc="""Sourced from LIKP-TRSPG // Shipment Blocking Reason""")
    TPSID = Column('TPSID', String(5), default=None, doc="""Sourced from LIKP-TPSID // ID for external transport system""")
    LIFEX = Column('LIFEX', String(35), default=None, doc="""Sourced from LIKP-LIFEX // External Identification of Delivery Note""")
    TERNR = Column('TERNR', String(12), default=None, doc="""Sourced from LIKP-TERNR // Order Number""")
    KALSM_CH = Column('KALSM_CH', String(6), default=None, doc="""Sourced from LIKP-KALSM_CH // Search procedure for batch determination""")
    KLIEF = Column('KLIEF', Boolean, default=None, doc="""Sourced from LIKP-KLIEF // Correction delivery""")
    KALSP = Column('KALSP', String(6), default=None, doc="""Sourced from LIKP-KALSP // Shipping: Pricing procedure""")
    KNUMP = Column('KNUMP', String(10), default=None, doc="""Sourced from LIKP-KNUMP // Number of document condition - pricing""")
    NETWR = Column('NETWR', Numeric(15,3,3), default=None, doc="""Sourced from LIKP-NETWR // Net Value of the Sales Order in Document Currency""")
    AULWE = Column('AULWE', String(10), default=None, doc="""Sourced from LIKP-AULWE // Route Schedule""")
    WERKS = Column('WERKS', String(4), default=None, doc="""Sourced from LIKP-WERKS // Receiving plant for deliveries""")
    LCNUM = Column('LCNUM', String(10), default=None, doc="""Sourced from LIKP-LCNUM // Financial doc. processing: Internal financial doc. number""")
    ABSSC = Column('ABSSC', String(6), default=None, doc="""Sourced from LIKP-ABSSC // Payment guarantee procedure""")
    KOUHR = Column('KOUHR', Time, default=None, doc="""Sourced from LIKP-KOUHR // Picking time (local time, with reference to a plant)""")
    TDUHR = Column('TDUHR', Time, default=None, doc="""Sourced from LIKP-TDUHR // Transp. Planning Time (Local, Relating to a Shipping Point)""")
    LDUHR = Column('LDUHR', Time, default=None, doc="""Sourced from LIKP-LDUHR // Loading Time (Local Time Relating to a Shipping Point)""")
    WAUHR = Column('WAUHR', Time, default=None, doc="""Sourced from LIKP-WAUHR // Time of Goods Issue (Local, Relating to a Plant)""")
    LGTOR = Column('LGTOR', String(3), default=None, doc="""Sourced from LIKP-LGTOR // Door for Warehouse Number""")
    LGBZO = Column('LGBZO', String(10), default=None, doc="""Sourced from LIKP-LGBZO // Staging Area for Warehouse Complex""")
    AKWAE = Column('AKWAE', String(5), default=None, doc="""Sourced from LIKP-AKWAE // Currency key for letter-of-credit procg in foreign trade""")
    AKKUR = Column('AKKUR', Numeric(15,3,3), default=None, doc="""Sourced from LIKP-AKKUR // Exchange rate for letter-of-credit procg in foreign trade""")
    AKPRZ = Column('AKPRZ', Numeric(15,3,3), default=None, doc="""Sourced from LIKP-AKPRZ // Depreciation percentage for financial document processing""")
    PROLI = Column('PROLI', String(3), default=None, doc="""Sourced from LIKP-PROLI // Dangerous Goods Management Profile in SD Documents""")
    XBLNR = Column('XBLNR', String(25), default=None, doc="""Sourced from LIKP-XBLNR // Reference Document Number""")
    HANDLE = Column('HANDLE', Integer, default=None, doc="""Sourced from LIKP-HANDLE // Worldwide unique key for LIKP-VBELN""")
    TSEGFL = Column('TSEGFL', String(1), default=None, doc="""Sourced from LIKP-TSEGFL // Time segment exists""")
    TSEGTP = Column('TSEGTP', String(10), default=None, doc="""Sourced from LIKP-TSEGTP // Event group time segment delivery header""")
    TZONIS = Column('TZONIS', String(6), default=None, doc="""Sourced from LIKP-TZONIS // Time zone of delivering location""")
    TZONRC = Column('TZONRC', String(6), default=None, doc="""Sourced from LIKP-TZONRC // Time zone of recipient location""")
    CONT_DG = Column('CONT_DG', Boolean, default=None, doc="""Sourced from LIKP-CONT_DG // Indicator: Document contains dangerous goods""")
    VERURSYS = Column('VERURSYS', String(10), default=None, doc="""Sourced from LIKP-VERURSYS // Distribution delivery: Original system""")
    KZWAB = Column('KZWAB', String(1), default=None, doc="""Sourced from LIKP-KZWAB // Indicator for controlling goods movement""")
    VLSTK = Column('VLSTK', String(1), default=None, doc="""Sourced from LIKP-VLSTK // Distribution Status (Decentralized Warehouse Processing)""")
    TCODE = Column('TCODE', String(20), default=None, doc="""Sourced from LIKP-TCODE // Transaction Code""")
    VSART = Column('VSART', String(2), default=None, doc="""Sourced from LIKP-VSART // Shipping type""")
    TRMTYP = Column('TRMTYP', String(18), default=None, doc="""Sourced from LIKP-TRMTYP // Means of Transport""")
    SDABW = Column('SDABW', String(4), default=None, doc="""Sourced from LIKP-SDABW // Special processing indicator""")
    VBUND = Column('VBUND', String(6), default=None, doc="""Sourced from LIKP-VBUND // Company ID""")
    XWOFF = Column('XWOFF', Boolean, default=None, doc="""Sourced from LIKP-XWOFF // Calculation of val. open""")
    DIRTA = Column('DIRTA', Boolean, default=None, doc="""Sourced from LIKP-DIRTA // Automatic TO Creation Immediately After TR Generation""")
    PRVBE = Column('PRVBE', String(10), default=None, doc="""Sourced from LIKP-PRVBE // Production Supply Area""")
    FOLAR = Column('FOLAR', String(4), default=None, doc="""Sourced from LIKP-FOLAR // Delivery Type""")
    PODAT = Column('PODAT', Date, default=None, doc="""Sourced from LIKP-PODAT // Date (proof of delivery)""")
    POTIM = Column('POTIM', Time, default=None, doc="""Sourced from LIKP-POTIM // Confirmation time""")
    IMWRK = Column('IMWRK', Boolean, default=None, doc="""Sourced from LIKP-IMWRK // Delivery has Status 'In Plant'""")
    SPE_LOEKZ = Column('SPE_LOEKZ', Boolean, default=None, doc="""Sourced from LIKP-SPE_LOEKZ // Document deletion indicator""")
    SPE_LOC_SEQ = Column('SPE_LOC_SEQ', String(3), default=None, doc="""Sourced from LIKP-SPE_LOC_SEQ // Sequence of Intermediate Locations in Returns Process""")
    SPE_ACC_APP_STS = Column('SPE_ACC_APP_STS', String(1), default=None, doc="""Sourced from LIKP-SPE_ACC_APP_STS // Delivery Confirmation Status""")
    SPE_SHP_INF_STS = Column('SPE_SHP_INF_STS', String(1), default=None, doc="""Sourced from LIKP-SPE_SHP_INF_STS // Shipment Information Status""")
    SPE_RET_CANC = Column('SPE_RET_CANC', Boolean, default=None, doc="""Sourced from LIKP-SPE_RET_CANC // Returns: Flag showing that an ASN is cancelled""")
    SPE_WAUHR_IST = Column('SPE_WAUHR_IST', String(6), default=None, doc="""Sourced from LIKP-SPE_WAUHR_IST // Time of Goods Issue (Local, Relating to a Plant)""")
    SPE_WAZONE_IST = Column('SPE_WAZONE_IST', String(6), default=None, doc="""Sourced from LIKP-SPE_WAZONE_IST // Time Zone""")
    SPE_REV_VLSTK = Column('SPE_REV_VLSTK', String(1), default=None, doc="""Sourced from LIKP-SPE_REV_VLSTK // Distribution Status (Decentralized Warehouse Processing)""")
    SPE_LE_SCENARIO = Column('SPE_LE_SCENARIO', String(1), default=None, doc="""Sourced from LIKP-SPE_LE_SCENARIO // Scenario Logistic Execution""")
    SPE_ORIG_SYS = Column('SPE_ORIG_SYS', String(1), default=None, doc="""Sourced from LIKP-SPE_ORIG_SYS // Original System Type""")
    SPE_CHNG_SYS = Column('SPE_CHNG_SYS', String(1), default=None, doc="""Sourced from LIKP-SPE_CHNG_SYS // Last Changer's System Type""")
    SPE_GEOROUTE = Column('SPE_GEOROUTE', String(10), default=None, doc="""Sourced from LIKP-SPE_GEOROUTE // Description of a Geographical Route""")
    SPE_GEOROUTEIND = Column('SPE_GEOROUTEIND', String(1), default=None, doc="""Sourced from LIKP-SPE_GEOROUTEIND // Change Indicator for the Route""")
    SPE_CARRIER_IND = Column('SPE_CARRIER_IND', String(1), default=None, doc="""Sourced from LIKP-SPE_CARRIER_IND // Change Indicator for the Carrier""")
    SPE_GTS_REL = Column('SPE_GTS_REL', String(2), default=None, doc="""Sourced from LIKP-SPE_GTS_REL // Goods Traffic Type""")
    SPE_GTS_RT_CDE = Column('SPE_GTS_RT_CDE', String(10), default=None, doc="""Sourced from LIKP-SPE_GTS_RT_CDE // Route Code for SAP Global Trade Services""")
    SPE_REL_TMSTMP = Column('SPE_REL_TMSTMP', String(15), default=None, doc="""Sourced from LIKP-SPE_REL_TMSTMP // Release Time Stamp""")
    SPE_UNIT_SYSTEM = Column('SPE_UNIT_SYSTEM', String(10), default=None, doc="""Sourced from LIKP-SPE_UNIT_SYSTEM // Measurement Unit System""")
    SPE_INV_BFR_GI = Column('SPE_INV_BFR_GI', String(1), default=None, doc="""Sourced from LIKP-SPE_INV_BFR_GI // Invoice Creation Before Goods Issue""")
    SPE_QI_STATUS = Column('SPE_QI_STATUS', String(1), default=None, doc="""Sourced from LIKP-SPE_QI_STATUS // Status of Quality Inspection for Returns Deliveries""")
    SPE_RED_IND = Column('SPE_RED_IND', String(1), default=None, doc="""Sourced from LIKP-SPE_RED_IND // SPE indicator if redirecting has occured""")
    SAKES = Column('SAKES', String(1), default=None, doc="""Sourced from LIKP-SAKES // SAP Global Trade Services: Storage Status of Delivery""")
    SPE_LIFEX_TYPE = Column('SPE_LIFEX_TYPE', String(1), default=None, doc="""Sourced from LIKP-SPE_LIFEX_TYPE // Type of External Identification""")
    SPE_TTYPE = Column('SPE_TTYPE', String(10), default=None, doc="""Sourced from LIKP-SPE_TTYPE // Means of Transport""")
    SPE_PRO_NUMBER = Column('SPE_PRO_NUMBER', String(35), default=None, doc="""Sourced from LIKP-SPE_PRO_NUMBER // Partner Identification : Progressive Identification Number""")
    SPE_BILLING_IND = Column('SPE_BILLING_IND', String(1), default=None, doc="""Sourced from LIKP-SPE_BILLING_IND // EWM Billing Indicator""")
    PRINTER_PROFILE = Column('PRINTER_PROFILE', String(10), default=None, doc="""Sourced from LIKP-PRINTER_PROFILE // Description of print profile""")
    MSR_ACTIVE = Column('MSR_ACTIVE', String(1), default=None, doc="""Sourced from LIKP-MSR_ACTIVE // Advanced Returns Management Active""")
    PRTNR = Column('PRTNR', String(10), default=None, doc="""Sourced from LIKP-PRTNR // Confirmation number""")
    STGE_LOC_CHANGE = Column('STGE_LOC_CHANGE', String(1), default=None, doc="""Sourced from LIKP-STGE_LOC_CHANGE // Temporary Change of Storage Locations in Delivery""")
    DLV_SPLIT_INITIA = Column('DLV_SPLIT_INITIA', String(1), default=None, doc="""Sourced from LIKP-DLV_SPLIT_INITIA // Delivery Split Initiator""")
    DLV_VERSION = Column('DLV_VERSION', String(4), default=None, doc="""Sourced from LIKP-DLV_VERSION // Delivery Version""")
    HANDOVERLOC = Column('HANDOVERLOC', String(10), default=None, doc="""Sourced from LIKP-HANDOVERLOC // Location for a physical handover of goods""")
    HANDOVERDATE = Column('HANDOVERDATE', String(8), default=None, doc="""Sourced from LIKP-HANDOVERDATE // Handover Date at the Handover Location""")
    HANDOVERTIME = Column('HANDOVERTIME', String(6), default=None, doc="""Sourced from LIKP-HANDOVERTIME // Handover time at the handover location""")
    HANDOVERTZONE = Column('HANDOVERTZONE', String(6), default=None, doc="""Sourced from LIKP-HANDOVERTZONE // Time Zone of Handover Location""")
    BORGR_GRP = Column('BORGR_GRP', String(35), default=None, doc="""Sourced from LIKP-BORGR_GRP // Inbound Dely Group: Multi-Level Goods Receipt Automotive""")
    YYRELEASE_DT = Column('YYRELEASE_DT', String(8), default=None, doc="""Sourced from LIKP-YYRELEASE_DT // ASN Release Date""")
    YYRELEASE_TM = Column('YYRELEASE_TM', String(6), default=None, doc="""Sourced from LIKP-YYRELEASE_TM // ASN Release Time""")
    YYNUM_ORDERS = Column('YYNUM_ORDERS', String(2), default=None, doc="""Sourced from LIKP-YYNUM_ORDERS // Number of delivery notes in this BOL (856)""")
    YYRACKWEIGHT = Column('YYRACKWEIGHT', String(15), default=None, doc="""Sourced from LIKP-YYRACKWEIGHT // Rack weight (856)""")
    YYRACUOM = Column('YYRACUOM', String(3), default=None, doc="""Sourced from LIKP-YYRACUOM // Rack unit of measure""")
    YYDUNWEIGHT = Column('YYDUNWEIGHT', String(15), default=None, doc="""Sourced from LIKP-YYDUNWEIGHT // Dunnage Weight (For 856).""")
    YYDUNUOM = Column('YYDUNUOM', String(3), default=None, doc="""Sourced from LIKP-YYDUNUOM // Dunnage Unit of Measure""")

    sd_doc_id = synonym('VBELN')
    doc_create_user_id = synonym('ERNAM')
    doc_create_tm = synonym('ERZET')
    doc_create_dt = synonym('ERDAT')
    sales_district_id = synonym('BZIRK')
    shipping_receiving_point_cd = synonym('VSTEL')
    sales_org_cd = synonym('VKORG')
    delivery_type_cd = synonym('LFART')
    goods_issue_dt = synonym('WADAT')
    loading_dt = synonym('LDDAT')
    delivery_dt = synonym('LFDAT')
    picking_dt = synonym('KODAT')
    unloading_point = synonym('ABLAD')
    incoterms_cd = synonym('INCO1')
    incoterms_desc = synonym('INCO2')
    export_cd = synonym('EXPKZ')
    route_id = synonym('ROUTE')
    sd_doc_billing_block_cd = synonym('FAKSK')
    hdr_delivery_blk_cd = synonym('LIFSK')
    sd_doc_ctgy_cd = synonym('VBTYP')
    delivery_priority_cd = synonym('LPRIO')
    shipping_condition_cd = synonym('VSBED')
    customer_id = synonym('KUNNR')
    sold_to_customer_id = synonym('KUNAG')
    customer_group_id = synonym('KDGRP')
    net_wt = synonym('NTGEW')
    weight_uom_cd = synonym('GEWEI')
    vol = synonym('VOLUM')
    volume_uom_cd = synonym('VOLEH')
    delivery_tm = synonym('LFUHR')
    loading_point_cd = synonym('LSTEL')
    billing_dt = synonym('FKDAT')
    sd_doc_currency_cd = synonym('WAERK')
    sales_office_id = synonym('VKBUR')
    update_user_id = synonym('AENAM')
    update_dt = synonym('AEDAT')
    warehouse_nbr = synonym('LGNUM')
    intercompany_sales_org_cd = synonym('VKOIV')
    interco_distr_chan_cd = synonym('VTWIV')
    intercompany_billing_div_cd = synonym('SPAIV')
    intercompany_billing_type_cd = synonym('FKAIV')
    intercompany_billing_dt = synonym('FKDIV')
    intercompany_customer_id = synonym('KUNIV')
    credit_control_area_cd = synonym('KKBER')
    sap_bill_of_lading_id = synonym('BOLNR')
    means_of_transportation_type_cd = synonym('TRATY')
    means_of_transportation_id = synonym('TRAID')
    credit_mgmt_release_dt = synonym('CMFRE')
    actl_goods_issue_dt = synonym('WADAT_IST')
    ship_blocking_reason_cd = synonym('TRSPG')
    correction_delivery_ind = synonym('KLIEF')
    shipping_pricing_procedure_cd = synonym('KALSP')
    doc_currency_net_value_qty = synonym('NETWR')
    route_schd_id = synonym('AULWE')
    picking_tm = synonym('KOUHR')
    loading_tm = synonym('LDUHR')
    goods_issue_tm = synonym('WAUHR')
    distribution_status_cd = synonym('VLSTK')
    means_of_transportation = synonym('TRMTYP')
    special_processing_cd = synonym('SDABW')
    delivrey_version_cd = synonym('DLV_VERSION')


################################################################################




################################################################################

class DeliveryItem(SAP_Base):
    """\
    Table sourced from: LIPS
    Description: SD document: Delivery: Item data
    """

    __tablename__ = "LIPS"

    VBELN = Column('VBELN', String(10), primary_key = True, doc="""Sourced from LIPS-VBELN // Delivery""")
    POSNR = Column('POSNR', String(6), primary_key = True, doc="""Sourced from LIPS-POSNR // Delivery Item""")
    PSTYV = Column('PSTYV', String(4), default=None, doc="""Sourced from LIPS-PSTYV // Delivery item category""")
    ERNAM = Column('ERNAM', String(12), default=None, doc="""Sourced from LIPS-ERNAM // Name of Person who Created the Object""")
    ERZET = Column('ERZET', Time, default=None, doc="""Sourced from LIPS-ERZET // Entry time""")
    ERDAT = Column('ERDAT', Date, default=None, doc="""Sourced from LIPS-ERDAT // Date on Which Record Was Created""")
    MATNR = Column('MATNR', String(18), default=None, doc="""Sourced from LIPS-MATNR // Material Number""")
    MATWA = Column('MATWA', String(18), default=None, doc="""Sourced from LIPS-MATWA // Material entered""")
    MATKL = Column('MATKL', String(9), default=None, doc="""Sourced from LIPS-MATKL // Material Group""")
    WERKS = Column('WERKS', String(4), default=None, doc="""Sourced from LIPS-WERKS // Plant""")
    LGORT = Column('LGORT', String(4), default=None, doc="""Sourced from LIPS-LGORT // Storage Location""")
    CHARG = Column('CHARG', String(10), default=None, doc="""Sourced from LIPS-CHARG // Batch Number""")
    LICHN = Column('LICHN', String(15), default=None, doc="""Sourced from LIPS-LICHN // Vendor Batch Number""")
    KDMAT = Column('KDMAT', String(35), default=None, doc="""Sourced from LIPS-KDMAT // Material belonging to the customer""")
    PRODH = Column('PRODH', String(18), default=None, doc="""Sourced from LIPS-PRODH // Product hierarchy""")
    LFIMG = Column('LFIMG', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-LFIMG // Actual quantity delivered (in sales units)""")
    MEINS = Column('MEINS', String(3), default=None, doc="""Sourced from LIPS-MEINS // Base Unit of Measure""")
    VRKME = Column('VRKME', String(3), default=None, doc="""Sourced from LIPS-VRKME // Sales unit""")
    UMVKZ = Column('UMVKZ', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-UMVKZ // Numerator (factor) for conversion of sales quantity into SKU""")
    UMVKN = Column('UMVKN', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-UMVKN // Denominator (Divisor) for Conversion of Sales Qty into SKU""")
    NTGEW = Column('NTGEW', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-NTGEW // Net weight""")
    BRGEW = Column('BRGEW', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-BRGEW // Gross weight""")
    GEWEI = Column('GEWEI', String(3), default=None, doc="""Sourced from LIPS-GEWEI // Weight Unit""")
    VOLUM = Column('VOLUM', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-VOLUM // Volume""")
    VOLEH = Column('VOLEH', String(3), default=None, doc="""Sourced from LIPS-VOLEH // Volume unit""")
    KZTLF = Column('KZTLF', String(1), default=None, doc="""Sourced from LIPS-KZTLF // Partial delivery at item level""")
    UEBTK = Column('UEBTK', Boolean, default=None, doc="""Sourced from LIPS-UEBTK // Indicator: Unlimited Overdelivery Allowed""")
    UEBTO = Column('UEBTO', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-UEBTO // Overdelivery Tolerance Limit""")
    UNTTO = Column('UNTTO', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-UNTTO // Underdelivery Tolerance Limit""")
    CHSPL = Column('CHSPL', Boolean, default=None, doc="""Sourced from LIPS-CHSPL // Batch split allowed""")
    FAKSP = Column('FAKSP', String(2), default=None, doc="""Sourced from LIPS-FAKSP // Block""")
    MBDAT = Column('MBDAT', Date, default=None, doc="""Sourced from LIPS-MBDAT // Material Staging/Availability Date""")
    LGMNG = Column('LGMNG', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-LGMNG // Actual quantity delivered in stockkeeping units""")
    ARKTX = Column('ARKTX', String(40), default=None, doc="""Sourced from LIPS-ARKTX // Short text for sales order item""")
    LGPBE = Column('LGPBE', String(10), default=None, doc="""Sourced from LIPS-LGPBE // Storage Bin""")
    VBELV = Column('VBELV', String(10), default=None, doc="""Sourced from LIPS-VBELV // Originating document""")
    POSNV = Column('POSNV', String(6), default=None, doc="""Sourced from LIPS-POSNV // Originating item""")
    VBTYV = Column('VBTYV', String(1), default=None, doc="""Sourced from LIPS-VBTYV // SD document category""")
    VGSYS = Column('VGSYS', String(10), default=None, doc="""Sourced from LIPS-VGSYS // Logical System in the Preceding Document""")
    VGBEL = Column('VGBEL', String(10), default=None, doc="""Sourced from LIPS-VGBEL // Document number of the reference document""")
    VGPOS = Column('VGPOS', String(6), default=None, doc="""Sourced from LIPS-VGPOS // Item number of the reference item""")
    UPFLU = Column('UPFLU', String(1), default=None, doc="""Sourced from LIPS-UPFLU // Update indicator for delivery document flow""")
    UEPOS = Column('UEPOS', String(6), default=None, doc="""Sourced from LIPS-UEPOS // Higher-level item in bill of material structures""")
    FKREL = Column('FKREL', String(1), default=None, doc="""Sourced from LIPS-FKREL // Relevant for Billing""")
    LADGR = Column('LADGR', String(4), default=None, doc="""Sourced from LIPS-LADGR // Loading Group""")
    TRAGR = Column('TRAGR', String(4), default=None, doc="""Sourced from LIPS-TRAGR // Transportation Group""")
    KOMKZ = Column('KOMKZ', String(1), default=None, doc="""Sourced from LIPS-KOMKZ // Indicator for picking control""")
    LGNUM = Column('LGNUM', String(3), default=None, doc="""Sourced from LIPS-LGNUM // Warehouse Number / Warehouse Complex""")
    LISPL = Column('LISPL', String(1), default=None, doc="""Sourced from LIPS-LISPL // Split to warehouse number required""")
    LGTYP = Column('LGTYP', String(3), default=None, doc="""Sourced from LIPS-LGTYP // Storage Type""")
    LGPLA = Column('LGPLA', String(10), default=None, doc="""Sourced from LIPS-LGPLA // Storage Bin""")
    BWTEX = Column('BWTEX', Boolean, default=None, doc="""Sourced from LIPS-BWTEX // Indicator: Separate valuation""")
    BWART = Column('BWART', String(3), default=None, doc="""Sourced from LIPS-BWART // Movement Type (Inventory Management)""")
    BWLVS = Column('BWLVS', String(3), default=None, doc="""Sourced from LIPS-BWLVS // Movement Type for Warehouse Management""")
    KZDLG = Column('KZDLG', Boolean, default=None, doc="""Sourced from LIPS-KZDLG // Indicator: dynamic storage bin in warehouse management""")
    BDART = Column('BDART', String(2), default=None, doc="""Sourced from LIPS-BDART // Requirement type""")
    PLART = Column('PLART', String(1), default=None, doc="""Sourced from LIPS-PLART // Planning type""")
    MTART = Column('MTART', String(4), default=None, doc="""Sourced from LIPS-MTART // Material Type""")
    XCHPF = Column('XCHPF', Boolean, default=None, doc="""Sourced from LIPS-XCHPF // Batch management requirement indicator""")
    XCHAR = Column('XCHAR', Boolean, default=None, doc="""Sourced from LIPS-XCHAR // Batch management indicator (internal)""")
    VGREF = Column('VGREF', Boolean, default=None, doc="""Sourced from LIPS-VGREF // Preceding document has resulted from reference""")
    POSAR = Column('POSAR', String(1), default=None, doc="""Sourced from LIPS-POSAR // Item type""")
    BWTAR = Column('BWTAR', String(10), default=None, doc="""Sourced from LIPS-BWTAR // Valuation Type""")
    SUMBD = Column('SUMBD', String(1), default=None, doc="""Sourced from LIPS-SUMBD // Summing up of requirements""")
    MTVFP = Column('MTVFP', String(2), default=None, doc="""Sourced from LIPS-MTVFP // Checking Group for Availability Check""")
    EANNR = Column('EANNR', String(13), default=None, doc="""Sourced from LIPS-EANNR // European Article Number (EAN) - obsolete!!!!!""")
    GSBER = Column('GSBER', String(4), default=None, doc="""Sourced from LIPS-GSBER // Business Area""")
    VKBUR = Column('VKBUR', String(4), default=None, doc="""Sourced from LIPS-VKBUR // Sales Office""")
    VKGRP = Column('VKGRP', String(3), default=None, doc="""Sourced from LIPS-VKGRP // Sales Group""")
    VTWEG = Column('VTWEG', String(2), default=None, doc="""Sourced from LIPS-VTWEG // Distribution Channel""")
    SPART = Column('SPART', String(2), default=None, doc="""Sourced from LIPS-SPART // Division""")
    GRKOR = Column('GRKOR', String(3), default=None, doc="""Sourced from LIPS-GRKOR // Delivery group (items are delivered together)""")
    FMENG = Column('FMENG', Boolean, default=None, doc="""Sourced from LIPS-FMENG // Quantity is Fixed""")
    ANTLF = Column('ANTLF', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-ANTLF // Maximum Number of Partial Deliveries Allowed Per Item""")
    VBEAF = Column('VBEAF', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-VBEAF // Fixed shipping processing time in days (= setup time)""")
    VBEAV = Column('VBEAV', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-VBEAV // Variable shipping processing time in days""")
    STAFO = Column('STAFO', String(6), default=None, doc="""Sourced from LIPS-STAFO // Update group for statistics update""")
    WAVWR = Column('WAVWR', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-WAVWR // Cost in document currency""")
    KZWI1 = Column('KZWI1', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-KZWI1 // Subtotal 1 from pricing procedure for condition""")
    KZWI2 = Column('KZWI2', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-KZWI2 // Subtotal 2 from pricing procedure for condition""")
    KZWI3 = Column('KZWI3', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-KZWI3 // Subtotal 3 from pricing procedure for condition""")
    KZWI4 = Column('KZWI4', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-KZWI4 // Subtotal 4 from pricing procedure for condition""")
    KZWI5 = Column('KZWI5', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-KZWI5 // Subtotal 5 from pricing procedure for condition""")
    KZWI6 = Column('KZWI6', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-KZWI6 // Subtotal 6 from pricing procedure for condition""")
    SOBKZ = Column('SOBKZ', String(1), default=None, doc="""Sourced from LIPS-SOBKZ // Special Stock Indicator""")
    AEDAT = Column('AEDAT', Date, default=None, doc="""Sourced from LIPS-AEDAT // Changed On""")
    EAN11 = Column('EAN11', String(18), default=None, doc="""Sourced from LIPS-EAN11 // International Article Number (EAN/UPC)""")
    KVGR1 = Column('KVGR1', String(3), default=None, doc="""Sourced from LIPS-KVGR1 // Customer group 1""")
    KVGR2 = Column('KVGR2', String(3), default=None, doc="""Sourced from LIPS-KVGR2 // Customer group 2""")
    KVGR3 = Column('KVGR3', String(3), default=None, doc="""Sourced from LIPS-KVGR3 // Customer group 3""")
    KVGR4 = Column('KVGR4', String(3), default=None, doc="""Sourced from LIPS-KVGR4 // Customer group 4""")
    KVGR5 = Column('KVGR5', String(3), default=None, doc="""Sourced from LIPS-KVGR5 // Customer group 5""")
    MVGR1 = Column('MVGR1', String(3), default=None, doc="""Sourced from LIPS-MVGR1 // Material group 1""")
    MVGR2 = Column('MVGR2', String(3), default=None, doc="""Sourced from LIPS-MVGR2 // Material group 2""")
    MVGR3 = Column('MVGR3', String(3), default=None, doc="""Sourced from LIPS-MVGR3 // Material group 3""")
    MVGR4 = Column('MVGR4', String(3), default=None, doc="""Sourced from LIPS-MVGR4 // Material group 4""")
    MVGR5 = Column('MVGR5', String(3), default=None, doc="""Sourced from LIPS-MVGR5 // Material group 5""")
    VPZUO = Column('VPZUO', String(1), default=None, doc="""Sourced from LIPS-VPZUO // Allocation Indicator""")
    VGTYP = Column('VGTYP', String(1), default=None, doc="""Sourced from LIPS-VGTYP // SD document category""")
    RFVGTYP = Column('RFVGTYP', String(1), default=None, doc="""Sourced from LIPS-RFVGTYP // Type of preceding document in central system""")
    KOSTL = Column('KOSTL', String(10), default=None, doc="""Sourced from LIPS-KOSTL // Cost Center""")
    KOKRS = Column('KOKRS', String(4), default=None, doc="""Sourced from LIPS-KOKRS // Controlling Area""")
    PAOBJNR = Column('PAOBJNR', String(10), default=None, doc="""Sourced from LIPS-PAOBJNR // Profitability Segment Number (CO-PA)""")
    PRCTR = Column('PRCTR', String(10), default=None, doc="""Sourced from LIPS-PRCTR // Profit Center""")
    PS_PSP_PNR = Column('PS_PSP_PNR', String(8), default=None, doc="""Sourced from LIPS-PS_PSP_PNR // Work Breakdown Structure Element (WBS Element)""")
    AUFNR = Column('AUFNR', String(12), default=None, doc="""Sourced from LIPS-AUFNR // Order Number""")
    POSNR_PP = Column('POSNR_PP', String(4), default=None, doc="""Sourced from LIPS-POSNR_PP // Order Item Number""")
    KDAUF = Column('KDAUF', String(10), default=None, doc="""Sourced from LIPS-KDAUF // Sales Order Number""")
    KDPOS = Column('KDPOS', String(6), default=None, doc="""Sourced from LIPS-KDPOS // Item Number in Sales Order""")
    VPMAT = Column('VPMAT', String(18), default=None, doc="""Sourced from LIPS-VPMAT // Planning material""")
    VPWRK = Column('VPWRK', String(4), default=None, doc="""Sourced from LIPS-VPWRK // Planning plant""")
    PRBME = Column('PRBME', String(3), default=None, doc="""Sourced from LIPS-PRBME // Base unit of measure for product group""")
    UMREF = Column('UMREF', String(16), default=None, doc="""Sourced from LIPS-UMREF // Conversion factor: quantities""")
    KNTTP = Column('KNTTP', String(1), default=None, doc="""Sourced from LIPS-KNTTP // Account Assignment Category""")
    KZVBR = Column('KZVBR', String(1), default=None, doc="""Sourced from LIPS-KZVBR // Consumption Posting""")
    FIPOS = Column('FIPOS', String(14), default=None, doc="""Sourced from LIPS-FIPOS // Commitment Item""")
    FISTL = Column('FISTL', String(16), default=None, doc="""Sourced from LIPS-FISTL // Funds Center""")
    GEBER = Column('GEBER', String(10), default=None, doc="""Sourced from LIPS-GEBER // Fund""")
    PCKPF = Column('PCKPF', String(1), default=None, doc="""Sourced from LIPS-PCKPF // Packing control""")
    BEDAR_LF = Column('BEDAR_LF', String(3), default=None, doc="""Sourced from LIPS-BEDAR_LF // Requirements class""")
    CMPNT = Column('CMPNT', Boolean, default=None, doc="""Sourced from LIPS-CMPNT // ID: Item with active credit function / relevant for credit""")
    KCMENG = Column('KCMENG', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-KCMENG // Cumulative batch quantity of all split items (in StckUnit)""")
    KCBRGEW = Column('KCBRGEW', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-KCBRGEW // Cumulative gross weight of all batch split items""")
    KCNTGEW = Column('KCNTGEW', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-KCNTGEW // Cumulative net weight of all batch split items""")
    KCVOLUM = Column('KCVOLUM', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-KCVOLUM // Cumulative volume of all batch split items""")
    UECHA = Column('UECHA', String(6), default=None, doc="""Sourced from LIPS-UECHA // Higher-Level Item of Batch Split Item""")
    CUOBJ = Column('CUOBJ', String(18), default=None, doc="""Sourced from LIPS-CUOBJ // Configuration""")
    CUOBJ_CH = Column('CUOBJ_CH', String(18), default=None, doc="""Sourced from LIPS-CUOBJ_CH // Internal object number of the batch classification""")
    ANZSN = Column('ANZSN', Integer, default=None, doc="""Sourced from LIPS-ANZSN // Number of serial numbers""")
    SERAIL = Column('SERAIL', String(4), default=None, doc="""Sourced from LIPS-SERAIL // Serial Number Profile""")
    KCGEWEI = Column('KCGEWEI', String(3), default=None, doc="""Sourced from LIPS-KCGEWEI // Weight Unit""")
    KCVOLEH = Column('KCVOLEH', String(3), default=None, doc="""Sourced from LIPS-KCVOLEH // Volume unit""")
    SERNR = Column('SERNR', String(8), default=None, doc="""Sourced from LIPS-SERNR // BOM explosion number""")
    ABRLI = Column('ABRLI', String(4), default=None, doc="""Sourced from LIPS-ABRLI // Internal delivery schedule number""")
    ABART = Column('ABART', String(1), default=None, doc="""Sourced from LIPS-ABART // Release type""")
    ABRVW = Column('ABRVW', String(3), default=None, doc="""Sourced from LIPS-ABRVW // Usage Indicator""")
    QPLOS = Column('QPLOS', String(12), default=None, doc="""Sourced from LIPS-QPLOS // Inspection Lot Number""")
    QTLOS = Column('QTLOS', String(6), default=None, doc="""Sourced from LIPS-QTLOS // Partial lot number""")
    NACHL = Column('NACHL', Boolean, default=None, doc="""Sourced from LIPS-NACHL // Customer has not posted goods receipt""")
    MAGRV = Column('MAGRV', String(4), default=None, doc="""Sourced from LIPS-MAGRV // Material Group: Packaging Materials""")
    OBJKO = Column('OBJKO', String(22), default=None, doc="""Sourced from LIPS-OBJKO // Object number at header level""")
    OBJPO = Column('OBJPO', String(22), default=None, doc="""Sourced from LIPS-OBJPO // Object number at item level""")
    AESKD = Column('AESKD', String(17), default=None, doc="""Sourced from LIPS-AESKD // Customer Engineering Change Status""")
    SHKZG = Column('SHKZG', Boolean, default=None, doc="""Sourced from LIPS-SHKZG // Returns Item""")
    PROSA = Column('PROSA', String(1), default=None, doc="""Sourced from LIPS-PROSA // ID for material determination""")
    UEPVW = Column('UEPVW', String(1), default=None, doc="""Sourced from LIPS-UEPVW // ID for higher-level item usage""")
    EMPST = Column('EMPST', String(25), default=None, doc="""Sourced from LIPS-EMPST // Receiving point""")
    ABTNR = Column('ABTNR', String(4), default=None, doc="""Sourced from LIPS-ABTNR // Department number""")
    KOQUI = Column('KOQUI', Boolean, default=None, doc="""Sourced from LIPS-KOQUI // Picking is subject to confirmation""")
    STADAT = Column('STADAT', Date, default=None, doc="""Sourced from LIPS-STADAT // Statistics date""")
    AKTNR = Column('AKTNR', String(10), default=None, doc="""Sourced from LIPS-AKTNR // Promotion""")
    KNUMH_CH = Column('KNUMH_CH', String(10), default=None, doc="""Sourced from LIPS-KNUMH_CH // Number of condition record from batch determination""")
    PREFE = Column('PREFE', String(1), default=None, doc="""Sourced from LIPS-PREFE // Preference indicator in export/import""")
    EXART = Column('EXART', String(2), default=None, doc="""Sourced from LIPS-EXART // Business Transaction Type for Foreign Trade""")
    CLINT = Column('CLINT', String(10), default=None, doc="""Sourced from LIPS-CLINT // Internal Class Number""")
    CHMVS = Column('CHMVS', String(3), default=None, doc="""Sourced from LIPS-CHMVS // Batches: Exit to quantity proposal""")
    ABELN = Column('ABELN', String(10), default=None, doc="""Sourced from LIPS-ABELN // Allocation Table Number""")
    ABELP = Column('ABELP', String(5), default=None, doc="""Sourced from LIPS-ABELP // Item number of allocation table""")
    LFIMG_FLO = Column('LFIMG_FLO', Float, default=None, doc="""Sourced from LIPS-LFIMG_FLO // Internal field/ Do not use     / LFIMG in float / MUM""")
    LGMNG_FLO = Column('LGMNG_FLO', Float, default=None, doc="""Sourced from LIPS-LGMNG_FLO // Internal field/ Do not use     / LGMNG in float / MUM""")
    KCMENG_FLO = Column('KCMENG_FLO', Float, default=None, doc="""Sourced from LIPS-KCMENG_FLO // Internal field/ Do not use     / KCMENG in float / MUM""")
    KZUMW = Column('KZUMW', Boolean, default=None, doc="""Sourced from LIPS-KZUMW // Environmentally Relevant""")
    KMPMG = Column('KMPMG', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-KMPMG // Component quantity""")
    AUREL = Column('AUREL', String(1), default=None, doc="""Sourced from LIPS-AUREL // Relevant to Allocation Table""")
    KPEIN = Column('KPEIN', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-KPEIN // Condition pricing unit""")
    KMEIN = Column('KMEIN', String(3), default=None, doc="""Sourced from LIPS-KMEIN // Condition unit""")
    NETPR = Column('NETPR', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-NETPR // Net price""")
    NETWR = Column('NETWR', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-NETWR // Net Value in Document Currency""")
    KOWRR = Column('KOWRR', String(1), default=None, doc="""Sourced from LIPS-KOWRR // Statistical values""")
    KZBEW = Column('KZBEW', String(1), default=None, doc="""Sourced from LIPS-KZBEW // Movement Indicator""")
    MFRGR = Column('MFRGR', String(8), default=None, doc="""Sourced from LIPS-MFRGR // Material freight group""")
    CHHPV = Column('CHHPV', Boolean, default=None, doc="""Sourced from LIPS-CHHPV // Pack accumulated batches / movement type item""")
    ABFOR = Column('ABFOR', String(2), default=None, doc="""Sourced from LIPS-ABFOR // Form of payment guarantee""")
    ABGES = Column('ABGES', String(16), default=None, doc="""Sourced from LIPS-ABGES // Guaranteed (factor between 0 and 1)""")
    MBUHR = Column('MBUHR', Time, default=None, doc="""Sourced from LIPS-MBUHR // Material Staging Time (Local, Relating to a Plant)""")
    WKTNR = Column('WKTNR', String(10), default=None, doc="""Sourced from LIPS-WKTNR // Value contract no.""")
    WKTPS = Column('WKTPS', String(6), default=None, doc="""Sourced from LIPS-WKTPS // Value contract item""")
    J_1BCFOP = Column('J_1BCFOP', String(10), default=None, doc="""Sourced from LIPS-J_1BCFOP // CFOP Code and Extension""")
    J_1BTAXLW1 = Column('J_1BTAXLW1', String(3), default=None, doc="""Sourced from LIPS-J_1BTAXLW1 // Tax law: ICMS""")
    J_1BTAXLW2 = Column('J_1BTAXLW2', String(3), default=None, doc="""Sourced from LIPS-J_1BTAXLW2 // Tax law: IPI""")
    J_1BTXSDC = Column('J_1BTXSDC', String(2), default=None, doc="""Sourced from LIPS-J_1BTXSDC // SD tax code""")
    SITUA = Column('SITUA', String(2), default=None, doc="""Sourced from LIPS-SITUA // Indicator for situation""")
    RSNUM = Column('RSNUM', String(10), default=None, doc="""Sourced from LIPS-RSNUM // Number of Reservation/Dependent Requirement""")
    RSPOS = Column('RSPOS', String(4), default=None, doc="""Sourced from LIPS-RSPOS // Item Number of Reservation/Dependent Requirement""")
    RSART = Column('RSART', String(1), default=None, doc="""Sourced from LIPS-RSART // Record type""")
    KANNR = Column('KANNR', String(35), default=None, doc="""Sourced from LIPS-KANNR // KANBAN/sequence number""")
    KZFME = Column('KZFME', String(1), default=None, doc="""Sourced from LIPS-KZFME // ID: Leading unit of measure for completing a transaction""")
    PROFL = Column('PROFL', String(3), default=None, doc="""Sourced from LIPS-PROFL // Dangerous Goods Indicator Profile""")
    KCMENGVME = Column('KCMENGVME', String(15), default=None, doc="""Sourced from LIPS-KCMENGVME // Cumulative batch quantity of all split items in sales units""")
    KCMENGVMEF = Column('KCMENGVMEF', Float, default=None, doc="""Sourced from LIPS-KCMENGVMEF // Cumulated batch split quantity in VRKME and float""")
    KZBWS = Column('KZBWS', String(1), default=None, doc="""Sourced from LIPS-KZBWS // Valuation of Special Stock""")
    PSPNR = Column('PSPNR', String(8), default=None, doc="""Sourced from LIPS-PSPNR // Project definition (internal)""")
    EPRIO = Column('EPRIO', String(4), default=None, doc="""Sourced from LIPS-EPRIO // Withdrawal sequence group for stocks""")
    RULES = Column('RULES', String(4), default=None, doc="""Sourced from LIPS-RULES // Stock determination rule""")
    KZBEF = Column('KZBEF', Boolean, default=None, doc="""Sourced from LIPS-KZBEF // Indicator Inventory Management active""")
    MPROF = Column('MPROF', String(4), default=None, doc="""Sourced from LIPS-MPROF // Manufacturer Part Profile""")
    EMATN = Column('EMATN', String(18), default=None, doc="""Sourced from LIPS-EMATN // Material Number Corresponding to Manufacturer Part Number""")
    LGBZO = Column('LGBZO', String(10), default=None, doc="""Sourced from LIPS-LGBZO // Staging Area for Warehouse Complex""")
    HANDLE = Column('HANDLE', Integer, default=None, doc="""Sourced from LIPS-HANDLE // Worldwide unique key for LIPS-VBELN & LIPS_POSNR""")
    VERURPOS = Column('VERURPOS', String(6), default=None, doc="""Sourced from LIPS-VERURPOS // Distribution delivery: Original item""")
    LIFEXPOS = Column('LIFEXPOS', String(6), default=None, doc="""Sourced from LIPS-LIFEXPOS // External item number""")
    NOATP = Column('NOATP', String(1), default=None, doc="""Sourced from LIPS-NOATP // Indicator: deactivate availability check""")
    NOPCK = Column('NOPCK', Boolean, default=None, doc="""Sourced from LIPS-NOPCK // Indicator: not relevant for picking""")
    RBLVS = Column('RBLVS', String(3), default=None, doc="""Sourced from LIPS-RBLVS // Reference movement type for WM from material movements""")
    BERID = Column('BERID', String(10), default=None, doc="""Sourced from LIPS-BERID // MRP Area""")
    BESTQ = Column('BESTQ', String(1), default=None, doc="""Sourced from LIPS-BESTQ // Stock Category in the Warehouse Management System""")
    UMBSQ = Column('UMBSQ', String(1), default=None, doc="""Sourced from LIPS-UMBSQ // Stock Category in the Warehouse Management System""")
    UMMAT = Column('UMMAT', String(18), default=None, doc="""Sourced from LIPS-UMMAT // Receiving/Issuing Material""")
    UMWRK = Column('UMWRK', String(4), default=None, doc="""Sourced from LIPS-UMWRK // Receiving/Issuing Plant""")
    UMLGO = Column('UMLGO', String(4), default=None, doc="""Sourced from LIPS-UMLGO // Receiving/Issuing Storage Location""")
    UMCHA = Column('UMCHA', String(10), default=None, doc="""Sourced from LIPS-UMCHA // Receiving/Issuing Batch""")
    UMBAR = Column('UMBAR', String(10), default=None, doc="""Sourced from LIPS-UMBAR // Valuation Type of Transfer Batch""")
    UMSOK = Column('UMSOK', String(1), default=None, doc="""Sourced from LIPS-UMSOK // Special Stock Indicator for Physical Stock Transfer""")
    SONUM = Column('SONUM', String(16), default=None, doc="""Sourced from LIPS-SONUM // Special Stock Number""")
    USONU = Column('USONU', String(16), default=None, doc="""Sourced from LIPS-USONU // Special Stock Number""")
    AKKUR = Column('AKKUR', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-AKKUR // Exchange rate for letter-of-credit procg in foreign trade""")
    AKMNG = Column('AKMNG', String(1), default=None, doc="""Sourced from LIPS-AKMNG // Current Qty Field for Arithmetic Operations in Doc.Process.""")
    VKGRU = Column('VKGRU', String(3), default=None, doc="""Sourced from LIPS-VKGRU // Repair Processing: Classification of Items""")
    SHKZG_UM = Column('SHKZG_UM', String(1), default=None, doc="""Sourced from LIPS-SHKZG_UM // Indicator: UNMAT in main posting""")
    INSMK = Column('INSMK', String(1), default=None, doc="""Sourced from LIPS-INSMK // Stock Type""")
    KZECH = Column('KZECH', String(1), default=None, doc="""Sourced from LIPS-KZECH // Determination of batch entry in the production/process order""")
    FLGWM = Column('FLGWM', String(1), default=None, doc="""Sourced from LIPS-FLGWM // Indicator: Copy dest. storage data from preceding document""")
    BERKZ = Column('BERKZ', String(1), default=None, doc="""Sourced from LIPS-BERKZ // Material Staging Indicator for Production Supply""")
    HUPOS = Column('HUPOS', String(1), default=None, doc="""Sourced from LIPS-HUPOS // Indicator: Delivery item is a HU item""")
    NOWAB = Column('NOWAB', String(1), default=None, doc="""Sourced from LIPS-NOWAB // Indicator: Item Not Relevant for Goods Movements""")
    KONTO = Column('KONTO', String(10), default=None, doc="""Sourced from LIPS-KONTO // G/L Account Number""")
    KZEAR = Column('KZEAR', Boolean, default=None, doc="""Sourced from LIPS-KZEAR // Final Issue for This Reservation""")
    HSDAT = Column('HSDAT', Date, default=None, doc="""Sourced from LIPS-HSDAT // Date of Manufacture""")
    VFDAT = Column('VFDAT', Date, default=None, doc="""Sourced from LIPS-VFDAT // Shelf Life Expiration or Best-Before Date""")
    LFGJA = Column('LFGJA', String(4), default=None, doc="""Sourced from LIPS-LFGJA // Fiscal Year of Current Period""")
    LFBNR = Column('LFBNR', String(10), default=None, doc="""Sourced from LIPS-LFBNR // Document No. of a Reference Document""")
    LFPOS = Column('LFPOS', String(4), default=None, doc="""Sourced from LIPS-LFPOS // Item of a Reference Document""")
    GRUND = Column('GRUND', String(4), default=None, doc="""Sourced from LIPS-GRUND // Reason for goods movment""")
    FOBWA = Column('FOBWA', String(3), default=None, doc="""Sourced from LIPS-FOBWA // Subsequent movement type""")
    DLVTP = Column('DLVTP', String(2), default=None, doc="""Sourced from LIPS-DLVTP // Delivery Category""")
    EXBWR = Column('EXBWR', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-EXBWR // Externally Entered Posting Amount in Local Currency""")
    BPMNG = Column('BPMNG', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-BPMNG // Quantity in Purchase Order Price Unit""")
    EXVKW = Column('EXVKW', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-EXVKW // Externally Entered Sales Value in Local Currency""")
    CMPRE_FLT = Column('CMPRE_FLT', Float, default=None, doc="""Sourced from LIPS-CMPRE_FLT // Item credit price""")
    KZPOD = Column('KZPOD', String(1), default=None, doc="""Sourced from LIPS-KZPOD // POD indicator (relevance, verification, confirmation)""")
    LFDEZ = Column('LFDEZ', String(1), default=None, doc="""Sourced from LIPS-LFDEZ // Not relevant for distribution for WMS""")
    UMREV = Column('UMREV', String(16), default=None, doc="""Sourced from LIPS-UMREV // Conversion Factor of Delivery Quantity VRKME for MEINS""")
    PODREL = Column('PODREL', String(1), default=None, doc="""Sourced from LIPS-PODREL // POD Control (Proof of Delivery)""")
    KZUML = Column('KZUML', Boolean, default=None, doc="""Sourced from LIPS-KZUML // Stock transfer/transfer posting""")
    FKBER = Column('FKBER', String(16), default=None, doc="""Sourced from LIPS-FKBER // Functional Area""")
    GRANT_NBR = Column('GRANT_NBR', String(20), default=None, doc="""Sourced from LIPS-GRANT_NBR // Grant""")
    KZWSO = Column('KZWSO', String(1), default=None, doc="""Sourced from LIPS-KZWSO // Units of measure usage""")
    GMCONTROL = Column('GMCONTROL', String(1), default=None, doc="""Sourced from LIPS-GMCONTROL // Goods Movement Control""")
    POSTING_CHANGE = Column('POSTING_CHANGE', String(1), default=None, doc="""Sourced from LIPS-POSTING_CHANGE // Goods Movement Control: HU""")
    UM_PS_PSP_PNR = Column('UM_PS_PSP_PNR', String(8), default=None, doc="""Sourced from LIPS-UM_PS_PSP_PNR // Receiving/Issuing (WBS Element)""")
    PRE_VL_ETENS = Column('PRE_VL_ETENS', String(4), default=None, doc="""Sourced from LIPS-PRE_VL_ETENS // Sequential Number of Vendor Confirmation""")
    SPE_GEN_ELIKZ = Column('SPE_GEN_ELIKZ', Boolean, default=None, doc="""Sourced from LIPS-SPE_GEN_ELIKZ // 'Delivery Completed' Indicator""")
    SPE_SCRAP_IND = Column('SPE_SCRAP_IND', String(1), default=None, doc="""Sourced from LIPS-SPE_SCRAP_IND // Scrap Indicator for EWM Processing""")
    SPE_AUTH_NUMBER = Column('SPE_AUTH_NUMBER', String(20), default=None, doc="""Sourced from LIPS-SPE_AUTH_NUMBER // Return Material Authorization Number""")
    SPE_FOLLOW_UP = Column('SPE_FOLLOW_UP', String(4), default=None, doc="""Sourced from LIPS-SPE_FOLLOW_UP // Default Follow-Up Activity Code""")
    SPE_EXP_DATE_EXT = Column('SPE_EXP_DATE_EXT', String(15), default=None, doc="""Sourced from LIPS-SPE_EXP_DATE_EXT // End date of validity period of returns delivery""")
    SPE_EXP_DATE_INT = Column('SPE_EXP_DATE_INT', String(15), default=None, doc="""Sourced from LIPS-SPE_EXP_DATE_INT // End date of internal validity period of returns delivery""")
    SPE_AUTH_COMPLET = Column('SPE_AUTH_COMPLET', String(1), default=None, doc="""Sourced from LIPS-SPE_AUTH_COMPLET // RMA completion indicator""")
    ORMNG = Column('ORMNG', Numeric(15,3,3), default=None, doc="""Sourced from LIPS-ORMNG // Original Quantity of Delivery Item""")
    SPE_ATP_TMSTMP = Column('SPE_ATP_TMSTMP', String(15), default=None, doc="""Sourced from LIPS-SPE_ATP_TMSTMP // ATP Time Stamp""")
    SPE_ORIG_SYS = Column('SPE_ORIG_SYS', String(1), default=None, doc="""Sourced from LIPS-SPE_ORIG_SYS // Original System Type""")
    SPE_LIEFFZ = Column('SPE_LIEFFZ', String(15), default=None, doc="""Sourced from LIPS-SPE_LIEFFZ // Cumulative Qty for SchedAgr - Vendor's Point of View""")
    SPE_IMWRK = Column('SPE_IMWRK', Boolean, default=None, doc="""Sourced from LIPS-SPE_IMWRK // Inbound Delivery item has Status 'In Plant'""")
    SPE_LIFEXPOS2 = Column('SPE_LIFEXPOS2', String(35), default=None, doc="""Sourced from LIPS-SPE_LIFEXPOS2 // External item identifier""")
    SPE_EXCEPT_CODE = Column('SPE_EXCEPT_CODE', String(4), default=None, doc="""Sourced from LIPS-SPE_EXCEPT_CODE // Exception Code Warehouse for Quantity Difference""")
    SPE_KEEP_QTY = Column('SPE_KEEP_QTY', String(13), default=None, doc="""Sourced from LIPS-SPE_KEEP_QTY // Retention Quantity for Scrap. Process in EWM""")
    SPE_ALTERNATE = Column('SPE_ALTERNATE', String(40), default=None, doc="""Sourced from LIPS-SPE_ALTERNATE // Alternate Product Number""")
    SPE_MAT_SUBST = Column('SPE_MAT_SUBST', String(1), default=None, doc="""Sourced from LIPS-SPE_MAT_SUBST // Reason for material substitution""")
    SPE_APO_QNTYFAC = Column('SPE_APO_QNTYFAC', String(5), default=None, doc="""Sourced from LIPS-SPE_APO_QNTYFAC // Numerator of Quotient for Unit of Measure Conversion""")
    SPE_APO_QNTYDIV = Column('SPE_APO_QNTYDIV', String(5), default=None, doc="""Sourced from LIPS-SPE_APO_QNTYDIV // Denominator of Quotient for Unit of Measure Conversion""")
    SPE_HERKL = Column('SPE_HERKL', String(3), default=None, doc="""Sourced from LIPS-SPE_HERKL // Country of origin of the material""")
    SPE_BXP_DATE_EXT = Column('SPE_BXP_DATE_EXT', String(15), default=None, doc="""Sourced from LIPS-SPE_BXP_DATE_EXT // Begin date of validity period of returns delivery""")
    SPE_VERSION = Column('SPE_VERSION', String(4), default=None, doc="""Sourced from LIPS-SPE_VERSION // Delivery Version at Confirmation""")
    SPE_COMPL_MVT = Column('SPE_COMPL_MVT', Boolean, default=None, doc="""Sourced from LIPS-SPE_COMPL_MVT // Completion of Goods Movements after Difference Postings""")
    J_1BTAXLW4 = Column('J_1BTAXLW4', String(3), default=None, doc="""Sourced from LIPS-J_1BTAXLW4 // COFINS Tax Law""")
    J_1BTAXLW5 = Column('J_1BTAXLW5', String(3), default=None, doc="""Sourced from LIPS-J_1BTAXLW5 // PIS Tax Law""")
    J_1BTAXLW3 = Column('J_1BTAXLW3', String(3), default=None, doc="""Sourced from LIPS-J_1BTAXLW3 // ISS Tax Law""")
    BUDGET_PD = Column('BUDGET_PD', String(10), default=None, doc="""Sourced from LIPS-BUDGET_PD // FM: Budget Period""")
    KBNKZ = Column('KBNKZ', String(1), default=None, doc="""Sourced from LIPS-KBNKZ // Kanban Indicator""")
    FARR_RELTYPE = Column('FARR_RELTYPE', String(10), default=None, doc="""Sourced from LIPS-FARR_RELTYPE // Revenue Accounting Type""")
    SITKZ = Column('SITKZ', String(1), default=None, doc="""Sourced from LIPS-SITKZ // Specification for Issuing Valuated Stock in Transit""")
    SGT_RCAT = Column('SGT_RCAT', String(16), default=None, doc="""Sourced from LIPS-SGT_RCAT // Requirement Segment""")
    SGT_SCAT = Column('SGT_SCAT', String(16), default=None, doc="""Sourced from LIPS-SGT_SCAT // Stock Segment""")
    CONS_ORDER = Column('CONS_ORDER', String(1), default=None, doc="""Sourced from LIPS-CONS_ORDER // Purchase Order for Consignment""")
    YYSHIPMENT_DATE = Column('YYSHIPMENT_DATE', Date, default=None, doc="""Sourced from LIPS-YYSHIPMENT_DATE // Shipment date""")
    YYARRIVE_DATE = Column('YYARRIVE_DATE', Date, default=None, doc="""Sourced from LIPS-YYARRIVE_DATE // Arrival Date""")
    YYARRIVE_TIME = Column('YYARRIVE_TIME', Time, default=None, doc="""Sourced from LIPS-YYARRIVE_TIME // Arrival time""")
    YPOST_DATE = Column('YPOST_DATE', String(8), default=None, doc="""Sourced from LIPS-YPOST_DATE // Goods Issue Date""")
    YYLAND1 = Column('YYLAND1', String(3), default=None, doc="""Sourced from LIPS-YYLAND1 // Country Key""")
    YYARRIVE_DT = Column('YYARRIVE_DT', String(8), default=None, doc="""Sourced from LIPS-YYARRIVE_DT // Arrival date for VBAP line items""")
    YYARRIVE_TM = Column('YYARRIVE_TM', String(6), default=None, doc="""Sourced from LIPS-YYARRIVE_TM // Arrival time for VBAP line items""")
    YYSHIPMENT_DT = Column('YYSHIPMENT_DT', String(8), default=None, doc="""Sourced from LIPS-YYSHIPMENT_DT // Shipment date for VBAP line items""")
    YYCOSTCTR = Column('YYCOSTCTR', String(10), default=None, doc="""Sourced from LIPS-YYCOSTCTR // Cost Center""")

    sd_doc_id = synonym('VBELN')
    sd_doc_item_id = synonym('POSNR')
    sd_item_ctgy_cd = synonym('PSTYV')
    doc_create_user_id = synonym('ERNAM')
    doc_create_tm = synonym('ERZET')
    doc_create_dt = synonym('ERDAT')
    material_id = synonym('MATNR')
    entered_material_id = synonym('MATWA')
    material_group_cd = synonym('MATKL')
    vendor_batch_id = synonym('LICHN')
    sls_uom_delivered_qty = synonym('LFIMG')
    uom_cd = synonym('MEINS')
    sls_uom_cd = synonym('VRKME')
    sls_uom_conversion_num = synonym('UMVKZ')
    sls_uom_conversion_denom = synonym('UMVKN')
    net_wt = synonym('NTGEW')
    gross_wt = synonym('BRGEW')
    weight_uom_cd = synonym('GEWEI')
    vol = synonym('VOLUM')
    volume_uom_cd = synonym('VOLEH')
    item_partial_delivery_cd = synonym('KZTLF')
    batch_split_allowed_ind = synonym('CHSPL')
    block_cd = synonym('FAKSP')
    material_availability_dt = synonym('MBDAT')
    sku_uom_delivery_qty = synonym('LGMNG')
    sd_item_descr = synonym('ARKTX')
    storage_bin_id = synonym('LGPBE')
    originating_doc_id = synonym('VBELV')
    originating_item_id = synonym('POSNV')
    reference_doc_id = synonym('VGBEL')
    reference_item_id = synonym('VGPOS')
    flow_table_update_ind = synonym('UPFLU')
    billing_relevant_cd = synonym('FKREL')
    loading_grp_id = synonym('LADGR')
    warehouse_nbr = synonym('LGNUM')
    storage_type_id = synonym('LGTYP')
    separate_valuation_ind = synonym('BWTEX')
    im_matl_mvmnt_type_cd = synonym('BWART')
    wm_matl_mvmnt_type_cd = synonym('BWLVS')
    reqt_type_cd = synonym('BDART')
    planning_type_cd = synonym('PLART')
    material_type_id = synonym('MTART')
    batch_mgmt_required_ind = synonym('XCHPF')
    internal_batch_mgmt_ind = synonym('XCHAR')
    item_type_cd = synonym('POSAR')
    availability_checking_group_id = synonym('MTVFP')
    sales_office_id = synonym('VKBUR')
    sales_group_id = synonym('VKGRP')
    distr_chan_cd = synonym('VTWEG')
    div_cd = synonym('SPART')
    delivery_group_cd = synonym('GRKOR')
    qty_fixed_ind = synonym('FMENG')
    max_nbr_partial_deliveries = synonym('ANTLF')
    special_stock_cd = synonym('SOBKZ')
    update_dt = synonym('AEDAT')
    freight_policy_cd = synonym('KVGR2')
    allocation_cd = synonym('VPZUO')
    preceding_sd_doc_ctgy_cd = synonym('RFVGTYP')
    cost_center_id = synonym('KOSTL')
    order_id = synonym('AUFNR')
    sales_order_id = synonym('KDAUF')
    sales_order_item_id = synonym('KDPOS')
    prod_grp_base_uom_cd = synonym('PRBME')
    receiving_point_cd = synonym('EMPST')
    net_price_qty = synonym('NETPR')
    doc_currency_net_value_qty = synonym('NETWR')
    movement_cd = synonym('KZBEW')
    material_staging_tm = synonym('MBUHR')
    special_stock_valuation_Cd = synonym('KZBWS')
    mfg_part_nbr_matl_id = synonym('EMATN')
    mrp_area_id = synonym('BERID')
    wm_stk_ctgy_cd = synonym('BESTQ')
    stock_type_cd = synonym('INSMK')
    mfg_dt = synonym('HSDAT')
    ref_doc_id = synonym('LFBNR')
    ref_doc_item_id = synonym('LFPOS')
    delivery_ctgy_cd = synonym('DLVTP')
    prch_ord_price_unit_qty = synonym('BPMNG')
    original_inbound_delivery_qty = synonym('ORMNG')


################################################################################




################################################################################

class MaterialDesc(SAP_Base):
    """\
    Table sourced from: MAKT
    Description: Material Descriptions
    """

    __tablename__ = "MAKT"

    MATNR = Column('MATNR', String(18), primary_key = True, doc="""Sourced from MAKT-MATNR // Material Number""")
    SPRAS = Column('SPRAS', String(1), primary_key = True, doc="""Sourced from MAKT-SPRAS // Language Key""")
    MAKTX = Column('MAKTX', String(40), default=None, doc="""Sourced from MAKT-MAKTX // Material Description (Short Text)""")
    MAKTG = Column('MAKTG', String(40), default=None, doc="""Sourced from MAKT-MAKTG // Material description in upper case for matchcodes""")

    material_id = synonym('MATNR')
    language_cd = synonym('SPRAS')
    material_desc = synonym('MAKTX')
    material_desc_uppercase = synonym('MAKTG')


################################################################################




################################################################################

class Material(SAP_Base):
    """\
    Table sourced from: MARA
    Description: General Material Data
    """

    __tablename__ = "MARA"

    MATNR = Column('MATNR', String(18), primary_key = True, doc="""Sourced from MARA-MATNR // Material Number""")
    ERSDA = Column('ERSDA', Date, default=None, doc="""Sourced from MARA-ERSDA // Created On""")
    ERNAM = Column('ERNAM', String(12), default=None, doc="""Sourced from MARA-ERNAM // Name of Person who Created the Object""")
    LAEDA = Column('LAEDA', Date, default=None, doc="""Sourced from MARA-LAEDA // Date of Last Change""")
    AENAM = Column('AENAM', String(12), default=None, doc="""Sourced from MARA-AENAM // Name of Person Who Changed Object""")
    VPSTA = Column('VPSTA', String(15), default=None, doc="""Sourced from MARA-VPSTA // Maintenance status of complete material""")
    PSTAT = Column('PSTAT', String(15), default=None, doc="""Sourced from MARA-PSTAT // Maintenance status""")
    LVORM = Column('LVORM', Boolean, default=None, doc="""Sourced from MARA-LVORM // Flag Material for Deletion at Client Level""")
    MTART = Column('MTART', String(4), default=None, doc="""Sourced from MARA-MTART // Material Type""")
    MBRSH = Column('MBRSH', String(1), default=None, doc="""Sourced from MARA-MBRSH // Industry sector""")
    MATKL = Column('MATKL', String(9), default=None, doc="""Sourced from MARA-MATKL // Material Group""")
    BISMT = Column('BISMT', String(18), default=None, doc="""Sourced from MARA-BISMT // Old material number""")
    MEINS = Column('MEINS', String(3), default=None, doc="""Sourced from MARA-MEINS // Base Unit of Measure""")
    BSTME = Column('BSTME', String(3), default=None, doc="""Sourced from MARA-BSTME // Purchase Order Unit of Measure""")
    ZEINR = Column('ZEINR', String(22), default=None, doc="""Sourced from MARA-ZEINR // Document number (without document management system)""")
    ZEIAR = Column('ZEIAR', String(3), default=None, doc="""Sourced from MARA-ZEIAR // Document type (without Document Management system)""")
    ZEIVR = Column('ZEIVR', String(2), default=None, doc="""Sourced from MARA-ZEIVR // Document version (without Document Management system)""")
    ZEIFO = Column('ZEIFO', String(4), default=None, doc="""Sourced from MARA-ZEIFO // Page format of document (without Document Management system)""")
    AESZN = Column('AESZN', String(6), default=None, doc="""Sourced from MARA-AESZN // Document change number (without document management system)""")
    BLATT = Column('BLATT', String(3), default=None, doc="""Sourced from MARA-BLATT // Page number of document (without Document Management system)""")
    BLANZ = Column('BLANZ', String(3), default=None, doc="""Sourced from MARA-BLANZ // Number of sheets (without Document Management system)""")
    FERTH = Column('FERTH', String(18), default=None, doc="""Sourced from MARA-FERTH // Production/inspection memo""")
    FORMT = Column('FORMT', String(4), default=None, doc="""Sourced from MARA-FORMT // Page Format of Production Memo""")
    GROES = Column('GROES', String(32), default=None, doc="""Sourced from MARA-GROES // Size/dimensions""")
    WRKST = Column('WRKST', String(48), default=None, doc="""Sourced from MARA-WRKST // Basic Material""")
    NORMT = Column('NORMT', String(18), default=None, doc="""Sourced from MARA-NORMT // Industry Standard Description (such as ANSI or ISO)""")
    LABOR = Column('LABOR', String(3), default=None, doc="""Sourced from MARA-LABOR // Laboratory/design office""")
    EKWSL = Column('EKWSL', String(4), default=None, doc="""Sourced from MARA-EKWSL // Purchasing Value Key""")
    BRGEW = Column('BRGEW', Numeric(15,3,3), default=None, doc="""Sourced from MARA-BRGEW // Gross Weight""")
    NTGEW = Column('NTGEW', Numeric(15,3,3), default=None, doc="""Sourced from MARA-NTGEW // Net Weight""")
    GEWEI = Column('GEWEI', String(3), default=None, doc="""Sourced from MARA-GEWEI // Weight Unit""")
    VOLUM = Column('VOLUM', Numeric(15,3,3), default=None, doc="""Sourced from MARA-VOLUM // Volume""")
    VOLEH = Column('VOLEH', String(3), default=None, doc="""Sourced from MARA-VOLEH // Volume unit""")
    BEHVO = Column('BEHVO', String(2), default=None, doc="""Sourced from MARA-BEHVO // Container requirements""")
    RAUBE = Column('RAUBE', String(2), default=None, doc="""Sourced from MARA-RAUBE // Storage conditions""")
    TEMPB = Column('TEMPB', String(2), default=None, doc="""Sourced from MARA-TEMPB // Temperature conditions indicator""")
    DISST = Column('DISST', String(3), default=None, doc="""Sourced from MARA-DISST // Low-Level Code""")
    TRAGR = Column('TRAGR', String(4), default=None, doc="""Sourced from MARA-TRAGR // Transportation Group""")
    STOFF = Column('STOFF', String(18), default=None, doc="""Sourced from MARA-STOFF // Hazardous material number""")
    SPART = Column('SPART', String(2), default=None, doc="""Sourced from MARA-SPART // Division""")
    KUNNR = Column('KUNNR', String(10), default=None, doc="""Sourced from MARA-KUNNR // Competitor""")
    EANNR = Column('EANNR', String(13), default=None, doc="""Sourced from MARA-EANNR // European Article Number (EAN) - obsolete!!!!!""")
    WESCH = Column('WESCH', Numeric(15,3,3), default=None, doc="""Sourced from MARA-WESCH // Quantity: Number of GR/GI slips to be printed""")
    BWVOR = Column('BWVOR', String(1), default=None, doc="""Sourced from MARA-BWVOR // Procurement rule""")
    BWSCL = Column('BWSCL', String(1), default=None, doc="""Sourced from MARA-BWSCL // Source of Supply""")
    SAISO = Column('SAISO', String(4), default=None, doc="""Sourced from MARA-SAISO // Season Category""")
    ETIAR = Column('ETIAR', String(2), default=None, doc="""Sourced from MARA-ETIAR // Label type""")
    ETIFO = Column('ETIFO', String(2), default=None, doc="""Sourced from MARA-ETIFO // Label form""")
    ENTAR = Column('ENTAR', String(1), default=None, doc="""Sourced from MARA-ENTAR // Deactivated""")
    EAN11 = Column('EAN11', String(18), default=None, doc="""Sourced from MARA-EAN11 // International Article Number (EAN/UPC)""")
    NUMTP = Column('NUMTP', String(2), default=None, doc="""Sourced from MARA-NUMTP // Category of International Article Number (EAN)""")
    LAENG = Column('LAENG', Numeric(15,3,3), default=None, doc="""Sourced from MARA-LAENG // Length""")
    BREIT = Column('BREIT', Numeric(15,3,3), default=None, doc="""Sourced from MARA-BREIT // Width""")
    HOEHE = Column('HOEHE', Numeric(15,3,3), default=None, doc="""Sourced from MARA-HOEHE // Height""")
    MEABM = Column('MEABM', String(3), default=None, doc="""Sourced from MARA-MEABM // Unit of Dimension for Length/Width/Height""")
    PRDHA = Column('PRDHA', String(18), default=None, doc="""Sourced from MARA-PRDHA // Product hierarchy""")
    AEKLK = Column('AEKLK', Boolean, default=None, doc="""Sourced from MARA-AEKLK // Stock Transfer Net Change Costing""")
    CADKZ = Column('CADKZ', Boolean, default=None, doc="""Sourced from MARA-CADKZ // CAD Indicator""")
    QMPUR = Column('QMPUR', Boolean, default=None, doc="""Sourced from MARA-QMPUR // QM in Procurement is Active""")
    ERGEW = Column('ERGEW', Numeric(15,3,3), default=None, doc="""Sourced from MARA-ERGEW // Allowed packaging weight""")
    ERGEI = Column('ERGEI', String(3), default=None, doc="""Sourced from MARA-ERGEI // Unit of weight (allowed packaging weight)""")
    ERVOL = Column('ERVOL', Numeric(15,3,3), default=None, doc="""Sourced from MARA-ERVOL // Allowed packaging volume""")
    ERVOE = Column('ERVOE', String(3), default=None, doc="""Sourced from MARA-ERVOE // Volume unit (allowed packaging volume)""")
    GEWTO = Column('GEWTO', Numeric(15,3,3), default=None, doc="""Sourced from MARA-GEWTO // Excess Weight Tolerance for Handling unit""")
    VOLTO = Column('VOLTO', Numeric(15,3,3), default=None, doc="""Sourced from MARA-VOLTO // Excess Volume Tolerance of the Handling Unit""")
    VABME = Column('VABME', String(1), default=None, doc="""Sourced from MARA-VABME // Variable Purchase Order Unit Active""")
    KZREV = Column('KZREV', Boolean, default=None, doc="""Sourced from MARA-KZREV // Revision Level Has Been Assigned to the Material""")
    KZKFG = Column('KZKFG', Boolean, default=None, doc="""Sourced from MARA-KZKFG // Configurable Material""")
    XCHPF = Column('XCHPF', Boolean, default=None, doc="""Sourced from MARA-XCHPF // Batch management requirement indicator""")
    VHART = Column('VHART', String(4), default=None, doc="""Sourced from MARA-VHART // Packaging Material Type""")
    FUELG = Column('FUELG', Numeric(15,3,3), default=None, doc="""Sourced from MARA-FUELG // Maximum level (by volume)""")
    STFAK = Column('STFAK', Integer, default=None, doc="""Sourced from MARA-STFAK // Stacking factor""")
    MAGRV = Column('MAGRV', String(4), default=None, doc="""Sourced from MARA-MAGRV // Material Group: Packaging Materials""")
    BEGRU = Column('BEGRU', String(4), default=None, doc="""Sourced from MARA-BEGRU // Authorization Group""")
    DATAB = Column('DATAB', Date, default=None, doc="""Sourced from MARA-DATAB // Valid-From Date""")
    LIQDT = Column('LIQDT', Date, default=None, doc="""Sourced from MARA-LIQDT // Deletion date""")
    SAISJ = Column('SAISJ', String(4), default=None, doc="""Sourced from MARA-SAISJ // Season Year""")
    PLGTP = Column('PLGTP', String(2), default=None, doc="""Sourced from MARA-PLGTP // Price Band Category""")
    MLGUT = Column('MLGUT', String(1), default=None, doc="""Sourced from MARA-MLGUT // Empties Bill of Material""")
    EXTWG = Column('EXTWG', String(18), default=None, doc="""Sourced from MARA-EXTWG // External Material Group""")
    SATNR = Column('SATNR', String(18), default=None, doc="""Sourced from MARA-SATNR // Cross-Plant Configurable Material""")
    ATTYP = Column('ATTYP', String(2), default=None, doc="""Sourced from MARA-ATTYP // Material Category""")
    KZKUP = Column('KZKUP', String(1), default=None, doc="""Sourced from MARA-KZKUP // Indicator: Material can be co-product""")
    KZNFM = Column('KZNFM', Boolean, default=None, doc="""Sourced from MARA-KZNFM // Indicator: The material has a follow-up material""")
    PMATA = Column('PMATA', String(18), default=None, doc="""Sourced from MARA-PMATA // Pricing Reference Material""")
    MSTAE = Column('MSTAE', String(2), default=None, doc="""Sourced from MARA-MSTAE // Cross-Plant Material Status""")
    MSTAV = Column('MSTAV', String(2), default=None, doc="""Sourced from MARA-MSTAV // Cross-distribution-chain material status""")
    MSTDE = Column('MSTDE', Date, default=None, doc="""Sourced from MARA-MSTDE // Date from which the cross-plant material status is valid""")
    MSTDV = Column('MSTDV', Date, default=None, doc="""Sourced from MARA-MSTDV // Date from which the X-distr.-chain material status is valid""")
    TAKLV = Column('TAKLV', String(1), default=None, doc="""Sourced from MARA-TAKLV // Tax classification of the material""")
    RBNRM = Column('RBNRM', String(9), default=None, doc="""Sourced from MARA-RBNRM // Catalog Profile""")
    MHDRZ = Column('MHDRZ', Numeric(15,3,3), default=None, doc="""Sourced from MARA-MHDRZ // Minimum Remaining Shelf Life""")
    MHDHB = Column('MHDHB', Numeric(15,3,3), default=None, doc="""Sourced from MARA-MHDHB // Total shelf life""")
    MHDLP = Column('MHDLP', Numeric(15,3,3), default=None, doc="""Sourced from MARA-MHDLP // Storage percentage""")
    INHME = Column('INHME', String(3), default=None, doc="""Sourced from MARA-INHME // Content unit""")
    INHAL = Column('INHAL', Numeric(15,3,3), default=None, doc="""Sourced from MARA-INHAL // Net contents""")
    VPREH = Column('VPREH', Numeric(15,3,3), default=None, doc="""Sourced from MARA-VPREH // Comparison price unit""")
    ETIAG = Column('ETIAG', String(18), default=None, doc="""Sourced from MARA-ETIAG // IS-R Labeling: material grouping (deactivated in 4.0)""")
    INHBR = Column('INHBR', Numeric(15,3,3), default=None, doc="""Sourced from MARA-INHBR // Gross contents""")
    CMETH = Column('CMETH', String(1), default=None, doc="""Sourced from MARA-CMETH // Quantity Conversion Method""")
    CUOBF = Column('CUOBF', String(18), default=None, doc="""Sourced from MARA-CUOBF // Internal object number""")
    KZUMW = Column('KZUMW', Boolean, default=None, doc="""Sourced from MARA-KZUMW // Environmentally Relevant""")
    KOSCH = Column('KOSCH', String(18), default=None, doc="""Sourced from MARA-KOSCH // Product allocation determination procedure""")
    SPROF = Column('SPROF', String(1), default=None, doc="""Sourced from MARA-SPROF // Pricing profile for variants""")
    NRFHG = Column('NRFHG', String(1), default=None, doc="""Sourced from MARA-NRFHG // Material qualifies for discount in kind""")
    MFRPN = Column('MFRPN', String(40), default=None, doc="""Sourced from MARA-MFRPN // Manufacturer Part Number""")
    MFRNR = Column('MFRNR', String(10), default=None, doc="""Sourced from MARA-MFRNR // Number of a Manufacturer""")
    BMATN = Column('BMATN', String(18), default=None, doc="""Sourced from MARA-BMATN // Number of firm's own (internal) inventory-managed material""")
    MPROF = Column('MPROF', String(4), default=None, doc="""Sourced from MARA-MPROF // Manufacturer Part Profile""")
    KZWSM = Column('KZWSM', String(1), default=None, doc="""Sourced from MARA-KZWSM // Units of measure usage""")
    SAITY = Column('SAITY', String(2), default=None, doc="""Sourced from MARA-SAITY // Rollout in a Season""")
    PROFL = Column('PROFL', String(3), default=None, doc="""Sourced from MARA-PROFL // Dangerous Goods Indicator Profile""")
    IHIVI = Column('IHIVI', Boolean, default=None, doc="""Sourced from MARA-IHIVI // Indicator: Highly Viscous""")
    ILOOS = Column('ILOOS', Boolean, default=None, doc="""Sourced from MARA-ILOOS // Indicator: In Bulk/Liquid""")
    SERLV = Column('SERLV', String(1), default=None, doc="""Sourced from MARA-SERLV // Level of Explicitness for Serial Number""")
    KZGVH = Column('KZGVH', Boolean, default=None, doc="""Sourced from MARA-KZGVH // Packaging Material is Closed Packaging""")
    XGCHP = Column('XGCHP', Boolean, default=None, doc="""Sourced from MARA-XGCHP // Indicator: Approved batch record required""")
    KZEFF = Column('KZEFF', Boolean, default=None, doc="""Sourced from MARA-KZEFF // Assign effectivity parameter values/ override change numbers""")
    COMPL = Column('COMPL', String(2), default=None, doc="""Sourced from MARA-COMPL // Material completion level""")
    IPRKZ = Column('IPRKZ', String(1), default=None, doc="""Sourced from MARA-IPRKZ // Period Indicator for Shelf Life Expiration Date""")
    RDMHD = Column('RDMHD', String(1), default=None, doc="""Sourced from MARA-RDMHD // Rounding rule for calculation of SLED""")
    PRZUS = Column('PRZUS', Boolean, default=None, doc="""Sourced from MARA-PRZUS // Indicator: Product composition printed on packaging""")
    MTPOS_MARA = Column('MTPOS_MARA', String(4), default=None, doc="""Sourced from MARA-MTPOS_MARA // General item category group""")
    BFLME = Column('BFLME', String(1), default=None, doc="""Sourced from MARA-BFLME // Generic Material with Logistical Variants""")
    MATFI = Column('MATFI', Boolean, default=None, doc="""Sourced from MARA-MATFI // Material Is Locked""")
    CMREL = Column('CMREL', String(1), default=None, doc="""Sourced from MARA-CMREL // Relevant for Configuration Management""")
    BBTYP = Column('BBTYP', String(1), default=None, doc="""Sourced from MARA-BBTYP // Assortment List Type""")
    SLED_BBD = Column('SLED_BBD', String(1), default=None, doc="""Sourced from MARA-SLED_BBD // Expiration Date""")
    GTIN_VARIANT = Column('GTIN_VARIANT', String(2), default=None, doc="""Sourced from MARA-GTIN_VARIANT // Global Trade Item Number Variant""")
    GENNR = Column('GENNR', String(18), default=None, doc="""Sourced from MARA-GENNR // Material Number of the Generic Material in Prepack Materials""")
    RMATP = Column('RMATP', String(18), default=None, doc="""Sourced from MARA-RMATP // Reference material for materials packed in same way""")
    GDS_RELEVANT = Column('GDS_RELEVANT', Boolean, default=None, doc="""Sourced from MARA-GDS_RELEVANT // Indicator: Global Data Synchronization-Relevant""")
    WEORA = Column('WEORA', Boolean, default=None, doc="""Sourced from MARA-WEORA // Acceptance At Origin""")
    HUTYP_DFLT = Column('HUTYP_DFLT', String(4), default=None, doc="""Sourced from MARA-HUTYP_DFLT // Standard HU Type""")
    PILFERABLE = Column('PILFERABLE', Boolean, default=None, doc="""Sourced from MARA-PILFERABLE // Pilferable""")
    WHSTC = Column('WHSTC', String(2), default=None, doc="""Sourced from MARA-WHSTC // Warehouse Storage Condition""")
    WHMATGR = Column('WHMATGR', String(4), default=None, doc="""Sourced from MARA-WHMATGR // Warehouse Material Group""")
    HNDLCODE = Column('HNDLCODE', String(4), default=None, doc="""Sourced from MARA-HNDLCODE // Handling Indicator""")
    HAZMAT = Column('HAZMAT', Boolean, default=None, doc="""Sourced from MARA-HAZMAT // Relevant for Hazardous Substances""")
    HUTYP = Column('HUTYP', String(4), default=None, doc="""Sourced from MARA-HUTYP // Handling Unit Type""")
    TARE_VAR = Column('TARE_VAR', Boolean, default=None, doc="""Sourced from MARA-TARE_VAR // Variable Tare Weight""")
    MAXC = Column('MAXC', String(15), default=None, doc="""Sourced from MARA-MAXC // Maximum Allowed Capacity of Packaging Material""")
    MAXC_TOL = Column('MAXC_TOL', String(3), default=None, doc="""Sourced from MARA-MAXC_TOL // Overcapacity Tolerance of the Handling Unit""")
    MAXL = Column('MAXL', String(15), default=None, doc="""Sourced from MARA-MAXL // Maximum Packing Length of Packaging Material""")
    MAXB = Column('MAXB', String(15), default=None, doc="""Sourced from MARA-MAXB // Maximum Packing Width of Packaging Material""")
    MAXH = Column('MAXH', String(15), default=None, doc="""Sourced from MARA-MAXH // Maximum Packing Height of Packaging Material""")
    MAXDIM_UOM = Column('MAXDIM_UOM', String(3), default=None, doc="""Sourced from MARA-MAXDIM_UOM // Unit of Measure for Maximum Packing Length/Width/Height""")
    HERKL = Column('HERKL', String(3), default=None, doc="""Sourced from MARA-HERKL // Country of origin of the material""")
    MFRGR = Column('MFRGR', String(8), default=None, doc="""Sourced from MARA-MFRGR // Material freight group""")
    QQTIMEUOM = Column('QQTIMEUOM', String(3), default=None, doc="""Sourced from MARA-QQTIMEUOM // Time Unit for Quarantine Period""")
    QGRP = Column('QGRP', String(4), default=None, doc="""Sourced from MARA-QGRP // Quality Inspection Group""")
    SERIAL = Column('SERIAL', String(4), default=None, doc="""Sourced from MARA-SERIAL // Serial Number Profile""")
    PS_SMARTFORM = Column('PS_SMARTFORM', String(30), default=None, doc="""Sourced from MARA-PS_SMARTFORM // Form Name""")
    LOGUNIT = Column('LOGUNIT', String(3), default=None, doc="""Sourced from MARA-LOGUNIT // EWM CW: Logistics Unit of Measure""")
    CWQREL = Column('CWQREL', Boolean, default=None, doc="""Sourced from MARA-CWQREL // EWM CW: Material Is a Catch Weight Material""")
    CWQPROC = Column('CWQPROC', String(2), default=None, doc="""Sourced from MARA-CWQPROC // EWM CW: Catch Weight Profile for Entering CW Quantity""")
    CWQTOLGR = Column('CWQTOLGR', String(9), default=None, doc="""Sourced from MARA-CWQTOLGR // EWM-CW: Catch Weight Tolerance Group for EWM""")
    ADPROF = Column('ADPROF', String(3), default=None, doc="""Sourced from MARA-ADPROF // Adjustment Profile""")
    IPMIPPRODUCT = Column('IPMIPPRODUCT', String(40), default=None, doc="""Sourced from MARA-IPMIPPRODUCT // ID for an Intellectual Property (CRM Product)""")
    ALLOW_PMAT_IGNO = Column('ALLOW_PMAT_IGNO', Boolean, default=None, doc="""Sourced from MARA-ALLOW_PMAT_IGNO // Variant Price Allowed (for Material Master)""")
    MEDIUM = Column('MEDIUM', String(6), default=None, doc="""Sourced from MARA-MEDIUM // Medium""")
    COMMODITY = Column('COMMODITY', String(18), default=None, doc="""Sourced from MARA-COMMODITY // Physical Commodity""")
    ANIMAL_ORIGIN = Column('ANIMAL_ORIGIN', String(1), default=None, doc="""Sourced from MARA-ANIMAL_ORIGIN // Indicator: Contains Non-Textile Parts of Animal Origin""")
    TEXTILE_COMP_IND = Column('TEXTILE_COMP_IND', String(1), default=None, doc="""Sourced from MARA-TEXTILE_COMP_IND // Indicator: New Textile Composition Function""")
    SGT_CSGR = Column('SGT_CSGR', String(4), default=None, doc="""Sourced from MARA-SGT_CSGR // Segmentation Structure""")
    SGT_COVSA = Column('SGT_COVSA', String(8), default=None, doc="""Sourced from MARA-SGT_COVSA // Segmentation Strategy""")
    SGT_STAT = Column('SGT_STAT', String(1), default=None, doc="""Sourced from MARA-SGT_STAT // Segmentation Material Master Status""")
    SGT_SCOPE = Column('SGT_SCOPE', String(1), default=None, doc="""Sourced from MARA-SGT_SCOPE // Segmentation Strategy Scope""")
    SGT_REL = Column('SGT_REL', String(1), default=None, doc="""Sourced from MARA-SGT_REL // Segmentation Relevant""")
    ANP = Column('ANP', String(9), default=None, doc="""Sourced from MARA-ANP // ANP Code""")
    FSH_MG_AT1 = Column('FSH_MG_AT1', String(10), default=None, doc="""Sourced from MARA-FSH_MG_AT1 // Fashion Information Field: 1""")
    FSH_MG_AT2 = Column('FSH_MG_AT2', String(10), default=None, doc="""Sourced from MARA-FSH_MG_AT2 // Fashion Information Field: 2""")
    FSH_MG_AT3 = Column('FSH_MG_AT3', String(6), default=None, doc="""Sourced from MARA-FSH_MG_AT3 // Fashion Information Field: 3""")
    FSH_SEALV = Column('FSH_SEALV', String(1), default=None, doc="""Sourced from MARA-FSH_SEALV // Indicator: Use of Season""")
    FSH_SEAIM = Column('FSH_SEAIM', Boolean, default=None, doc="""Sourced from MARA-FSH_SEAIM // Indicator: Season Active in Inventory Management""")
    FSH_SC_MID = Column('FSH_SC_MID', String(2), default=None, doc="""Sourced from MARA-FSH_SC_MID // Material Conversion ID for Characteristic Value Conversion""")
    PACKCODE = Column('PACKCODE', String(10), default=None, doc="""Sourced from MARA-PACKCODE // Packaging Code""")
    DG_PACK_STATUS = Column('DG_PACK_STATUS', String(10), default=None, doc="""Sourced from MARA-DG_PACK_STATUS // Dangerous Goods Packaging Status""")
    MCOND = Column('MCOND', String(1), default=None, doc="""Sourced from MARA-MCOND // Material Condition Management""")
    RETDELC = Column('RETDELC', String(1), default=None, doc="""Sourced from MARA-RETDELC // Return Code""")
    LOGLEV_RETO = Column('LOGLEV_RETO', String(1), default=None, doc="""Sourced from MARA-LOGLEV_RETO // Return to Logistics Level""")
    NSNID = Column('NSNID', String(9), default=None, doc="""Sourced from MARA-NSNID // NATO Item Identification Number""")
    IMATN = Column('IMATN', String(18), default=None, doc="""Sourced from MARA-IMATN // FFF class""")
    PICNUM = Column('PICNUM', String(18), default=None, doc="""Sourced from MARA-PICNUM // Supersession chain number""")
    BSTAT = Column('BSTAT', String(2), default=None, doc="""Sourced from MARA-BSTAT // Creation Status - Seasonal Procurement""")
    COLOR_ATINN = Column('COLOR_ATINN', String(10), default=None, doc="""Sourced from MARA-COLOR_ATINN // Internal Charactieristic Number for Color Characteristics""")
    SIZE1_ATINN = Column('SIZE1_ATINN', String(10), default=None, doc="""Sourced from MARA-SIZE1_ATINN // Internal Char. Number for Characteristics for Main Sizes""")
    SIZE2_ATINN = Column('SIZE2_ATINN', String(10), default=None, doc="""Sourced from MARA-SIZE2_ATINN // Internal Char. Number for Characteristics for Second Sizes""")
    COLOR = Column('COLOR', Integer, default=None, doc="""Sourced from MARA-COLOR // Characteristic Value for Colors of Variants""")
    SIZE1 = Column('SIZE1', String(18), default=None, doc="""Sourced from MARA-SIZE1 // Characteristic Value for Main Sizes of Variants""")
    SIZE2 = Column('SIZE2', String(18), default=None, doc="""Sourced from MARA-SIZE2 // Characteristic Value for Second Size for Variants""")
    FREE_CHAR = Column('FREE_CHAR', String(18), default=None, doc="""Sourced from MARA-FREE_CHAR // Characteristic Value for Evaluation Purposes""")
    CARE_CODE = Column('CARE_CODE', String(16), default=None, doc="""Sourced from MARA-CARE_CODE // Care Codes (such as Washing Code, Ironing Code, etc.)""")
    BRAND_ID = Column('BRAND_ID', String(4), default=None, doc="""Sourced from MARA-BRAND_ID // Brand""")
    FIBER_CODE1 = Column('FIBER_CODE1', String(3), default=None, doc="""Sourced from MARA-FIBER_CODE1 // Fiber Code for Textiles (Component 1)""")
    FIBER_PART1 = Column('FIBER_PART1', String(3), default=None, doc="""Sourced from MARA-FIBER_PART1 // Percentage Share of Fiber (Component 1)""")
    FIBER_CODE2 = Column('FIBER_CODE2', String(3), default=None, doc="""Sourced from MARA-FIBER_CODE2 // Fiber Code for Textiles (Component 2)""")
    FIBER_PART2 = Column('FIBER_PART2', String(3), default=None, doc="""Sourced from MARA-FIBER_PART2 // Percentage Share of Fiber (Component 2)""")
    FIBER_CODE3 = Column('FIBER_CODE3', String(3), default=None, doc="""Sourced from MARA-FIBER_CODE3 // Fiber Code for Textiles (Component 3)""")
    FIBER_PART3 = Column('FIBER_PART3', String(3), default=None, doc="""Sourced from MARA-FIBER_PART3 // Percentage Share of Fiber (Component 3)""")
    FIBER_CODE4 = Column('FIBER_CODE4', String(3), default=None, doc="""Sourced from MARA-FIBER_CODE4 // Fiber Code for Textiles (Component 4)""")
    FIBER_PART4 = Column('FIBER_PART4', String(3), default=None, doc="""Sourced from MARA-FIBER_PART4 // Percentage Share of Fiber (Component 4)""")
    FIBER_CODE5 = Column('FIBER_CODE5', String(3), default=None, doc="""Sourced from MARA-FIBER_CODE5 // Fiber Code for Textiles (Component 5)""")
    FIBER_PART5 = Column('FIBER_PART5', String(3), default=None, doc="""Sourced from MARA-FIBER_PART5 // Percentage Share of Fiber (Component 5)""")
    FASHGRD = Column('FASHGRD', String(4), default=None, doc="""Sourced from MARA-FASHGRD // Fashion Grade""")
    PSM_CODE = Column('PSM_CODE', String(2), default=None, doc="""Sourced from MARA-PSM_CODE // Code of Protected Species Management""")
    YYDESIGNCODE = Column('YYDESIGNCODE', String(1), default=None, doc="""Sourced from MARA-YYDESIGNCODE // Tire Design Category Code""")
    YYTICCODE = Column('YYTICCODE', String(5), default=None, doc="""Sourced from MARA-YYTICCODE // TIC Code""")
    YYTICVERSION = Column('YYTICVERSION', String(2), default=None, doc="""Sourced from MARA-YYTICVERSION // TIC Version""")
    YYPRIORITY = Column('YYPRIORITY', String(2), default=None, doc="""Sourced from MARA-YYPRIORITY // Priority""")
    YYTYPE = Column('YYTYPE', String(30), default=None, doc="""Sourced from MARA-YYTYPE // Type of Material""")
    YYSTKSTRAT = Column('YYSTKSTRAT', String(3), default=None, doc="""Sourced from MARA-YYSTKSTRAT // Stocking Strategy""")
    YYSTCC = Column('YYSTCC', String(10), default=None, doc="""Sourced from MARA-YYSTCC // STCC Code""")
    YYIMPORT = Column('YYIMPORT', String(2), default=None, doc="""Sourced from MARA-YYIMPORT // Manufacturing/Import Flag""")
    YYCODE18A = Column('YYCODE18A', String(18), default=None, doc="""Sourced from MARA-YYCODE18A // Kelly Manufacturing Material Code""")
    YYCODE18B = Column('YYCODE18B', String(18), default=None, doc="""Sourced from MARA-YYCODE18B // Dunlop Material Code""")
    YYUNIVERS1 = Column('YYUNIVERS1', String(5), default=None, doc="""Sourced from MARA-YYUNIVERS1 // Cost Collector Key""")
    YYUNIVERS2 = Column('YYUNIVERS2', String(5), default=None, doc="""Sourced from MARA-YYUNIVERS2 // Universal Field for future use""")
    YYUNIVERS3 = Column('YYUNIVERS3', String(5), default=None, doc="""Sourced from MARA-YYUNIVERS3 // Universal Field for future use""")
    YYUNIVERS4 = Column('YYUNIVERS4', String(3), default=None, doc="""Sourced from MARA-YYUNIVERS4 // XPLOR Blocking Indicator""")
    YYUNIVERS5 = Column('YYUNIVERS5', String(3), default=None, doc="""Sourced from MARA-YYUNIVERS5 // CSIS Store Room Class""")
    YYUNIVERS6 = Column('YYUNIVERS6', String(3), default=None, doc="""Sourced from MARA-YYUNIVERS6 // Catalogue/Label  Source""")
    YYUNIVERS7 = Column('YYUNIVERS7', String(3), default=None, doc="""Sourced from MARA-YYUNIVERS7 // Universal Field for future use""")
    YYUNIVERS8 = Column('YYUNIVERS8', String(3), default=None, doc="""Sourced from MARA-YYUNIVERS8 // Universal Field for future use""")
    YYCATLAG = Column('YYCATLAG', String(35), default=None, doc="""Sourced from MARA-YYCATLAG // Catalogue / Label ID""")
    YYCORELVL = Column('YYCORELVL', String(1), default=None, doc="""Sourced from MARA-YYCORELVL // Product Core Level""")

    material_id = synonym('MATNR')
    create_dt = synonym('ERSDA')
    doc_create_user_id = synonym('ERNAM')
    last_change_dt = synonym('LAEDA')
    update_user_id = synonym('AENAM')
    deleted_ind = synonym('LVORM')
    material_type_id = synonym('MTART')
    material_group_cd = synonym('MATKL')
    old_matl_id = synonym('BISMT')
    uom_cd = synonym('MEINS')
    prch_ord_uom_cd = synonym('BSTME')
    size_dimension_txt = synonym('GROES')
    puch_value_cd = synonym('EKWSL')
    gross_wt = synonym('BRGEW')
    net_wt = synonym('NTGEW')
    weight_uom_cd = synonym('GEWEI')
    vol = synonym('VOLUM')
    volume_uom_cd = synonym('VOLEH')
    div_cd = synonym('SPART')
    customer_id = synonym('KUNNR')
    procurement_rule_cd = synonym('BWVOR')
    supply_source_cd = synonym('BWSCL')
    length = synonym('LAENG')
    width = synonym('BREIT')
    height = synonym('HOEHE')
    lwh_uom_cd = synonym('MEABM')
    packaging_wt = synonym('ERGEW')
    wt_uom_cd = synonym('ERGEI')
    packaging_vol = synonym('ERVOL')
    vol_uom_cd = synonym('ERVOE')
    configurable_material_ind = synonym('KZKFG')
    batch_mgmt_required_ind = synonym('XCHPF')
    auth_grp_id = synonym('BEGRU')
    valid_from_dt = synonym('DATAB')
    deletion_dt = synonym('LIQDT')
    ext_matl_grp_id = synonym('EXTWG')
    matl_ctgy_id = synonym('ATTYP')
    co_product_ind = synonym('KZKUP')
    material_status_cd = synonym('MSTAE')
    cross_distr_material_status_cd = synonym('MSTAV')
    product_alloc_procedure_cd = synonym('KOSCH')
    mfg_part_nbr = synonym('MFRPN')
    material_locked_ind = synonym('MATFI')
    origin_country_cd = synonym('HERKL')


################################################################################




################################################################################

class MaterialFacility(SAP_Base):
    """\
    Table sourced from: MARC
    Description: Plant Data for Material
    """

    __tablename__ = "MARC"

    MATNR = Column('MATNR', String(18), primary_key = True, doc="""Sourced from MARC-MATNR // Material Number""")
    WERKS = Column('WERKS', String(4), primary_key = True, doc="""Sourced from MARC-WERKS // Plant""")
    PSTAT = Column('PSTAT', String(15), default=None, doc="""Sourced from MARC-PSTAT // Maintenance status""")
    LVORM = Column('LVORM', Boolean, default=None, doc="""Sourced from MARC-LVORM // Flag Material for Deletion at Plant Level""")
    BWTTY = Column('BWTTY', String(1), default=None, doc="""Sourced from MARC-BWTTY // Valuation Category""")
    XCHAR = Column('XCHAR', Boolean, default=None, doc="""Sourced from MARC-XCHAR // Batch management indicator (internal)""")
    MMSTA = Column('MMSTA', String(2), default=None, doc="""Sourced from MARC-MMSTA // Plant-Specific Material Status""")
    MMSTD = Column('MMSTD', Date, default=None, doc="""Sourced from MARC-MMSTD // Date from which the plant-specific material status is valid""")
    MAABC = Column('MAABC', String(1), default=None, doc="""Sourced from MARC-MAABC // ABC Indicator""")
    KZKRI = Column('KZKRI', Boolean, default=None, doc="""Sourced from MARC-KZKRI // Indicator: Critical part""")
    EKGRP = Column('EKGRP', String(3), default=None, doc="""Sourced from MARC-EKGRP // Purchasing Group""")
    AUSME = Column('AUSME', String(3), default=None, doc="""Sourced from MARC-AUSME // Unit of issue""")
    DISPR = Column('DISPR', String(4), default=None, doc="""Sourced from MARC-DISPR // Material: MRP profile""")
    DISMM = Column('DISMM', String(2), default=None, doc="""Sourced from MARC-DISMM // MRP Type""")
    DISPO = Column('DISPO', String(3), default=None, doc="""Sourced from MARC-DISPO // MRP Controller (Materials Planner)""")
    KZDIE = Column('KZDIE', Boolean, default=None, doc="""Sourced from MARC-KZDIE // Indicator: MRP controller is buyer (deactivated)""")
    PLIFZ = Column('PLIFZ', Numeric(15,3,3), default=None, doc="""Sourced from MARC-PLIFZ // Planned Delivery Time in Days""")
    WEBAZ = Column('WEBAZ', Numeric(15,3,3), default=None, doc="""Sourced from MARC-WEBAZ // Goods Receipt Processing Time in Days""")
    PERKZ = Column('PERKZ', String(1), default=None, doc="""Sourced from MARC-PERKZ // Period Indicator""")
    AUSSS = Column('AUSSS', Numeric(15,3,3), default=None, doc="""Sourced from MARC-AUSSS // Assembly scrap in percent""")
    DISLS = Column('DISLS', String(2), default=None, doc="""Sourced from MARC-DISLS // Lot size (materials planning)""")
    BESKZ = Column('BESKZ', String(1), default=None, doc="""Sourced from MARC-BESKZ // Procurement Type""")
    SOBSL = Column('SOBSL', String(2), default=None, doc="""Sourced from MARC-SOBSL // Special procurement type""")
    MINBE = Column('MINBE', Numeric(15,3,3), default=None, doc="""Sourced from MARC-MINBE // Reorder Point""")
    EISBE = Column('EISBE', Numeric(15,3,3), default=None, doc="""Sourced from MARC-EISBE // Safety Stock""")
    BSTMI = Column('BSTMI', Numeric(15,3,3), default=None, doc="""Sourced from MARC-BSTMI // Minimum Lot Size""")
    BSTMA = Column('BSTMA', Numeric(15,3,3), default=None, doc="""Sourced from MARC-BSTMA // Maximum Lot Size""")
    BSTFE = Column('BSTFE', Numeric(15,3,3), default=None, doc="""Sourced from MARC-BSTFE // Fixed lot size""")
    BSTRF = Column('BSTRF', Numeric(15,3,3), default=None, doc="""Sourced from MARC-BSTRF // Rounding value for purchase order quantity""")
    MABST = Column('MABST', Numeric(15,3,3), default=None, doc="""Sourced from MARC-MABST // Maximum stock level""")
    LOSFX = Column('LOSFX', Numeric(15,3,3), default=None, doc="""Sourced from MARC-LOSFX // Ordering costs""")
    SBDKZ = Column('SBDKZ', String(1), default=None, doc="""Sourced from MARC-SBDKZ // Dependent requirements ind. for individual and coll. reqmts""")
    LAGPR = Column('LAGPR', String(1), default=None, doc="""Sourced from MARC-LAGPR // Storage costs indicator""")
    ALTSL = Column('ALTSL', String(1), default=None, doc="""Sourced from MARC-ALTSL // Method for Selecting Alternative Bills of Material""")
    KZAUS = Column('KZAUS', String(1), default=None, doc="""Sourced from MARC-KZAUS // Discontinuation indicator""")
    AUSDT = Column('AUSDT', Date, default=None, doc="""Sourced from MARC-AUSDT // Effective-Out Date""")
    NFMAT = Column('NFMAT', String(18), default=None, doc="""Sourced from MARC-NFMAT // Follow-Up Material""")
    KZBED = Column('KZBED', String(1), default=None, doc="""Sourced from MARC-KZBED // Indicator for Requirements Grouping""")
    MISKZ = Column('MISKZ', String(1), default=None, doc="""Sourced from MARC-MISKZ // Mixed MRP indicator""")
    FHORI = Column('FHORI', String(3), default=None, doc="""Sourced from MARC-FHORI // Scheduling Margin Key for Floats""")
    PFREI = Column('PFREI', Boolean, default=None, doc="""Sourced from MARC-PFREI // Indicator: automatic fixing of planned orders""")
    FFREI = Column('FFREI', Boolean, default=None, doc="""Sourced from MARC-FFREI // Release indicator for production orders""")
    RGEKZ = Column('RGEKZ', String(1), default=None, doc="""Sourced from MARC-RGEKZ // Indicator: Backflush""")
    FEVOR = Column('FEVOR', String(3), default=None, doc="""Sourced from MARC-FEVOR // Production Supervisor""")
    BEARZ = Column('BEARZ', Numeric(15,3,3), default=None, doc="""Sourced from MARC-BEARZ // Processing time""")
    RUEZT = Column('RUEZT', Numeric(15,3,3), default=None, doc="""Sourced from MARC-RUEZT // Setup and teardown time""")
    TRANZ = Column('TRANZ', Numeric(15,3,3), default=None, doc="""Sourced from MARC-TRANZ // Interoperation time""")
    BASMG = Column('BASMG', Numeric(15,3,3), default=None, doc="""Sourced from MARC-BASMG // Base quantity""")
    DZEIT = Column('DZEIT', Numeric(15,3,3), default=None, doc="""Sourced from MARC-DZEIT // In-house production time""")
    MAXLZ = Column('MAXLZ', Numeric(15,3,3), default=None, doc="""Sourced from MARC-MAXLZ // Maximum Storage Period""")
    LZEIH = Column('LZEIH', String(3), default=None, doc="""Sourced from MARC-LZEIH // Unit for maximum storage period""")
    KZPRO = Column('KZPRO', Boolean, default=None, doc="""Sourced from MARC-KZPRO // Indicator: withdrawal of stock from production bin""")
    GPMKZ = Column('GPMKZ', Boolean, default=None, doc="""Sourced from MARC-GPMKZ // Indicator: Material Included in Rough-Cut Planning""")
    UEETO = Column('UEETO', Numeric(15,3,3), default=None, doc="""Sourced from MARC-UEETO // Overdelivery tolerance limit""")
    UEETK = Column('UEETK', Boolean, default=None, doc="""Sourced from MARC-UEETK // Indicator: Unlimited Overdelivery Allowed""")
    UNETO = Column('UNETO', Numeric(15,3,3), default=None, doc="""Sourced from MARC-UNETO // Underdelivery tolerance limit""")
    WZEIT = Column('WZEIT', Numeric(15,3,3), default=None, doc="""Sourced from MARC-WZEIT // Total replenishment lead time (in workdays)""")
    ATPKZ = Column('ATPKZ', String(1), default=None, doc="""Sourced from MARC-ATPKZ // Replacement part""")
    VZUSL = Column('VZUSL', Numeric(15,3,3), default=None, doc="""Sourced from MARC-VZUSL // Surcharge factor for cost in percent""")
    HERBL = Column('HERBL', String(2), default=None, doc="""Sourced from MARC-HERBL // State of manufacture""")
    INSMK = Column('INSMK', String(1), default=None, doc="""Sourced from MARC-INSMK // Post to Inspection Stock""")
    SPROZ = Column('SPROZ', Numeric(15,3,3), default=None, doc="""Sourced from MARC-SPROZ // Sample for quality inspection (in %) (deactivated)""")
    QUAZT = Column('QUAZT', Numeric(15,3,3), default=None, doc="""Sourced from MARC-QUAZT // Quarantine period (deactivated)""")
    SSQSS = Column('SSQSS', String(8), default=None, doc="""Sourced from MARC-SSQSS // Control Key for Quality Management in Procurement""")
    MPDAU = Column('MPDAU', Numeric(15,3,3), default=None, doc="""Sourced from MARC-MPDAU // Mean inspection duration (deactivated)""")
    KZPPV = Column('KZPPV', String(1), default=None, doc="""Sourced from MARC-KZPPV // Indicator for inspection plan (deactivated)""")
    KZDKZ = Column('KZDKZ', Boolean, default=None, doc="""Sourced from MARC-KZDKZ // Documentation required indicator""")
    WSTGH = Column('WSTGH', Numeric(15,3,3), default=None, doc="""Sourced from MARC-WSTGH // Active substance content (deactivated)""")
    PRFRQ = Column('PRFRQ', Numeric(15,3,3), default=None, doc="""Sourced from MARC-PRFRQ // Interval until next recurring inspection""")
    NKMPR = Column('NKMPR', Date, default=None, doc="""Sourced from MARC-NKMPR // Date according to check sampling inspection (deactivated)""")
    UMLMC = Column('UMLMC', String(13), default=None, doc="""Sourced from MARC-UMLMC // Stock in Transfer (Plant to Plant)""")
    LADGR = Column('LADGR', String(4), default=None, doc="""Sourced from MARC-LADGR // Loading Group""")
    XCHPF = Column('XCHPF', Boolean, default=None, doc="""Sourced from MARC-XCHPF // Batch management requirement indicator""")
    USEQU = Column('USEQU', String(1), default=None, doc="""Sourced from MARC-USEQU // Quota arrangement usage""")
    LGRAD = Column('LGRAD', Numeric(15,3,3), default=None, doc="""Sourced from MARC-LGRAD // Service level""")
    AUFTL = Column('AUFTL', String(1), default=None, doc="""Sourced from MARC-AUFTL // Splitting Indicator""")
    PLVAR = Column('PLVAR', String(2), default=None, doc="""Sourced from MARC-PLVAR // Plan Version""")
    OTYPE = Column('OTYPE', String(2), default=None, doc="""Sourced from MARC-OTYPE // Object Type""")
    OBJID = Column('OBJID', String(8), default=None, doc="""Sourced from MARC-OBJID // Object ID""")
    MTVFP = Column('MTVFP', String(2), default=None, doc="""Sourced from MARC-MTVFP // Checking Group for Availability Check""")
    PERIV = Column('PERIV', String(2), default=None, doc="""Sourced from MARC-PERIV // Fiscal Year Variant""")
    KZKFK = Column('KZKFK', Boolean, default=None, doc="""Sourced from MARC-KZKFK // Indicator: take correction factors into account""")
    VRVEZ = Column('VRVEZ', Numeric(15,3,3), default=None, doc="""Sourced from MARC-VRVEZ // Shipping setup time""")
    VBAMG = Column('VBAMG', Numeric(15,3,3), default=None, doc="""Sourced from MARC-VBAMG // Base quantity for capacity planning in shipping""")
    VBEAZ = Column('VBEAZ', Numeric(15,3,3), default=None, doc="""Sourced from MARC-VBEAZ // Shipping processing time""")
    LIZYK = Column('LIZYK', String(4), default=None, doc="""Sourced from MARC-LIZYK // Deactivated""")
    BWSCL = Column('BWSCL', String(1), default=None, doc="""Sourced from MARC-BWSCL // Source of Supply""")
    KAUTB = Column('KAUTB', String(1), default=None, doc="""Sourced from MARC-KAUTB // Indicator: 'automatic purchase order allowed'""")
    KORDB = Column('KORDB', Boolean, default=None, doc="""Sourced from MARC-KORDB // Indicator: Source list requirement""")
    STAWN = Column('STAWN', String(17), default=None, doc="""Sourced from MARC-STAWN // Commodity Code/Import Code Number for Foreign Trade""")
    HERKL = Column('HERKL', String(3), default=None, doc="""Sourced from MARC-HERKL // Country of origin of the material""")
    HERKR = Column('HERKR', String(3), default=None, doc="""Sourced from MARC-HERKR // Region of origin of material (non-preferential origin)""")
    EXPME = Column('EXPME', String(3), default=None, doc="""Sourced from MARC-EXPME // Unit of measure for commodity code (foreign trade)""")
    MTVER = Column('MTVER', String(4), default=None, doc="""Sourced from MARC-MTVER // Export/import material group""")
    PRCTR = Column('PRCTR', String(10), default=None, doc="""Sourced from MARC-PRCTR // Profit Center""")
    TRAME = Column('TRAME', Numeric(15,3,3), default=None, doc="""Sourced from MARC-TRAME // Stock in Transit""")
    MRPPP = Column('MRPPP', String(3), default=None, doc="""Sourced from MARC-MRPPP // PPC planning calendar""")
    SAUFT = Column('SAUFT', Boolean, default=None, doc="""Sourced from MARC-SAUFT // Ind.: Repetitive mfg allowed""")
    FXHOR = Column('FXHOR', String(3), default=None, doc="""Sourced from MARC-FXHOR // Planning time fence""")
    VRMOD = Column('VRMOD', String(1), default=None, doc="""Sourced from MARC-VRMOD // Consumption mode""")
    VINT1 = Column('VINT1', String(3), default=None, doc="""Sourced from MARC-VINT1 // Consumption period: backward""")
    VINT2 = Column('VINT2', String(3), default=None, doc="""Sourced from MARC-VINT2 // Consumption period: forward""")
    VERKZ = Column('VERKZ', Boolean, default=None, doc="""Sourced from MARC-VERKZ // Version Indicator""")
    STLAL = Column('STLAL', String(2), default=None, doc="""Sourced from MARC-STLAL // Alternative BOM""")
    STLAN = Column('STLAN', String(1), default=None, doc="""Sourced from MARC-STLAN // BOM Usage""")
    PLNNR = Column('PLNNR', String(8), default=None, doc="""Sourced from MARC-PLNNR // Key for Task List Group""")
    APLAL = Column('APLAL', String(2), default=None, doc="""Sourced from MARC-APLAL // Group Counter""")
    LOSGR = Column('LOSGR', Numeric(15,3,3), default=None, doc="""Sourced from MARC-LOSGR // Lot Size for Product Costing""")
    SOBSK = Column('SOBSK', String(2), default=None, doc="""Sourced from MARC-SOBSK // Special Procurement Type for Costing""")
    FRTME = Column('FRTME', String(3), default=None, doc="""Sourced from MARC-FRTME // Production unit""")
    LGPRO = Column('LGPRO', String(4), default=None, doc="""Sourced from MARC-LGPRO // Issue Storage Location""")
    DISGR = Column('DISGR', String(4), default=None, doc="""Sourced from MARC-DISGR // MRP Group""")
    KAUSF = Column('KAUSF', Numeric(15,3,3), default=None, doc="""Sourced from MARC-KAUSF // Component scrap in percent""")
    QZGTP = Column('QZGTP', String(4), default=None, doc="""Sourced from MARC-QZGTP // Certificate Type""")
    QMATV = Column('QMATV', Boolean, default=None, doc="""Sourced from MARC-QMATV // Inspection Setup Exists for Material/Plant""")
    TAKZT = Column('TAKZT', Numeric(15,3,3), default=None, doc="""Sourced from MARC-TAKZT // Takt time""")
    RWPRO = Column('RWPRO', String(3), default=None, doc="""Sourced from MARC-RWPRO // Range of coverage profile""")
    COPAM = Column('COPAM', String(10), default=None, doc="""Sourced from MARC-COPAM // Local field name for CO/PA link to SOP""")
    ABCIN = Column('ABCIN', String(1), default=None, doc="""Sourced from MARC-ABCIN // Physical inventory indicator for cycle counting""")
    AWSLS = Column('AWSLS', String(6), default=None, doc="""Sourced from MARC-AWSLS // Variance Key""")
    SERNP = Column('SERNP', String(4), default=None, doc="""Sourced from MARC-SERNP // Serial Number Profile""")
    CUOBJ = Column('CUOBJ', String(18), default=None, doc="""Sourced from MARC-CUOBJ // Internal object number""")
    STDPD = Column('STDPD', String(18), default=None, doc="""Sourced from MARC-STDPD // Configurable material""")
    SFEPR = Column('SFEPR', String(4), default=None, doc="""Sourced from MARC-SFEPR // Repetitive manufacturing profile""")
    XMCNG = Column('XMCNG', Boolean, default=None, doc="""Sourced from MARC-XMCNG // Negative stocks allowed in plant""")
    QSSYS = Column('QSSYS', String(4), default=None, doc="""Sourced from MARC-QSSYS // Required QM System for Vendor""")
    LFRHY = Column('LFRHY', String(3), default=None, doc="""Sourced from MARC-LFRHY // Planning cycle""")
    RDPRF = Column('RDPRF', String(4), default=None, doc="""Sourced from MARC-RDPRF // Rounding Profile""")
    VRBMT = Column('VRBMT', String(18), default=None, doc="""Sourced from MARC-VRBMT // Reference material for consumption""")
    VRBWK = Column('VRBWK', String(4), default=None, doc="""Sourced from MARC-VRBWK // Reference plant for consumption""")
    VRBDT = Column('VRBDT', Date, default=None, doc="""Sourced from MARC-VRBDT // To date of the material to be copied for consumption""")
    VRBFK = Column('VRBFK', Numeric(15,3,3), default=None, doc="""Sourced from MARC-VRBFK // Multiplier for reference material for consumption""")
    AUTRU = Column('AUTRU', Boolean, default=None, doc="""Sourced from MARC-AUTRU // Reset Forecast Model Automatically""")
    PREFE = Column('PREFE', String(1), default=None, doc="""Sourced from MARC-PREFE // Preference indicator in export/import""")
    PRENC = Column('PRENC', String(1), default=None, doc="""Sourced from MARC-PRENC // Exemption certificate: Indicator for legal control""")
    PRENO = Column('PRENO', String(8), default=None, doc="""Sourced from MARC-PRENO // Exemption certificate number for legal control""")
    PREND = Column('PREND', Date, default=None, doc="""Sourced from MARC-PREND // Exemption certificate: Issue date of exemption certificate""")
    PRENE = Column('PRENE', String(1), default=None, doc="""Sourced from MARC-PRENE // Indicator: Vendor declaration exists""")
    PRENG = Column('PRENG', Date, default=None, doc="""Sourced from MARC-PRENG // Validity date of vendor declaration""")
    ITARK = Column('ITARK', Boolean, default=None, doc="""Sourced from MARC-ITARK // Indicator: Military goods""")
    SERVG = Column('SERVG', String(1), default=None, doc="""Sourced from MARC-SERVG // IS-R service level""")
    KZKUP = Column('KZKUP', String(1), default=None, doc="""Sourced from MARC-KZKUP // Indicator: Material can be co-product""")
    STRGR = Column('STRGR', String(2), default=None, doc="""Sourced from MARC-STRGR // Planning strategy group""")
    CUOBV = Column('CUOBV', String(18), default=None, doc="""Sourced from MARC-CUOBV // Internal object number of configurable material for planning""")
    LGFSB = Column('LGFSB', String(4), default=None, doc="""Sourced from MARC-LGFSB // Default storage location for external procurement""")
    SCHGT = Column('SCHGT', Boolean, default=None, doc="""Sourced from MARC-SCHGT // Indicator: Bulk Material""")
    CCFIX = Column('CCFIX', Boolean, default=None, doc="""Sourced from MARC-CCFIX // CC indicator is fixed""")
    EPRIO = Column('EPRIO', String(4), default=None, doc="""Sourced from MARC-EPRIO // Stock determination group""")
    QMATA = Column('QMATA', String(6), default=None, doc="""Sourced from MARC-QMATA // Material Authorization Group for Activities in QM""")
    RESVP = Column('RESVP', Numeric(15,3,3), default=None, doc="""Sourced from MARC-RESVP // Period of adjustment for planned independent requirements""")
    PLNTY = Column('PLNTY', String(1), default=None, doc="""Sourced from MARC-PLNTY // Task List Type""")
    UOMGR = Column('UOMGR', String(3), default=None, doc="""Sourced from MARC-UOMGR // Unit of Mearsure Group (Oil, Natural Gas,...)""")
    UMRSL = Column('UMRSL', String(4), default=None, doc="""Sourced from MARC-UMRSL // Conversion Group (Oil, Natural Gas,..)""")
    ABFAC = Column('ABFAC', String(2), default=None, doc="""Sourced from MARC-ABFAC // Air Bouyancy Factor""")
    SFCPF = Column('SFCPF', String(6), default=None, doc="""Sourced from MARC-SFCPF // Production Scheduling Profile""")
    SHFLG = Column('SHFLG', String(1), default=None, doc="""Sourced from MARC-SHFLG // Safety time indicator (with or without safety time)""")
    SHZET = Column('SHZET', String(2), default=None, doc="""Sourced from MARC-SHZET // Safety time (in workdays)""")
    MDACH = Column('MDACH', String(2), default=None, doc="""Sourced from MARC-MDACH // Action control: planned order processing""")
    KZECH = Column('KZECH', String(1), default=None, doc="""Sourced from MARC-KZECH // Determination of batch entry in the production/process order""")
    MEGRU = Column('MEGRU', String(4), default=None, doc="""Sourced from MARC-MEGRU // Unit of Measure Group""")
    MFRGR = Column('MFRGR', String(8), default=None, doc="""Sourced from MARC-MFRGR // Material freight group""")
    VKUMC = Column('VKUMC', Numeric(15,3,3), default=None, doc="""Sourced from MARC-VKUMC // Stock transfer sales value (plant to plant) for VO material""")
    VKTRW = Column('VKTRW', Numeric(15,3,3), default=None, doc="""Sourced from MARC-VKTRW // Transit value at sales price for value-only material""")
    KZAGL = Column('KZAGL', String(1), default=None, doc="""Sourced from MARC-KZAGL // Indicator: smooth promotion consumption""")
    FVIDK = Column('FVIDK', String(4), default=None, doc="""Sourced from MARC-FVIDK // Production Version To Be Costed""")
    FXPRU = Column('FXPRU', Boolean, default=None, doc="""Sourced from MARC-FXPRU // Fixed-Price Co-Product""")
    LOGGR = Column('LOGGR', String(4), default=None, doc="""Sourced from MARC-LOGGR // Logistics handling group for workload calculation""")
    FPRFM = Column('FPRFM', String(3), default=None, doc="""Sourced from MARC-FPRFM // Distribution profile of material in plant""")
    GLGMG = Column('GLGMG', Numeric(15,3,3), default=None, doc="""Sourced from MARC-GLGMG // Tied Empties Stock""")
    VKGLG = Column('VKGLG', Numeric(15,3,3), default=None, doc="""Sourced from MARC-VKGLG // Sales value of tied empties stock""")
    INDUS = Column('INDUS', String(2), default=None, doc="""Sourced from MARC-INDUS // Material CFOP category""")
    MOWNR = Column('MOWNR', String(12), default=None, doc="""Sourced from MARC-MOWNR // CAP: Number of CAP products list""")
    MOGRU = Column('MOGRU', String(6), default=None, doc="""Sourced from MARC-MOGRU // Common Agricultural Policy: CAP products group-Foreign Trade""")
    CASNR = Column('CASNR', String(15), default=None, doc="""Sourced from MARC-CASNR // CAS number for pharmaceutical products in foreign trade""")
    GPNUM = Column('GPNUM', String(9), default=None, doc="""Sourced from MARC-GPNUM // Production statistics: PRODCOM number for foreign trade""")
    STEUC = Column('STEUC', String(16), default=None, doc="""Sourced from MARC-STEUC // Control code for consumption taxes in foreign trade""")
    FABKZ = Column('FABKZ', String(1), default=None, doc="""Sourced from MARC-FABKZ // Indicator: Item Relevant to JIT Delivery Schedules""")
    MATGR = Column('MATGR', String(20), default=None, doc="""Sourced from MARC-MATGR // Group of Materials for Transition Matrix""")
    VSPVB = Column('VSPVB', String(10), default=None, doc="""Sourced from MARC-VSPVB // Proposed Supply Area in Material Master Record""")
    DPLFS = Column('DPLFS', String(2), default=None, doc="""Sourced from MARC-DPLFS // Fair share rule""")
    DPLPU = Column('DPLPU', String(1), default=None, doc="""Sourced from MARC-DPLPU // Indicator: push distribution""")
    DPLHO = Column('DPLHO', Numeric(15,3,3), default=None, doc="""Sourced from MARC-DPLHO // Deployment horizon in days""")
    MINLS = Column('MINLS', Numeric(15,3,3), default=None, doc="""Sourced from MARC-MINLS // Minimum lot size for Supply Demand Match""")
    MAXLS = Column('MAXLS', Numeric(15,3,3), default=None, doc="""Sourced from MARC-MAXLS // Maximum lot size for Supply Demand Match""")
    FIXLS = Column('FIXLS', String(13), default=None, doc="""Sourced from MARC-FIXLS // Fixed lot size for Supply Demand Match""")
    LTINC = Column('LTINC', String(13), default=None, doc="""Sourced from MARC-LTINC // Lot size increment for  Supply Demand Match""")
    COMPL = Column('COMPL', String(2), default=None, doc="""Sourced from MARC-COMPL // This field is no longer used""")
    CONVT = Column('CONVT', String(2), default=None, doc="""Sourced from MARC-CONVT // Conversion types for production figures""")
    SHPRO = Column('SHPRO', String(3), default=None, doc="""Sourced from MARC-SHPRO // Period Profile for Safety Time""")
    AHDIS = Column('AHDIS', String(1), default=None, doc="""Sourced from MARC-AHDIS // MRP relevancy for dependent requirements""")
    DIBER = Column('DIBER', Boolean, default=None, doc="""Sourced from MARC-DIBER // Indicator: MRP area exists""")
    KZPSP = Column('KZPSP', String(1), default=None, doc="""Sourced from MARC-KZPSP // Indicator for cross-project material""")
    OCMPF = Column('OCMPF', String(6), default=None, doc="""Sourced from MARC-OCMPF // Overall profile for order change management""")
    APOKZ = Column('APOKZ', String(1), default=None, doc="""Sourced from MARC-APOKZ // Indicator: Is material relevant for APO""")
    MCRUE = Column('MCRUE', Boolean, default=None, doc="""Sourced from MARC-MCRUE // MARDH rec. already exists for per. before last of MARD per.""")
    LFMON = Column('LFMON', String(2), default=None, doc="""Sourced from MARC-LFMON // Current period (posting period)""")
    LFGJA = Column('LFGJA', String(4), default=None, doc="""Sourced from MARC-LFGJA // Fiscal Year of Current Period""")
    EISLO = Column('EISLO', Numeric(15,3,3), default=None, doc="""Sourced from MARC-EISLO // Minimum Safety Stock""")
    NCOST = Column('NCOST', String(1), default=None, doc="""Sourced from MARC-NCOST // Do Not Cost""")
    ROTATION_DATE = Column('ROTATION_DATE', String(1), default=None, doc="""Sourced from MARC-ROTATION_DATE // Strategy for Putaway and Stock Removal""")
    UCHKZ = Column('UCHKZ', String(1), default=None, doc="""Sourced from MARC-UCHKZ // Indicator for Original Batch Management""")
    UCMAT = Column('UCMAT', String(18), default=None, doc="""Sourced from MARC-UCMAT // Reference Material for Original Batches""")
    BWESB = Column('BWESB', Numeric(15,3,3), default=None, doc="""Sourced from MARC-BWESB // Valuated Goods Receipt Blocked Stock""")
    SGT_COVS = Column('SGT_COVS', String(8), default=None, doc="""Sourced from MARC-SGT_COVS // Segmentation Strategy""")
    SGT_STATC = Column('SGT_STATC', String(1), default=None, doc="""Sourced from MARC-SGT_STATC // Segmentation Status""")
    SGT_SCOPE = Column('SGT_SCOPE', String(1), default=None, doc="""Sourced from MARC-SGT_SCOPE // Segmentation Strategy Scope""")
    SGT_MRPSI = Column('SGT_MRPSI', String(1), default=None, doc="""Sourced from MARC-SGT_MRPSI // Sort Stock based on Segment""")
    SGT_PRCM = Column('SGT_PRCM', String(1), default=None, doc="""Sourced from MARC-SGT_PRCM // Consumption Priority""")
    SGT_CHINT = Column('SGT_CHINT', Boolean, default=None, doc="""Sourced from MARC-SGT_CHINT // Discrete Batch Number""")
    SGT_STK_PRT = Column('SGT_STK_PRT', String(1), default=None, doc="""Sourced from MARC-SGT_STK_PRT // Stock Protection Indicator""")
    SGT_DEFSC = Column('SGT_DEFSC', String(16), default=None, doc="""Sourced from MARC-SGT_DEFSC // Default Stock Segment value""")
    FSH_MG_ARUN_REQ = Column('FSH_MG_ARUN_REQ', String(1), default=None, doc="""Sourced from MARC-FSH_MG_ARUN_REQ // Order Allocation Run""")
    FSH_SEAIM = Column('FSH_SEAIM', Boolean, default=None, doc="""Sourced from MARC-FSH_SEAIM // Indicator: Season Active in Inventory Management""")
    IUID_RELEVANT = Column('IUID_RELEVANT', String(1), default=None, doc="""Sourced from MARC-IUID_RELEVANT // IUID-Relevant""")
    IUID_TYPE = Column('IUID_TYPE', String(10), default=None, doc="""Sourced from MARC-IUID_TYPE // Structure Type of UII""")
    UID_IEA = Column('UID_IEA', String(1), default=None, doc="""Sourced from MARC-UID_IEA // External Allocation of UII""")
    CONS_PROCG = Column('CONS_PROCG', String(1), default=None, doc="""Sourced from MARC-CONS_PROCG // Consignment Control""")
    GI_PR_TIME = Column('GI_PR_TIME', String(3), default=None, doc="""Sourced from MARC-GI_PR_TIME // Goods Issue Processing Time in Days""")
    MULTIPLE_EKGRP = Column('MULTIPLE_EKGRP', String(1), default=None, doc="""Sourced from MARC-MULTIPLE_EKGRP // Purchasing Across Purchasing Group""")
    REF_SCHEMA = Column('REF_SCHEMA', String(2), default=None, doc="""Sourced from MARC-REF_SCHEMA // Reference Determination Schema""")
    MIN_TROC = Column('MIN_TROC', String(3), default=None, doc="""Sourced from MARC-MIN_TROC // Minimum Target Range of Coverage""")
    MAX_TROC = Column('MAX_TROC', String(3), default=None, doc="""Sourced from MARC-MAX_TROC // Maximum Target Range of Coverage""")
    TARGET_STOCK = Column('TARGET_STOCK', String(13), default=None, doc="""Sourced from MARC-TARGET_STOCK // Target Stock""")

    material_id = synonym('MATNR')
    deleted_ind = synonym('LVORM')
    internal_batch_mgmt_ind = synonym('XCHAR')
    material_facility_status_cd = synonym('MMSTA')
    material_facility_status_dt = synonym('MMSTD')
    critical_part_ind = synonym('KZKRI')
    prch_grp_cd = synonym('EKGRP')
    mrp_matl_profile_cd = synonym('DISPR')
    mrp_type_cd = synonym('DISMM')
    mrp_controller_cd = synonym('DISPO')
    mrp_lot_size_cd = synonym('DISLS')
    prcu_type_cd = synonym('BESKZ')
    special_procurement_type_cd = synonym('SOBSL')
    reorder_point_qty = synonym('MINBE')
    safety_stock_qty = synonym('EISBE')
    min_lot_size_qty = synonym('BSTMI')
    max_lot_size_qty = synonym('BSTMA')
    fixed_lot_size_qty = synonym('BSTFE')
    prch_ord_rounding_qty = synonym('BSTRF')
    max_stock_level_qty = synonym('MABST')
    ordering_costs_qty = synonym('LOSFX')
    processing_tm = synonym('BEARZ')
    base_uom_cd = synonym('BASMG')
    in_house_production_time_qty = synonym('DZEIT')
    stock_type_cd = synonym('INSMK')
    loading_grp_id = synonym('LADGR')
    batch_mgmt_required_ind = synonym('XCHPF')
    availability_checking_group_id = synonym('MTVFP')
    supply_source_cd = synonym('BWSCL')
    origin_country_cd = synonym('HERKL')
    origin_region_cd = synonym('HERKR')
    in_transit_stock_qty = synonym('TRAME')
    planned_lot_size_qty = synonym('LOSGR')
    production_uom_cd = synonym('FRTME')
    mrp_grp_cd = synonym('DISGR')
    negative_facility_stocks_allowed_ind = synonym('XMCNG')
    military_goods_ind = synonym('ITARK')
    co_product_ind = synonym('KZKUP')
    uom_group_cd = synonym('MEGRU')
    jit_deliv_schedule_rlvnt_ind = synonym('FABKZ')
    fair_share_rule_cd = synonym('DPLFS')
    push_distribution_cd = synonym('DPLPU')
    deployment_horizon_days = synonym('DPLHO')
    mrp_area_exists_ind = synonym('DIBER')
    min_safety_stock_qty = synonym('EISLO')
    valuated_blocked_stock_qty = synonym('BWESB')


################################################################################




################################################################################

class MaterialStock(SAP_Base):
    """\
    Table sourced from: MARD
    Description: Storage Location Data for Material
    """

    __tablename__ = "MARD"

    MATNR = Column('MATNR', String(18), primary_key = True, doc="""Sourced from MARD-MATNR // Material Number""")
    WERKS = Column('WERKS', String(4), primary_key = True, doc="""Sourced from MARD-WERKS // Plant""")
    LGORT = Column('LGORT', String(4), primary_key = True, doc="""Sourced from MARD-LGORT // Storage Location""")
    PSTAT = Column('PSTAT', String(15), default=None, doc="""Sourced from MARD-PSTAT // Maintenance status""")
    LVORM = Column('LVORM', Boolean, default=None, doc="""Sourced from MARD-LVORM // Flag Material for Deletion at Storage Location Level""")
    LFGJA = Column('LFGJA', String(4), default=None, doc="""Sourced from MARD-LFGJA // Fiscal Year of Current Period""")
    LFMON = Column('LFMON', String(2), default=None, doc="""Sourced from MARD-LFMON // Current period (posting period)""")
    SPERR = Column('SPERR', String(1), default=None, doc="""Sourced from MARD-SPERR // Physical Inventory Blocking Indicator""")
    LABST = Column('LABST', Numeric(15,3,3), default=None, doc="""Sourced from MARD-LABST // Valuated Unrestricted-Use Stock""")
    UMLME = Column('UMLME', Numeric(15,3,3), default=None, doc="""Sourced from MARD-UMLME // Stock in transfer (from one storage location to another)""")
    INSME = Column('INSME', Numeric(15,3,3), default=None, doc="""Sourced from MARD-INSME // Stock in Quality Inspection""")
    EINME = Column('EINME', Numeric(15,3,3), default=None, doc="""Sourced from MARD-EINME // Total Stock of All Restricted Batches""")
    SPEME = Column('SPEME', Numeric(15,3,3), default=None, doc="""Sourced from MARD-SPEME // Blocked Stock""")
    RETME = Column('RETME', Numeric(15,3,3), default=None, doc="""Sourced from MARD-RETME // Blocked Stock Returns""")
    VMLAB = Column('VMLAB', Numeric(15,3,3), default=None, doc="""Sourced from MARD-VMLAB // Valuated unrestricted-use stock in previous period""")
    VMUML = Column('VMUML', Numeric(15,3,3), default=None, doc="""Sourced from MARD-VMUML // Stock in Transfer in Previous Period""")
    VMINS = Column('VMINS', Numeric(15,3,3), default=None, doc="""Sourced from MARD-VMINS // Stock in Quality Inspection in Previous Period""")
    VMEIN = Column('VMEIN', Numeric(15,3,3), default=None, doc="""Sourced from MARD-VMEIN // Restricted-Use Stock in Previous Period""")
    VMSPE = Column('VMSPE', Numeric(15,3,3), default=None, doc="""Sourced from MARD-VMSPE // Blocked stock of previous period""")
    VMRET = Column('VMRET', Numeric(15,3,3), default=None, doc="""Sourced from MARD-VMRET // Blocked Stock Returns in Previous Period""")
    KZILL = Column('KZILL', String(3), default=None, doc="""Sourced from MARD-KZILL // Physical inventory indicator for whse stock in current year""")
    KZILQ = Column('KZILQ', String(3), default=None, doc="""Sourced from MARD-KZILQ // Phys. inventory ind. f. stock in qual. insp. in current year""")
    KZILE = Column('KZILE', String(3), default=None, doc="""Sourced from MARD-KZILE // Physical inventory indicator for restricted-use stock""")
    KZILS = Column('KZILS', String(3), default=None, doc="""Sourced from MARD-KZILS // Physical inventory indicator for blocked stock""")
    KZVLL = Column('KZVLL', String(3), default=None, doc="""Sourced from MARD-KZVLL // Physical inventory indicator for stock in previous year""")
    KZVLQ = Column('KZVLQ', String(3), default=None, doc="""Sourced from MARD-KZVLQ // Phys. inventory ind. f. stock in qual. insp. in prev. period""")
    KZVLE = Column('KZVLE', String(3), default=None, doc="""Sourced from MARD-KZVLE // Physical inventory ind. for restricted-use stock, prev.pd""")
    KZVLS = Column('KZVLS', String(3), default=None, doc="""Sourced from MARD-KZVLS // Phys. inventory indicator for blocked stock in prev. period""")
    DISKZ = Column('DISKZ', String(1), default=None, doc="""Sourced from MARD-DISKZ // Storage location MRP indicator""")
    LSOBS = Column('LSOBS', String(2), default=None, doc="""Sourced from MARD-LSOBS // Special procurement type at storage location level""")
    LMINB = Column('LMINB', Numeric(15,3,3), default=None, doc="""Sourced from MARD-LMINB // Reorder point for storage location MRP""")
    LBSTF = Column('LBSTF', Numeric(15,3,3), default=None, doc="""Sourced from MARD-LBSTF // Replenishment quantity for storage location MRP""")
    HERKL = Column('HERKL', String(3), default=None, doc="""Sourced from MARD-HERKL // Country of origin of the material""")
    EXPPG = Column('EXPPG', String(1), default=None, doc="""Sourced from MARD-EXPPG // Preference indicator (deactivated)""")
    EXVER = Column('EXVER', String(2), default=None, doc="""Sourced from MARD-EXVER // Export indicator (deactivated)""")
    LGPBE = Column('LGPBE', String(10), default=None, doc="""Sourced from MARD-LGPBE // Storage Bin""")
    KLABS = Column('KLABS', Numeric(15,3,3), default=None, doc="""Sourced from MARD-KLABS // Unrestricted-Use Consignment Stock""")
    KINSM = Column('KINSM', Numeric(15,3,3), default=None, doc="""Sourced from MARD-KINSM // Consignment Stock in Quality Inspection""")
    KEINM = Column('KEINM', Numeric(15,3,3), default=None, doc="""Sourced from MARD-KEINM // Restricted-Use Consignment Stock""")
    KSPEM = Column('KSPEM', Numeric(15,3,3), default=None, doc="""Sourced from MARD-KSPEM // Blocked Consignment Stock""")
    DLINL = Column('DLINL', Date, default=None, doc="""Sourced from MARD-DLINL // Date of Last Posted Count for Unrestricted-Use Stock""")
    PRCTL = Column('PRCTL', String(10), default=None, doc="""Sourced from MARD-PRCTL // Profit Center""")
    ERSDA = Column('ERSDA', Date, default=None, doc="""Sourced from MARD-ERSDA // Created On""")
    VKLAB = Column('VKLAB', Numeric(15,3,3), default=None, doc="""Sourced from MARD-VKLAB // Stock value of a value-only material at sales price""")
    VKUML = Column('VKUML', Numeric(15,3,3), default=None, doc="""Sourced from MARD-VKUML // Sales value in stock transfer (SLOc to SLoc)""")
    LWMKB = Column('LWMKB', String(3), default=None, doc="""Sourced from MARD-LWMKB // Picking area for lean WM""")
    BSKRF = Column('BSKRF', Float, default=None, doc="""Sourced from MARD-BSKRF // Inventory correction factor""")
    MDRUE = Column('MDRUE', Boolean, default=None, doc="""Sourced from MARD-MDRUE // MARDH rec. already exists for per. before last of MARD per.""")
    MDJIN = Column('MDJIN', String(4), default=None, doc="""Sourced from MARD-MDJIN // Fiscal year of current physical inventory indicator""")

    material_id = synonym('MATNR')
    deleted_ind = synonym('LVORM')
    unrestricted_stock_qty = synonym('LABST')
    in_transfer_stock_qty = synonym('UMLME')
    quality_inspection_stock_qty = synonym('INSME')
    all_restricted_total_stock_qty = synonym('EINME')
    blocked_stock_qty = synonym('SPEME')
    returnst_stock_qty = synonym('RETME')
    mrp_storage_loc_cd = synonym('DISKZ')
    special_procurement_cd = synonym('LSOBS')
    stor_loc_reorder_point_qty = synonym('LMINB')
    stor_loc_replenishment_qty = synonym('LBSTF')
    origin_country_cd = synonym('HERKL')
    storage_bin_id = synonym('LGPBE')
    unrestricted_consignment_stock_qty = synonym('KLABS')
    qual_insp_consignment_stock_qty = synonym('KINSM')
    consignment_stock_qty = synonym('KEINM')
    last_count_of_unrestricted_dt = synonym('DLINL')
    create_dt = synonym('ERSDA')


################################################################################




################################################################################

class MaterialUOM(SAP_Base):
    """\
    Table sourced from: MARM
    Description: Units of Measure for Material
    """

    __tablename__ = "MARM"

    MATNR = Column('MATNR', String(18), primary_key = True, doc="""Sourced from MARM-MATNR // Material Number""")
    MEINH = Column('MEINH', String(3), primary_key = True, doc="""Sourced from MARM-MEINH // Alternative Unit of Measure for Stockkeeping Unit""")
    UMREZ = Column('UMREZ', Numeric(15,3,3), default=None, doc="""Sourced from MARM-UMREZ // Numerator for Conversion to Base Units of Measure""")
    UMREN = Column('UMREN', Numeric(15,3,3), default=None, doc="""Sourced from MARM-UMREN // Denominator for conversion to base units of measure""")
    EANNR = Column('EANNR', String(13), default=None, doc="""Sourced from MARM-EANNR // European Article Number (EAN) - obsolete!!!!!""")
    EAN11 = Column('EAN11', String(18), default=None, doc="""Sourced from MARM-EAN11 // International Article Number (EAN/UPC)""")
    NUMTP = Column('NUMTP', String(2), default=None, doc="""Sourced from MARM-NUMTP // Category of International Article Number (EAN)""")
    LAENG = Column('LAENG', Numeric(15,3,3), default=None, doc="""Sourced from MARM-LAENG // Length""")
    BREIT = Column('BREIT', Numeric(15,3,3), default=None, doc="""Sourced from MARM-BREIT // Width""")
    HOEHE = Column('HOEHE', Numeric(15,3,3), default=None, doc="""Sourced from MARM-HOEHE // Height""")
    MEABM = Column('MEABM', String(3), default=None, doc="""Sourced from MARM-MEABM // Unit of Dimension for Length/Width/Height""")
    VOLUM = Column('VOLUM', Numeric(15,3,3), default=None, doc="""Sourced from MARM-VOLUM // Volume""")
    VOLEH = Column('VOLEH', String(3), default=None, doc="""Sourced from MARM-VOLEH // Volume unit""")
    BRGEW = Column('BRGEW', Numeric(15,3,3), default=None, doc="""Sourced from MARM-BRGEW // Gross Weight""")
    GEWEI = Column('GEWEI', String(3), default=None, doc="""Sourced from MARM-GEWEI // Weight Unit""")
    MESUB = Column('MESUB', String(3), default=None, doc="""Sourced from MARM-MESUB // Lower-Level Unit of Measure in a Packing Hierarchy""")
    ATINN = Column('ATINN', String(10), default=None, doc="""Sourced from MARM-ATINN // Internal characteristic""")
    MESRT = Column('MESRT', String(2), default=None, doc="""Sourced from MARM-MESRT // Unit of measure sort number""")
    XFHDW = Column('XFHDW', Boolean, default=None, doc="""Sourced from MARM-XFHDW // Leading batch-specific unit of measure""")
    XBEWW = Column('XBEWW', Boolean, default=None, doc="""Sourced from MARM-XBEWW // Valuation based on the batch-specific unit of measure""")
    KZWSO = Column('KZWSO', String(1), default=None, doc="""Sourced from MARM-KZWSO // Units of measure usage""")
    MSEHI = Column('MSEHI', String(3), default=None, doc="""Sourced from MARM-MSEHI // Unit of Measurement of Characteristic""")
    BFLME_MARM = Column('BFLME_MARM', String(1), default=None, doc="""Sourced from MARM-BFLME_MARM // Generic Material with Logistical Variants""")
    GTIN_VARIANT = Column('GTIN_VARIANT', String(2), default=None, doc="""Sourced from MARM-GTIN_VARIANT // Global Trade Item Number Variant""")
    NEST_FTR = Column('NEST_FTR', String(3), default=None, doc="""Sourced from MARM-NEST_FTR // Remaining Volume after Nesting (in Percentage)""")
    MAX_STACK = Column('MAX_STACK', String(3), default=None, doc="""Sourced from MARM-MAX_STACK // Maximum Stacking Factor""")
    CAPAUSE = Column('CAPAUSE', String(15), default=None, doc="""Sourced from MARM-CAPAUSE // Capacity Usage""")
    TY2TQ = Column('TY2TQ', String(1), default=None, doc="""Sourced from MARM-TY2TQ // EWM-CW: Category of Unit of Measure""")

    material_id = synonym('MATNR')
    base_uom_conversin_num = synonym('UMREZ')
    base_uom_conversion_denom = synonym('UMREN')
    length = synonym('LAENG')
    width = synonym('BREIT')
    height = synonym('HOEHE')
    lwh_uom_cd = synonym('MEABM')
    vol = synonym('VOLUM')
    volume_uom_cd = synonym('VOLEH')
    gross_wt = synonym('BRGEW')
    weight_uom_cd = synonym('GEWEI')
    uom_sort_key = synonym('MESRT')
    unit_of_measure_cd = synonym('MSEHI')


################################################################################




################################################################################

class MaterialBOM(SAP_Base):
    """\
    Table sourced from: MAST
    Description: Material to BOM Link
    """

    __tablename__ = "MAST"

    MATNR = Column('MATNR', String(18), primary_key = True, doc="""Sourced from MAST-MATNR // Material Number""")
    WERKS = Column('WERKS', String(4), primary_key = True, doc="""Sourced from MAST-WERKS // Plant""")
    STLAN = Column('STLAN', String(1), primary_key = True, doc="""Sourced from MAST-STLAN // BOM Usage""")
    STLNR = Column('STLNR', String(8), primary_key = True, doc="""Sourced from MAST-STLNR // Bill of material""")
    STLAL = Column('STLAL', String(2), primary_key = True, doc="""Sourced from MAST-STLAL // Alternative BOM""")
    LOSVN = Column('LOSVN', Numeric(15,3,3), default=None, doc="""Sourced from MAST-LOSVN // From Lot Size""")
    LOSBS = Column('LOSBS', Numeric(15,3,3), default=None, doc="""Sourced from MAST-LOSBS // To Lot Size""")
    ANDAT = Column('ANDAT', Date, default=None, doc="""Sourced from MAST-ANDAT // Date record created on""")
    ANNAM = Column('ANNAM', String(12), default=None, doc="""Sourced from MAST-ANNAM // User who created record""")
    AEDAT = Column('AEDAT', Date, default=None, doc="""Sourced from MAST-AEDAT // Changed On""")
    AENAM = Column('AENAM', String(12), default=None, doc="""Sourced from MAST-AENAM // Name of Person Who Changed Object""")
    CSLTY = Column('CSLTY', Boolean, default=None, doc="""Sourced from MAST-CSLTY // Indicator: configured material (material variant)""")

    material_id = synonym('MATNR')
    from_lot_size_qty = synonym('LOSVN')
    to_lot_size_qty = synonym('LOSBS')
    create_user_id = synonym('ANNAM')
    update_dt = synonym('AEDAT')
    update_user_id = synonym('AENAM')
    configured_matl_ind = synonym('CSLTY')


################################################################################




################################################################################

class MaterialValuation(SAP_Base):
    """\
    Table sourced from: MBEW
    Description: Material Valuation
    """

    __tablename__ = "MBEW"

    MATNR = Column('MATNR', String(18), primary_key = True, doc="""Sourced from MBEW-MATNR // Material Number""")
    BWKEY = Column('BWKEY', String(4), primary_key = True, doc="""Sourced from MBEW-BWKEY // Valuation Area""")
    BWTAR = Column('BWTAR', String(10), primary_key = True, doc="""Sourced from MBEW-BWTAR // Valuation Type""")
    LVORM = Column('LVORM', Boolean, default=None, doc="""Sourced from MBEW-LVORM // Deletion flag for all material data of a valuation type""")
    LBKUM = Column('LBKUM', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-LBKUM // Total Valuated Stock""")
    SALK3 = Column('SALK3', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-SALK3 // Value of Total Valuated Stock""")
    VPRSV = Column('VPRSV', String(1), default=None, doc="""Sourced from MBEW-VPRSV // Price Control Indicator""")
    VERPR = Column('VERPR', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-VERPR // Moving Average Price/Periodic Unit Price""")
    STPRS = Column('STPRS', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-STPRS // Standard price""")
    PEINH = Column('PEINH', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-PEINH // Price Unit""")
    BKLAS = Column('BKLAS', String(4), default=None, doc="""Sourced from MBEW-BKLAS // Valuation Class""")
    SALKV = Column('SALKV', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-SALKV // Value based on moving average price (only with price ctrl S)""")
    VMKUM = Column('VMKUM', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-VMKUM // Total valuated stock in previous period""")
    VMSAL = Column('VMSAL', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-VMSAL // Value of total valuated stock in previous period""")
    VMVPR = Column('VMVPR', String(1), default=None, doc="""Sourced from MBEW-VMVPR // Price Control Indicator in Previous Period""")
    VMVER = Column('VMVER', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-VMVER // Moving Average Price/Periodic Unit Price in Previous Period""")
    VMSTP = Column('VMSTP', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-VMSTP // Standard price in the previous period""")
    VMPEI = Column('VMPEI', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-VMPEI // Price unit of previous period""")
    VMBKL = Column('VMBKL', String(4), default=None, doc="""Sourced from MBEW-VMBKL // Valuation Class in Previous Period""")
    VMSAV = Column('VMSAV', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-VMSAV // Value based on moving average price (previous period)""")
    VJKUM = Column('VJKUM', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-VJKUM // Total Valuated Stock in Previous Year""")
    VJSAL = Column('VJSAL', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-VJSAL // Value of total valuated stock in previous year""")
    VJVPR = Column('VJVPR', String(1), default=None, doc="""Sourced from MBEW-VJVPR // Price Control Indicator in Previous Year""")
    VJVER = Column('VJVER', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-VJVER // Moving Average Price/Periodic Unit Price in Previous Year""")
    VJSTP = Column('VJSTP', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-VJSTP // Standard price in previous year""")
    VJPEI = Column('VJPEI', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-VJPEI // Price unit of previous year""")
    VJBKL = Column('VJBKL', String(4), default=None, doc="""Sourced from MBEW-VJBKL // Valuation Class in Previous Year""")
    VJSAV = Column('VJSAV', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-VJSAV // Value based on moving average price (previous year)""")
    LFGJA = Column('LFGJA', String(4), default=None, doc="""Sourced from MBEW-LFGJA // Fiscal Year of Current Period""")
    LFMON = Column('LFMON', String(2), default=None, doc="""Sourced from MBEW-LFMON // Current period (posting period)""")
    BWTTY = Column('BWTTY', String(1), default=None, doc="""Sourced from MBEW-BWTTY // Valuation Category""")
    STPRV = Column('STPRV', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-STPRV // Previous price""")
    LAEPR = Column('LAEPR', Date, default=None, doc="""Sourced from MBEW-LAEPR // Date of the last price change""")
    ZKPRS = Column('ZKPRS', String(11), default=None, doc="""Sourced from MBEW-ZKPRS // Future price""")
    ZKDAT = Column('ZKDAT', String(8), default=None, doc="""Sourced from MBEW-ZKDAT // Date as of which the price is valid""")
    TIMESTAMP = Column('TIMESTAMP', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-TIMESTAMP // UTC Time Stamp in Short Form (YYYYMMDDhhmmss)""")
    BWPRS = Column('BWPRS', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-BWPRS // Valuation price based on tax law: level 1""")
    BWPRH = Column('BWPRH', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-BWPRH // Valuation price based on commercial law: level 1""")
    VJBWS = Column('VJBWS', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-VJBWS // Valuation price based on tax law: level 3""")
    VJBWH = Column('VJBWH', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-VJBWH // Valuation price based on commercial law: level 3""")
    VVJSL = Column('VVJSL', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-VVJSL // Value of total valuated stock in year before last""")
    VVJLB = Column('VVJLB', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-VVJLB // Total valuated stock in year before last""")
    VVMLB = Column('VVMLB', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-VVMLB // Total valuated stock in period before last""")
    VVSAL = Column('VVSAL', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-VVSAL // Value of total valuated stock in period before last""")
    ZPLPR = Column('ZPLPR', String(11), default=None, doc="""Sourced from MBEW-ZPLPR // Future planned price""")
    ZPLP1 = Column('ZPLP1', String(11), default=None, doc="""Sourced from MBEW-ZPLP1 // Future Planned Price 1""")
    ZPLP2 = Column('ZPLP2', String(11), default=None, doc="""Sourced from MBEW-ZPLP2 // Future Planned Price 2""")
    ZPLP3 = Column('ZPLP3', String(11), default=None, doc="""Sourced from MBEW-ZPLP3 // Future Planned Price 3""")
    ZPLD1 = Column('ZPLD1', String(8), default=None, doc="""Sourced from MBEW-ZPLD1 // Date from Which Future Planned Price 1 Is Valid""")
    ZPLD2 = Column('ZPLD2', String(8), default=None, doc="""Sourced from MBEW-ZPLD2 // Date from Which Future Planned Price 2 Is Valid""")
    ZPLD3 = Column('ZPLD3', String(8), default=None, doc="""Sourced from MBEW-ZPLD3 // Date from Which Future Planned Price 3 Is Valid""")
    PPERZ = Column('PPERZ', String(6), default=None, doc="""Sourced from MBEW-PPERZ // Period for future standard cost estimate (deactivated)""")
    PPERL = Column('PPERL', String(6), default=None, doc="""Sourced from MBEW-PPERL // Period for current standard cost estimate (deactivated)""")
    PPERV = Column('PPERV', String(6), default=None, doc="""Sourced from MBEW-PPERV // Period for previous standard cost estimate (deactivated)""")
    KALKZ = Column('KALKZ', Boolean, default=None, doc="""Sourced from MBEW-KALKZ // Indicator: standard cost estimate for future period""")
    KALKL = Column('KALKL', Boolean, default=None, doc="""Sourced from MBEW-KALKL // Standard Cost Estimate for Current Period""")
    KALKV = Column('KALKV', Boolean, default=None, doc="""Sourced from MBEW-KALKV // Indicator: standard cost estimate for previous period""")
    KALSC = Column('KALSC', String(6), default=None, doc="""Sourced from MBEW-KALSC // Overhead key (deactivated)""")
    XLIFO = Column('XLIFO', String(1), default=None, doc="""Sourced from MBEW-XLIFO // LIFO/FIFO-Relevant""")
    MYPOL = Column('MYPOL', String(4), default=None, doc="""Sourced from MBEW-MYPOL // Pool number for LIFO valuation""")
    BWPH1 = Column('BWPH1', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-BWPH1 // Valuation price based on commercial law: level 2""")
    BWPS1 = Column('BWPS1', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-BWPS1 // Valuation price based on tax law: level 2""")
    ABWKZ = Column('ABWKZ', String(2), default=None, doc="""Sourced from MBEW-ABWKZ // Lowest value: devaluation indicator""")
    PSTAT = Column('PSTAT', String(15), default=None, doc="""Sourced from MBEW-PSTAT // Maintenance status""")
    KALN1 = Column('KALN1', String(12), default=None, doc="""Sourced from MBEW-KALN1 // Cost Estimate Number - Product Costing""")
    KALNR = Column('KALNR', String(12), default=None, doc="""Sourced from MBEW-KALNR // Cost Estimate Number for Cost Est. w/o Qty Structure""")
    BWVA1 = Column('BWVA1', String(3), default=None, doc="""Sourced from MBEW-BWVA1 // Valuation Variant for Future Standard Cost Estimate""")
    BWVA2 = Column('BWVA2', String(3), default=None, doc="""Sourced from MBEW-BWVA2 // Valuation Variant for Current Standard Cost Estimate""")
    BWVA3 = Column('BWVA3', String(3), default=None, doc="""Sourced from MBEW-BWVA3 // Valuation Variant for Previous Standard Cost Estimate""")
    VERS1 = Column('VERS1', String(2), default=None, doc="""Sourced from MBEW-VERS1 // Costing Version of Future Standard Cost Estimate""")
    VERS2 = Column('VERS2', String(2), default=None, doc="""Sourced from MBEW-VERS2 // Costing Version of Current Standard Cost Estimate""")
    VERS3 = Column('VERS3', String(2), default=None, doc="""Sourced from MBEW-VERS3 // Costing Version of Previous Standard Cost Estimate""")
    HRKFT = Column('HRKFT', String(4), default=None, doc="""Sourced from MBEW-HRKFT // Origin Group as Subdivision of Cost Element""")
    KOSGR = Column('KOSGR', String(10), default=None, doc="""Sourced from MBEW-KOSGR // Costing Overhead Group""")
    PPRDZ = Column('PPRDZ', String(3), default=None, doc="""Sourced from MBEW-PPRDZ // Period of Future Standard Cost Estimate""")
    PPRDL = Column('PPRDL', String(3), default=None, doc="""Sourced from MBEW-PPRDL // Period of Current Standard Cost Estimate""")
    PPRDV = Column('PPRDV', String(3), default=None, doc="""Sourced from MBEW-PPRDV // Period of Previous Standard Cost Estimate""")
    PDATZ = Column('PDATZ', String(4), default=None, doc="""Sourced from MBEW-PDATZ // Fiscal Year of Future Standard Cost Estimate""")
    PDATL = Column('PDATL', String(4), default=None, doc="""Sourced from MBEW-PDATL // Fiscal Year of Current Standard Cost Estimate""")
    PDATV = Column('PDATV', String(4), default=None, doc="""Sourced from MBEW-PDATV // Fiscal Year of Previous Standard Cost Estimate""")
    EKALR = Column('EKALR', Boolean, default=None, doc="""Sourced from MBEW-EKALR // Material Is Costed with Quantity Structure""")
    VPLPR = Column('VPLPR', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-VPLPR // Previous planned price""")
    MLMAA = Column('MLMAA', Boolean, default=None, doc="""Sourced from MBEW-MLMAA // Material ledger activated at material level""")
    MLAST = Column('MLAST', String(1), default=None, doc="""Sourced from MBEW-MLAST // Material Price Determination: Control""")
    LPLPR = Column('LPLPR', String(11), default=None, doc="""Sourced from MBEW-LPLPR // Current Planned Price""")
    VKSAL = Column('VKSAL', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-VKSAL // Value of Total Valuated Stock at Sales Price""")
    HKMAT = Column('HKMAT', String(1), default=None, doc="""Sourced from MBEW-HKMAT // Material-related origin""")
    SPERW = Column('SPERW', String(1), default=None, doc="""Sourced from MBEW-SPERW // Physical Inventory Blocking Indicator""")
    KZIWL = Column('KZIWL', String(3), default=None, doc="""Sourced from MBEW-KZIWL // Phys. inventory indicator for  value-only material""")
    WLINL = Column('WLINL', String(8), default=None, doc="""Sourced from MBEW-WLINL // Date of Last Posted Count for Unrestricted-Use Stock""")
    ABCIW = Column('ABCIW', String(1), default=None, doc="""Sourced from MBEW-ABCIW // Physical inventory indicator for cycle counting""")
    BWSPA = Column('BWSPA', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-BWSPA // Valuation margin""")
    LPLPX = Column('LPLPX', String(11), default=None, doc="""Sourced from MBEW-LPLPX // Fixed Portion of Current Planned Price""")
    VPLPX = Column('VPLPX', String(11), default=None, doc="""Sourced from MBEW-VPLPX // Fixed Portion of Previous Planned Price""")
    FPLPX = Column('FPLPX', String(11), default=None, doc="""Sourced from MBEW-FPLPX // Fixed Portion of Future Planned Price""")
    LBWST = Column('LBWST', String(1), default=None, doc="""Sourced from MBEW-LBWST // Val. Strat. for Current Plan Price, Sales Order/Proj. Stock""")
    VBWST = Column('VBWST', String(1), default=None, doc="""Sourced from MBEW-VBWST // Valuation Strategy for Previous Plan Price, Special Stock""")
    FBWST = Column('FBWST', String(1), default=None, doc="""Sourced from MBEW-FBWST // Valuation Strategy for Future Planned Price, Special Stock""")
    EKLAS = Column('EKLAS', String(4), default=None, doc="""Sourced from MBEW-EKLAS // Valuation Class for Sales Order Stock""")
    QKLAS = Column('QKLAS', String(4), default=None, doc="""Sourced from MBEW-QKLAS // Valuation Class for Project Stock""")
    MTUSE = Column('MTUSE', String(1), default=None, doc="""Sourced from MBEW-MTUSE // Usage of the material""")
    MTORG = Column('MTORG', String(1), default=None, doc="""Sourced from MBEW-MTORG // Origin of the material""")
    OWNPR = Column('OWNPR', Boolean, default=None, doc="""Sourced from MBEW-OWNPR // Produced in-house""")
    XBEWM = Column('XBEWM', Boolean, default=None, doc="""Sourced from MBEW-XBEWM // Valuation based on the batch-specific unit of measure""")
    BWPEI = Column('BWPEI', Numeric(15,3,3), default=None, doc="""Sourced from MBEW-BWPEI // Price unit for valuation prices based on tax/commercial law""")
    MBRUE = Column('MBRUE', Boolean, default=None, doc="""Sourced from MBEW-MBRUE // MBEWH rec. already exists for per. before last of MBEW per.""")
    OKLAS = Column('OKLAS', String(4), default=None, doc="""Sourced from MBEW-OKLAS // Valuation Class for Special Stock at the Vendor""")
    OIPPINV = Column('OIPPINV', String(1), default=None, doc="""Sourced from MBEW-OIPPINV // Prepaid Inventory Flag for Material Valuation Type Segment""")

    material_id = synonym('MATNR')
    valuation_area_id = synonym('BWKEY')
    deleted_ind = synonym('LVORM')
    total_valuated_stock_qty = synonym('LBKUM')
    price_uom_cd = synonym('PEINH')
    last_price_change_dt = synonym('LAEPR')
    valuation_margin_qty = synonym('BWSPA')


################################################################################




################################################################################

class MaterialBatch(SAP_Base):
    """\
    Table sourced from: MCH1
    Description: Batches (if Batch Management Cross-Plant)
    """

    __tablename__ = "MCH1"

    MATNR = Column('MATNR', String(18), primary_key = True, doc="""Sourced from MCH1-MATNR // Material Number""")
    CHARG = Column('CHARG', String(10), primary_key = True, doc="""Sourced from MCH1-CHARG // Batch Number""")
    LVORM = Column('LVORM', Boolean, default=None, doc="""Sourced from MCH1-LVORM // Deletion Flag for All Data in a Batch""")
    ERSDA = Column('ERSDA', Date, default=None, doc="""Sourced from MCH1-ERSDA // Created On""")
    ERNAM = Column('ERNAM', String(12), default=None, doc="""Sourced from MCH1-ERNAM // Name of Person who Created the Object""")
    AENAM = Column('AENAM', String(12), default=None, doc="""Sourced from MCH1-AENAM // Name of Person Who Changed Object""")
    LAEDA = Column('LAEDA', Date, default=None, doc="""Sourced from MCH1-LAEDA // Date of Last Change""")
    VERAB = Column('VERAB', Date, default=None, doc="""Sourced from MCH1-VERAB // Availability date""")
    VFDAT = Column('VFDAT', Date, default=None, doc="""Sourced from MCH1-VFDAT // Shelf Life Expiration or Best-Before Date""")
    ZUSCH = Column('ZUSCH', String(1), default=None, doc="""Sourced from MCH1-ZUSCH // Batch status key""")
    ZUSTD = Column('ZUSTD', Boolean, default=None, doc="""Sourced from MCH1-ZUSTD // Batch in Restricted-Use Stock""")
    ZAEDT = Column('ZAEDT', String(8), default=None, doc="""Sourced from MCH1-ZAEDT // Date of last status change""")
    LIFNR = Column('LIFNR', String(10), default=None, doc="""Sourced from MCH1-LIFNR // Vendor Account Number""")
    LICHA = Column('LICHA', String(15), default=None, doc="""Sourced from MCH1-LICHA // Vendor Batch Number""")
    VLCHA = Column('VLCHA', String(10), default=None, doc="""Sourced from MCH1-VLCHA // Original batch number (deactivated)""")
    VLWRK = Column('VLWRK', String(4), default=None, doc="""Sourced from MCH1-VLWRK // Original plant  (deactivated)""")
    VLMAT = Column('VLMAT', String(18), default=None, doc="""Sourced from MCH1-VLMAT // Original material    (deactivated)""")
    CHAME = Column('CHAME', String(3), default=None, doc="""Sourced from MCH1-CHAME // Unit of issue for batch (deactivated)""")
    LWEDT = Column('LWEDT', Date, default=None, doc="""Sourced from MCH1-LWEDT // Date of last goods receipt""")
    FVDT1 = Column('FVDT1', String(8), default=None, doc="""Sourced from MCH1-FVDT1 // Date for unrestricted use""")
    FVDT2 = Column('FVDT2', String(8), default=None, doc="""Sourced from MCH1-FVDT2 // Date for unrestricted use""")
    FVDT3 = Column('FVDT3', String(8), default=None, doc="""Sourced from MCH1-FVDT3 // Date for unrestricted use""")
    FVDT4 = Column('FVDT4', String(8), default=None, doc="""Sourced from MCH1-FVDT4 // Date for unrestricted use""")
    FVDT5 = Column('FVDT5', String(8), default=None, doc="""Sourced from MCH1-FVDT5 // Date for unrestricted use""")
    FVDT6 = Column('FVDT6', String(8), default=None, doc="""Sourced from MCH1-FVDT6 // Date for unrestricted use""")
    HERKL = Column('HERKL', String(3), default=None, doc="""Sourced from MCH1-HERKL // Country of origin of the material""")
    HERKR = Column('HERKR', String(3), default=None, doc="""Sourced from MCH1-HERKR // Region of origin of material (non-preferential origin)""")
    MTVER = Column('MTVER', String(4), default=None, doc="""Sourced from MCH1-MTVER // Export/import material group""")
    QNDAT = Column('QNDAT', String(8), default=None, doc="""Sourced from MCH1-QNDAT // Next Inspection Date""")
    HSDAT = Column('HSDAT', Date, default=None, doc="""Sourced from MCH1-HSDAT // Date of Manufacture""")
    CUOBJ_BM = Column('CUOBJ_BM', String(18), default=None, doc="""Sourced from MCH1-CUOBJ_BM // Internal object no.: Batch classification""")
    DEACT_BM = Column('DEACT_BM', Boolean, default=None, doc="""Sourced from MCH1-DEACT_BM // Batch is no longer active""")
    BATCH_TYPE = Column('BATCH_TYPE', String(1), default=None, doc="""Sourced from MCH1-BATCH_TYPE // Type of Batch""")
    SGT_SCAT = Column('SGT_SCAT', String(16), default=None, doc="""Sourced from MCH1-SGT_SCAT // Stock Segment""")

    material_id = synonym('MATNR')
    deleted_ind = synonym('LVORM')
    create_dt = synonym('ERSDA')
    doc_create_user_id = synonym('ERNAM')
    update_user_id = synonym('AENAM')
    last_change_dt = synonym('LAEDA')
    availability_dt = synonym('VERAB')
    origin_country_cd = synonym('HERKL')
    origin_region_cd = synonym('HERKR')
    mfg_dt = synonym('HSDAT')
    batch_deactivated_ind = synonym('DEACT_BM')


################################################################################




################################################################################

class MaterialFacilityBatch(SAP_Base):
    """\
    Table sourced from: MCHA
    Description: Batches
    """

    __tablename__ = "MCHA"

    MATNR = Column('MATNR', String(18), primary_key = True, doc="""Sourced from MCHA-MATNR // Material Number""")
    WERKS = Column('WERKS', String(4), primary_key = True, doc="""Sourced from MCHA-WERKS // Plant""")
    CHARG = Column('CHARG', String(10), primary_key = True, doc="""Sourced from MCHA-CHARG // Batch Number""")
    LVORM = Column('LVORM', Boolean, default=None, doc="""Sourced from MCHA-LVORM // Deletion Flag for All Data on a Batch at a Plant""")
    ERSDA = Column('ERSDA', Date, default=None, doc="""Sourced from MCHA-ERSDA // Created On""")
    ERNAM = Column('ERNAM', String(12), default=None, doc="""Sourced from MCHA-ERNAM // Name of Person who Created the Object""")
    AENAM = Column('AENAM', String(12), default=None, doc="""Sourced from MCHA-AENAM // Name of Person Who Changed Object""")
    LAEDA = Column('LAEDA', Date, default=None, doc="""Sourced from MCHA-LAEDA // Date of Last Change""")
    VERAB = Column('VERAB', Date, default=None, doc="""Sourced from MCHA-VERAB // Availability date""")
    VFDAT = Column('VFDAT', Date, default=None, doc="""Sourced from MCHA-VFDAT // Shelf Life Expiration or Best-Before Date""")
    ZUSCH = Column('ZUSCH', String(1), default=None, doc="""Sourced from MCHA-ZUSCH // Batch status key""")
    ZUSTD = Column('ZUSTD', Boolean, default=None, doc="""Sourced from MCHA-ZUSTD // Batch in Restricted-Use Stock""")
    ZAEDT = Column('ZAEDT', String(8), default=None, doc="""Sourced from MCHA-ZAEDT // Date of last status change""")
    LIFNR = Column('LIFNR', String(10), default=None, doc="""Sourced from MCHA-LIFNR // Vendor Account Number""")
    LICHA = Column('LICHA', String(15), default=None, doc="""Sourced from MCHA-LICHA // Vendor Batch Number""")
    VLCHA = Column('VLCHA', String(10), default=None, doc="""Sourced from MCHA-VLCHA // Original batch number (deactivated)""")
    VLWRK = Column('VLWRK', String(4), default=None, doc="""Sourced from MCHA-VLWRK // Original plant  (deactivated)""")
    VLMAT = Column('VLMAT', String(18), default=None, doc="""Sourced from MCHA-VLMAT // Original material    (deactivated)""")
    BWTAR = Column('BWTAR', String(10), default=None, doc="""Sourced from MCHA-BWTAR // Valuation Type""")
    CHAME = Column('CHAME', String(3), default=None, doc="""Sourced from MCHA-CHAME // Unit of issue for batch (deactivated)""")
    LWEDT = Column('LWEDT', Date, default=None, doc="""Sourced from MCHA-LWEDT // Date of last goods receipt""")
    FVDT1 = Column('FVDT1', String(8), default=None, doc="""Sourced from MCHA-FVDT1 // Date for unrestricted use""")
    FVDT2 = Column('FVDT2', String(8), default=None, doc="""Sourced from MCHA-FVDT2 // Date for unrestricted use""")
    FVDT3 = Column('FVDT3', String(8), default=None, doc="""Sourced from MCHA-FVDT3 // Date for unrestricted use""")
    FVDT4 = Column('FVDT4', String(8), default=None, doc="""Sourced from MCHA-FVDT4 // Date for unrestricted use""")
    FVDT5 = Column('FVDT5', String(8), default=None, doc="""Sourced from MCHA-FVDT5 // Date for unrestricted use""")
    FVDT6 = Column('FVDT6', String(8), default=None, doc="""Sourced from MCHA-FVDT6 // Date for unrestricted use""")
    HERKL = Column('HERKL', String(3), default=None, doc="""Sourced from MCHA-HERKL // Country of origin of the material""")
    HERKR = Column('HERKR', String(3), default=None, doc="""Sourced from MCHA-HERKR // Region of origin of material (non-preferential origin)""")
    MTVER = Column('MTVER', String(4), default=None, doc="""Sourced from MCHA-MTVER // Export/import material group""")
    QNDAT = Column('QNDAT', String(8), default=None, doc="""Sourced from MCHA-QNDAT // Next Inspection Date""")
    HSDAT = Column('HSDAT', Date, default=None, doc="""Sourced from MCHA-HSDAT // Date of Manufacture""")
    CUOBJ_BM = Column('CUOBJ_BM', String(18), default=None, doc="""Sourced from MCHA-CUOBJ_BM // Internal object no.: Batch classification""")
    DEACT_BM = Column('DEACT_BM', Boolean, default=None, doc="""Sourced from MCHA-DEACT_BM // Batch is no longer active""")
    BATCH_TYPE = Column('BATCH_TYPE', String(1), default=None, doc="""Sourced from MCHA-BATCH_TYPE // Type of Batch""")
    SGT_SCAT = Column('SGT_SCAT', String(16), default=None, doc="""Sourced from MCHA-SGT_SCAT // Stock Segment""")

    material_id = synonym('MATNR')
    deleted_ind = synonym('LVORM')
    create_dt = synonym('ERSDA')
    doc_create_user_id = synonym('ERNAM')
    update_user_id = synonym('AENAM')
    last_change_dt = synonym('LAEDA')
    availability_dt = synonym('VERAB')
    origin_country_cd = synonym('HERKL')
    origin_region_cd = synonym('HERKR')
    mfg_dt = synonym('HSDAT')
    batch_deactivated_ind = synonym('DEACT_BM')


################################################################################




################################################################################

class MaterialBatchStock(SAP_Base):
    """\
    Table sourced from: MCHB
    Description: Batch Stocks
    """

    __tablename__ = "MCHB"

    MATNR = Column('MATNR', String(18), primary_key = True, doc="""Sourced from MCHB-MATNR // Material Number""")
    WERKS = Column('WERKS', String(4), primary_key = True, doc="""Sourced from MCHB-WERKS // Plant""")
    LGORT = Column('LGORT', String(4), primary_key = True, doc="""Sourced from MCHB-LGORT // Storage Location""")
    CHARG = Column('CHARG', String(10), primary_key = True, doc="""Sourced from MCHB-CHARG // Batch Number""")
    LVORM = Column('LVORM', Boolean, default=None, doc="""Sourced from MCHB-LVORM // Deletion Flag for All Data on a Batch Stock""")
    ERSDA = Column('ERSDA', Date, default=None, doc="""Sourced from MCHB-ERSDA // Created On""")
    ERNAM = Column('ERNAM', String(12), default=None, doc="""Sourced from MCHB-ERNAM // Name of Person who Created the Object""")
    LAEDA = Column('LAEDA', Date, default=None, doc="""Sourced from MCHB-LAEDA // Date of Last Change""")
    AENAM = Column('AENAM', String(12), default=None, doc="""Sourced from MCHB-AENAM // Name of Person Who Changed Object""")
    LFGJA = Column('LFGJA', String(4), default=None, doc="""Sourced from MCHB-LFGJA // Fiscal Year of Current Period""")
    LFMON = Column('LFMON', String(2), default=None, doc="""Sourced from MCHB-LFMON // Current period (posting period)""")
    SPERC = Column('SPERC', String(1), default=None, doc="""Sourced from MCHB-SPERC // Physical Inventory Blocking Indicator""")
    CLABS = Column('CLABS', String(13), default=None, doc="""Sourced from MCHB-CLABS // Valuated Unrestricted-Use Stock""")
    CUMLM = Column('CUMLM', String(13), default=None, doc="""Sourced from MCHB-CUMLM // Stock in transfer (from one storage location to another)""")
    CINSM = Column('CINSM', String(13), default=None, doc="""Sourced from MCHB-CINSM // Stock in Quality Inspection""")
    CEINM = Column('CEINM', String(13), default=None, doc="""Sourced from MCHB-CEINM // Total Stock of All Restricted Batches""")
    CSPEM = Column('CSPEM', String(13), default=None, doc="""Sourced from MCHB-CSPEM // Blocked Stock""")
    CRETM = Column('CRETM', String(13), default=None, doc="""Sourced from MCHB-CRETM // Blocked Stock Returns""")
    CVMLA = Column('CVMLA', String(13), default=None, doc="""Sourced from MCHB-CVMLA // Valuated unrestricted-use stock in previous period""")
    CVMUM = Column('CVMUM', String(13), default=None, doc="""Sourced from MCHB-CVMUM // Stock in Transfer in Previous Period""")
    CVMIN = Column('CVMIN', String(13), default=None, doc="""Sourced from MCHB-CVMIN // Stock in Quality Inspection in Previous Period""")
    CVMEI = Column('CVMEI', String(13), default=None, doc="""Sourced from MCHB-CVMEI // Restricted-Use Stock in Previous Period""")
    CVMSP = Column('CVMSP', String(13), default=None, doc="""Sourced from MCHB-CVMSP // Blocked stock of previous period""")
    CVMRE = Column('CVMRE', String(13), default=None, doc="""Sourced from MCHB-CVMRE // Blocked Stock Returns in Previous Period""")
    KZICL = Column('KZICL', String(3), default=None, doc="""Sourced from MCHB-KZICL // Physical inventory indicator for whse stock in current year""")
    KZICQ = Column('KZICQ', String(3), default=None, doc="""Sourced from MCHB-KZICQ // Phys. inventory ind. f. stock in qual. insp. in current year""")
    KZICE = Column('KZICE', String(3), default=None, doc="""Sourced from MCHB-KZICE // Physical inventory indicator for restricted-use stock""")
    KZICS = Column('KZICS', String(3), default=None, doc="""Sourced from MCHB-KZICS // Physical inventory indicator for blocked stock""")
    KZVCL = Column('KZVCL', String(3), default=None, doc="""Sourced from MCHB-KZVCL // Physical inventory indicator for stock in previous year""")
    KZVCQ = Column('KZVCQ', String(3), default=None, doc="""Sourced from MCHB-KZVCQ // Phys. inventory ind. f. stock in qual. insp. in prev. period""")
    KZVCE = Column('KZVCE', String(3), default=None, doc="""Sourced from MCHB-KZVCE // Physical inventory ind. for restricted-use stock, prev.pd""")
    KZVCS = Column('KZVCS', String(3), default=None, doc="""Sourced from MCHB-KZVCS // Phys. inventory indicator for blocked stock in prev. period""")
    HERKL = Column('HERKL', String(3), default=None, doc="""Sourced from MCHB-HERKL // Country of origin of the material""")
    CHDLL = Column('CHDLL', String(8), default=None, doc="""Sourced from MCHB-CHDLL // Date of Last Posted Count for Unrestricted-Use Stock""")
    CHJIN = Column('CHJIN', String(4), default=None, doc="""Sourced from MCHB-CHJIN // Fiscal year of current physical inventory indicator""")
    CHRUE = Column('CHRUE', Boolean, default=None, doc="""Sourced from MCHB-CHRUE // MCHBH rec. already exists for per. before last of MCHB per.""")
    SGT_SCAT = Column('SGT_SCAT', String(16), default=None, doc="""Sourced from MCHB-SGT_SCAT // Stock Segment""")

    material_id = synonym('MATNR')
    deleted_ind = synonym('LVORM')
    create_dt = synonym('ERSDA')
    doc_create_user_id = synonym('ERNAM')
    last_change_dt = synonym('LAEDA')
    update_user_id = synonym('AENAM')
    origin_country_cd = synonym('HERKL')


################################################################################




################################################################################

class MaterialMovementHdr(SAP_Base):
    """\
    Table sourced from: MKPF
    Description: Header: Material Document
    """

    __tablename__ = "MKPF"

    MBLNR = Column('MBLNR', String(10), primary_key = True, doc="""Sourced from MKPF-MBLNR // Number of Material Document""")
    MJAHR = Column('MJAHR', String(4), primary_key = True, doc="""Sourced from MKPF-MJAHR // Material Document Year""")
    VGART = Column('VGART', String(2), default=None, doc="""Sourced from MKPF-VGART // Transaction/Event Type""")
    BLART = Column('BLART', String(2), default=None, doc="""Sourced from MKPF-BLART // Document Type""")
    BLAUM = Column('BLAUM', String(2), default=None, doc="""Sourced from MKPF-BLAUM // Document type of revaluation document""")
    BLDAT = Column('BLDAT', Date, default=None, doc="""Sourced from MKPF-BLDAT // Document Date in Document""")
    BUDAT = Column('BUDAT', Date, default=None, doc="""Sourced from MKPF-BUDAT // Posting Date in the Document""")
    CPUDT = Column('CPUDT', Date, default=None, doc="""Sourced from MKPF-CPUDT // Day On Which Accounting Document Was Entered""")
    CPUTM = Column('CPUTM', Time, default=None, doc="""Sourced from MKPF-CPUTM // Time of Entry""")
    AEDAT = Column('AEDAT', Date, default=None, doc="""Sourced from MKPF-AEDAT // Changed On""")
    USNAM = Column('USNAM', String(12), default=None, doc="""Sourced from MKPF-USNAM // User name""")
    TCODE = Column('TCODE', String(4), default=None, doc="""Sourced from MKPF-TCODE // Not More Closely Defined Area, Possibly Used for Patchlevels""")
    XBLNR = Column('XBLNR', String(16), default=None, doc="""Sourced from MKPF-XBLNR // Reference Document Number""")
    BKTXT = Column('BKTXT', String(25), default=None, doc="""Sourced from MKPF-BKTXT // Document Header Text""")
    FRATH = Column('FRATH', Numeric(15,3,3), default=None, doc="""Sourced from MKPF-FRATH // Unplanned delivery costs""")
    FRBNR = Column('FRBNR', String(16), default=None, doc="""Sourced from MKPF-FRBNR // Number of Bill of Lading at Time of Goods Receipt""")
    WEVER = Column('WEVER', String(1), default=None, doc="""Sourced from MKPF-WEVER // Version for Printing GR/GI Slip""")
    XABLN = Column('XABLN', String(10), default=None, doc="""Sourced from MKPF-XABLN // Goods Receipt/Issue Slip Number""")
    AWSYS = Column('AWSYS', String(10), default=None, doc="""Sourced from MKPF-AWSYS // Logical System""")
    BLA2D = Column('BLA2D', String(2), default=None, doc="""Sourced from MKPF-BLA2D // Doc. type for additional doc. in purchase account management""")
    TCODE2 = Column('TCODE2', String(20), default=None, doc="""Sourced from MKPF-TCODE2 // Transaction Code""")
    BFWMS = Column('BFWMS', String(1), default=None, doc="""Sourced from MKPF-BFWMS // Control posting for external WMS""")
    EXNUM = Column('EXNUM', String(10), default=None, doc="""Sourced from MKPF-EXNUM // Number of foreign trade data in MM and SD documents""")
    SPE_BUDAT_UHR = Column('SPE_BUDAT_UHR', String(6), default=None, doc="""Sourced from MKPF-SPE_BUDAT_UHR // Time of Goods Issue (Local, Relating to a Plant)""")
    SPE_BUDAT_ZONE = Column('SPE_BUDAT_ZONE', String(6), default=None, doc="""Sourced from MKPF-SPE_BUDAT_ZONE // Time Zone""")
    LE_VBELN = Column('LE_VBELN', String(10), default=None, doc="""Sourced from MKPF-LE_VBELN // Delivery""")
    SPE_LOGSYS = Column('SPE_LOGSYS', String(10), default=None, doc="""Sourced from MKPF-SPE_LOGSYS // Logical System of EWM Material Document""")
    SPE_MDNUM_EWM = Column('SPE_MDNUM_EWM', String(16), default=None, doc="""Sourced from MKPF-SPE_MDNUM_EWM // Number of Material Document in EWM""")
    GTS_CUSREF_NO = Column('GTS_CUSREF_NO', String(35), default=None, doc="""Sourced from MKPF-GTS_CUSREF_NO // Customs Reference Number for Scrapping""")
    FLS_RSTO = Column('FLS_RSTO', Boolean, default=None, doc="""Sourced from MKPF-FLS_RSTO // Store Return with Inbound and Outbound Delivery""")
    MSR_ACTIVE = Column('MSR_ACTIVE', String(1), default=None, doc="""Sourced from MKPF-MSR_ACTIVE // Advanced Returns Management Active""")
    KNUMV = Column('KNUMV', String(10), default=None, doc="""Sourced from MKPF-KNUMV // Number of the document condition""")

    material_doc_id = synonym('MBLNR')
    material_doc_year = synonym('MJAHR')
    doc_type_cd = synonym('BLART')
    doc_post_dt = synonym('BUDAT')
    acctng_doc_create_dt = synonym('CPUDT')
    acctng_doc_create_tm = synonym('CPUTM')
    update_dt = synonym('AEDAT')
    user_id = synonym('USNAM')
    doc_hdr_tdxt = synonym('BKTXT')
    unplanned_delivery_cost_qty = synonym('FRATH')
    goods_receipt_bill_of_lading_id = synonym('FRBNR')


################################################################################




################################################################################

class MaterialMovementItem(SAP_Base):
    """\
    Table sourced from: MSEG
    Description: Document Segment: Material
    """

    __tablename__ = "MSEG"

    MBLNR = Column('MBLNR', String(10), primary_key = True, doc="""Sourced from MSEG-MBLNR // Number of Material Document""")
    MJAHR = Column('MJAHR', String(4), primary_key = True, doc="""Sourced from MSEG-MJAHR // Material Document Year""")
    ZEILE = Column('ZEILE', String(4), primary_key = True, doc="""Sourced from MSEG-ZEILE // Item in Material Document""")
    LINE_ID = Column('LINE_ID', String(6), default=None, doc="""Sourced from MSEG-LINE_ID // Unique identification of document line""")
    PARENT_ID = Column('PARENT_ID', String(6), default=None, doc="""Sourced from MSEG-PARENT_ID // Identifier of immediately superior line""")
    LINE_DEPTH = Column('LINE_DEPTH', String(2), default=None, doc="""Sourced from MSEG-LINE_DEPTH // Hierarchy level of line in document""")
    MAA_URZEI = Column('MAA_URZEI', String(4), default=None, doc="""Sourced from MSEG-MAA_URZEI // Original Line for Account Assignment Item in Material Doc.""")
    BWART = Column('BWART', String(3), default=None, doc="""Sourced from MSEG-BWART // Movement Type (Inventory Management)""")
    XAUTO = Column('XAUTO', String(1), default=None, doc="""Sourced from MSEG-XAUTO // Item automatically created""")
    MATNR = Column('MATNR', String(18), default=None, doc="""Sourced from MSEG-MATNR // Material Number""")
    WERKS = Column('WERKS', String(4), default=None, doc="""Sourced from MSEG-WERKS // Plant""")
    LGORT = Column('LGORT', String(4), default=None, doc="""Sourced from MSEG-LGORT // Storage Location""")
    CHARG = Column('CHARG', String(10), default=None, doc="""Sourced from MSEG-CHARG // Batch Number""")
    INSMK = Column('INSMK', String(1), default=None, doc="""Sourced from MSEG-INSMK // Stock Type""")
    ZUSCH = Column('ZUSCH', String(1), default=None, doc="""Sourced from MSEG-ZUSCH // Batch status key""")
    ZUSTD = Column('ZUSTD', Boolean, default=None, doc="""Sourced from MSEG-ZUSTD // Batch in Restricted-Use Stock""")
    SOBKZ = Column('SOBKZ', String(1), default=None, doc="""Sourced from MSEG-SOBKZ // Special Stock Indicator""")
    LIFNR = Column('LIFNR', String(10), default=None, doc="""Sourced from MSEG-LIFNR // Vendor Account Number""")
    KUNNR = Column('KUNNR', String(10), default=None, doc="""Sourced from MSEG-KUNNR // Account Number of Customer""")
    KDAUF = Column('KDAUF', String(10), default=None, doc="""Sourced from MSEG-KDAUF // Sales Order Number""")
    KDPOS = Column('KDPOS', String(6), default=None, doc="""Sourced from MSEG-KDPOS // Item Number in Sales Order""")
    KDEIN = Column('KDEIN', String(4), default=None, doc="""Sourced from MSEG-KDEIN // Delivery Schedule for Sales Order""")
    PLPLA = Column('PLPLA', String(10), default=None, doc="""Sourced from MSEG-PLPLA // Distribution of Differences""")
    SHKZG = Column('SHKZG', String(1), default=None, doc="""Sourced from MSEG-SHKZG // Debit/Credit Indicator""")
    WAERS = Column('WAERS', String(5), default=None, doc="""Sourced from MSEG-WAERS // Currency Key""")
    DMBTR = Column('DMBTR', Numeric(15,3,3), default=None, doc="""Sourced from MSEG-DMBTR // Amount in Local Currency""")
    BNBTR = Column('BNBTR', Numeric(15,3,3), default=None, doc="""Sourced from MSEG-BNBTR // Delivery costs in local currency""")
    BUALT = Column('BUALT', Numeric(15,3,3), default=None, doc="""Sourced from MSEG-BUALT // Amount Posted in Alternative Price Control""")
    SHKUM = Column('SHKUM', String(1), default=None, doc="""Sourced from MSEG-SHKUM // Debit/credit indicator in revaluation""")
    DMBUM = Column('DMBUM', Numeric(15,3,3), default=None, doc="""Sourced from MSEG-DMBUM // Revaluation amount on back-posting to a previous period""")
    BWTAR = Column('BWTAR', String(10), default=None, doc="""Sourced from MSEG-BWTAR // Valuation Type""")
    MENGE = Column('MENGE', String(13), default=None, doc="""Sourced from MSEG-MENGE // Quantity""")
    MEINS = Column('MEINS', String(3), default=None, doc="""Sourced from MSEG-MEINS // Base Unit of Measure""")
    ERFMG = Column('ERFMG', Numeric(15,3,3), default=None, doc="""Sourced from MSEG-ERFMG // Quantity in Unit of Entry""")
    ERFME = Column('ERFME', String(3), default=None, doc="""Sourced from MSEG-ERFME // Unit of Entry""")
    BPMNG = Column('BPMNG', Numeric(15,3,3), default=None, doc="""Sourced from MSEG-BPMNG // Quantity in Purchase Order Price Unit""")
    BPRME = Column('BPRME', String(3), default=None, doc="""Sourced from MSEG-BPRME // Order Price Unit (Purchasing)""")
    EBELN = Column('EBELN', String(10), default=None, doc="""Sourced from MSEG-EBELN // Purchase Order Number""")
    EBELP = Column('EBELP', String(5), default=None, doc="""Sourced from MSEG-EBELP // Item Number of Purchasing Document""")
    LFBJA = Column('LFBJA', String(4), default=None, doc="""Sourced from MSEG-LFBJA // Fiscal Year of a Reference Document""")
    LFBNR = Column('LFBNR', String(10), default=None, doc="""Sourced from MSEG-LFBNR // Document No. of a Reference Document""")
    LFPOS = Column('LFPOS', String(4), default=None, doc="""Sourced from MSEG-LFPOS // Item of a Reference Document""")
    SJAHR = Column('SJAHR', String(4), default=None, doc="""Sourced from MSEG-SJAHR // Material Document Year""")
    SMBLN = Column('SMBLN', String(10), default=None, doc="""Sourced from MSEG-SMBLN // Number of Material Document""")
    SMBLP = Column('SMBLP', String(4), default=None, doc="""Sourced from MSEG-SMBLP // Item in Material Document""")
    ELIKZ = Column('ELIKZ', Boolean, default=None, doc="""Sourced from MSEG-ELIKZ // 'Delivery Completed' Indicator""")
    SGTXT = Column('SGTXT', String(50), default=None, doc="""Sourced from MSEG-SGTXT // Item Text""")
    EQUNR = Column('EQUNR', String(18), default=None, doc="""Sourced from MSEG-EQUNR // Equipment Number""")
    WEMPF = Column('WEMPF', String(12), default=None, doc="""Sourced from MSEG-WEMPF // Goods Recipient/Ship-To Party""")
    ABLAD = Column('ABLAD', String(25), default=None, doc="""Sourced from MSEG-ABLAD // Unloading Point""")
    GSBER = Column('GSBER', String(4), default=None, doc="""Sourced from MSEG-GSBER // Business Area""")
    KOKRS = Column('KOKRS', String(4), default=None, doc="""Sourced from MSEG-KOKRS // Controlling Area""")
    PARGB = Column('PARGB', String(4), default=None, doc="""Sourced from MSEG-PARGB // Trading Partner's Business Area""")
    PARBU = Column('PARBU', String(4), default=None, doc="""Sourced from MSEG-PARBU // Clearing company code""")
    KOSTL = Column('KOSTL', String(10), default=None, doc="""Sourced from MSEG-KOSTL // Cost Center""")
    PROJN = Column('PROJN', String(16), default=None, doc="""Sourced from MSEG-PROJN // Old: Project number : No longer used --> PS_POSNR""")
    AUFNR = Column('AUFNR', String(12), default=None, doc="""Sourced from MSEG-AUFNR // Order Number""")
    ANLN1 = Column('ANLN1', String(12), default=None, doc="""Sourced from MSEG-ANLN1 // Main Asset Number""")
    ANLN2 = Column('ANLN2', String(4), default=None, doc="""Sourced from MSEG-ANLN2 // Asset Subnumber""")
    XSKST = Column('XSKST', Boolean, default=None, doc="""Sourced from MSEG-XSKST // Indicator: Statistical Posting to Cost Center""")
    XSAUF = Column('XSAUF', Boolean, default=None, doc="""Sourced from MSEG-XSAUF // Indicator: Posting to Order Is Statistical""")
    XSPRO = Column('XSPRO', Boolean, default=None, doc="""Sourced from MSEG-XSPRO // Indicator: Posting to Project Is Statistical""")
    XSERG = Column('XSERG', Boolean, default=None, doc="""Sourced from MSEG-XSERG // Indicator: Posting to Profitability Analysis Is Statistical""")
    GJAHR = Column('GJAHR', String(4), default=None, doc="""Sourced from MSEG-GJAHR // Fiscal Year""")
    XRUEM = Column('XRUEM', Boolean, default=None, doc="""Sourced from MSEG-XRUEM // Allow Posting to Previous Period (Backposting)""")
    XRUEJ = Column('XRUEJ', Boolean, default=None, doc="""Sourced from MSEG-XRUEJ // Indicator: post to previous year""")
    BUKRS = Column('BUKRS', String(4), default=None, doc="""Sourced from MSEG-BUKRS // Company Code""")
    BELNR = Column('BELNR', String(10), default=None, doc="""Sourced from MSEG-BELNR // Accounting Document Number""")
    BUZEI = Column('BUZEI', String(3), default=None, doc="""Sourced from MSEG-BUZEI // Number of Line Item Within Accounting Document""")
    BELUM = Column('BELUM', String(10), default=None, doc="""Sourced from MSEG-BELUM // Accounting Document Number""")
    BUZUM = Column('BUZUM', String(3), default=None, doc="""Sourced from MSEG-BUZUM // Number of Line Item Within Accounting Document""")
    RSNUM = Column('RSNUM', String(10), default=None, doc="""Sourced from MSEG-RSNUM // Number of Reservation/Dependent Requirement""")
    RSPOS = Column('RSPOS', String(4), default=None, doc="""Sourced from MSEG-RSPOS // Item Number of Reservation/Dependent Requirement""")
    KZEAR = Column('KZEAR', Boolean, default=None, doc="""Sourced from MSEG-KZEAR // Final Issue for This Reservation""")
    PBAMG = Column('PBAMG', String(13), default=None, doc="""Sourced from MSEG-PBAMG // Quantity""")
    KZSTR = Column('KZSTR', String(1), default=None, doc="""Sourced from MSEG-KZSTR // Transaction/event is relevant to statistics""")
    UMMAT = Column('UMMAT', String(18), default=None, doc="""Sourced from MSEG-UMMAT // Receiving/Issuing Material""")
    UMWRK = Column('UMWRK', String(4), default=None, doc="""Sourced from MSEG-UMWRK // Receiving/Issuing Plant""")
    UMLGO = Column('UMLGO', String(4), default=None, doc="""Sourced from MSEG-UMLGO // Receiving/Issuing Storage Location""")
    UMCHA = Column('UMCHA', String(10), default=None, doc="""Sourced from MSEG-UMCHA // Receiving/Issuing Batch""")
    UMZST = Column('UMZST', String(1), default=None, doc="""Sourced from MSEG-UMZST // Status of Transfer Batch""")
    UMZUS = Column('UMZUS', String(1), default=None, doc="""Sourced from MSEG-UMZUS // Status key of transfer batch""")
    UMBAR = Column('UMBAR', String(10), default=None, doc="""Sourced from MSEG-UMBAR // Valuation Type of Transfer Batch""")
    UMSOK = Column('UMSOK', String(1), default=None, doc="""Sourced from MSEG-UMSOK // Special Stock Indicator for Physical Stock Transfer""")
    KZBEW = Column('KZBEW', String(1), default=None, doc="""Sourced from MSEG-KZBEW // Movement Indicator""")
    KZVBR = Column('KZVBR', String(1), default=None, doc="""Sourced from MSEG-KZVBR // Consumption Posting""")
    KZZUG = Column('KZZUG', String(1), default=None, doc="""Sourced from MSEG-KZZUG // Receipt Indicator""")
    WEUNB = Column('WEUNB', Boolean, default=None, doc="""Sourced from MSEG-WEUNB // Goods Receipt, Non-Valuated""")
    PALAN = Column('PALAN', Numeric(15,3,3), default=None, doc="""Sourced from MSEG-PALAN // WMS Number of pallets""")
    LGNUM = Column('LGNUM', String(3), default=None, doc="""Sourced from MSEG-LGNUM // Warehouse Number / Warehouse Complex""")
    LGTYP = Column('LGTYP', String(3), default=None, doc="""Sourced from MSEG-LGTYP // Storage Type""")
    LGPLA = Column('LGPLA', String(10), default=None, doc="""Sourced from MSEG-LGPLA // Storage Bin""")
    BESTQ = Column('BESTQ', String(1), default=None, doc="""Sourced from MSEG-BESTQ // Stock Category in the Warehouse Management System""")
    BWLVS = Column('BWLVS', String(3), default=None, doc="""Sourced from MSEG-BWLVS // Movement Type for Warehouse Management""")
    TBNUM = Column('TBNUM', String(10), default=None, doc="""Sourced from MSEG-TBNUM // Transfer Requirement Number""")
    TBPOS = Column('TBPOS', String(4), default=None, doc="""Sourced from MSEG-TBPOS // Transfer Requirement Item""")
    XBLVS = Column('XBLVS', Boolean, default=None, doc="""Sourced from MSEG-XBLVS // Indicator: posting in warehouse management system""")
    VSCHN = Column('VSCHN', Boolean, default=None, doc="""Sourced from MSEG-VSCHN // Ind: interim storage posting for source stor.type and bin""")
    NSCHN = Column('NSCHN', Boolean, default=None, doc="""Sourced from MSEG-NSCHN // Ind.: interim storage posting for dest.stor.type and bin""")
    DYPLA = Column('DYPLA', Boolean, default=None, doc="""Sourced from MSEG-DYPLA // Indicator: dynamic storage bin""")
    UBNUM = Column('UBNUM', String(10), default=None, doc="""Sourced from MSEG-UBNUM // Posting Change Number""")
    TBPRI = Column('TBPRI', String(1), default=None, doc="""Sourced from MSEG-TBPRI // Transfer Priority""")
    TANUM = Column('TANUM', String(10), default=None, doc="""Sourced from MSEG-TANUM // Transfer Order Number""")
    WEANZ = Column('WEANZ', String(3), default=None, doc="""Sourced from MSEG-WEANZ // Number of GR/GI Slips to Be Printed""")
    GRUND = Column('GRUND', String(4), default=None, doc="""Sourced from MSEG-GRUND // Reason for Movement""")
    EVERS = Column('EVERS', String(2), default=None, doc="""Sourced from MSEG-EVERS // Shipping Instructions""")
    EVERE = Column('EVERE', String(2), default=None, doc="""Sourced from MSEG-EVERE // Compliance with Shipping Instructions""")
    IMKEY = Column('IMKEY', String(8), default=None, doc="""Sourced from MSEG-IMKEY // Internal Key for Real Estate Object""")
    KSTRG = Column('KSTRG', String(12), default=None, doc="""Sourced from MSEG-KSTRG // Cost Object""")
    PAOBJNR = Column('PAOBJNR', String(10), default=None, doc="""Sourced from MSEG-PAOBJNR // Profitability Segment Number (CO-PA)""")
    PRCTR = Column('PRCTR', String(10), default=None, doc="""Sourced from MSEG-PRCTR // Profit Center""")
    PS_PSP_PNR = Column('PS_PSP_PNR', String(8), default=None, doc="""Sourced from MSEG-PS_PSP_PNR // Work Breakdown Structure Element (WBS Element)""")
    NPLNR = Column('NPLNR', String(12), default=None, doc="""Sourced from MSEG-NPLNR // Network Number for Account Assignment""")
    AUFPL = Column('AUFPL', String(10), default=None, doc="""Sourced from MSEG-AUFPL // Routing number of operations in the order""")
    APLZL = Column('APLZL', String(8), default=None, doc="""Sourced from MSEG-APLZL // Internal counter""")
    AUFPS = Column('AUFPS', String(4), default=None, doc="""Sourced from MSEG-AUFPS // Order Item Number""")
    VPTNR = Column('VPTNR', String(10), default=None, doc="""Sourced from MSEG-VPTNR // Partner Account Number""")
    FIPOS = Column('FIPOS', String(14), default=None, doc="""Sourced from MSEG-FIPOS // Commitment Item""")
    SAKTO = Column('SAKTO', String(10), default=None, doc="""Sourced from MSEG-SAKTO // G/L Account Number""")
    BSTMG = Column('BSTMG', Numeric(15,3,3), default=None, doc="""Sourced from MSEG-BSTMG // Goods receipt quantity in order unit""")
    BSTME = Column('BSTME', String(3), default=None, doc="""Sourced from MSEG-BSTME // Purchase Order Unit of Measure""")
    XWSBR = Column('XWSBR', Boolean, default=None, doc="""Sourced from MSEG-XWSBR // Reversal of GR allowed for GR-based IV despite invoice""")
    EMLIF = Column('EMLIF', String(10), default=None, doc="""Sourced from MSEG-EMLIF // Vendor to be supplied/who is to receive delivery""")
    EXBWR = Column('EXBWR', Numeric(15,3,3), default=None, doc="""Sourced from MSEG-EXBWR // Externally Entered Posting Amount in Local Currency""")
    VKWRT = Column('VKWRT', Numeric(15,3,3), default=None, doc="""Sourced from MSEG-VKWRT // Value at Sales Prices Including Value-Added Tax""")
    AKTNR = Column('AKTNR', String(10), default=None, doc="""Sourced from MSEG-AKTNR // Promotion""")
    ZEKKN = Column('ZEKKN', String(2), default=None, doc="""Sourced from MSEG-ZEKKN // Sequential Number of Account Assignment""")
    VFDAT = Column('VFDAT', Date, default=None, doc="""Sourced from MSEG-VFDAT // Shelf Life Expiration or Best-Before Date""")
    CUOBJ_CH = Column('CUOBJ_CH', String(18), default=None, doc="""Sourced from MSEG-CUOBJ_CH // Internal object number of the batch classification""")
    EXVKW = Column('EXVKW', Numeric(15,3,3), default=None, doc="""Sourced from MSEG-EXVKW // Externally Entered Sales Value in Local Currency""")
    PPRCTR = Column('PPRCTR', String(10), default=None, doc="""Sourced from MSEG-PPRCTR // Partner Profit Center""")
    RSART = Column('RSART', String(1), default=None, doc="""Sourced from MSEG-RSART // Record type""")
    GEBER = Column('GEBER', String(10), default=None, doc="""Sourced from MSEG-GEBER // Fund""")
    FISTL = Column('FISTL', String(16), default=None, doc="""Sourced from MSEG-FISTL // Funds Center""")
    MATBF = Column('MATBF', String(18), default=None, doc="""Sourced from MSEG-MATBF // Material in Respect of Which Stock is Managed""")
    UMMAB = Column('UMMAB', String(18), default=None, doc="""Sourced from MSEG-UMMAB // Receiving/Issuing Material""")
    BUSTM = Column('BUSTM', String(4), default=None, doc="""Sourced from MSEG-BUSTM // Posting string for quantities""")
    BUSTW = Column('BUSTW', String(4), default=None, doc="""Sourced from MSEG-BUSTW // Posting String for Values""")
    MENGU = Column('MENGU', Boolean, default=None, doc="""Sourced from MSEG-MENGU // Quantity Updating in Material Master Record""")
    WERTU = Column('WERTU', Boolean, default=None, doc="""Sourced from MSEG-WERTU // Value Update in Material Master Record""")
    LBKUM = Column('LBKUM', Numeric(15,3,3), default=None, doc="""Sourced from MSEG-LBKUM // Total valuated stock before the posting""")
    SALK3 = Column('SALK3', Numeric(15,3,3), default=None, doc="""Sourced from MSEG-SALK3 // Value of total valuated stock before the posting""")
    VPRSV = Column('VPRSV', String(1), default=None, doc="""Sourced from MSEG-VPRSV // Price Control Indicator""")
    FKBER = Column('FKBER', String(16), default=None, doc="""Sourced from MSEG-FKBER // Functional Area""")
    DABRBZ = Column('DABRBZ', String(8), default=None, doc="""Sourced from MSEG-DABRBZ // Reference Date for Settlement""")
    VKWRA = Column('VKWRA', Numeric(15,3,3), default=None, doc="""Sourced from MSEG-VKWRA // Value at sales prices excluding value-added tax""")
    DABRZ = Column('DABRZ', String(8), default=None, doc="""Sourced from MSEG-DABRZ // Reference Date for Settlement""")
    XBEAU = Column('XBEAU', Boolean, default=None, doc="""Sourced from MSEG-XBEAU // Purchase order created at time of goods receipt""")
    LSMNG = Column('LSMNG', Numeric(15,3,3), default=None, doc="""Sourced from MSEG-LSMNG // Quantity in Unit of Measure from Delivery Note""")
    LSMEH = Column('LSMEH', String(3), default=None, doc="""Sourced from MSEG-LSMEH // Unit of Measure From Delivery Note""")
    KZBWS = Column('KZBWS', String(1), default=None, doc="""Sourced from MSEG-KZBWS // Valuation of Special Stock""")
    QINSPST = Column('QINSPST', String(1), default=None, doc="""Sourced from MSEG-QINSPST // Status of Goods Receipt Inspection""")
    URZEI = Column('URZEI', String(4), default=None, doc="""Sourced from MSEG-URZEI // Original line in material document""")
    J_1BEXBASE = Column('J_1BEXBASE', Numeric(15,3,3), default=None, doc="""Sourced from MSEG-J_1BEXBASE // Alternate base amount in document currency""")
    MWSKZ = Column('MWSKZ', String(2), default=None, doc="""Sourced from MSEG-MWSKZ // Tax on sales/purchases code""")
    TXJCD = Column('TXJCD', String(15), default=None, doc="""Sourced from MSEG-TXJCD // Tax Jurisdiction""")
    EMATN = Column('EMATN', String(18), default=None, doc="""Sourced from MSEG-EMATN // Material Number Corresponding to Manufacturer Part Number""")
    J_1AGIRUPD = Column('J_1AGIRUPD', String(1), default=None, doc="""Sourced from MSEG-J_1AGIRUPD // Goods issue revaluation performed""")
    VKMWS = Column('VKMWS', String(2), default=None, doc="""Sourced from MSEG-VKMWS // Tax on sales/purchases code""")
    HSDAT = Column('HSDAT', Date, default=None, doc="""Sourced from MSEG-HSDAT // Date of Manufacture""")
    BERKZ = Column('BERKZ', String(1), default=None, doc="""Sourced from MSEG-BERKZ // Material Staging Indicator for Production Supply""")
    MAT_KDAUF = Column('MAT_KDAUF', String(10), default=None, doc="""Sourced from MSEG-MAT_KDAUF // Sales Order Number of Valuated Sales Order Stock""")
    MAT_KDPOS = Column('MAT_KDPOS', String(6), default=None, doc="""Sourced from MSEG-MAT_KDPOS // Sales Order Item of Valuated Sales Order Stock""")
    MAT_PSPNR = Column('MAT_PSPNR', String(8), default=None, doc="""Sourced from MSEG-MAT_PSPNR // Valuated Sales Order Stock WBS Element""")
    XWOFF = Column('XWOFF', Boolean, default=None, doc="""Sourced from MSEG-XWOFF // Calculation of val. open""")
    BEMOT = Column('BEMOT', String(2), default=None, doc="""Sourced from MSEG-BEMOT // Accounting Indicator""")
    PRZNR = Column('PRZNR', String(12), default=None, doc="""Sourced from MSEG-PRZNR // Business Process""")
    LLIEF = Column('LLIEF', String(10), default=None, doc="""Sourced from MSEG-LLIEF // Supplying Vendor""")
    LSTAR = Column('LSTAR', String(6), default=None, doc="""Sourced from MSEG-LSTAR // Activity Type""")
    XOBEW = Column('XOBEW', Boolean, default=None, doc="""Sourced from MSEG-XOBEW // Vendor Stock Valuation Indicator""")
    GRANT_NBR = Column('GRANT_NBR', String(20), default=None, doc="""Sourced from MSEG-GRANT_NBR // Grant""")
    ZUSTD_T156M = Column('ZUSTD_T156M', String(1), default=None, doc="""Sourced from MSEG-ZUSTD_T156M // Stock Type Modification (Read from Table T156M)""")
    SPE_GTS_STOCK_TY = Column('SPE_GTS_STOCK_TY', String(1), default=None, doc="""Sourced from MSEG-SPE_GTS_STOCK_TY // GTS Stock Type""")
    KBLNR = Column('KBLNR', String(10), default=None, doc="""Sourced from MSEG-KBLNR // Document Number for Earmarked Funds""")
    KBLPOS = Column('KBLPOS', String(3), default=None, doc="""Sourced from MSEG-KBLPOS // Earmarked Funds: Document Item""")
    XMACC = Column('XMACC', String(1), default=None, doc="""Sourced from MSEG-XMACC // Multiple Account Assignment""")
    VGART_MKPF = Column('VGART_MKPF', String(2), default=None, doc="""Sourced from MSEG-VGART_MKPF // Transaction/Event Type""")
    BUDAT_MKPF = Column('BUDAT_MKPF', String(8), default=None, doc="""Sourced from MSEG-BUDAT_MKPF // Posting Date in the Document""")
    CPUDT_MKPF = Column('CPUDT_MKPF', String(8), default=None, doc="""Sourced from MSEG-CPUDT_MKPF // Day On Which Accounting Document Was Entered""")
    CPUTM_MKPF = Column('CPUTM_MKPF', String(6), default=None, doc="""Sourced from MSEG-CPUTM_MKPF // Time of Entry""")
    USNAM_MKPF = Column('USNAM_MKPF', String(12), default=None, doc="""Sourced from MSEG-USNAM_MKPF // User name""")
    XBLNR_MKPF = Column('XBLNR_MKPF', String(16), default=None, doc="""Sourced from MSEG-XBLNR_MKPF // Reference Document Number""")
    TCODE2_MKPF = Column('TCODE2_MKPF', String(20), default=None, doc="""Sourced from MSEG-TCODE2_MKPF // Transaction Code""")
    VBELN_IM = Column('VBELN_IM', String(10), default=None, doc="""Sourced from MSEG-VBELN_IM // Delivery""")
    VBELP_IM = Column('VBELP_IM', String(6), default=None, doc="""Sourced from MSEG-VBELP_IM // Delivery Item""")
    SGT_SCAT = Column('SGT_SCAT', String(16), default=None, doc="""Sourced from MSEG-SGT_SCAT // Stock Segment""")
    SGT_UMSCAT = Column('SGT_UMSCAT', String(16), default=None, doc="""Sourced from MSEG-SGT_UMSCAT // Receiving/Issuing Stock Segment""")
    _DATAAGING = Column('_DATAAGING', String(8), default=None, doc="""Sourced from MSEG-_DATAAGING // Data Filter Value for Data Aging""")
    SGT_RCAT = Column('SGT_RCAT', String(16), default=None, doc="""Sourced from MSEG-SGT_RCAT // Requirement Segment""")
    OINAVNW = Column('OINAVNW', String(13), default=None, doc="""Sourced from MSEG-OINAVNW // Non-deductible input tax""")
    OICONDCOD = Column('OICONDCOD', String(2), default=None, doc="""Sourced from MSEG-OICONDCOD // Joint Venture Indicator (Condition Key)""")
    CONDI = Column('CONDI', String(2), default=None, doc="""Sourced from MSEG-CONDI // Joint Venture Indicator (Condition Key)""")

    material_doc_id = synonym('MBLNR')
    material_doc_year = synonym('MJAHR')
    im_matl_mvmnt_type_cd = synonym('BWART')
    material_id = synonym('MATNR')
    stock_type_cd = synonym('INSMK')
    special_stock_cd = synonym('SOBKZ')
    customer_id = synonym('KUNNR')
    sales_order_id = synonym('KDAUF')
    sales_order_item_id = synonym('KDPOS')
    sales_order_delivery_schd_id = synonym('KDEIN')
    currency_cd = synonym('WAERS')
    deliv_cost_qty = synonym('BNBTR')
    uom_cd = synonym('MEINS')
    entry_uom_qty = synonym('ERFMG')
    entry_uom_cd = synonym('ERFME')
    prch_ord_price_unit_qty = synonym('BPMNG')
    prch_order_price_uom_cd = synonym('BPRME')
    prch_doc_id = synonym('EBELN')
    prch_doc_item_id = synonym('EBELP')
    ref_doc_fiscal_year = synonym('LFBJA')
    ref_doc_id = synonym('LFBNR')
    ref_doc_item_id = synonym('LFPOS')
    delivery_complete_ind = synonym('ELIKZ')
    item_desc = synonym('SGTXT')
    unloading_point = synonym('ABLAD')
    cost_center_id = synonym('KOSTL')
    order_id = synonym('AUFNR')
    fiscal_year = synonym('GJAHR')
    company_cd = synonym('BUKRS')
    movement_cd = synonym('KZBEW')
    warehouse_nbr = synonym('LGNUM')
    storage_type_id = synonym('LGTYP')
    wm_stk_ctgy_cd = synonym('BESTQ')
    wm_matl_mvmnt_type_cd = synonym('BWLVS')
    dynamic_storage_bin_ind = synonym('DYPLA')
    order_item_id = synonym('AUFPS')
    prch_ord_qty = synonym('BSTMG')
    prch_ord_uom_cd = synonym('BSTME')
    receiving_vendor_id = synonym('EMLIF')
    total_valuated_stock_qty = synonym('LBKUM')
    delivery_note_uom_qty = synonym('LSMNG')
    special_stock_valuation_Cd = synonym('KZBWS')
    matl_doc_original_item_id = synonym('URZEI')
    mfg_part_nbr_matl_id = synonym('EMATN')
    mfg_dt = synonym('HSDAT')


################################################################################




################################################################################

class SalesOrderStock(SAP_Base):
    """\
    Table sourced from: MSKA
    Description: Sales Order Stock
    """

    __tablename__ = "MSKA"

    MATNR = Column('MATNR', String(18), primary_key = True, doc="""Sourced from MSKA-MATNR // Material Number""")
    WERKS = Column('WERKS', String(4), primary_key = True, doc="""Sourced from MSKA-WERKS // Plant""")
    LGORT = Column('LGORT', String(4), primary_key = True, doc="""Sourced from MSKA-LGORT // Storage Location""")
    CHARG = Column('CHARG', String(10), primary_key = True, doc="""Sourced from MSKA-CHARG // Batch Number""")
    SOBKZ = Column('SOBKZ', String(1), primary_key = True, doc="""Sourced from MSKA-SOBKZ // Special Stock Indicator""")
    VBELN = Column('VBELN', String(10), primary_key = True, doc="""Sourced from MSKA-VBELN // Sales and Distribution Document Number""")
    POSNR = Column('POSNR', String(6), primary_key = True, doc="""Sourced from MSKA-POSNR // Item number of the SD document""")
    LFGJA = Column('LFGJA', String(4), default=None, doc="""Sourced from MSKA-LFGJA // Fiscal Year of Current Period""")
    LFMON = Column('LFMON', String(2), default=None, doc="""Sourced from MSKA-LFMON // Current period (posting period)""")
    KASPR = Column('KASPR', String(1), default=None, doc="""Sourced from MSKA-KASPR // Physical Inventory Blocking Indicator""")
    KALAB = Column('KALAB', String(13), default=None, doc="""Sourced from MSKA-KALAB // Valuated Unrestricted-Use Stock""")
    KAINS = Column('KAINS', String(13), default=None, doc="""Sourced from MSKA-KAINS // Stock in Quality Inspection""")
    KASPE = Column('KASPE', String(13), default=None, doc="""Sourced from MSKA-KASPE // Blocked Stock""")
    KAVLA = Column('KAVLA', String(13), default=None, doc="""Sourced from MSKA-KAVLA // Valuated unrestricted-use stock in previous period""")
    KAVIN = Column('KAVIN', String(13), default=None, doc="""Sourced from MSKA-KAVIN // Stock in Quality Inspection in Previous Period""")
    KAVSP = Column('KAVSP', String(13), default=None, doc="""Sourced from MSKA-KAVSP // Blocked stock of previous period""")
    KAILL = Column('KAILL', String(3), default=None, doc="""Sourced from MSKA-KAILL // Physical inventory indicator for whse stock in current year""")
    KAILQ = Column('KAILQ', String(3), default=None, doc="""Sourced from MSKA-KAILQ // Phys. inventory ind. f. stock in qual. insp. in current year""")
    KAILS = Column('KAILS', String(3), default=None, doc="""Sourced from MSKA-KAILS // Physical inventory indicator for blocked stock""")
    KAVLL = Column('KAVLL', String(3), default=None, doc="""Sourced from MSKA-KAVLL // Physical inventory indicator for stock in previous year""")
    KAVLQ = Column('KAVLQ', String(3), default=None, doc="""Sourced from MSKA-KAVLQ // Phys. inventory ind. f. stock in qual. insp. in prev. period""")
    KAVLS = Column('KAVLS', String(3), default=None, doc="""Sourced from MSKA-KAVLS // Phys. inventory indicator for blocked stock in prev. period""")
    KAFLL = Column('KAFLL', String(3), default=None, doc="""Sourced from MSKA-KAFLL // Physical inventory indicator for stock in following year""")
    KAFLQ = Column('KAFLQ', String(3), default=None, doc="""Sourced from MSKA-KAFLQ // Physical inventory indicator, quality insp.stck, follow.yr.""")
    KAFLS = Column('KAFLS', String(3), default=None, doc="""Sourced from MSKA-KAFLS // Phys. inventory ind. for blocked stock in following period""")
    KADLL = Column('KADLL', String(8), default=None, doc="""Sourced from MSKA-KADLL // Date of Last Posted Count for Unrestricted-Use Stock""")
    KAEIN = Column('KAEIN', String(13), default=None, doc="""Sourced from MSKA-KAEIN // Total Stock of All Restricted Batches""")
    KAVEI = Column('KAVEI', String(13), default=None, doc="""Sourced from MSKA-KAVEI // Restricted-Use Stock in Previous Period""")
    ERSDA = Column('ERSDA', Date, default=None, doc="""Sourced from MSKA-ERSDA // Created On""")
    KAJIN = Column('KAJIN', String(4), default=None, doc="""Sourced from MSKA-KAJIN // Fiscal year of current physical inventory indicator""")
    KARUE = Column('KARUE', Boolean, default=None, doc="""Sourced from MSKA-KARUE // MxxxH rec. already exists for per. before last of Mxxx per.""")
    SGT_SCAT = Column('SGT_SCAT', String(16), default=None, doc="""Sourced from MSKA-SGT_SCAT // Stock Segment""")

    material_id = synonym('MATNR')
    special_stock_cd = synonym('SOBKZ')
    sd_doc_id = synonym('VBELN')
    sd_doc_item_id = synonym('POSNR')
    create_dt = synonym('ERSDA')


################################################################################




################################################################################

class SpecialVendorStock(SAP_Base):
    """\
    Table sourced from: MSLB
    Description: Special Stocks with Vendor
    """

    __tablename__ = "MSLB"

    MATNR = Column('MATNR', String(18), primary_key = True, doc="""Sourced from MSLB-MATNR // Material Number""")
    WERKS = Column('WERKS', String(4), primary_key = True, doc="""Sourced from MSLB-WERKS // Plant""")
    CHARG = Column('CHARG', String(10), primary_key = True, doc="""Sourced from MSLB-CHARG // Batch Number""")
    SOBKZ = Column('SOBKZ', String(1), primary_key = True, doc="""Sourced from MSLB-SOBKZ // Special Stock Indicator""")
    LIFNR = Column('LIFNR', String(10), primary_key = True, doc="""Sourced from MSLB-LIFNR // Account Number of Vendor or Creditor""")
    LFGJA = Column('LFGJA', String(4), default=None, doc="""Sourced from MSLB-LFGJA // Fiscal Year of Current Period""")
    LFMON = Column('LFMON', String(2), default=None, doc="""Sourced from MSLB-LFMON // Current period (posting period)""")
    LBSPR = Column('LBSPR', String(1), default=None, doc="""Sourced from MSLB-LBSPR // Physical Inventory Blocking Indicator""")
    LBLAB = Column('LBLAB', String(13), default=None, doc="""Sourced from MSLB-LBLAB // Valuated Unrestricted-Use Stock""")
    LBINS = Column('LBINS', String(13), default=None, doc="""Sourced from MSLB-LBINS // Stock in Quality Inspection""")
    LBVLA = Column('LBVLA', String(13), default=None, doc="""Sourced from MSLB-LBVLA // Valuated unrestricted-use stock in previous period""")
    LBVIN = Column('LBVIN', String(13), default=None, doc="""Sourced from MSLB-LBVIN // Stock in Quality Inspection in Previous Period""")
    LBILL = Column('LBILL', String(3), default=None, doc="""Sourced from MSLB-LBILL // Physical inventory indicator for whse stock in current year""")
    LBILQ = Column('LBILQ', String(3), default=None, doc="""Sourced from MSLB-LBILQ // Phys. inventory ind. f. stock in qual. insp. in current year""")
    LBVLL = Column('LBVLL', String(3), default=None, doc="""Sourced from MSLB-LBVLL // Physical inventory indicator for stock in previous year""")
    LBVLQ = Column('LBVLQ', String(3), default=None, doc="""Sourced from MSLB-LBVLQ // Phys. inventory ind. f. stock in qual. insp. in prev. period""")
    LBFLL = Column('LBFLL', String(3), default=None, doc="""Sourced from MSLB-LBFLL // Physical inventory indicator for stock in following year""")
    LBFLQ = Column('LBFLQ', String(3), default=None, doc="""Sourced from MSLB-LBFLQ // Physical inventory indicator, quality insp.stck, follow.yr.""")
    LBDLL = Column('LBDLL', String(8), default=None, doc="""Sourced from MSLB-LBDLL // Date of Last Posted Count for Unrestricted-Use Stock""")
    LBEIN = Column('LBEIN', String(13), default=None, doc="""Sourced from MSLB-LBEIN // Total Stock of All Restricted Batches""")
    LBVEI = Column('LBVEI', String(13), default=None, doc="""Sourced from MSLB-LBVEI // Restricted-Use Stock in Previous Period""")
    ERSDA = Column('ERSDA', Date, default=None, doc="""Sourced from MSLB-ERSDA // Created On""")
    LBJIN = Column('LBJIN', String(4), default=None, doc="""Sourced from MSLB-LBJIN // Fiscal year of current physical inventory indicator""")
    LBRUE = Column('LBRUE', Boolean, default=None, doc="""Sourced from MSLB-LBRUE // MxxxH rec. already exists for per. before last of Mxxx per.""")
    LBUML = Column('LBUML', String(13), default=None, doc="""Sourced from MSLB-LBUML // Stock in Transfer for Subcontracting (Plant to Plant)""")

    material_id = synonym('MATNR')
    special_stock_cd = synonym('SOBKZ')
    create_dt = synonym('ERSDA')


################################################################################




################################################################################

class ProjectStock(SAP_Base):
    """\
    Table sourced from: MSPR
    Description: Project Stock
    """

    __tablename__ = "MSPR"

    MATNR = Column('MATNR', String(18), primary_key = True, doc="""Sourced from MSPR-MATNR // Material Number""")
    WERKS = Column('WERKS', String(4), primary_key = True, doc="""Sourced from MSPR-WERKS // Plant""")
    LGORT = Column('LGORT', String(4), primary_key = True, doc="""Sourced from MSPR-LGORT // Storage Location""")
    CHARG = Column('CHARG', String(10), primary_key = True, doc="""Sourced from MSPR-CHARG // Batch Number""")
    SOBKZ = Column('SOBKZ', String(1), primary_key = True, doc="""Sourced from MSPR-SOBKZ // Special Stock Indicator""")
    PSPNR = Column('PSPNR', String(8), primary_key = True, doc="""Sourced from MSPR-PSPNR // Work Breakdown Structure Element (WBS Element)""")
    LFGJA = Column('LFGJA', String(4), default=None, doc="""Sourced from MSPR-LFGJA // Fiscal Year of Current Period""")
    LFMON = Column('LFMON', String(2), default=None, doc="""Sourced from MSPR-LFMON // Current period (posting period)""")
    PRSPR = Column('PRSPR', String(1), default=None, doc="""Sourced from MSPR-PRSPR // Physical Inventory Blocking Indicator""")
    PRLAB = Column('PRLAB', String(13), default=None, doc="""Sourced from MSPR-PRLAB // Valuated Unrestricted-Use Stock""")
    PRINS = Column('PRINS', String(13), default=None, doc="""Sourced from MSPR-PRINS // Stock in Quality Inspection""")
    PRSPE = Column('PRSPE', String(13), default=None, doc="""Sourced from MSPR-PRSPE // Blocked Stock""")
    PRVLA = Column('PRVLA', String(13), default=None, doc="""Sourced from MSPR-PRVLA // Valuated unrestricted-use stock in previous period""")
    PRVIN = Column('PRVIN', String(13), default=None, doc="""Sourced from MSPR-PRVIN // Stock in Quality Inspection in Previous Period""")
    PRVSP = Column('PRVSP', String(13), default=None, doc="""Sourced from MSPR-PRVSP // Blocked stock of previous period""")
    PRILL = Column('PRILL', String(3), default=None, doc="""Sourced from MSPR-PRILL // Physical inventory indicator for whse stock in current year""")
    PRILQ = Column('PRILQ', String(3), default=None, doc="""Sourced from MSPR-PRILQ // Phys. inventory ind. f. stock in qual. insp. in current year""")
    PRILS = Column('PRILS', String(3), default=None, doc="""Sourced from MSPR-PRILS // Physical inventory indicator for blocked stock""")
    PRVLL = Column('PRVLL', String(3), default=None, doc="""Sourced from MSPR-PRVLL // Physical inventory indicator for stock in previous year""")
    PRVLQ = Column('PRVLQ', String(3), default=None, doc="""Sourced from MSPR-PRVLQ // Phys. inventory ind. f. stock in qual. insp. in prev. period""")
    PRVLS = Column('PRVLS', String(3), default=None, doc="""Sourced from MSPR-PRVLS // Phys. inventory indicator for blocked stock in prev. period""")
    PRFLL = Column('PRFLL', String(3), default=None, doc="""Sourced from MSPR-PRFLL // Physical inventory indicator for stock in following year""")
    PRFLQ = Column('PRFLQ', String(3), default=None, doc="""Sourced from MSPR-PRFLQ // Physical inventory indicator, quality insp.stck, follow.yr.""")
    PRFLS = Column('PRFLS', String(3), default=None, doc="""Sourced from MSPR-PRFLS // Phys. inventory ind. for blocked stock in following period""")
    PRDLL = Column('PRDLL', String(8), default=None, doc="""Sourced from MSPR-PRDLL // Date of Last Posted Count for Unrestricted-Use Stock""")
    PREIN = Column('PREIN', String(13), default=None, doc="""Sourced from MSPR-PREIN // Total Stock of All Restricted Batches""")
    PRVEI = Column('PRVEI', String(13), default=None, doc="""Sourced from MSPR-PRVEI // Restricted-Use Stock in Previous Period""")
    ERSDA = Column('ERSDA', Date, default=None, doc="""Sourced from MSPR-ERSDA // Created On""")
    PRJIN = Column('PRJIN', String(4), default=None, doc="""Sourced from MSPR-PRJIN // Fiscal year of current physical inventory indicator""")
    PRRUE = Column('PRRUE', Boolean, default=None, doc="""Sourced from MSPR-PRRUE // MxxxH rec. already exists for per. before last of Mxxx per.""")

    material_id = synonym('MATNR')
    special_stock_cd = synonym('SOBKZ')
    check_price_ind = synonym('PRSPR')
    create_dt = synonym('ERSDA')


################################################################################




################################################################################

class MaterialConsumption(SAP_Base):
    """\
    Table sourced from: MVER
    Description: Material Consumption
    """

    __tablename__ = "MVER"

    MATNR = Column('MATNR', String(18), primary_key = True, doc="""Sourced from MVER-MATNR // Material Number""")
    WERKS = Column('WERKS', String(4), primary_key = True, doc="""Sourced from MVER-WERKS // Plant""")
    GJAHR = Column('GJAHR', String(4), primary_key = True, doc="""Sourced from MVER-GJAHR // Fiscal Year""")
    PERKZ = Column('PERKZ', String(1), primary_key = True, doc="""Sourced from MVER-PERKZ // Period Indicator""")
    ZAHLR = Column('ZAHLR', String(2), primary_key = True, doc="""Sourced from MVER-ZAHLR // Number of follow-on records in Table MVER""")
    GSV01 = Column('GSV01', String(13), default=None, doc="""Sourced from MVER-GSV01 // Total consumption""")
    GSV02 = Column('GSV02', String(13), default=None, doc="""Sourced from MVER-GSV02 // Total consumption""")
    GSV03 = Column('GSV03', String(13), default=None, doc="""Sourced from MVER-GSV03 // Total consumption""")
    GSV04 = Column('GSV04', String(13), default=None, doc="""Sourced from MVER-GSV04 // Total consumption""")
    GSV05 = Column('GSV05', String(13), default=None, doc="""Sourced from MVER-GSV05 // Total consumption""")
    GSV06 = Column('GSV06', String(13), default=None, doc="""Sourced from MVER-GSV06 // Total consumption""")
    GSV07 = Column('GSV07', String(13), default=None, doc="""Sourced from MVER-GSV07 // Total consumption""")
    GSV08 = Column('GSV08', String(13), default=None, doc="""Sourced from MVER-GSV08 // Total consumption""")
    GSV09 = Column('GSV09', String(13), default=None, doc="""Sourced from MVER-GSV09 // Total consumption""")
    GSV10 = Column('GSV10', String(13), default=None, doc="""Sourced from MVER-GSV10 // Total consumption""")
    GSV11 = Column('GSV11', String(13), default=None, doc="""Sourced from MVER-GSV11 // Total consumption""")
    GSV12 = Column('GSV12', String(13), default=None, doc="""Sourced from MVER-GSV12 // Total consumption""")
    GSV13 = Column('GSV13', String(13), default=None, doc="""Sourced from MVER-GSV13 // Total consumption""")
    UNV01 = Column('UNV01', String(13), default=None, doc="""Sourced from MVER-UNV01 // Unplanned consumption""")
    UNV02 = Column('UNV02', String(13), default=None, doc="""Sourced from MVER-UNV02 // Unplanned consumption""")
    UNV03 = Column('UNV03', String(13), default=None, doc="""Sourced from MVER-UNV03 // Unplanned consumption""")
    UNV04 = Column('UNV04', String(13), default=None, doc="""Sourced from MVER-UNV04 // Unplanned consumption""")
    UNV05 = Column('UNV05', String(13), default=None, doc="""Sourced from MVER-UNV05 // Unplanned consumption""")
    UNV06 = Column('UNV06', String(13), default=None, doc="""Sourced from MVER-UNV06 // Unplanned consumption""")
    UNV07 = Column('UNV07', String(13), default=None, doc="""Sourced from MVER-UNV07 // Unplanned consumption""")
    UNV08 = Column('UNV08', String(13), default=None, doc="""Sourced from MVER-UNV08 // Unplanned consumption""")
    UNV09 = Column('UNV09', String(13), default=None, doc="""Sourced from MVER-UNV09 // Unplanned consumption""")
    UNV10 = Column('UNV10', String(13), default=None, doc="""Sourced from MVER-UNV10 // Unplanned consumption""")
    UNV11 = Column('UNV11', String(13), default=None, doc="""Sourced from MVER-UNV11 // Unplanned consumption""")
    UNV12 = Column('UNV12', String(13), default=None, doc="""Sourced from MVER-UNV12 // Unplanned consumption""")
    UNV13 = Column('UNV13', String(13), default=None, doc="""Sourced from MVER-UNV13 // Unplanned consumption""")
    MGV01 = Column('MGV01', String(13), default=None, doc="""Sourced from MVER-MGV01 // Manually corrected total consumption""")
    MGV02 = Column('MGV02', String(13), default=None, doc="""Sourced from MVER-MGV02 // Manually corrected total consumption""")
    MGV03 = Column('MGV03', String(13), default=None, doc="""Sourced from MVER-MGV03 // Manually corrected total consumption""")
    MGV04 = Column('MGV04', String(13), default=None, doc="""Sourced from MVER-MGV04 // Manually corrected total consumption""")
    MGV05 = Column('MGV05', String(13), default=None, doc="""Sourced from MVER-MGV05 // Manually corrected total consumption""")
    MGV06 = Column('MGV06', String(13), default=None, doc="""Sourced from MVER-MGV06 // Manually corrected total consumption""")
    MGV07 = Column('MGV07', String(13), default=None, doc="""Sourced from MVER-MGV07 // Manually corrected total consumption""")
    MGV08 = Column('MGV08', String(13), default=None, doc="""Sourced from MVER-MGV08 // Manually corrected total consumption""")
    MGV09 = Column('MGV09', String(13), default=None, doc="""Sourced from MVER-MGV09 // Manually corrected total consumption""")
    MGV10 = Column('MGV10', String(13), default=None, doc="""Sourced from MVER-MGV10 // Manually corrected total consumption""")
    MGV11 = Column('MGV11', String(13), default=None, doc="""Sourced from MVER-MGV11 // Manually corrected total consumption""")
    MGV12 = Column('MGV12', String(13), default=None, doc="""Sourced from MVER-MGV12 // Manually corrected total consumption""")
    MGV13 = Column('MGV13', String(13), default=None, doc="""Sourced from MVER-MGV13 // Manually corrected total consumption""")
    MUV01 = Column('MUV01', String(13), default=None, doc="""Sourced from MVER-MUV01 // Manually corrected unplanned consumption""")
    MUV02 = Column('MUV02', String(13), default=None, doc="""Sourced from MVER-MUV02 // Manually corrected unplanned consumption""")
    MUV03 = Column('MUV03', String(13), default=None, doc="""Sourced from MVER-MUV03 // Manually corrected unplanned consumption""")
    MUV04 = Column('MUV04', String(13), default=None, doc="""Sourced from MVER-MUV04 // Manually corrected unplanned consumption""")
    MUV05 = Column('MUV05', String(13), default=None, doc="""Sourced from MVER-MUV05 // Manually corrected unplanned consumption""")
    MUV06 = Column('MUV06', String(13), default=None, doc="""Sourced from MVER-MUV06 // Manually corrected unplanned consumption""")
    MUV07 = Column('MUV07', String(13), default=None, doc="""Sourced from MVER-MUV07 // Manually corrected unplanned consumption""")
    MUV08 = Column('MUV08', String(13), default=None, doc="""Sourced from MVER-MUV08 // Manually corrected unplanned consumption""")
    MUV09 = Column('MUV09', String(13), default=None, doc="""Sourced from MVER-MUV09 // Manually corrected unplanned consumption""")
    MUV10 = Column('MUV10', String(13), default=None, doc="""Sourced from MVER-MUV10 // Manually corrected unplanned consumption""")
    MUV11 = Column('MUV11', String(13), default=None, doc="""Sourced from MVER-MUV11 // Manually corrected unplanned consumption""")
    MUV12 = Column('MUV12', String(13), default=None, doc="""Sourced from MVER-MUV12 // Manually corrected unplanned consumption""")
    MUV13 = Column('MUV13', String(13), default=None, doc="""Sourced from MVER-MUV13 // Manually corrected unplanned consumption""")

    material_id = synonym('MATNR')
    fiscal_year = synonym('GJAHR')


################################################################################




################################################################################

class MaterialSalesOrg(SAP_Base):
    """\
    Table sourced from: MVKE
    Description: Sales Data for Material
    """

    __tablename__ = "MVKE"

    MATNR = Column('MATNR', String(18), primary_key = True, doc="""Sourced from MVKE-MATNR // Material Number""")
    VKORG = Column('VKORG', String(4), primary_key = True, doc="""Sourced from MVKE-VKORG // Sales Organization""")
    VTWEG = Column('VTWEG', String(2), primary_key = True, doc="""Sourced from MVKE-VTWEG // Distribution Channel""")
    LVORM = Column('LVORM', Boolean, default=None, doc="""Sourced from MVKE-LVORM // Ind.: Flag material for deletion at distribution chain level""")
    VERSG = Column('VERSG', String(1), default=None, doc="""Sourced from MVKE-VERSG // Material statistics group""")
    BONUS = Column('BONUS', String(2), default=None, doc="""Sourced from MVKE-BONUS // Volume rebate group""")
    PROVG = Column('PROVG', String(2), default=None, doc="""Sourced from MVKE-PROVG // Commission group""")
    SKTOF = Column('SKTOF', Boolean, default=None, doc="""Sourced from MVKE-SKTOF // Cash discount indicator""")
    VMSTA = Column('VMSTA', String(2), default=None, doc="""Sourced from MVKE-VMSTA // Distribution-chain-specific material status""")
    VMSTD = Column('VMSTD', Date, default=None, doc="""Sourced from MVKE-VMSTD // Date from which distr.-chain-spec. material status is valid""")
    AUMNG = Column('AUMNG', Numeric(15,3,3), default=None, doc="""Sourced from MVKE-AUMNG // Minimum order quantity in base unit of measure""")
    LFMNG = Column('LFMNG', String(13), default=None, doc="""Sourced from MVKE-LFMNG // Minimum delivery quantity in delivery note processing""")
    EFMNG = Column('EFMNG', Numeric(15,3,3), default=None, doc="""Sourced from MVKE-EFMNG // Minimum make-to-order quantity""")
    SCMNG = Column('SCMNG', Numeric(15,3,3), default=None, doc="""Sourced from MVKE-SCMNG // Delivery unit""")
    SCHME = Column('SCHME', String(3), default=None, doc="""Sourced from MVKE-SCHME // Unit of measure of delivery unit""")
    VRKME = Column('VRKME', String(3), default=None, doc="""Sourced from MVKE-VRKME // Sales unit""")
    MTPOS = Column('MTPOS', String(4), default=None, doc="""Sourced from MVKE-MTPOS // Item category group from material master""")
    DWERK = Column('DWERK', String(4), default=None, doc="""Sourced from MVKE-DWERK // Delivering Plant (Own or External)""")
    PRODH = Column('PRODH', String(18), default=None, doc="""Sourced from MVKE-PRODH // Product hierarchy""")
    PMATN = Column('PMATN', String(18), default=None, doc="""Sourced from MVKE-PMATN // Pricing Reference Material""")
    KONDM = Column('KONDM', String(2), default=None, doc="""Sourced from MVKE-KONDM // Material Pricing Group""")
    KTGRM = Column('KTGRM', String(2), default=None, doc="""Sourced from MVKE-KTGRM // Account assignment group for this material""")
    MVGR1 = Column('MVGR1', String(3), default=None, doc="""Sourced from MVKE-MVGR1 // Material group 1""")
    MVGR2 = Column('MVGR2', String(3), default=None, doc="""Sourced from MVKE-MVGR2 // Material group 2""")
    MVGR3 = Column('MVGR3', String(3), default=None, doc="""Sourced from MVKE-MVGR3 // Material group 3""")
    MVGR4 = Column('MVGR4', String(3), default=None, doc="""Sourced from MVKE-MVGR4 // Material group 4""")
    MVGR5 = Column('MVGR5', String(3), default=None, doc="""Sourced from MVKE-MVGR5 // Material group 5""")
    SSTUF = Column('SSTUF', String(2), default=None, doc="""Sourced from MVKE-SSTUF // Assortment grade""")
    PFLKS = Column('PFLKS', String(1), default=None, doc="""Sourced from MVKE-PFLKS // External assortment priority""")
    LSTFL = Column('LSTFL', String(2), default=None, doc="""Sourced from MVKE-LSTFL // Listing procedure for store or other assortment categories""")
    LSTVZ = Column('LSTVZ', String(2), default=None, doc="""Sourced from MVKE-LSTVZ // Listing procedure for distr. center assortment categories""")
    LSTAK = Column('LSTAK', String(1), default=None, doc="""Sourced from MVKE-LSTAK // Listing functions (assortments) are active""")
    LDVFL = Column('LDVFL', Date, default=None, doc="""Sourced from MVKE-LDVFL // Date from which listed in the store""")
    LDBFL = Column('LDBFL', Date, default=None, doc="""Sourced from MVKE-LDBFL // Date to which listed in the store""")
    LDVZL = Column('LDVZL', Date, default=None, doc="""Sourced from MVKE-LDVZL // Date from which listed in the distribution center""")
    LDBZL = Column('LDBZL', Date, default=None, doc="""Sourced from MVKE-LDBZL // Date to which listed in the central warehouse/distr. center""")
    VDVFL = Column('VDVFL', Date, default=None, doc="""Sourced from MVKE-VDVFL // Date from which sold in the store""")
    VDBFL = Column('VDBFL', Date, default=None, doc="""Sourced from MVKE-VDBFL // Date to which sold in the store""")
    VDVZL = Column('VDVZL', Date, default=None, doc="""Sourced from MVKE-VDVZL // Date from which sold in the distribution center""")
    VDBZL = Column('VDBZL', Date, default=None, doc="""Sourced from MVKE-VDBZL // Date to which sold in the distribution center""")
    PRAT1 = Column('PRAT1', String(1), default=None, doc="""Sourced from MVKE-PRAT1 // ID for product attribute 1""")
    PRAT2 = Column('PRAT2', String(1), default=None, doc="""Sourced from MVKE-PRAT2 // ID for product attribute 2""")
    PRAT3 = Column('PRAT3', String(1), default=None, doc="""Sourced from MVKE-PRAT3 // ID for product attribute 3""")
    PRAT4 = Column('PRAT4', String(1), default=None, doc="""Sourced from MVKE-PRAT4 // ID for product attribute 4""")
    PRAT5 = Column('PRAT5', String(1), default=None, doc="""Sourced from MVKE-PRAT5 // ID for product attribute 5""")
    PRAT6 = Column('PRAT6', String(1), default=None, doc="""Sourced from MVKE-PRAT6 // ID for product attribute 6""")
    PRAT7 = Column('PRAT7', String(1), default=None, doc="""Sourced from MVKE-PRAT7 // ID for product attribute 7""")
    PRAT8 = Column('PRAT8', String(1), default=None, doc="""Sourced from MVKE-PRAT8 // ID for product attribute 8""")
    PRAT9 = Column('PRAT9', String(1), default=None, doc="""Sourced from MVKE-PRAT9 // ID for product attribute 9""")
    PRATA = Column('PRATA', String(1), default=None, doc="""Sourced from MVKE-PRATA // ID for product attribute 10""")
    RDPRF = Column('RDPRF', String(4), default=None, doc="""Sourced from MVKE-RDPRF // Rounding Profile""")
    MEGRU = Column('MEGRU', String(4), default=None, doc="""Sourced from MVKE-MEGRU // Unit of Measure Group""")
    LFMAX = Column('LFMAX', String(13), default=None, doc="""Sourced from MVKE-LFMAX // Maximum delivery quantity in store order processing""")
    RJART = Column('RJART', Boolean, default=None, doc="""Sourced from MVKE-RJART // Flag rackjobber material""")
    PBIND = Column('PBIND', String(1), default=None, doc="""Sourced from MVKE-PBIND // Indicator for price fixing""")
    VAVME = Column('VAVME', Boolean, default=None, doc="""Sourced from MVKE-VAVME // Variable Sales Unit Not Allowed""")
    MATKC = Column('MATKC', String(1), default=None, doc="""Sourced from MVKE-MATKC // Competition characterization of a material""")
    PVMSO = Column('PVMSO', String(8), default=None, doc="""Sourced from MVKE-PVMSO // Material sorting in product proposal""")
    PLGTP = Column('PLGTP', String(2), default=None, doc="""Sourced from MVKE-PLGTP // Price Band Category""")

    material_id = synonym('MATNR')
    sales_org_cd = synonym('VKORG')
    distr_chan_cd = synonym('VTWEG')
    deleted_ind = synonym('LVORM')
    volume_rebate_grp_id = synonym('BONUS')
    distr_chain_material_status_cd = synonym('VMSTA')
    distr_chain_material_status_dt = synonym('VMSTD')
    scrap_qty = synonym('AUMNG')
    delivery_uom_cd = synonym('SCHME')
    sls_uom_cd = synonym('VRKME')
    facility_id = synonym('DWERK')
    pricing_ref_material_id = synonym('PMATN')
    material_pricing_grp_cd = synonym('KONDM')
    uom_group_cd = synonym('MEGRU')


################################################################################




################################################################################

class StorageLocation(SAP_Base):
    """\
    Table sourced from: T001L
    Description: Storage Locations
    """

    __tablename__ = "T001L"

    WERKS = Column('WERKS', String(4), primary_key = True, doc="""Sourced from T001L-WERKS // Plant""")
    LGORT = Column('LGORT', String(4), primary_key = True, doc="""Sourced from T001L-LGORT // Storage Location""")
    LGOBE = Column('LGOBE', String(16), default=None, doc="""Sourced from T001L-LGOBE // Description of Storage Location""")
    SPART = Column('SPART', String(2), default=None, doc="""Sourced from T001L-SPART // Division""")
    XLONG = Column('XLONG', Boolean, default=None, doc="""Sourced from T001L-XLONG // Negative stocks allowed in storage location""")
    XBUFX = Column('XBUFX', Boolean, default=None, doc="""Sourced from T001L-XBUFX // Freezing book inventory bal. allowed in stor. loc.""")
    DISKZ = Column('DISKZ', String(1), default=None, doc="""Sourced from T001L-DISKZ // Storage location MRP indicator""")
    XBLGO = Column('XBLGO', Boolean, default=None, doc="""Sourced from T001L-XBLGO // Storage location authorization for goods movements active""")
    XRESS = Column('XRESS', Boolean, default=None, doc="""Sourced from T001L-XRESS // Storage location is allocated to resource (storage resource)""")
    XHUPF = Column('XHUPF', Boolean, default=None, doc="""Sourced from T001L-XHUPF // Handling unit requirement""")
    PARLG = Column('PARLG', String(4), default=None, doc="""Sourced from T001L-PARLG // Partner storage location of the handling unit""")
    VKORG = Column('VKORG', String(4), default=None, doc="""Sourced from T001L-VKORG // Sales Organization""")
    VTWEG = Column('VTWEG', String(2), default=None, doc="""Sourced from T001L-VTWEG // Distribution Channel""")
    VSTEL = Column('VSTEL', String(4), default=None, doc="""Sourced from T001L-VSTEL // Shipping Point/Receiving Point""")
    LIFNR = Column('LIFNR', String(10), default=None, doc="""Sourced from T001L-LIFNR // Vendor Account Number""")
    KUNNR = Column('KUNNR', String(10), default=None, doc="""Sourced from T001L-KUNNR // Account Number of Customer""")
    MESBS = Column('MESBS', String(60), default=None, doc="""Sourced from T001L-MESBS // Business System of MES""")
    MESST = Column('MESST', String(1), default=None, doc="""Sourced from T001L-MESST // Type of inventory management for production storage location""")
    OIH_LICNO = Column('OIH_LICNO', String(15), default=None, doc="""Sourced from T001L-OIH_LICNO // License number for untaxed stock""")
    OIG_ITRFL = Column('OIG_ITRFL', Boolean, default=None, doc="""Sourced from T001L-OIG_ITRFL // TD in-transit flag""")
    OIB_TNKASSIGN = Column('OIB_TNKASSIGN', String(1), default=None, doc="""Sourced from T001L-OIB_TNKASSIGN // Silo Managament: Tank assignment indicator""")

    storage_location_desc = synonym('LGOBE')
    div_cd = synonym('SPART')
    negative_stor_loc_stocks_allowed_ind = synonym('XLONG')
    mrp_storage_loc_cd = synonym('DISKZ')
    sales_org_cd = synonym('VKORG')
    distr_chan_cd = synonym('VTWEG')
    shipping_receiving_point_cd = synonym('VSTEL')
    customer_id = synonym('KUNNR')


################################################################################




################################################################################

class Facility(SAP_Base):
    """\
    Table sourced from: T001W
    Description: Plants/Branches
    """

    __tablename__ = "T001W"

    WERKS = Column('WERKS', String(4), primary_key = True, doc="""Sourced from T001W-WERKS // Plant""")
    NAME1 = Column('NAME1', String(30), default=None, doc="""Sourced from T001W-NAME1 // Name""")
    BWKEY = Column('BWKEY', String(4), default=None, doc="""Sourced from T001W-BWKEY // Valuation Area""")
    KUNNR = Column('KUNNR', String(10), default=None, doc="""Sourced from T001W-KUNNR // Customer number of plant""")
    LIFNR = Column('LIFNR', String(10), default=None, doc="""Sourced from T001W-LIFNR // Vendor number of plant""")
    FABKL = Column('FABKL', String(2), default=None, doc="""Sourced from T001W-FABKL // Factory calendar key""")
    NAME2 = Column('NAME2', String(30), default=None, doc="""Sourced from T001W-NAME2 // Name 2""")
    STRAS = Column('STRAS', String(30), default=None, doc="""Sourced from T001W-STRAS // House number and street""")
    PFACH = Column('PFACH', String(10), default=None, doc="""Sourced from T001W-PFACH // PO Box""")
    PSTLZ = Column('PSTLZ', String(10), default=None, doc="""Sourced from T001W-PSTLZ // Postal Code""")
    ORT01 = Column('ORT01', String(25), default=None, doc="""Sourced from T001W-ORT01 // City""")
    EKORG = Column('EKORG', String(4), default=None, doc="""Sourced from T001W-EKORG // Purchasing Organization""")
    VKORG = Column('VKORG', String(4), default=None, doc="""Sourced from T001W-VKORG // Sales organization for intercompany billing""")
    CHAZV = Column('CHAZV', Boolean, default=None, doc="""Sourced from T001W-CHAZV // Indicator: batch status management active""")
    KKOWK = Column('KKOWK', String(1), default=None, doc="""Sourced from T001W-KKOWK // Indicator: Conditions at plant level""")
    KORDB = Column('KORDB', Boolean, default=None, doc="""Sourced from T001W-KORDB // Indicator: Source list requirement""")
    BEDPL = Column('BEDPL', Boolean, default=None, doc="""Sourced from T001W-BEDPL // Activating requirements planning""")
    LAND1 = Column('LAND1', String(3), default=None, doc="""Sourced from T001W-LAND1 // Country Key""")
    REGIO = Column('REGIO', String(3), default=None, doc="""Sourced from T001W-REGIO // Region (State, Province, County)""")
    COUNC = Column('COUNC', String(3), default=None, doc="""Sourced from T001W-COUNC // County Code""")
    CITYC = Column('CITYC', String(4), default=None, doc="""Sourced from T001W-CITYC // City Code""")
    ADRNR = Column('ADRNR', String(10), default=None, doc="""Sourced from T001W-ADRNR // Address""")
    IWERK = Column('IWERK', String(4), default=None, doc="""Sourced from T001W-IWERK // Maintenance Planning Plant""")
    TXJCD = Column('TXJCD', String(15), default=None, doc="""Sourced from T001W-TXJCD // Tax Jurisdiction""")
    VTWEG = Column('VTWEG', String(2), default=None, doc="""Sourced from T001W-VTWEG // Distribution channel for intercompany billing""")
    SPART = Column('SPART', String(2), default=None, doc="""Sourced from T001W-SPART // Division for intercompany billing""")
    SPRAS = Column('SPRAS', String(1), default=None, doc="""Sourced from T001W-SPRAS // Language Key""")
    WKSOP = Column('WKSOP', Boolean, default=None, doc="""Sourced from T001W-WKSOP // SOP plant""")
    AWSLS = Column('AWSLS', String(6), default=None, doc="""Sourced from T001W-AWSLS // Variance Key""")
    CHAZV_OLD = Column('CHAZV_OLD', Boolean, default=None, doc="""Sourced from T001W-CHAZV_OLD // Indicator: batch status management active""")
    VLFKZ = Column('VLFKZ', String(1), default=None, doc="""Sourced from T001W-VLFKZ // Plant category""")
    BZIRK = Column('BZIRK', String(6), default=None, doc="""Sourced from T001W-BZIRK // Sales district""")
    ZONE1 = Column('ZONE1', String(10), default=None, doc="""Sourced from T001W-ZONE1 // Supply region (region supplied)""")
    TAXIW = Column('TAXIW', String(1), default=None, doc="""Sourced from T001W-TAXIW // Tax Indicator: Plant (Purchasing)""")
    BZQHL = Column('BZQHL', Boolean, default=None, doc="""Sourced from T001W-BZQHL // Take regular vendor into account""")
    LET01 = Column('LET01', String(3), default=None, doc="""Sourced from T001W-LET01 // Number of Days for First Reminder/Expediter""")
    LET02 = Column('LET02', String(3), default=None, doc="""Sourced from T001W-LET02 // Number of Days for Second Reminder/Expediter""")
    LET03 = Column('LET03', String(3), default=None, doc="""Sourced from T001W-LET03 // Number of Days for Third Reminder/Expediter""")
    TXNAM_MA1 = Column('TXNAM_MA1', String(16), default=None, doc="""Sourced from T001W-TXNAM_MA1 // Text name of 1st dunning of vendor declarations""")
    TXNAM_MA2 = Column('TXNAM_MA2', String(16), default=None, doc="""Sourced from T001W-TXNAM_MA2 // Text name of the 2nd dunning of vendor declarations""")
    TXNAM_MA3 = Column('TXNAM_MA3', String(16), default=None, doc="""Sourced from T001W-TXNAM_MA3 // Text name of 3rd dunning of vendor declarations""")
    BETOL = Column('BETOL', String(3), default=None, doc="""Sourced from T001W-BETOL // Number of days for PO tolerance - Compress info records - SU""")
    J_1BBRANCH = Column('J_1BBRANCH', String(4), default=None, doc="""Sourced from T001W-J_1BBRANCH // Business Place""")
    VTBFI = Column('VTBFI', String(2), default=None, doc="""Sourced from T001W-VTBFI // Rule for determining the sales area for stock transfers""")
    FPRFW = Column('FPRFW', String(3), default=None, doc="""Sourced from T001W-FPRFW // Distribution profile at plant level""")
    ACHVM = Column('ACHVM', Boolean, default=None, doc="""Sourced from T001W-ACHVM // Central archiving marker for master record""")
    DVSART = Column('DVSART', String(1), default=None, doc="""Sourced from T001W-DVSART // Batch Record: Type of DMS Used""")
    NODETYPE = Column('NODETYPE', String(3), default=None, doc="""Sourced from T001W-NODETYPE // Node type: supply chain network""")
    NSCHEMA = Column('NSCHEMA', String(4), default=None, doc="""Sourced from T001W-NSCHEMA // Structure for name formation""")
    PKOSA = Column('PKOSA', String(1), default=None, doc="""Sourced from T001W-PKOSA // Cost Object Controlling linking active""")
    MISCH = Column('MISCH', String(1), default=None, doc="""Sourced from T001W-MISCH // Updating is active for mixed costing""")
    MGVUPD = Column('MGVUPD', String(1), default=None, doc="""Sourced from T001W-MGVUPD // Updating is active in actual costing""")
    VSTEL = Column('VSTEL', String(4), default=None, doc="""Sourced from T001W-VSTEL // Shipping Point/Receiving Point""")
    MGVLAUPD = Column('MGVLAUPD', String(1), default=None, doc="""Sourced from T001W-MGVLAUPD // Update of Activity Consumption in the Quantity Structure""")
    MGVLAREVAL = Column('MGVLAREVAL', String(1), default=None, doc="""Sourced from T001W-MGVLAREVAL // Control of Credit of Cost Centers""")
    SOURCING = Column('SOURCING', String(1), default=None, doc="""Sourced from T001W-SOURCING // Invoke Added-Function Source Determination via ATP""")
    OILIVAL = Column('OILIVAL', String(1), default=None, doc="""Sourced from T001W-OILIVAL // Exchange valuation indicator""")
    OIHVTYPE = Column('OIHVTYPE', String(1), default=None, doc="""Sourced from T001W-OIHVTYPE // Vendor type (refinery/mill/other) (Brazil)""")
    OIHCREDIPI = Column('OIHCREDIPI', String(1), default=None, doc="""Sourced from T001W-OIHCREDIPI // IPI credit allowed""")
    STORETYPE = Column('STORETYPE', String(1), default=None, doc="""Sourced from T001W-STORETYPE // Store Category to Differentiate Store, Dep. Store, Shop""")
    DEP_STORE = Column('DEP_STORE', String(4), default=None, doc="""Sourced from T001W-DEP_STORE // Superior Department Store""")

    name = synonym('NAME1')
    valuation_area_id = synonym('BWKEY')
    customer_id = synonym('KUNNR')
    factory_calendar_cd = synonym('FABKL')
    name2 = synonym('NAME2')
    po_box = synonym('PFACH')
    city = synonym('ORT01')
    prch_org_cd = synonym('EKORG')
    sales_org_cd = synonym('VKORG')
    batch_mgmt_active_ind = synonym('CHAZV')
    country_cd = synonym('LAND1')
    region = synonym('REGIO')
    county_cd = synonym('COUNC')
    city_cd = synonym('CITYC')
    addr_id = synonym('ADRNR')
    distr_chan_cd = synonym('VTWEG')
    div_cd = synonym('SPART')
    language_cd = synonym('SPRAS')
    facility_ctgy_cd = synonym('VLFKZ')
    sales_district_id = synonym('BZIRK')
    shipping_receiving_point_cd = synonym('VSTEL')


################################################################################




################################################################################

class UnitOfMeasure(SAP_Base):
    """\
    Table sourced from: T006
    Description: Units of Measurement
    """

    __tablename__ = "T006"

    MSEHI = Column('MSEHI', String(3), primary_key = True, doc="""Sourced from T006-MSEHI // Unit of Measurement""")
    KZEX3 = Column('KZEX3', Boolean, default=None, doc="""Sourced from T006-KZEX3 // 3-char indicator for external unit of measurement""")
    KZEX6 = Column('KZEX6', Boolean, default=None, doc="""Sourced from T006-KZEX6 // 6-char. ID for external unit of measurement""")
    ANDEC = Column('ANDEC', Integer, default=None, doc="""Sourced from T006-ANDEC // No. of decimal places to which rounding should be performed""")
    KZKEH = Column('KZKEH', Boolean, default=None, doc="""Sourced from T006-KZKEH // Commercial measurement unit ID""")
    KZWOB = Column('KZWOB', Boolean, default=None, doc="""Sourced from T006-KZWOB // Value-based commitment indicator""")
    KZ1EH = Column('KZ1EH', Boolean, default=None, doc="""Sourced from T006-KZ1EH // Indicator (1) unit (indicator not yet defined)""")
    KZ2EH = Column('KZ2EH', Boolean, default=None, doc="""Sourced from T006-KZ2EH // Indicator (2) unit (indicator not yet defined)""")
    DIMID = Column('DIMID', String(6), default=None, doc="""Sourced from T006-DIMID // Dimension key""")
    EXP10 = Column('EXP10', Integer, default=None, doc="""Sourced from T006-EXP10 // base ten exponent for conversion to SI unit""")
    ADDKO = Column('ADDKO', Numeric(15,3,3), default=None, doc="""Sourced from T006-ADDKO // Additive constant for conversion to SI unit""")
    EXPON = Column('EXPON', Integer, default=None, doc="""Sourced from T006-EXPON // Base ten exponent for floating-point display""")
    DECAN = Column('DECAN', Integer, default=None, doc="""Sourced from T006-DECAN // Number of decimal places for number display""")
    ISOCODE = Column('ISOCODE', String(3), default=None, doc="""Sourced from T006-ISOCODE // ISO code for unit of measurement""")
    PRIMARY = Column('PRIMARY', Boolean, default=None, doc="""Sourced from T006-PRIMARY // Selection field for conversion from ISO code to int. code""")
    TEMP_VALUE = Column('TEMP_VALUE', Float, default=None, doc="""Sourced from T006-TEMP_VALUE // Temperature""")
    TEMP_UNIT = Column('TEMP_UNIT', String(3), default=None, doc="""Sourced from T006-TEMP_UNIT // Temperature unit""")
    FAMUNIT = Column('FAMUNIT', String(1), default=None, doc="""Sourced from T006-FAMUNIT // Unit of measurement family""")
    PRESS_VAL = Column('PRESS_VAL', Float, default=None, doc="""Sourced from T006-PRESS_VAL // Pressure Value""")
    PRESS_UNIT = Column('PRESS_UNIT', String(3), default=None, doc="""Sourced from T006-PRESS_UNIT // Unit of Pressure""")

    unit_of_measure_cd = synonym('MSEHI')
    decimal_rounding_qty = synonym('ANDEC')
    uom_family_cd = synonym('FAMUNIT')


################################################################################




################################################################################

class MaterialGroup(SAP_Base):
    """\
    Table sourced from: T023
    Description: Material Groups
    """

    __tablename__ = "T023"

    MATKL = Column('MATKL', String(9), primary_key = True, doc="""Sourced from T023-MATKL // Material Group""")
    SPART = Column('SPART', String(2), default=None, doc="""Sourced from T023-SPART // Division""")
    LREF3 = Column('LREF3', String(3), default=None, doc="""Sourced from T023-LREF3 // Material group-related supply relat. between plants /DEACT.""")
    WWGDA = Column('WWGDA', String(18), default=None, doc="""Sourced from T023-WWGDA // Material group reference material""")
    WWGPA = Column('WWGPA', String(18), default=None, doc="""Sourced from T023-WWGPA // Material group material""")
    ABTNR = Column('ABTNR', String(4), default=None, doc="""Sourced from T023-ABTNR // Department number""")
    BEGRU = Column('BEGRU', String(4), default=None, doc="""Sourced from T023-BEGRU // Authorization Group""")
    GEWEI = Column('GEWEI', String(3), default=None, doc="""Sourced from T023-GEWEI // Default unit of weight in the material master""")
    J_1BNBM = Column('J_1BNBM', String(16), default=None, doc="""Sourced from T023-J_1BNBM // Brazilian NCM Code""")
    BKLAS = Column('BKLAS', String(4), default=None, doc="""Sourced from T023-BKLAS // Valuation Class""")
    EKWSL = Column('EKWSL', String(4), default=None, doc="""Sourced from T023-EKWSL // Purchasing Value Key""")
    ANLKL = Column('ANLKL', String(8), default=None, doc="""Sourced from T023-ANLKL // Default: Asset Class for Creation of Asset""")
    DEF_SCHDSC = Column('DEF_SCHDSC', String(6), default=None, doc="""Sourced from T023-DEF_SCHDSC // Event Scenario""")
    PRICE_GROUP = Column('PRICE_GROUP', String(6), default=None, doc="""Sourced from T023-PRICE_GROUP // Price Level Group""")

    material_group_cd = synonym('MATKL')
    div_cd = synonym('SPART')
    auth_grp_id = synonym('BEGRU')
    weight_uom_cd = synonym('GEWEI')
    puch_value_cd = synonym('EKWSL')


################################################################################




################################################################################

class MaterialGroupDesc(SAP_Base):
    """\
    Table sourced from: T023T
    Description: Material Group Descriptions
    """

    __tablename__ = "T023T"

    SPRAS = Column('SPRAS', String(1), primary_key = True, doc="""Sourced from T023T-SPRAS // Language Key""")
    MATKL = Column('MATKL', String(9), primary_key = True, doc="""Sourced from T023T-MATKL // Material Group""")
    WGBEZ = Column('WGBEZ', String(20), default=None, doc="""Sourced from T023T-WGBEZ // Material Group Description""")
    WGBEZ60 = Column('WGBEZ60', String(60), default=None, doc="""Sourced from T023T-WGBEZ60 // Long text describing the material group""")

    language_cd = synonym('SPRAS')
    material_group_cd = synonym('MATKL')
    material_group_desc = synonym('WGBEZ')
    material_group_long_desc = synonym('WGBEZ60')


################################################################################




################################################################################

class MaterialType(SAP_Base):
    """\
    Table sourced from: T134
    Description: Material Types
    """

    __tablename__ = "T134"

    MTART = Column('MTART', String(4), primary_key = True, doc="""Sourced from T134-MTART // Material Type""")
    MTREF = Column('MTREF', String(4), default=None, doc="""Sourced from T134-MTREF // Reference material type""")
    MBREF = Column('MBREF', String(4), default=None, doc="""Sourced from T134-MBREF // Screen reference depending on the material type""")
    FLREF = Column('FLREF', String(4), default=None, doc="""Sourced from T134-FLREF // Field reference for material master""")
    NUMKI = Column('NUMKI', String(2), default=None, doc="""Sourced from T134-NUMKI // Number range""")
    NUMKE = Column('NUMKE', String(2), default=None, doc="""Sourced from T134-NUMKE // Number range""")
    ENVOP = Column('ENVOP', Boolean, default=None, doc="""Sourced from T134-ENVOP // External Number Assignment Without Validation""")
    BSEXT = Column('BSEXT', String(1), default=None, doc="""Sourced from T134-BSEXT // External Purchase Orders Allowed""")
    BSINT = Column('BSINT', String(1), default=None, doc="""Sourced from T134-BSINT // Internal purchase orders allowed""")
    PSTAT = Column('PSTAT', String(15), default=None, doc="""Sourced from T134-PSTAT // Maintenance status""")
    KKREF = Column('KKREF', String(4), default=None, doc="""Sourced from T134-KKREF // Account category reference""")
    VPRSV = Column('VPRSV', String(1), default=None, doc="""Sourced from T134-VPRSV // Price Control Indicator""")
    KZVPR = Column('KZVPR', Boolean, default=None, doc="""Sourced from T134-KZVPR // Price Control Mandatory""")
    VMTPO = Column('VMTPO', String(4), default=None, doc="""Sourced from T134-VMTPO // Default value for material item category group""")
    EKALR = Column('EKALR', Boolean, default=None, doc="""Sourced from T134-EKALR // Material Is Costed with Quantity Structure""")
    KZGRP = Column('KZGRP', String(1), default=None, doc="""Sourced from T134-KZGRP // Grouping indicator""")
    KZKFG = Column('KZKFG', Boolean, default=None, doc="""Sourced from T134-KZKFG // Configurable Material""")
    BEGRU = Column('BEGRU', String(4), default=None, doc="""Sourced from T134-BEGRU // Authorization group in the material master""")
    KZPRC = Column('KZPRC', Boolean, default=None, doc="""Sourced from T134-KZPRC // Material Master Record for a Process""")
    KZPIP = Column('KZPIP', Boolean, default=None, doc="""Sourced from T134-KZPIP // Pipeline Handling Mandatory""")
    PRDRU = Column('PRDRU', Boolean, default=None, doc="""Sourced from T134-PRDRU // Display price on cash register display and print on receipt""")
    ARANZ = Column('ARANZ', Boolean, default=None, doc="""Sourced from T134-ARANZ // Display material on cash register display""")
    WMAKG = Column('WMAKG', String(1), default=None, doc="""Sourced from T134-WMAKG // Material type ID""")
    IZUST = Column('IZUST', String(1), default=None, doc="""Sourced from T134-IZUST // Initial status of a new batch""")
    ARDEL = Column('ARDEL', String(4), default=None, doc="""Sourced from T134-ARDEL // Time in days until a material is deleted""")
    KZMPN = Column('KZMPN', Boolean, default=None, doc="""Sourced from T134-KZMPN // Manufacturer Part""")
    MSTAE = Column('MSTAE', String(2), default=None, doc="""Sourced from T134-MSTAE // Cross-Plant Material Status""")
    CCHIS = Column('CCHIS', String(1), default=None, doc="""Sourced from T134-CCHIS // Control (time) of history requirement: Material""")
    CTYPE = Column('CTYPE', String(3), default=None, doc="""Sourced from T134-CTYPE // Class Type""")
    CLASS = Column('CLASS', String(18), default=None, doc="""Sourced from T134-CLASS // Class number""")
    CHNEU = Column('CHNEU', String(1), default=None, doc="""Sourced from T134-CHNEU // Batch Creation Control (Automatic/Manual)""")
    VTYPE = Column('VTYPE', String(10), default=None, doc="""Sourced from T134-VTYPE // Version Category""")
    VNUMKI = Column('VNUMKI', String(2), default=None, doc="""Sourced from T134-VNUMKI // Number range""")
    VNUMKE = Column('VNUMKE', String(2), default=None, doc="""Sourced from T134-VNUMKE // Number range""")
    KZRAC = Column('KZRAC', Boolean, default=None, doc="""Sourced from T134-KZRAC // Returnable Packaging Logistics is mandatory""")

    material_type_id = synonym('MTART')
    ext_prch_ord_allowed_cd = synonym('BSEXT')
    int_prch_ord_allowed_cd = synonym('BSINT')
    configurable_material_ind = synonym('KZKFG')
    auth_grp_id = synonym('BEGRU')
    material_status_cd = synonym('MSTAE')


################################################################################




################################################################################

class MaterialTypeDesc(SAP_Base):
    """\
    Table sourced from: T134T
    Description: Material Type Descriptions
    """

    __tablename__ = "T134T"

    SPRAS = Column('SPRAS', String(1), primary_key = True, doc="""Sourced from T134T-SPRAS // Language Key""")
    MTART = Column('MTART', String(4), primary_key = True, doc="""Sourced from T134T-MTART // Material Type""")
    MTBEZ = Column('MTBEZ', String(25), default=None, doc="""Sourced from T134T-MTBEZ // Description of material type""")

    language_cd = synonym('SPRAS')
    material_type_id = synonym('MTART')
    material_type_desc = synonym('MTBEZ')


################################################################################




################################################################################

class MaterialStatus(SAP_Base):
    """\
    Table sourced from: T141
    Description: Material Status from Materials Management/PPC View
    """

    __tablename__ = "T141"

    MMSTA = Column('MMSTA', String(2), primary_key = True, doc="""Sourced from T141-MMSTA // Material status from MM/PP view""")
    DEINK = Column('DEINK', String(1), default=None, doc="""Sourced from T141-DEINK // Message if material is used in Purchasing""")
    DSTLK = Column('DSTLK', String(1), default=None, doc="""Sourced from T141-DSTLK // Message if Material Is Used in BOM Header""")
    DSTLP = Column('DSTLP', String(1), default=None, doc="""Sourced from T141-DSTLP // Message if material is used as BOM item""")
    DAPLA = Column('DAPLA', String(1), default=None, doc="""Sourced from T141-DAPLA // Message if material is used in routing/master recipe""")
    DPBED = Column('DPBED', String(1), default=None, doc="""Sourced from T141-DPBED // Message if independent requirement is created for material""")
    DDISP = Column('DDISP', String(1), default=None, doc="""Sourced from T141-DDISP // Message if material is used in MRP""")
    DFAPO = Column('DFAPO', String(1), default=None, doc="""Sourced from T141-DFAPO // Message if Material Used in Production Order or Network Item""")
    DFAKO = Column('DFAKO', String(1), default=None, doc="""Sourced from T141-DFAKO // Message if material is used in production order header""")
    DINST = Column('DINST', String(1), default=None, doc="""Sourced from T141-DINST // Message if material is used in Plant Maintenance""")
    DBEST = Column('DBEST', String(1), default=None, doc="""Sourced from T141-DBEST // Message if material is used in Inventory Management""")
    DPROG = Column('DPROG', String(1), default=None, doc="""Sourced from T141-DPROG // Message if material is used in Forecasting""")
    DFHMI = Column('DFHMI', String(1), default=None, doc="""Sourced from T141-DFHMI // Message if PRT are assigned to routing or order""")
    DQMPF = Column('DQMPF', String(1), default=None, doc="""Sourced from T141-DQMPF // Message if material is used in QM inspection procedures""")
    DTBED = Column('DTBED', String(1), default=None, doc="""Sourced from T141-DTBED // Message if material used in WM transfer reqmt/posting change""")
    DTAUF = Column('DTAUF', String(1), default=None, doc="""Sourced from T141-DTAUF // Message if material is used in WM transfer order""")
    DERZK = Column('DERZK', String(1), default=None, doc="""Sourced from T141-DERZK // Procedure When Creating Material Cost Estimate""")
    DLFPL = Column('DLFPL', String(1), default=None, doc="""Sourced from T141-DLFPL // Message if material used in long-term planning""")
    DLOCK = Column('DLOCK', Boolean, default=None, doc="""Sourced from T141-DLOCK // Indicator: distribution lock""")
    AUPRF = Column('AUPRF', String(10), default=None, doc="""Sourced from T141-AUPRF // Profile Name for ALE Change Authorization""")
    JSPPP = Column('JSPPP', String(1), default=None, doc="""Sourced from T141-JSPPP // Locked for Purchase Order Quantity Planning""")
    JSPPO = Column('JSPPO', String(1), default=None, doc="""Sourced from T141-JSPPO // Blocked for Purchase Order Generation""")

    material_facility_status_cd = synonym('MMSTA')
    distribution_lock_ind = synonym('DLOCK')


################################################################################




################################################################################

class MaterialStatusDesc(SAP_Base):
    """\
    Table sourced from: T141T
    Description: Descriptions of Material Status from MM/PP View
    """

    __tablename__ = "T141T"

    SPRAS = Column('SPRAS', String(1), primary_key = True, doc="""Sourced from T141T-SPRAS // Language Key""")
    MMSTA = Column('MMSTA', String(2), primary_key = True, doc="""Sourced from T141T-MMSTA // Plant-Specific Material Status""")
    MTSTB = Column('MTSTB', String(25), default=None, doc="""Sourced from T141T-MTSTB // Description of material status from MM/PP view""")

    language_cd = synonym('SPRAS')
    material_facility_status_cd = synonym('MMSTA')


################################################################################




################################################################################

class MaterialMovementType(SAP_Base):
    """\
    Table sourced from: T156
    Description: Movement Type
    """

    __tablename__ = "T156"

    BWART = Column('BWART', String(3), primary_key = True, doc="""Sourced from T156-BWART // Movement Type (Inventory Management)""")
    SHKZG = Column('SHKZG', String(1), default=None, doc="""Sourced from T156-SHKZG // Debit/Credit Indicator""")
    KZWES = Column('KZWES', String(1), default=None, doc="""Sourced from T156-KZWES // GR blocked stock""")
    KZVBU = Column('KZVBU', String(1), default=None, doc="""Sourced from T156-KZVBU // Consumption posting""")
    KZDRU = Column('KZDRU', String(1), default=None, doc="""Sourced from T156-KZDRU // Printing of document item""")
    KZKON = Column('KZKON', String(1), default=None, doc="""Sourced from T156-KZKON // Display or suppress account field/manual account assignment""")
    CHNEU = Column('CHNEU', String(1), default=None, doc="""Sourced from T156-CHNEU // Batch Creation Control (Automatic/Manual)""")
    KZZDE = Column('KZZDE', Boolean, default=None, doc="""Sourced from T156-KZZDE // Maintain status data of a batch""")
    RSTYP = Column('RSTYP', String(1), default=None, doc="""Sourced from T156-RSTYP // Account assignment of reservation""")
    SELPA = Column('SELPA', String(10), default=None, doc="""Sourced from T156-SELPA // Selection parameter for purchasing lists""")
    XLAUT = Column('XLAUT', Boolean, default=None, doc="""Sourced from T156-XLAUT // Automatic creation of storage location allowed""")
    KZSTR = Column('KZSTR', String(1), default=None, doc="""Sourced from T156-KZSTR // Transaction/event is relevant to statistics""")
    KZGRU = Column('KZGRU', String(1), default=None, doc="""Sourced from T156-KZGRU // Control: Reason for Movement""")
    XINVB = Column('XINVB', Boolean, default=None, doc="""Sourced from T156-XINVB // Generate physical inventory document for material doc. item""")
    QSSBW = Column('QSSBW', String(1), default=None, doc="""Sourced from T156-QSSBW // Inspection by quality assurance""")
    KZBWA = Column('KZBWA', String(2), default=None, doc="""Sourced from T156-KZBWA // Movement type category""")
    XSTBW = Column('XSTBW', Boolean, default=None, doc="""Sourced from T156-XSTBW // Reversal movement type""")
    XPBED = Column('XPBED', Boolean, default=None, doc="""Sourced from T156-XPBED // Requirements reduction upon goods movements""")
    XWSBR = Column('XWSBR', Boolean, default=None, doc="""Sourced from T156-XWSBR // Reversal of GR allowed for GR-based IV despite invoice""")
    KZMHD = Column('KZMHD', String(1), default=None, doc="""Sourced from T156-KZMHD // Check Best Before Date/Production Date""")
    KZCLA = Column('KZCLA', String(1), default=None, doc="""Sourced from T156-KZCLA // Option to classify batches""")
    XKOKO = Column('XKOKO', String(1), default=None, doc="""Sourced from T156-XKOKO // Cost element accounting""")
    XKCFC = Column('XKCFC', Boolean, default=None, doc="""Sourced from T156-XKCFC // Extended classification via CFC""")
    XNEBE = Column('XNEBE', Boolean, default=None, doc="""Sourced from T156-XNEBE // Create purchase order automatically""")
    J_1BNFREL = Column('J_1BNFREL', String(1), default=None, doc="""Sourced from T156-J_1BNFREL // Nota Fiscal Relevance""")
    J_1BNFTYPE = Column('J_1BNFTYPE', String(2), default=None, doc="""Sourced from T156-J_1BNFTYPE // Nota Fiscal Type""")
    J_1BITMTYP = Column('J_1BITMTYP', String(2), default=None, doc="""Sourced from T156-J_1BITMTYP // Nota Fiscal Item Type""")
    J_1BSPCSTO = Column('J_1BSPCSTO', String(2), default=None, doc="""Sourced from T156-J_1BSPCSTO // Nota Fiscal Special Case for CFOP Determination""")
    J_1BPARTYP = Column('J_1BPARTYP', String(1), default=None, doc="""Sourced from T156-J_1BPARTYP // Nota Fiscal Partner Type""")
    J_1BPARVW = Column('J_1BPARVW', String(2), default=None, doc="""Sourced from T156-J_1BPARVW // Nota Fiscal Partner Function""")
    RULES = Column('RULES', String(4), default=None, doc="""Sourced from T156-RULES // Stock determination rule""")
    J_1AREVIDX = Column('J_1AREVIDX', Boolean, default=None, doc="""Sourced from T156-J_1AREVIDX // Relevant to Goods Issue Revaluation""")
    J_1ADOCCL = Column('J_1ADOCCL', String(1), default=None, doc="""Sourced from T156-J_1ADOCCL // Document Class""")
    J_1AEXPKZ = Column('J_1AEXPKZ', Boolean, default=None, doc="""Sourced from T156-J_1AEXPKZ // Material movement: Export indicator""")
    XOARC = Column('XOARC', Boolean, default=None, doc="""Sourced from T156-XOARC // Storage upon goods movements active""")
    BUSTR = Column('BUSTR', String(3), default=None, doc="""Sourced from T156-BUSTR // Posting string reference (Inventory Management)""")
    KZDIR = Column('KZDIR', String(1), default=None, doc="""Sourced from T156-KZDIR // Direction Indicator (Cross-System Flow of Goods)""")
    OIJ1BNFFI = Column('OIJ1BNFFI', Boolean, default=None, doc="""Sourced from T156-OIJ1BNFFI // Control Flag for Nota Fiscal creation (Gain/Loss)""")
    MILL_CPCONF = Column('MILL_CPCONF', String(1), default=None, doc="""Sourced from T156-MILL_CPCONF // Indicator for Adoption of Conf. in Batch Classification""")
    CO_WIPB_CPCONF = Column('CO_WIPB_CPCONF', String(1), default=None, doc="""Sourced from T156-CO_WIPB_CPCONF // Indicator for Adoption of Conf. in Batch Classification""")
    XWIPB = Column('XWIPB', Boolean, default=None, doc="""Sourced from T156-XWIPB // Indicator: Movement Type Allows WIP Batches""")

    im_matl_mvmnt_type_cd = synonym('BWART')
    gr_blocked_stock_qty = synonym('KZWES')
    movement_type_ctgy_cd = synonym('KZBWA')
    material_movement_export_ind = synonym('J_1AEXPKZ')


################################################################################




################################################################################

class MaterialMovementTypeDesc(SAP_Base):
    """\
    Table sourced from: T156T
    Description: Movement Type Text
    """

    __tablename__ = "T156T"

    SPRAS = Column('SPRAS', String(1), primary_key = True, doc="""Sourced from T156T-SPRAS // Language Key""")
    BWART = Column('BWART', String(3), primary_key = True, doc="""Sourced from T156T-BWART // Movement Type (Inventory Management)""")
    SOBKZ = Column('SOBKZ', String(1), primary_key = True, doc="""Sourced from T156T-SOBKZ // Special Stock Indicator""")
    KZBEW = Column('KZBEW', String(1), primary_key = True, doc="""Sourced from T156T-KZBEW // Movement Indicator""")
    KZZUG = Column('KZZUG', String(1), primary_key = True, doc="""Sourced from T156T-KZZUG // Receipt Indicator""")
    KZVBR = Column('KZVBR', String(1), primary_key = True, doc="""Sourced from T156T-KZVBR // Consumption Posting""")
    BTEXT = Column('BTEXT', String(20), default=None, doc="""Sourced from T156T-BTEXT // Movement Type Text (Inventory Management)""")

    language_cd = synonym('SPRAS')
    im_matl_mvmnt_type_cd = synonym('BWART')
    special_stock_cd = synonym('SOBKZ')
    movement_cd = synonym('KZBEW')
    stock_type_txt = synonym('BTEXT')


################################################################################




################################################################################

class SDOrderType(SAP_Base):
    """\
    Table sourced from: T176
    Description: Sales Documents: Customer Order Types
    """

    __tablename__ = "T176"

    BSARK = Column('BSARK', String(4), primary_key = True, doc="""Sourced from T176-BSARK // Customer purchase order type""")

    cust_prch_ord_type_cd = synonym('BSARK')


################################################################################




################################################################################

class SDOrderTypeDesc(SAP_Base):
    """\
    Table sourced from: T176T
    Description: Sales Documents: Customer Order Types: Texts
    """

    __tablename__ = "T176T"

    SPRAS = Column('SPRAS', String(1), primary_key = True, doc="""Sourced from T176T-SPRAS // Language Key""")
    BSARK = Column('BSARK', String(4), primary_key = True, doc="""Sourced from T176T-BSARK // Customer purchase order type""")
    VTEXT = Column('VTEXT', String(20), default=None, doc="""Sourced from T176T-VTEXT // Description""")

    language_cd = synonym('SPRAS')
    cust_prch_ord_type_cd = synonym('BSARK')


################################################################################




################################################################################

class ProductHierarchy(SAP_Base):
    """\
    Table sourced from: T179
    Description: Materials: Product Hierarchies
    """

    __tablename__ = "T179"

    PRODH = Column('PRODH', String(18), primary_key = True, doc="""Sourced from T179-PRODH // Product hierarchy""")
    STUFE = Column('STUFE', Numeric(15,3,3), default=None, doc="""Sourced from T179-STUFE // Number of the level in the product hierarchy""")




################################################################################




################################################################################

class ProductHierarchyDesc(SAP_Base):
    """\
    Table sourced from: T179T
    Description: Materials: Product hierarchies: Texts
    """

    __tablename__ = "T179T"

    SPRAS = Column('SPRAS', String(1), primary_key = True, doc="""Sourced from T179T-SPRAS // Language Key""")
    PRODH = Column('PRODH', String(18), primary_key = True, doc="""Sourced from T179T-PRODH // Product hierarchy""")
    VTEXT = Column('VTEXT', String(40), default=None, doc="""Sourced from T179T-VTEXT // Description""")

    language_cd = synonym('SPRAS')


################################################################################




################################################################################

class Incoterm(SAP_Base):
    """\
    Table sourced from: TINC
    Description: Customers: Incoterms
    """

    __tablename__ = "TINC"

    INCO1 = Column('INCO1', String(3), primary_key = True, doc="""Sourced from TINC-INCO1 // Incoterms (Part 1)""")
    ORTOB = Column('ORTOB', Boolean, default=None, doc="""Sourced from TINC-ORTOB // Location is mandatory""")
    OITITLE = Column('OITITLE', String(1), default=None, doc="""Sourced from TINC-OITITLE // Location of title transfer for Incoterms purposes""")
    OIG_GLPOD = Column('OIG_GLPOD', String(1), default=None, doc="""Sourced from TINC-OIG_GLPOD // Goods issue at loading, proof of delivery (POD)""")

    incoterms_cd = synonym('INCO1')


################################################################################




################################################################################

class IncotermDesc(SAP_Base):
    """\
    Table sourced from: TINCT
    Description: Customers: Incoterms: Texts
    """

    __tablename__ = "TINCT"

    SPRAS = Column('SPRAS', String(1), primary_key = True, doc="""Sourced from TINCT-SPRAS // Language Key""")
    INCO1 = Column('INCO1', String(3), primary_key = True, doc="""Sourced from TINCT-INCO1 // Incoterms (Part 1)""")
    BEZEI = Column('BEZEI', String(30), default=None, doc="""Sourced from TINCT-BEZEI // Description""")

    language_cd = synonym('SPRAS')
    incoterms_cd = synonym('INCO1')
    cntrl_area_nm = synonym('BEZEI')


################################################################################




################################################################################

class DeliveryPriority(SAP_Base):
    """\
    Table sourced from: TPRIO
    Description: Customers: Delivery Priorities
    """

    __tablename__ = "TPRIO"

    LPRIO = Column('LPRIO', String(2), primary_key = True, doc="""Sourced from TPRIO-LPRIO // Delivery Priority""")
    APRIO = Column('APRIO', String(1), default=None, doc="""Sourced from TPRIO-APRIO // Order priority""")

    delivery_priority_cd = synonym('LPRIO')


################################################################################




################################################################################

class SalesDivisions(SAP_Base):
    """\
    Table sourced from: TSPA
    Description: Organizational Unit: Sales Divisions
    """

    __tablename__ = "TSPA"

    SPART = Column('SPART', String(2), primary_key = True, doc="""Sourced from TSPA-SPART // Division""")

    div_cd = synonym('SPART')


################################################################################




################################################################################

class SalesOffices(SAP_Base):
    """\
    Table sourced from: TVBUR
    Description: Organizational Unit: Sales Offices
    """

    __tablename__ = "TVBUR"

    VKBUR = Column('VKBUR', String(4), primary_key = True, doc="""Sourced from TVBUR-VKBUR // Sales Office""")
    ADRNR = Column('ADRNR', String(10), default=None, doc="""Sourced from TVBUR-ADRNR // Address""")
    ERNAM = Column('ERNAM', String(12), default=None, doc="""Sourced from TVBUR-ERNAM // User Who Created Data Record""")
    TXNAM_ADR = Column('TXNAM_ADR', String(16), default=None, doc="""Sourced from TVBUR-TXNAM_ADR // Text name for form text module short address""")
    TXNAM_KOP = Column('TXNAM_KOP', String(16), default=None, doc="""Sourced from TVBUR-TXNAM_KOP // Text name for form text module letter header""")
    TXNAM_FUS = Column('TXNAM_FUS', String(16), default=None, doc="""Sourced from TVBUR-TXNAM_FUS // Text name for formula text module footer lines""")
    TXNAM_GRU = Column('TXNAM_GRU', String(16), default=None, doc="""Sourced from TVBUR-TXNAM_GRU // Text name for form text module: Greeting""")
    TXNAM_SDB = Column('TXNAM_SDB', String(16), default=None, doc="""Sourced from TVBUR-TXNAM_SDB // Text names for layout-set module SDS sender""")
    ISPVKBURUE = Column('ISPVKBURUE', String(4), default=None, doc="""Sourced from TVBUR-ISPVKBURUE // IS-M: Higher level sales office""")

    sales_office_id = synonym('VKBUR')
    addr_id = synonym('ADRNR')
    doc_create_user_id = synonym('ERNAM')


################################################################################




################################################################################

class SalesGroups(SAP_Base):
    """\
    Table sourced from: TVBVK
    Description: Organizational Unit: Sales Groups per Sales Office
    """

    __tablename__ = "TVBVK"

    VKBUR = Column('VKBUR', String(4), primary_key = True, doc="""Sourced from TVBVK-VKBUR // Sales Office""")
    VKGRP = Column('VKGRP', String(3), primary_key = True, doc="""Sourced from TVBVK-VKGRP // Sales Group""")

    sales_office_id = synonym('VKBUR')
    sales_group_id = synonym('VKGRP')


################################################################################




################################################################################

class BillDocTypes(SAP_Base):
    """\
    Table sourced from: TVFK
    Description: Billing: Document Types
    """

    __tablename__ = "TVFK"

    FKART = Column('FKART', String(4), primary_key = True, doc="""Sourced from TVFK-FKART // Billing Type""")
    KOPGR = Column('KOPGR', String(4), default=None, doc="""Sourced from TVFK-KOPGR // Screen sequence group in doc. header""")
    NUMKI = Column('NUMKI', String(2), default=None, doc="""Sourced from TVFK-NUMKI // Number range in the case of internal number assignment""")
    NUMKE = Column('NUMKE', String(2), default=None, doc="""Sourced from TVFK-NUMKE // Number range in the case of external number assignment""")
    INCPO = Column('INCPO', String(6), default=None, doc="""Sourced from TVFK-INCPO // Increment of item number in the SD document""")
    KUNN0 = Column('KUNN0', String(1), default=None, doc="""Sourced from TVFK-KUNN0 // Billing type for rebate processing""")
    UEVOR = Column('UEVOR', String(4), default=None, doc="""Sourced from TVFK-UEVOR // F-code default for overview screen""")
    UMFNG = Column('UMFNG', String(20), default=None, doc="""Sourced from TVFK-UMFNG // Display Range""")
    RFBFK = Column('RFBFK', Boolean, default=None, doc="""Sourced from TVFK-RFBFK // Blocked for transfer to accounting""")
    TRVOG = Column('TRVOG', String(1), default=None, doc="""Sourced from TVFK-TRVOG // Transaction group""")
    TXN08 = Column('TXN08', String(8), default=None, doc="""Sourced from TVFK-TXN08 // Number of the standard text""")
    VBTYP = Column('VBTYP', String(1), default=None, doc="""Sourced from TVFK-VBTYP // SD document category""")
    ERNAM = Column('ERNAM', String(12), default=None, doc="""Sourced from TVFK-ERNAM // Name of Person who Created the Object""")
    PARGK = Column('PARGK', String(4), default=None, doc="""Sourced from TVFK-PARGK // Partner determination procedure for the billing doc.header""")
    PARGP = Column('PARGP', String(4), default=None, doc="""Sourced from TVFK-PARGP // Partner determination procedure for the billing doc.item""")
    KALSMC = Column('KALSMC', String(6), default=None, doc="""Sourced from TVFK-KALSMC // Account determination procedure""")
    FKARTS = Column('FKARTS', String(4), default=None, doc="""Sourced from TVFK-FKARTS // Billing type for cancellation""")
    TXTGR = Column('TXTGR', String(2), default=None, doc="""Sourced from TVFK-TXTGR // Text determination procedure""")
    KAPPL = Column('KAPPL', String(2), default=None, doc="""Sourced from TVFK-KAPPL // Application for output conditions""")
    KALSM = Column('KALSM', String(6), default=None, doc="""Sourced from TVFK-KALSM // Output determination procedure""")
    KSCHL = Column('KSCHL', String(4), default=None, doc="""Sourced from TVFK-KSCHL // Output Type""")
    STAFO = Column('STAFO', String(6), default=None, doc="""Sourced from TVFK-STAFO // Update group for statistics update""")
    KVSLV = Column('KVSLV', String(3), default=None, doc="""Sourced from TVFK-KVSLV // Account key for cash allocation""")
    KALVG = Column('KALVG', String(1), default=None, doc="""Sourced from TVFK-KALVG // Document procedure (for determining pricing procedure)""")
    TXTGR_P = Column('TXTGR_P', String(2), default=None, doc="""Sourced from TVFK-TXTGR_P // Text determination procedure for billing item""")
    STATI = Column('STATI', Boolean, default=None, doc="""Sourced from TVFK-STATI // Update statistics""")
    KALSMBP = Column('KALSMBP', String(6), default=None, doc="""Sourced from TVFK-KALSMBP // Procedure for item output""")
    BORVF = Column('BORVF', Boolean, default=None, doc="""Sourced from TVFK-BORVF // Billing document is relevant for rebate processing""")
    FKART_RL = Column('FKART_RL', String(4), default=None, doc="""Sourced from TVFK-FKART_RL // Invoice list type""")
    RELEP = Column('RELEP', Boolean, default=None, doc="""Sourced from TVFK-RELEP // Forward invoice lists with line items to FI""")
    TXTLF = Column('TXTLF', Boolean, default=None, doc="""Sourced from TVFK-TXTLF // Copy texts from delivery note""")
    HITYP_PR = Column('HITYP_PR', String(1), default=None, doc="""Sourced from TVFK-HITYP_PR // Hierarchy type for pricing""")
    FKART_AB = Column('FKART_AB', String(4), default=None, doc="""Sourced from TVFK-FKART_AB // Accrual billing type""")
    GRBED_S = Column('GRBED_S', String(3), default=None, doc="""Sourced from TVFK-GRBED_S // Copying requirements""")
    ORDNR_FI_S = Column('ORDNR_FI_S', String(1), default=None, doc="""Sourced from TVFK-ORDNR_FI_S // Allocation number FI""")
    XBLNR_FI_S = Column('XBLNR_FI_S', String(1), default=None, doc="""Sourced from TVFK-XBLNR_FI_S // FI reference number""")
    J_1BNFREL = Column('J_1BNFREL', String(1), default=None, doc="""Sourced from TVFK-J_1BNFREL // Nota Fiscal Relevance""")
    J_1BMAINPA = Column('J_1BMAINPA', String(2), default=None, doc="""Sourced from TVFK-J_1BMAINPA // Main partner function ID (e.g. SH for ship-to party)""")
    J_1BTDIDH = Column('J_1BTDIDH', String(4), default=None, doc="""Sourced from TVFK-J_1BTDIDH // Text Id. Nota Fiscal header""")
    J_1BTDCOH = Column('J_1BTDCOH', String(1), default=None, doc="""Sourced from TVFK-J_1BTDCOH // Number of text lines header""")
    J_1BTDIDL = Column('J_1BTDIDL', String(4), default=None, doc="""Sourced from TVFK-J_1BTDIDL // Text Id Nota Fiscal lines""")
    J_1BTDCOL = Column('J_1BTDCOL', String(1), default=None, doc="""Sourced from TVFK-J_1BTDCOL // Counter Number of text lines NF line""")
    FKTYP = Column('FKTYP', String(1), default=None, doc="""Sourced from TVFK-FKTYP // Billing category""")
    XNEGP = Column('XNEGP', String(1), default=None, doc="""Sourced from TVFK-XNEGP // Negative posting""")
    BLART = Column('BLART', String(2), default=None, doc="""Sourced from TVFK-BLART // Document Type""")
    XFILKD = Column('XFILKD', String(1), default=None, doc="""Sourced from TVFK-XFILKD // Branch/head office relationship""")
    XVALGS = Column('XVALGS', Boolean, default=None, doc="""Sourced from TVFK-XVALGS // Credit memo with value date""")
    KALSMCA = Column('KALSMCA', String(6), default=None, doc="""Sourced from TVFK-KALSMCA // Pricing procedure for account determination extra pay""")
    KALSMCB = Column('KALSMCB', String(6), default=None, doc="""Sourced from TVFK-KALSMCB // Pricing procedure for acc. determ. reconciliation account""")
    KALSMCC = Column('KALSMCC', String(6), default=None, doc="""Sourced from TVFK-KALSMCC // Pricing procedure for account determination cash settlement""")
    KALSMCD = Column('KALSMCD', String(6), default=None, doc="""Sourced from TVFK-KALSMCD // Pricing procedure for account determination payment cards""")
    XKOIV = Column('XKOIV', Boolean, default=None, doc="""Sourced from TVFK-XKOIV // Account assignment offsetting entry in intercompany billing""")
    J_1AINVREF = Column('J_1AINVREF', String(1), default=None, doc="""Sourced from TVFK-J_1AINVREF // Invoice reference in billing document""")
    J_1ACPDEL = Column('J_1ACPDEL', Boolean, default=None, doc="""Sourced from TVFK-J_1ACPDEL // Indicator: Copy branch from Delivery note""")
    UVEIB = Column('UVEIB', String(3), default=None, doc="""Sourced from TVFK-UVEIB // Doc. pricing procedure for incomplete export/import data""")
    FKART_MEV_RESET = Column('FKART_MEV_RESET', String(4), default=None, doc="""Sourced from TVFK-FKART_MEV_RESET // Billing Document Type for Period-End Reset""")
    VBTYP_EXT = Column('VBTYP_EXT', String(4), default=None, doc="""Sourced from TVFK-VBTYP_EXT // Extension of SD Document Category""")
    ISM_XKRVO = Column('ISM_XKRVO', Boolean, default=None, doc="""Sourced from TVFK-ISM_XKRVO // IS-M: Credit-Side Transaction Indicator""")
    OICINPD = Column('OICINPD', String(1), default=None, doc="""Sourced from TVFK-OICINPD // Invoice pricing date rule""")
    OIFEEPD = Column('OIFEEPD', String(1), default=None, doc="""Sourced from TVFK-OIFEEPD // Fee pricing date""")
    OIINVCYC1 = Column('OIINVCYC1', String(1), default=None, doc="""Sourced from TVFK-OIINVCYC1 // Invoice cycle indicator active (X/ )""")
    OIINVCYC2 = Column('OIINVCYC2', String(1), default=None, doc="""Sourced from TVFK-OIINVCYC2 // Invoice cycle indicator active (X/ )""")
    OIINVCYC3 = Column('OIINVCYC3', String(1), default=None, doc="""Sourced from TVFK-OIINVCYC3 // Invoice cycle indicator active (X/ )""")
    OIINVCYC4 = Column('OIINVCYC4', String(1), default=None, doc="""Sourced from TVFK-OIINVCYC4 // Invoice cycle indicator active (X/ )""")
    OIINVCYC5 = Column('OIINVCYC5', String(1), default=None, doc="""Sourced from TVFK-OIINVCYC5 // Invoice cycle indicator active (X/ )""")
    OIINVCYC6 = Column('OIINVCYC6', String(1), default=None, doc="""Sourced from TVFK-OIINVCYC6 // Invoice cycle indicator active (X/ )""")
    OIINVCYC7 = Column('OIINVCYC7', String(1), default=None, doc="""Sourced from TVFK-OIINVCYC7 // Invoice cycle indicator active (X/ )""")
    OIINVCYC8 = Column('OIINVCYC8', String(1), default=None, doc="""Sourced from TVFK-OIINVCYC8 // Invoice cycle indicator active (X/ )""")
    OIINVCYC9 = Column('OIINVCYC9', String(1), default=None, doc="""Sourced from TVFK-OIINVCYC9 // Invoice cycle indicator active (X/ )""")
    OINETEXIT = Column('OINETEXIT', String(3), default=None, doc="""Sourced from TVFK-OINETEXIT // User exit for netting cycle determination""")
    OIPTRMEX = Column('OIPTRMEX', String(3), default=None, doc="""Sourced from TVFK-OIPTRMEX // Payment term transfer to VBRK""")
    OIC_DIFFIN = Column('OIC_DIFFIN', String(1), default=None, doc="""Sourced from TVFK-OIC_DIFFIN // Differential invoice""")
    OIC_DICNTR = Column('OIC_DICNTR', String(1), default=None, doc="""Sourced from TVFK-OIC_DICNTR // Differential invoice control""")
    OIC_ACCVAL = Column('OIC_ACCVAL', String(3), default=None, doc="""Sourced from TVFK-OIC_ACCVAL // User exit to accumulate already-invoiced values""")
    OIC_ERRHA = Column('OIC_ERRHA', String(3), default=None, doc="""Sourced from TVFK-OIC_ERRHA // User exit for error handling/no breakdown of diff. amount""")
    OIC_FKART = Column('OIC_FKART', String(4), default=None, doc="""Sourced from TVFK-OIC_FKART // Default billing type for cancel / rebill""")
    OISELEXIT = Column('OISELEXIT', String(3), default=None, doc="""Sourced from TVFK-OISELEXIT // Movements index selection exit""")
    OIFINEXIT = Column('OIFINEXIT', String(3), default=None, doc="""Sourced from TVFK-OIFINEXIT // Financial document selection exit""")
    OINETRPT = Column('OINETRPT', String(40), default=None, doc="""Sourced from TVFK-OINETRPT // ABAP Program Name""")
    OIBTCEXIT = Column('OIBTCEXIT', String(3), default=None, doc="""Sourced from TVFK-OIBTCEXIT // BTCI generation exit for movements based netting""")
    OIAMWOFI = Column('OIAMWOFI', String(1), default=None, doc="""Sourced from TVFK-OIAMWOFI // Movements without financials indicator""")
    OIABALAN = Column('OIABALAN', String(1), default=None, doc="""Sourced from TVFK-OIABALAN // Include balances indicator""")
    OIINVAPP = Column('OIINVAPP', String(1), default=None, doc="""Sourced from TVFK-OIINVAPP // Invoice Approval Process (IAP) active flag""")
    OIINDCM = Column('OIINDCM', String(1), default=None, doc="""Sourced from TVFK-OIINDCM // Active flag f. Document Change Management (DCM) for invoice""")

    billing_type_cd = synonym('FKART')
    transaction_group_id = synonym('TRVOG')
    sd_doc_ctgy_cd = synonym('VBTYP')
    doc_create_user_id = synonym('ERNAM')
    bill_doc_rebate_rlvnt_ind = synonym('BORVF')
    pricing_hierarchy_type_cd = synonym('HITYP_PR')
    billing_ctgy_cd = synonym('FKTYP')
    doc_type_cd = synonym('BLART')


################################################################################




################################################################################

class SalesGroupDesc(SAP_Base):
    """\
    Table sourced from: TVGRT
    Description: Organizational Unit: Sales Groups: Texts
    """

    __tablename__ = "TVGRT"

    SPRAS = Column('SPRAS', String(1), primary_key = True, doc="""Sourced from TVGRT-SPRAS // Language Key""")
    VKGRP = Column('VKGRP', String(3), primary_key = True, doc="""Sourced from TVGRT-VKGRP // Sales Group""")
    BEZEI = Column('BEZEI', String(20), default=None, doc="""Sourced from TVGRT-BEZEI // Description""")

    language_cd = synonym('SPRAS')
    sales_group_id = synonym('VKGRP')
    cntrl_area_nm = synonym('BEZEI')


################################################################################




################################################################################

class SalesOfficeDesc(SAP_Base):
    """\
    Table sourced from: TVKBT
    Description: Organizational Unit: Sales Offices: Texts
    """

    __tablename__ = "TVKBT"

    SPRAS = Column('SPRAS', String(1), primary_key = True, doc="""Sourced from TVKBT-SPRAS // Language Key""")
    VKBUR = Column('VKBUR', String(4), primary_key = True, doc="""Sourced from TVKBT-VKBUR // Sales Office""")
    BEZEI = Column('BEZEI', String(20), default=None, doc="""Sourced from TVKBT-BEZEI // Description""")

    language_cd = synonym('SPRAS')
    sales_office_id = synonym('VKBUR')
    cntrl_area_nm = synonym('BEZEI')


################################################################################




################################################################################

class SalesOfficeOrgUnit(SAP_Base):
    """\
    Table sourced from: TVKBZ
    Description: Org.Unit: Sales Office: Assignment to Organizational Unit
    """

    __tablename__ = "TVKBZ"

    VKORG = Column('VKORG', String(4), primary_key = True, doc="""Sourced from TVKBZ-VKORG // Sales Organization""")
    VTWEG = Column('VTWEG', String(2), primary_key = True, doc="""Sourced from TVKBZ-VTWEG // Distribution Channel""")
    SPART = Column('SPART', String(2), primary_key = True, doc="""Sourced from TVKBZ-SPART // Division""")
    VKBUR = Column('VKBUR', String(4), primary_key = True, doc="""Sourced from TVKBZ-VKBUR // Sales Office""")

    sales_org_cd = synonym('VKORG')
    distr_chan_cd = synonym('VTWEG')
    div_cd = synonym('SPART')
    sales_office_id = synonym('VKBUR')


################################################################################




################################################################################

class SalesOrg(SAP_Base):
    """\
    Table sourced from: TVKO
    Description: Organizational Unit: Sales Organizations
    """

    __tablename__ = "TVKO"

    VKORG = Column('VKORG', String(4), primary_key = True, doc="""Sourced from TVKO-VKORG // Sales Organization""")
    WAERS = Column('WAERS', String(5), default=None, doc="""Sourced from TVKO-WAERS // Statistics currency""")
    BUKRS = Column('BUKRS', String(4), default=None, doc="""Sourced from TVKO-BUKRS // Company code of the sales organization""")
    ADRNR = Column('ADRNR', String(10), default=None, doc="""Sourced from TVKO-ADRNR // Address""")
    TXNAM_ADR = Column('TXNAM_ADR', String(16), default=None, doc="""Sourced from TVKO-TXNAM_ADR // Text name for form text module short address""")
    TXNAM_KOP = Column('TXNAM_KOP', String(16), default=None, doc="""Sourced from TVKO-TXNAM_KOP // Text name for form text module letter header""")
    TXNAM_FUS = Column('TXNAM_FUS', String(16), default=None, doc="""Sourced from TVKO-TXNAM_FUS // Text name for formula text module footer lines""")
    TXNAM_GRU = Column('TXNAM_GRU', String(16), default=None, doc="""Sourced from TVKO-TXNAM_GRU // Text name for form text module: Greeting""")
    VKOAU = Column('VKOAU', String(4), default=None, doc="""Sourced from TVKO-VKOAU // Reference sales org.for sales doc.types (by sales area)""")
    KUNNR = Column('KUNNR', String(10), default=None, doc="""Sourced from TVKO-KUNNR // Customer number for intercompany billing""")
    BOAVO = Column('BOAVO', Boolean, default=None, doc="""Sourced from TVKO-BOAVO // Rebate processing active in the sales organization""")
    VKOKL = Column('VKOKL', String(2), default=None, doc="""Sourced from TVKO-VKOKL // Sales organization calendar""")
    EKORG = Column('EKORG', String(4), default=None, doc="""Sourced from TVKO-EKORG // Purchasing Organization""")
    EKGRP = Column('EKGRP', String(3), default=None, doc="""Sourced from TVKO-EKGRP // Purchasing Group""")
    LIFNR = Column('LIFNR', String(10), default=None, doc="""Sourced from TVKO-LIFNR // Account Number of Vendor or Creditor""")
    WERKS = Column('WERKS', String(4), default=None, doc="""Sourced from TVKO-WERKS // Plant""")
    BSART = Column('BSART', String(4), default=None, doc="""Sourced from TVKO-BSART // Order Type (Purchasing)""")
    BSTYP = Column('BSTYP', String(1), default=None, doc="""Sourced from TVKO-BSTYP // Purchasing Document Category""")
    BWART = Column('BWART', String(3), default=None, doc="""Sourced from TVKO-BWART // Movement Type (Inventory Management)""")
    LGORT = Column('LGORT', String(4), default=None, doc="""Sourced from TVKO-LGORT // Storage Location""")
    TXNAM_SDB = Column('TXNAM_SDB', String(16), default=None, doc="""Sourced from TVKO-TXNAM_SDB // Text names for layout-set module SDS sender""")
    MWSKZ = Column('MWSKZ', String(2), default=None, doc="""Sourced from TVKO-MWSKZ // Tax code for SD documents""")
    XSTCEG = Column('XSTCEG', String(1), default=None, doc="""Sourced from TVKO-XSTCEG // Determining the VAT registration number""")
    J_1ANUTIME = Column('J_1ANUTIME', String(1), default=None, doc="""Sourced from TVKO-J_1ANUTIME // Time of numbering for deliveries""")
    MAXBI = Column('MAXBI', String(3), default=None, doc="""Sourced from TVKO-MAXBI // Maximum Number of Items in Billing Document""")
    PLAUFZ = Column('PLAUFZ', String(3), default=None, doc="""Sourced from TVKO-PLAUFZ // Price protection period""")
    PLAUEZ = Column('PLAUEZ', String(1), default=None, doc="""Sourced from TVKO-PLAUEZ // Unit for price protection""")

    sales_org_cd = synonym('VKORG')
    currency_cd = synonym('WAERS')
    company_cd = synonym('BUKRS')
    addr_id = synonym('ADRNR')
    customer_id = synonym('KUNNR')
    sales_org_rebate_proc_active_ind = synonym('BOAVO')
    sales_org_calendar_id = synonym('VKOKL')
    prch_org_cd = synonym('EKORG')
    prch_grp_cd = synonym('EKGRP')
    prch_ord_type_cd = synonym('BSART')
    prch_doc_ctgy_cd = synonym('BSTYP')
    im_matl_mvmnt_type_cd = synonym('BWART')
    bill_doc_max_item_count = synonym('MAXBI')


################################################################################




################################################################################

class SalesOrgDivisions(SAP_Base):
    """\
    Table sourced from: TVKOS
    Description: Organizational Unit: Divisions per Sales Organization
    """

    __tablename__ = "TVKOS"

    VKORG = Column('VKORG', String(4), primary_key = True, doc="""Sourced from TVKOS-VKORG // Sales Organization""")
    SPART = Column('SPART', String(2), primary_key = True, doc="""Sourced from TVKOS-SPART // Division""")
    SPAKU = Column('SPAKU', String(2), default=None, doc="""Sourced from TVKOS-SPAKU // Reference division for customers""")
    SPAKO = Column('SPAKO', String(2), default=None, doc="""Sourced from TVKOS-SPAKO // Reference division for conditions""")
    SPAAU = Column('SPAAU', String(2), default=None, doc="""Sourced from TVKOS-SPAAU // Reference division for document types (by sales area)""")

    sales_org_cd = synonym('VKORG')
    div_cd = synonym('SPART')


################################################################################




################################################################################

class SalesOrgDistrChan(SAP_Base):
    """\
    Table sourced from: TVKOV
    Description: Org. Unit: Distribution Channels per Sales Organization
    """

    __tablename__ = "TVKOV"

    VKORG = Column('VKORG', String(4), primary_key = True, doc="""Sourced from TVKOV-VKORG // Sales Organization""")
    VTWEG = Column('VTWEG', String(2), primary_key = True, doc="""Sourced from TVKOV-VTWEG // Distribution Channel""")
    VTWKO = Column('VTWKO', String(2), default=None, doc="""Sourced from TVKOV-VTWKO // Reference distribution channel for conditions""")
    VTWAU = Column('VTWAU', String(2), default=None, doc="""Sourced from TVKOV-VTWAU // Distribution channel for sales doc types""")
    VTWKU = Column('VTWKU', String(2), default=None, doc="""Sourced from TVKOV-VTWKU // Reference distrib.channel for cust.and material masters""")
    VLGFI = Column('VLGFI', String(4), default=None, doc="""Sourced from TVKOV-VLGFI // Reference Plant of the Category 'Store' (Material Master)""")
    VLTYP = Column('VLTYP', String(1), default=None, doc="""Sourced from TVKOV-VLTYP // Distribution chain category""")
    VLKEB = Column('VLKEB', String(1), default=None, doc="""Sourced from TVKOV-VLKEB // Allowed pricing levels below distribution chain level""")

    sales_org_cd = synonym('VKORG')
    distr_chan_cd = synonym('VTWEG')
    sd_doc_type_distr_chan_cd = synonym('VTWAU')


################################################################################




################################################################################

class SD_ItemCtgy(SAP_Base):
    """\
    Table sourced from: TVPT
    Description: Sales documents: Item categories
    """

    __tablename__ = "TVPT"

    PSTYV = Column('PSTYV', String(4), primary_key = True, doc="""Sourced from TVPT-PSTYV // Sales document item category""")
    PSTYO = Column('PSTYO', String(1), default=None, doc="""Sourced from TVPT-PSTYO // Object for which you define the item category""")

    sd_item_ctgy_cd = synonym('PSTYV')


################################################################################




################################################################################

class ShipPointOrgUnit(SAP_Base):
    """\
    Table sourced from: TVST
    Description: Organizational Unit: Shipping Points
    """

    __tablename__ = "TVST"

    VSTEL = Column('VSTEL', String(4), primary_key = True, doc="""Sourced from TVST-VSTEL // Shipping Point/Receiving Point""")
    FABKL = Column('FABKL', String(2), default=None, doc="""Sourced from TVST-FABKL // Factory calendar key""")
    VTRZT = Column('VTRZT', Numeric(15,3,3), default=None, doc="""Sourced from TVST-VTRZT // Rounding-up period for delivery scheduling (in days)""")
    ADRNR = Column('ADRNR', String(10), default=None, doc="""Sourced from TVST-ADRNR // Address""")
    ALAND = Column('ALAND', String(3), default=None, doc="""Sourced from TVST-ALAND // Departure country (country from which the goods are sent)""")
    AZONE = Column('AZONE', String(10), default=None, doc="""Sourced from TVST-AZONE // Departure zone""")
    TXNAM_ADR = Column('TXNAM_ADR', String(16), default=None, doc="""Sourced from TVST-TXNAM_ADR // Text name for form text module short address""")
    TXNAM_KOP = Column('TXNAM_KOP', String(16), default=None, doc="""Sourced from TVST-TXNAM_KOP // Text name for form text module letter header""")
    TXNAM_FUS = Column('TXNAM_FUS', String(16), default=None, doc="""Sourced from TVST-TXNAM_FUS // Text name for formula text module footer lines""")
    TXNAM_GRU = Column('TXNAM_GRU', String(16), default=None, doc="""Sourced from TVST-TXNAM_GRU // Text name for form text module: Greeting""")
    KSCHL = Column('KSCHL', String(4), default=None, doc="""Sourced from TVST-KSCHL // Output Type""")
    SPRAS = Column('SPRAS', String(1), default=None, doc="""Sourced from TVST-SPRAS // Message language""")
    ANZAL = Column('ANZAL', Numeric(15,3,3), default=None, doc="""Sourced from TVST-ANZAL // Number of messages (original + copies)""")
    VSZTP = Column('VSZTP', String(1), default=None, doc="""Sourced from TVST-VSZTP // Dispatch time""")
    NACHA = Column('NACHA', String(1), default=None, doc="""Sourced from TVST-NACHA // Message transmission medium""")
    LAZBS = Column('LAZBS', String(1), default=None, doc="""Sourced from TVST-LAZBS // Determine loading time""")
    RIZBS = Column('RIZBS', String(1), default=None, doc="""Sourced from TVST-RIZBS // Determine pick/pack time""")
    LAZZT = Column('LAZZT', Numeric(15,3,3), default=None, doc="""Sourced from TVST-LAZZT // Default loading time""")
    RIZZT = Column('RIZZT', Numeric(15,3,3), default=None, doc="""Sourced from TVST-RIZZT // Default pick/pack time""")
    KOQUI = Column('KOQUI', String(1), default=None, doc="""Sourced from TVST-KOQUI // Subject to pick confirmation""")
    KOMSU = Column('KOMSU', String(10), default=None, doc="""Sourced from TVST-KOMSU // Picking subsystem""")
    IMESS = Column('IMESS', Boolean, default=None, doc="""Sourced from TVST-IMESS // Display information messages in collective processing log""")
    TXNAM_SDB = Column('TXNAM_SDB', String(16), default=None, doc="""Sourced from TVST-TXNAM_SDB // Text names for layout-set module SDS sender""")
    ALW_SW = Column('ALW_SW', Boolean, default=None, doc="""Sourced from TVST-ALW_SW // Switch: use route schedules""")
    LOADTG = Column('LOADTG', Numeric(15,3,3), default=None, doc="""Sourced from TVST-LOADTG // Gross loading time (ignoring work times)""")
    LOADTN = Column('LOADTN', Numeric(15,3,3), default=None, doc="""Sourced from TVST-LOADTN // Loading time in working hours""")
    PIPATG = Column('PIPATG', Numeric(15,3,3), default=None, doc="""Sourced from TVST-PIPATG // Pick/pack time in workdays""")
    PIPATN = Column('PIPATN', Numeric(15,3,3), default=None, doc="""Sourced from TVST-PIPATN // Pick/pack time in work hours""")
    TSTRID = Column('TSTRID', String(10), default=None, doc="""Sourced from TVST-TSTRID // Working time from sales view""")
    ROUNDG = Column('ROUNDG', Numeric(15,3,3), default=None, doc="""Sourced from TVST-ROUNDG // Rounding period for shipping scheduling""")
    ROUNDN = Column('ROUNDN', Numeric(15,3,3), default=None, doc="""Sourced from TVST-ROUNDN // Rounding period in work hours""")

    shipping_receiving_point_cd = synonym('VSTEL')
    factory_calendar_cd = synonym('FABKL')
    addr_id = synonym('ADRNR')
    depart_country_cd = synonym('ALAND')
    language_cd = synonym('SPRAS')
    pick_pack_work_day_qty = synonym('PIPATG')
    pick_pack_work_hour_qty = synonym('PIPATN')


################################################################################




################################################################################

class FacilityShipPoint(SAP_Base):
    """\
    Table sourced from: TVSWZ
    Description: Shipping Points per Plant
    """

    __tablename__ = "TVSWZ"

    WERKS = Column('WERKS', String(4), primary_key = True, doc="""Sourced from TVSWZ-WERKS // Plant""")
    VSTEL = Column('VSTEL', String(4), primary_key = True, doc="""Sourced from TVSWZ-VSTEL // Shipping Point/Receiving Point""")

    shipping_receiving_point_cd = synonym('VSTEL')


################################################################################




################################################################################

class SalesAreaOrgUnit(SAP_Base):
    """\
    Table sourced from: TVTA
    Description: Organizational Unit: Sales Area(s)
    """

    __tablename__ = "TVTA"

    VKORG = Column('VKORG', String(4), primary_key = True, doc="""Sourced from TVTA-VKORG // Sales Organization""")
    VTWEG = Column('VTWEG', String(2), primary_key = True, doc="""Sourced from TVTA-VTWEG // Distribution Channel""")
    SPART = Column('SPART', String(2), primary_key = True, doc="""Sourced from TVTA-SPART // Division""")
    VTWKU = Column('VTWKU', String(2), default=None, doc="""Sourced from TVTA-VTWKU // Reference distrib.channel for cust.and material masters""")
    SPAKU = Column('SPAKU', String(2), default=None, doc="""Sourced from TVTA-SPAKU // Reference division for customers""")
    VTWKO = Column('VTWKO', String(2), default=None, doc="""Sourced from TVTA-VTWKO // Reference distribution channel for conditions""")
    SPAKO = Column('SPAKO', String(2), default=None, doc="""Sourced from TVTA-SPAKO // Reference division for conditions""")
    MABER = Column('MABER', String(2), default=None, doc="""Sourced from TVTA-MABER // Dunning Area""")
    VKOAU = Column('VKOAU', String(4), default=None, doc="""Sourced from TVTA-VKOAU // Reference sales org.for sales doc.types (by sales area)""")
    VTWAU = Column('VTWAU', String(2), default=None, doc="""Sourced from TVTA-VTWAU // Distribution channel for sales doc types""")
    SPAAU = Column('SPAAU', String(2), default=None, doc="""Sourced from TVTA-SPAAU // Reference division for document types (by sales area)""")
    GSBER = Column('GSBER', String(4), default=None, doc="""Sourced from TVTA-GSBER // Business Area""")
    REGGB = Column('REGGB', String(3), default=None, doc="""Sourced from TVTA-REGGB // Rule for determining the business area""")
    REVFP = Column('REVFP', String(1), default=None, doc="""Sourced from TVTA-REVFP // Rule for transferring the results of the availability check""")
    FIXMG = Column('FIXMG', Boolean, default=None, doc="""Sourced from TVTA-FIXMG // Delivery date and quantity fixed""")
    AFIND = Column('AFIND', Boolean, default=None, doc="""Sourced from TVTA-AFIND // Promo determination""")
    KKBER = Column('KKBER', String(4), default=None, doc="""Sourced from TVTA-KKBER // Credit Control Area""")
    J_1ASNR = Column('J_1ASNR', String(4), default=None, doc="""Sourced from TVTA-J_1ASNR // Branch for domestic operations""")
    J_1AESNR = Column('J_1AESNR', String(4), default=None, doc="""Sourced from TVTA-J_1AESNR // Branch for export operations""")
    ISP_VB = Column('ISP_VB', String(10), default=None, doc="""Sourced from TVTA-ISP_VB // IS-M: Distribution Zone""")
    ISM_BP_VTB_GROUP = Column('ISM_BP_VTB_GROUP', String(4), default=None, doc="""Sourced from TVTA-ISM_BP_VTB_GROUP // IS-M: Sales Area Group for Business Partner Selection""")
    J_3GKBAUL = Column('J_3GKBAUL', String(1), default=None, doc="""Sourced from TVTA-J_3GKBAUL // ETM-Relevant Indicator""")
    OID_CHECKC = Column('OID_CHECKC', String(1), default=None, doc="""Sourced from TVTA-OID_CHECKC // Check customer ship-to/sold-to warning/error/information""")

    sales_org_cd = synonym('VKORG')
    distr_chan_cd = synonym('VTWEG')
    div_cd = synonym('SPART')
    sd_doc_type_distr_chan_cd = synonym('VTWAU')
    deliv_dt_and_qty_fixed_ind = synonym('FIXMG')
    credit_control_area_cd = synonym('KKBER')


################################################################################




################################################################################

class DistrChanOrgUnit(SAP_Base):
    """\
    Table sourced from: TVTW
    Description: Organizational Unit: Distribution Channels
    """

    __tablename__ = "TVTW"

    VTWEG = Column('VTWEG', String(2), primary_key = True, doc="""Sourced from TVTW-VTWEG // Distribution Channel""")

    distr_chan_cd = synonym('VTWEG')


################################################################################




################################################################################

class SDIndexCredit(SAP_Base):
    """\
    Table sourced from: VAKCR
    Description: Sales Index: Orders in Credit Management
    """

    __tablename__ = "VAKCR"

    KKBER = Column('KKBER', String(4), primary_key = True, doc="""Sourced from VAKCR-KKBER // Credit Control Area""")
    CMGST = Column('CMGST', String(1), primary_key = True, doc="""Sourced from VAKCR-CMGST // Overall status of credit checks""")
    SBGRP = Column('SBGRP', String(3), primary_key = True, doc="""Sourced from VAKCR-SBGRP // Credit representative group for credit management""")
    CMNGV = Column('CMNGV', Date, primary_key = True, doc="""Sourced from VAKCR-CMNGV // Next date""")
    KNKLI = Column('KNKLI', String(10), primary_key = True, doc="""Sourced from VAKCR-KNKLI // Customer's account number with credit limit reference""")
    CTLPC = Column('CTLPC', String(3), primary_key = True, doc="""Sourced from VAKCR-CTLPC // Credit management: Risk category""")
    GRUPP = Column('GRUPP', String(4), primary_key = True, doc="""Sourced from VAKCR-GRUPP // Customer Credit Group""")
    CMFRE = Column('CMFRE', Date, primary_key = True, doc="""Sourced from VAKCR-CMFRE // Release date of the document determined by credit management""")
    CMNUP = Column('CMNUP', Date, primary_key = True, doc="""Sourced from VAKCR-CMNUP // Date of next credit check of document""")
    VKORG = Column('VKORG', String(4), primary_key = True, doc="""Sourced from VAKCR-VKORG // Sales Organization""")
    VTWEG = Column('VTWEG', String(2), primary_key = True, doc="""Sourced from VAKCR-VTWEG // Distribution Channel""")
    SPART = Column('SPART', String(2), primary_key = True, doc="""Sourced from VAKCR-SPART // Division""")
    VBELN = Column('VBELN', String(10), primary_key = True, doc="""Sourced from VAKCR-VBELN // Sales and Distribution Document Number""")

    credit_control_area_cd = synonym('KKBER')
    overall_credit_check_status_cd = synonym('CMGST')
    credit_mgmt_release_dt = synonym('CMFRE')
    next_credit_check_dt = synonym('CMNUP')
    sales_org_cd = synonym('VKORG')
    distr_chan_cd = synonym('VTWEG')
    div_cd = synonym('SPART')
    sd_doc_id = synonym('VBELN')


################################################################################




################################################################################

class SDIndexPartner(SAP_Base):
    """\
    Table sourced from: VAKPA
    Description: Sales Index: Orders by Partner Function
    """

    __tablename__ = "VAKPA"

    KUNDE = Column('KUNDE', String(10), primary_key = True, doc="""Sourced from VAKPA-KUNDE // Partner number (KUNNR, LIFNR, or PERNR)""")
    PARVW = Column('PARVW', String(2), primary_key = True, doc="""Sourced from VAKPA-PARVW // Partner Function""")
    VKORG = Column('VKORG', String(4), primary_key = True, doc="""Sourced from VAKPA-VKORG // Sales Organization""")
    TRVOG = Column('TRVOG', String(1), primary_key = True, doc="""Sourced from VAKPA-TRVOG // Transaction group""")
    AUDAT = Column('AUDAT', Date, primary_key = True, doc="""Sourced from VAKPA-AUDAT // Document Date (Date Received/Sent)""")
    VKBUR = Column('VKBUR', String(4), primary_key = True, doc="""Sourced from VAKPA-VKBUR // Sales Office""")
    VKGRP = Column('VKGRP', String(3), primary_key = True, doc="""Sourced from VAKPA-VKGRP // Sales Group""")
    VTWEG = Column('VTWEG', String(2), primary_key = True, doc="""Sourced from VAKPA-VTWEG // Distribution Channel""")
    SPART = Column('SPART', String(2), primary_key = True, doc="""Sourced from VAKPA-SPART // Division""")
    AUART = Column('AUART', String(4), primary_key = True, doc="""Sourced from VAKPA-AUART // Sales Document Type""")
    BSTNK = Column('BSTNK', String(20), primary_key = True, doc="""Sourced from VAKPA-BSTNK // Customer purchase order number""")
    KUNNR = Column('KUNNR', String(10), primary_key = True, doc="""Sourced from VAKPA-KUNNR // Sold-to party""")
    ERNAM = Column('ERNAM', String(12), primary_key = True, doc="""Sourced from VAKPA-ERNAM // Name of Person who Created the Object""")
    VBELN = Column('VBELN', String(10), primary_key = True, doc="""Sourced from VAKPA-VBELN // Sales and Distribution Document Number""")
    ADRNR_AG = Column('ADRNR_AG', String(10), default=None, doc="""Sourced from VAKPA-ADRNR_AG // Address number of the sold-to party""")
    ADRNR = Column('ADRNR', String(10), default=None, doc="""Sourced from VAKPA-ADRNR // Address""")
    DATAB = Column('DATAB', Date, default=None, doc="""Sourced from VAKPA-DATAB // Quotation or contract valid from""")
    DATBI = Column('DATBI', Date, default=None, doc="""Sourced from VAKPA-DATBI // Quotation or contract valid to""")

    partner_function_cd = synonym('PARVW')
    sales_org_cd = synonym('VKORG')
    transaction_group_id = synonym('TRVOG')
    doc_dt = synonym('AUDAT')
    sales_office_id = synonym('VKBUR')
    sales_group_id = synonym('VKGRP')
    distr_chan_cd = synonym('VTWEG')
    div_cd = synonym('SPART')
    sd_hdr_type_cd = synonym('AUART')
    cust_prch_ord_cd = synonym('BSTNK')
    customer_id = synonym('KUNNR')
    doc_create_user_id = synonym('ERNAM')
    sd_doc_id = synonym('VBELN')
    sold_to_addr_id = synonym('ADRNR_AG')
    addr_id = synonym('ADRNR')
    valid_from_dt = synonym('DATAB')
    valid_to_dt = synonym('DATBI')


################################################################################




################################################################################

class SDIndexMaterial(SAP_Base):
    """\
    Table sourced from: VAPMA
    Description: Sales Index: Order Items by Material
    """

    __tablename__ = "VAPMA"

    MATNR = Column('MATNR', String(18), primary_key = True, doc="""Sourced from VAPMA-MATNR // Material Number""")
    VKORG = Column('VKORG', String(4), primary_key = True, doc="""Sourced from VAPMA-VKORG // Sales Organization""")
    TRVOG = Column('TRVOG', String(1), primary_key = True, doc="""Sourced from VAPMA-TRVOG // Transaction group""")
    AUDAT = Column('AUDAT', Date, primary_key = True, doc="""Sourced from VAPMA-AUDAT // Document Date (Date Received/Sent)""")
    VTWEG = Column('VTWEG', String(2), primary_key = True, doc="""Sourced from VAPMA-VTWEG // Distribution Channel""")
    SPART = Column('SPART', String(2), primary_key = True, doc="""Sourced from VAPMA-SPART // Division""")
    AUART = Column('AUART', String(4), primary_key = True, doc="""Sourced from VAPMA-AUART // Sales Document Type""")
    KUNNR = Column('KUNNR', String(10), primary_key = True, doc="""Sourced from VAPMA-KUNNR // Sold-to party""")
    VKBUR = Column('VKBUR', String(4), primary_key = True, doc="""Sourced from VAPMA-VKBUR // Sales Office""")
    VKGRP = Column('VKGRP', String(3), primary_key = True, doc="""Sourced from VAPMA-VKGRP // Sales Group""")
    BSTNK = Column('BSTNK', String(20), primary_key = True, doc="""Sourced from VAPMA-BSTNK // Customer purchase order number""")
    ERNAM = Column('ERNAM', String(12), primary_key = True, doc="""Sourced from VAPMA-ERNAM // Name of Person who Created the Object""")
    VBELN = Column('VBELN', String(10), primary_key = True, doc="""Sourced from VAPMA-VBELN // Sales and Distribution Document Number""")
    POSNR = Column('POSNR', String(6), primary_key = True, doc="""Sourced from VAPMA-POSNR // Item number of the SD document""")
    WERKS = Column('WERKS', String(4), default=None, doc="""Sourced from VAPMA-WERKS // Plant""")
    ADRNR = Column('ADRNR', String(10), default=None, doc="""Sourced from VAPMA-ADRNR // Address number of the sold-to party""")
    DATAB = Column('DATAB', Date, default=None, doc="""Sourced from VAPMA-DATAB // Quotation or contract valid from""")
    DATBI = Column('DATBI', Date, default=None, doc="""Sourced from VAPMA-DATBI // Quotation or contract valid to""")

    material_id = synonym('MATNR')
    sales_org_cd = synonym('VKORG')
    transaction_group_id = synonym('TRVOG')
    doc_dt = synonym('AUDAT')
    distr_chan_cd = synonym('VTWEG')
    div_cd = synonym('SPART')
    sd_hdr_type_cd = synonym('AUART')
    customer_id = synonym('KUNNR')
    sales_office_id = synonym('VKBUR')
    sales_group_id = synonym('VKGRP')
    cust_prch_ord_cd = synonym('BSTNK')
    doc_create_user_id = synonym('ERNAM')
    sd_doc_id = synonym('VBELN')
    sd_doc_item_id = synonym('POSNR')
    addr_id = synonym('ADRNR')
    valid_from_dt = synonym('DATAB')
    valid_to_dt = synonym('DATBI')


################################################################################




################################################################################

class SD_SA(SAP_Base):
    """\
    Table sourced from: VBAG
    Description: Sales Document: Release Data by Schedule Line in Sch.Agrmt.
    """

    __tablename__ = "VBAG"

    VBELN = Column('VBELN', String(10), primary_key = True, doc="""Sourced from VBAG-VBELN // Sales Document""")
    POSNR = Column('POSNR', String(6), primary_key = True, doc="""Sourced from VBAG-POSNR // Sales Document Item""")
    ABART = Column('ABART', String(1), primary_key = True, doc="""Sourced from VBAG-ABART // Release type""")
    ABRUF = Column('ABRUF', String(10), primary_key = True, doc="""Sourced from VBAG-ABRUF // Forecast Delivery schedule number""")
    ABRDT = Column('ABRDT', Date, default=None, doc="""Sourced from VBAG-ABRDT // Delivery Schedule Date""")
    ABSTA = Column('ABSTA', String(1), default=None, doc="""Sourced from VBAG-ABSTA // Release status (current release, old release)""")
    ABEFZ = Column('ABEFZ', Numeric(15,3,3), default=None, doc="""Sourced from VBAG-ABEFZ // Cumulative figure for customer in sales unit""")
    ABMFR = Column('ABMFR', String(3), default=None, doc="""Sourced from VBAG-ABMFR // Number of days for which material is available""")
    ABFFR = Column('ABFFR', String(3), default=None, doc="""Sourced from VBAG-ABFFR // Number of days assigned for production""")
    ABHOR = Column('ABHOR', Date, default=None, doc="""Sourced from VBAG-ABHOR // JIT horizon""")

    sd_doc_id = synonym('VBELN')
    sd_doc_item_id = synonym('POSNR')
    jit_horizon = synonym('ABHOR')


################################################################################




################################################################################

class SD_Hdr(SAP_Base):
    """\
    Table sourced from: VBAK
    Description: Sales Document: Header Data
    """

    __tablename__ = "VBAK"

    VBELN = Column('VBELN', String(10), primary_key = True, doc="""Sourced from VBAK-VBELN // Sales Document""")
    ERDAT = Column('ERDAT', Date, default=None, doc="""Sourced from VBAK-ERDAT // Date on Which Record Was Created""")
    ERZET = Column('ERZET', Time, default=None, doc="""Sourced from VBAK-ERZET // Entry time""")
    ERNAM = Column('ERNAM', String(12), default=None, doc="""Sourced from VBAK-ERNAM // Name of Person who Created the Object""")
    ANGDT = Column('ANGDT', Date, default=None, doc="""Sourced from VBAK-ANGDT // Quotation/Inquiry is valid from""")
    BNDDT = Column('BNDDT', Date, default=None, doc="""Sourced from VBAK-BNDDT // Date until which bid/quotation is binding (valid-to date)""")
    AUDAT = Column('AUDAT', Date, default=None, doc="""Sourced from VBAK-AUDAT // Document Date (Date Received/Sent)""")
    VBTYP = Column('VBTYP', String(1), default=None, doc="""Sourced from VBAK-VBTYP // SD document category""")
    TRVOG = Column('TRVOG', String(1), default=None, doc="""Sourced from VBAK-TRVOG // Transaction group""")
    AUART = Column('AUART', String(4), default=None, doc="""Sourced from VBAK-AUART // Sales Document Type""")
    AUGRU = Column('AUGRU', String(3), default=None, doc="""Sourced from VBAK-AUGRU // Order reason (reason for the business transaction)""")
    GWLDT = Column('GWLDT', Date, default=None, doc="""Sourced from VBAK-GWLDT // Guarantee date""")
    SUBMI = Column('SUBMI', String(10), default=None, doc="""Sourced from VBAK-SUBMI // Collective number (SD)""")
    LIFSK = Column('LIFSK', String(2), default=None, doc="""Sourced from VBAK-LIFSK // Delivery block (document header)""")
    FAKSK = Column('FAKSK', String(2), default=None, doc="""Sourced from VBAK-FAKSK // Billing block in SD document""")
    NETWR = Column('NETWR', Numeric(15,3,3), default=None, doc="""Sourced from VBAK-NETWR // Net Value of the Sales Order in Document Currency""")
    WAERK = Column('WAERK', String(5), default=None, doc="""Sourced from VBAK-WAERK // SD Document Currency""")
    VKORG = Column('VKORG', String(4), default=None, doc="""Sourced from VBAK-VKORG // Sales Organization""")
    VTWEG = Column('VTWEG', String(2), default=None, doc="""Sourced from VBAK-VTWEG // Distribution Channel""")
    SPART = Column('SPART', String(2), default=None, doc="""Sourced from VBAK-SPART // Division""")
    VKGRP = Column('VKGRP', String(3), default=None, doc="""Sourced from VBAK-VKGRP // Sales Group""")
    VKBUR = Column('VKBUR', String(4), default=None, doc="""Sourced from VBAK-VKBUR // Sales Office""")
    GSBER = Column('GSBER', String(4), default=None, doc="""Sourced from VBAK-GSBER // Business Area""")
    GSKST = Column('GSKST', String(4), default=None, doc="""Sourced from VBAK-GSKST // Business area from cost center""")
    GUEBG = Column('GUEBG', Date, default=None, doc="""Sourced from VBAK-GUEBG // Valid-from date (outline agreements, product proposals)""")
    GUEEN = Column('GUEEN', Date, default=None, doc="""Sourced from VBAK-GUEEN // Valid-to date (outline agreements, product proposals)""")
    KNUMV = Column('KNUMV', String(10), default=None, doc="""Sourced from VBAK-KNUMV // Number of the document condition""")
    VDATU = Column('VDATU', String(8), default=None, doc="""Sourced from VBAK-VDATU // Requested delivery date""")
    VPRGR = Column('VPRGR', String(1), default=None, doc="""Sourced from VBAK-VPRGR // Proposed date type""")
    AUTLF = Column('AUTLF', Boolean, default=None, doc="""Sourced from VBAK-AUTLF // Complete delivery defined for each sales order?""")
    VBKLA = Column('VBKLA', String(9), default=None, doc="""Sourced from VBAK-VBKLA // Original system with release and transaction control""")
    VBKLT = Column('VBKLT', String(1), default=None, doc="""Sourced from VBAK-VBKLT // SD document indicator""")
    KALSM = Column('KALSM', String(6), default=None, doc="""Sourced from VBAK-KALSM // Sales and Distribution: Pricing Procedure in Pricing""")
    VSBED = Column('VSBED', String(2), default=None, doc="""Sourced from VBAK-VSBED // Shipping Conditions""")
    FKARA = Column('FKARA', String(4), default=None, doc="""Sourced from VBAK-FKARA // Proposed billing type for an order-related billing document""")
    AWAHR = Column('AWAHR', String(3), default=None, doc="""Sourced from VBAK-AWAHR // Sales probability""")
    KTEXT = Column('KTEXT', String(40), default=None, doc="""Sourced from VBAK-KTEXT // Search term for product proposal""")
    BSTNK = Column('BSTNK', String(20), default=None, doc="""Sourced from VBAK-BSTNK // Customer purchase order number""")
    BSARK = Column('BSARK', String(4), default=None, doc="""Sourced from VBAK-BSARK // Customer purchase order type""")
    BSTDK = Column('BSTDK', Date, default=None, doc="""Sourced from VBAK-BSTDK // Customer purchase order date""")
    BSTZD = Column('BSTZD', String(4), default=None, doc="""Sourced from VBAK-BSTZD // Purchase order number supplement""")
    IHREZ = Column('IHREZ', String(12), default=None, doc="""Sourced from VBAK-IHREZ // Your Reference""")
    BNAME = Column('BNAME', String(35), default=None, doc="""Sourced from VBAK-BNAME // Name of orderer""")
    TELF1 = Column('TELF1', String(16), default=None, doc="""Sourced from VBAK-TELF1 // Telephone Number""")
    MAHZA = Column('MAHZA', Numeric(15,3,3), default=None, doc="""Sourced from VBAK-MAHZA // Number of contacts from the customer""")
    MAHDT = Column('MAHDT', Date, default=None, doc="""Sourced from VBAK-MAHDT // Last customer contact date""")
    KUNNR = Column('KUNNR', String(10), default=None, doc="""Sourced from VBAK-KUNNR // Sold-to party""")
    KOSTL = Column('KOSTL', String(10), default=None, doc="""Sourced from VBAK-KOSTL // Cost Center""")
    STAFO = Column('STAFO', String(6), default=None, doc="""Sourced from VBAK-STAFO // Update group for statistics update""")
    STWAE = Column('STWAE', String(5), default=None, doc="""Sourced from VBAK-STWAE // Statistics currency""")
    AEDAT = Column('AEDAT', Date, default=None, doc="""Sourced from VBAK-AEDAT // Changed On""")
    KVGR1 = Column('KVGR1', String(3), default=None, doc="""Sourced from VBAK-KVGR1 // Customer group 1""")
    KVGR2 = Column('KVGR2', String(3), default=None, doc="""Sourced from VBAK-KVGR2 // Customer group 2""")
    KVGR3 = Column('KVGR3', String(3), default=None, doc="""Sourced from VBAK-KVGR3 // Customer group 3""")
    KVGR4 = Column('KVGR4', String(3), default=None, doc="""Sourced from VBAK-KVGR4 // Customer group 4""")
    KVGR5 = Column('KVGR5', String(3), default=None, doc="""Sourced from VBAK-KVGR5 // Customer group 5""")
    KNUMA = Column('KNUMA', String(10), default=None, doc="""Sourced from VBAK-KNUMA // Agreement (various conditions grouped together)""")
    KOKRS = Column('KOKRS', String(4), default=None, doc="""Sourced from VBAK-KOKRS // Controlling Area""")
    PS_PSP_PNR = Column('PS_PSP_PNR', String(8), default=None, doc="""Sourced from VBAK-PS_PSP_PNR // Work Breakdown Structure Element (WBS Element)""")
    KURST = Column('KURST', String(4), default=None, doc="""Sourced from VBAK-KURST // Exchange Rate Type""")
    KKBER = Column('KKBER', String(4), default=None, doc="""Sourced from VBAK-KKBER // Credit Control Area""")
    KNKLI = Column('KNKLI', String(10), default=None, doc="""Sourced from VBAK-KNKLI // Customer's account number with credit limit reference""")
    GRUPP = Column('GRUPP', String(4), default=None, doc="""Sourced from VBAK-GRUPP // Customer Credit Group""")
    SBGRP = Column('SBGRP', String(3), default=None, doc="""Sourced from VBAK-SBGRP // Credit representative group for credit management""")
    CTLPC = Column('CTLPC', String(3), default=None, doc="""Sourced from VBAK-CTLPC // Credit management: Risk category""")
    CMWAE = Column('CMWAE', String(5), default=None, doc="""Sourced from VBAK-CMWAE // Currency key of credit control area""")
    CMFRE = Column('CMFRE', Date, default=None, doc="""Sourced from VBAK-CMFRE // Release date of the document determined by credit management""")
    CMNUP = Column('CMNUP', Date, default=None, doc="""Sourced from VBAK-CMNUP // Date of next credit check of document""")
    CMNGV = Column('CMNGV', Date, default=None, doc="""Sourced from VBAK-CMNGV // Next date""")
    AMTBL = Column('AMTBL', String(15), default=None, doc="""Sourced from VBAK-AMTBL // Released credit value of the document""")
    HITYP_PR = Column('HITYP_PR', String(1), default=None, doc="""Sourced from VBAK-HITYP_PR // Hierarchy type for pricing""")
    ABRVW = Column('ABRVW', String(3), default=None, doc="""Sourced from VBAK-ABRVW // Usage Indicator""")
    ABDIS = Column('ABDIS', String(1), default=None, doc="""Sourced from VBAK-ABDIS // MRP for delivery schedule types""")
    VGBEL = Column('VGBEL', String(10), default=None, doc="""Sourced from VBAK-VGBEL // Document number of the reference document""")
    OBJNR = Column('OBJNR', String(22), default=None, doc="""Sourced from VBAK-OBJNR // Object number at header level""")
    BUKRS_VF = Column('BUKRS_VF', String(4), default=None, doc="""Sourced from VBAK-BUKRS_VF // Company code to be billed""")
    TAXK1 = Column('TAXK1', String(1), default=None, doc="""Sourced from VBAK-TAXK1 // Alternative tax classification""")
    TAXK2 = Column('TAXK2', String(1), default=None, doc="""Sourced from VBAK-TAXK2 // Tax classification 2 for customer""")
    TAXK3 = Column('TAXK3', String(1), default=None, doc="""Sourced from VBAK-TAXK3 // Tax classification 3 for customer""")
    TAXK4 = Column('TAXK4', String(1), default=None, doc="""Sourced from VBAK-TAXK4 // Tax Classification 4 Customer""")
    TAXK5 = Column('TAXK5', String(1), default=None, doc="""Sourced from VBAK-TAXK5 // Tax classification 5 for customer""")
    TAXK6 = Column('TAXK6', String(1), default=None, doc="""Sourced from VBAK-TAXK6 // Tax classification 6 for customer""")
    TAXK7 = Column('TAXK7', String(1), default=None, doc="""Sourced from VBAK-TAXK7 // Tax classification 7 for customer""")
    TAXK8 = Column('TAXK8', String(1), default=None, doc="""Sourced from VBAK-TAXK8 // Tax classification 8 for customer""")
    TAXK9 = Column('TAXK9', String(1), default=None, doc="""Sourced from VBAK-TAXK9 // Tax classification 9 for customer""")
    XBLNR = Column('XBLNR', String(16), default=None, doc="""Sourced from VBAK-XBLNR // Reference Document Number""")
    ZUONR = Column('ZUONR', String(18), default=None, doc="""Sourced from VBAK-ZUONR // Assignment number""")
    VGTYP = Column('VGTYP', String(1), default=None, doc="""Sourced from VBAK-VGTYP // Document category of preceding SD document""")
    KALSM_CH = Column('KALSM_CH', String(6), default=None, doc="""Sourced from VBAK-KALSM_CH // Search procedure for batch determination""")
    AGRZR = Column('AGRZR', String(2), default=None, doc="""Sourced from VBAK-AGRZR // Accrual period for order-related billing docs.to be accrued""")
    AUFNR = Column('AUFNR', String(12), default=None, doc="""Sourced from VBAK-AUFNR // Order Number""")
    QMNUM = Column('QMNUM', String(12), default=None, doc="""Sourced from VBAK-QMNUM // Notification No""")
    VBELN_GRP = Column('VBELN_GRP', String(10), default=None, doc="""Sourced from VBAK-VBELN_GRP // Mster contract number""")
    SCHEME_GRP = Column('SCHEME_GRP', String(4), default=None, doc="""Sourced from VBAK-SCHEME_GRP // Referencing requirement: Procedure""")
    ABRUF_PART = Column('ABRUF_PART', String(1), default=None, doc="""Sourced from VBAK-ABRUF_PART // Check partner authorizations""")
    ABHOD = Column('ABHOD', Date, default=None, doc="""Sourced from VBAK-ABHOD // Pick up date""")
    ABHOV = Column('ABHOV', String(6), default=None, doc="""Sourced from VBAK-ABHOV // Pick up time""")
    ABHOB = Column('ABHOB', String(6), default=None, doc="""Sourced from VBAK-ABHOB // Pick up time""")
    RPLNR = Column('RPLNR', String(10), default=None, doc="""Sourced from VBAK-RPLNR // Number of payment card plan type""")
    VZEIT = Column('VZEIT', String(6), default=None, doc="""Sourced from VBAK-VZEIT // Proposed schedule line time (local with ref. to sales org.)""")
    STCEG_L = Column('STCEG_L', String(3), default=None, doc="""Sourced from VBAK-STCEG_L // Tax Destination Country""")
    LANDTX = Column('LANDTX', String(3), default=None, doc="""Sourced from VBAK-LANDTX // Tax departure country""")
    XEGDR = Column('XEGDR', Boolean, default=None, doc="""Sourced from VBAK-XEGDR // Indicator: Triangular deal within the EU ?""")
    ENQUEUE_GRP = Column('ENQUEUE_GRP', String(1), default=None, doc="""Sourced from VBAK-ENQUEUE_GRP // Block master contr. until all lower level contracts updated""")
    DAT_FZAU = Column('DAT_FZAU', Date, default=None, doc="""Sourced from VBAK-DAT_FZAU // Cml delivery order qty date""")
    FMBDAT = Column('FMBDAT', String(8), default=None, doc="""Sourced from VBAK-FMBDAT // Material Staging/Availability Date""")
    VSNMR_V = Column('VSNMR_V', String(12), default=None, doc="""Sourced from VBAK-VSNMR_V // Sales document version number""")
    HANDLE = Column('HANDLE', Integer, default=None, doc="""Sourced from VBAK-HANDLE // International unique key for VBAK-VBELN""")
    PROLI = Column('PROLI', String(3), default=None, doc="""Sourced from VBAK-PROLI // Dangerous Goods Management Profile in SD Documents""")
    CONT_DG = Column('CONT_DG', Boolean, default=None, doc="""Sourced from VBAK-CONT_DG // Indicator: Document contains dangerous goods""")
    CRM_GUID = Column('CRM_GUID', String(70), default=None, doc="""Sourced from VBAK-CRM_GUID // Character field, length 70""")
    UPD_TMSTMP = Column('UPD_TMSTMP', String(21), default=None, doc="""Sourced from VBAK-UPD_TMSTMP // UTC Time Stamp in Long Form (YYYYMMDDhhmmssmmmuuun)""")
    MSR_ID = Column('MSR_ID', String(10), default=None, doc="""Sourced from VBAK-MSR_ID // Process Identification Number""")
    HANDOVERLOC = Column('HANDOVERLOC', String(10), default=None, doc="""Sourced from VBAK-HANDOVERLOC // Location for a physical handover of goods""")
    PSM_BUDAT = Column('PSM_BUDAT', Date, default=None, doc="""Sourced from VBAK-PSM_BUDAT // Posting Date in the Document""")
    SWENR = Column('SWENR', String(8), default=None, doc="""Sourced from VBAK-SWENR // Business  Entity Number""")
    SMENR = Column('SMENR', String(8), default=None, doc="""Sourced from VBAK-SMENR // Number of Sales Unit""")
    PHASE = Column('PHASE', String(11), default=None, doc="""Sourced from VBAK-PHASE // Sales Phase""")
    MTLAUR = Column('MTLAUR', String(1), default=None, doc="""Sourced from VBAK-MTLAUR // Marker for Low Income Housing""")
    STAGE = Column('STAGE', Numeric(15,3,3), default=None, doc="""Sourced from VBAK-STAGE // Construction Stage""")
    HB_CONT_REASON = Column('HB_CONT_REASON', String(2), default=None, doc="""Sourced from VBAK-HB_CONT_REASON // Contingency  data""")
    HB_EXPDATE = Column('HB_EXPDATE', String(8), default=None, doc="""Sourced from VBAK-HB_EXPDATE // Expiration date""")
    HB_RESDATE = Column('HB_RESDATE', String(8), default=None, doc="""Sourced from VBAK-HB_RESDATE // Resolution date""")
    LOGSYSB = Column('LOGSYSB', String(10), default=None, doc="""Sourced from VBAK-LOGSYSB // Logical system with which document was created""")
    KALCD = Column('KALCD', String(6), default=None, doc="""Sourced from VBAK-KALCD // Procedure for Campaign Determination""")
    MULTI = Column('MULTI', String(1), default=None, doc="""Sourced from VBAK-MULTI // Multiple Campaigns/Trade Promotions Active Indicator""")
    SPPAYM = Column('SPPAYM', String(2), default=None, doc="""Sourced from VBAK-SPPAYM // Payment Form for Special Payment Method""")
    YYSHIPMENT_DATE = Column('YYSHIPMENT_DATE', Date, default=None, doc="""Sourced from VBAK-YYSHIPMENT_DATE // Shipment date""")
    YYARRIVAL_DATE = Column('YYARRIVAL_DATE', Date, default=None, doc="""Sourced from VBAK-YYARRIVAL_DATE // Arrival Date""")
    YYARRIVE_TIME = Column('YYARRIVE_TIME', Time, default=None, doc="""Sourced from VBAK-YYARRIVE_TIME // Arrival time""")
    YYLOCCO = Column('YYLOCCO', String(10), default=None, doc="""Sourced from VBAK-YYLOCCO // City Coordinates""")
    YYLAND1 = Column('YYLAND1', String(3), default=None, doc="""Sourced from VBAK-YYLAND1 // Country Key""")
    YYUSERID = Column('YYUSERID', String(12), default=None, doc="""Sourced from VBAK-YYUSERID // Name of Person who Created the Object""")
    YYCOSTCTR = Column('YYCOSTCTR', String(10), default=None, doc="""Sourced from VBAK-YYCOSTCTR // Cost Center""")
    YYHDRTERMS = Column('YYHDRTERMS', String(4), default=None, doc="""Sourced from VBAK-YYHDRTERMS // Terms of Payment Key""")
    YYPROJECT = Column('YYPROJECT', String(10), default=None, doc="""Sourced from VBAK-YYPROJECT // Project Number""")
    YYRECON1 = Column('YYRECON1', String(3), default=None, doc="""Sourced from VBAK-YYRECON1 // GROW Recon Data 1""")
    YYRECON2 = Column('YYRECON2', String(2), default=None, doc="""Sourced from VBAK-YYRECON2 // GROW Recon Data 2""")
    YYRECON3 = Column('YYRECON3', String(2), default=None, doc="""Sourced from VBAK-YYRECON3 // GROW Recon Data 3""")
    YYRECON4 = Column('YYRECON4', String(1), default=None, doc="""Sourced from VBAK-YYRECON4 // GROW Recon Data 4""")
    YYKUNNR = Column('YYKUNNR', String(10), default=None, doc="""Sourced from VBAK-YYKUNNR // Sold-to party""")
    YYVKORG = Column('YYVKORG', String(4), default=None, doc="""Sourced from VBAK-YYVKORG // Sales Organization""")
    YYVTWEG = Column('YYVTWEG', String(2), default=None, doc="""Sourced from VBAK-YYVTWEG // Distribution Channel""")
    YYKDGRP = Column('YYKDGRP', String(2), default=None, doc="""Sourced from VBAK-YYKDGRP // Customer group""")
    YYRECON5 = Column('YYRECON5', String(1), default=None, doc="""Sourced from VBAK-YYRECON5 // GROW Recon Data 5""")
    YYRECON6 = Column('YYRECON6', String(10), default=None, doc="""Sourced from VBAK-YYRECON6 // GROW Recon Data 6""")

    sd_doc_id = synonym('VBELN')
    doc_create_dt = synonym('ERDAT')
    doc_create_tm = synonym('ERZET')
    doc_create_user_id = synonym('ERNAM')
    quote_validity_dt = synonym('ANGDT')
    quote_valid_to_dt = synonym('BNDDT')
    doc_dt = synonym('AUDAT')
    sd_doc_ctgy_cd = synonym('VBTYP')
    transaction_group_id = synonym('TRVOG')
    sd_hdr_type_cd = synonym('AUART')
    order_reason_cd = synonym('AUGRU')
    guarantee_dt = synonym('GWLDT')
    hdr_delivery_blk_cd = synonym('LIFSK')
    sd_doc_billing_block_cd = synonym('FAKSK')
    doc_currency_net_value_qty = synonym('NETWR')
    sd_doc_currency_cd = synonym('WAERK')
    sales_org_cd = synonym('VKORG')
    distr_chan_cd = synonym('VTWEG')
    div_cd = synonym('SPART')
    sales_group_id = synonym('VKGRP')
    sales_office_id = synonym('VKBUR')
    proposal_valid_from_dt = synonym('GUEBG')
    proposal_valid_to_dt = synonym('GUEEN')
    sd_doc_cd = synonym('VBKLT')
    shipping_condition_cd = synonym('VSBED')
    proposed_billing_type_cd = synonym('FKARA')
    cust_prch_ord_cd = synonym('BSTNK')
    cust_prch_ord_type_cd = synonym('BSARK')
    cust_prch_ord_dt = synonym('BSTDK')
    prch_ord_supp_cd = synonym('BSTZD')
    customer_id = synonym('KUNNR')
    cost_center_id = synonym('KOSTL')
    update_dt = synonym('AEDAT')
    freight_policy_cd = synonym('KVGR2')
    credit_control_area_cd = synonym('KKBER')
    credit_mgmt_release_dt = synonym('CMFRE')
    next_credit_check_dt = synonym('CMNUP')
    pricing_hierarchy_type_cd = synonym('HITYP_PR')
    reference_doc_id = synonym('VGBEL')
    billed_company_cd = synonym('BUKRS_VF')
    order_id = synonym('AUFNR')
    pick_up_dt = synonym('ABHOD')
    posting_dt = synonym('PSM_BUDAT')


################################################################################




################################################################################

class SD_Item(SAP_Base):
    """\
    Table sourced from: VBAP
    Description: Sales Document: Item Data
    """

    __tablename__ = "VBAP"

    VBELN = Column('VBELN', String(10), primary_key = True, doc="""Sourced from VBAP-VBELN // Sales Document""")
    POSNR = Column('POSNR', String(6), primary_key = True, doc="""Sourced from VBAP-POSNR // Sales Document Item""")
    MATNR = Column('MATNR', String(18), default=None, doc="""Sourced from VBAP-MATNR // Material Number""")
    MATWA = Column('MATWA', String(18), default=None, doc="""Sourced from VBAP-MATWA // Material entered""")
    PMATN = Column('PMATN', String(18), default=None, doc="""Sourced from VBAP-PMATN // Pricing Reference Material""")
    CHARG = Column('CHARG', String(10), default=None, doc="""Sourced from VBAP-CHARG // Batch Number""")
    MATKL = Column('MATKL', String(9), default=None, doc="""Sourced from VBAP-MATKL // Material Group""")
    ARKTX = Column('ARKTX', String(40), default=None, doc="""Sourced from VBAP-ARKTX // Short text for sales order item""")
    PSTYV = Column('PSTYV', String(4), default=None, doc="""Sourced from VBAP-PSTYV // Sales document item category""")
    POSAR = Column('POSAR', String(1), default=None, doc="""Sourced from VBAP-POSAR // Item type""")
    LFREL = Column('LFREL', Boolean, default=None, doc="""Sourced from VBAP-LFREL // Item is relevant for delivery""")
    FKREL = Column('FKREL', String(1), default=None, doc="""Sourced from VBAP-FKREL // Relevant for Billing""")
    UEPOS = Column('UEPOS', String(6), default=None, doc="""Sourced from VBAP-UEPOS // Higher-level item in bill of material structures""")
    GRPOS = Column('GRPOS', String(6), default=None, doc="""Sourced from VBAP-GRPOS // Item for which this item is an alternative""")
    ABGRU = Column('ABGRU', String(2), default=None, doc="""Sourced from VBAP-ABGRU // Reason for rejection of quotations and sales orders""")
    PRODH = Column('PRODH', String(18), default=None, doc="""Sourced from VBAP-PRODH // Product hierarchy""")
    ZWERT = Column('ZWERT', String(13), default=None, doc="""Sourced from VBAP-ZWERT // Target Value for Outline Agreement in Document Currency""")
    ZMENG = Column('ZMENG', String(13), default=None, doc="""Sourced from VBAP-ZMENG // Target quantity in sales units""")
    ZIEME = Column('ZIEME', String(3), default=None, doc="""Sourced from VBAP-ZIEME // Target quantity UoM""")
    UMZIZ = Column('UMZIZ', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-UMZIZ // Factor for converting sales units to base units (target qty)""")
    UMZIN = Column('UMZIN', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-UMZIN // Factor for converting sales units to base units (target qty)""")
    MEINS = Column('MEINS', String(3), default=None, doc="""Sourced from VBAP-MEINS // Base Unit of Measure""")
    SMENG = Column('SMENG', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-SMENG // Scale quantity in base unit of measure""")
    ABLFZ = Column('ABLFZ', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-ABLFZ // Rounding quantity for delivery""")
    ABDAT = Column('ABDAT', Date, default=None, doc="""Sourced from VBAP-ABDAT // Reconciliation Date for Agreed Cumulative Quantity""")
    ABSFZ = Column('ABSFZ', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-ABSFZ // Allowed deviation in quantity (absolute)""")
    POSEX = Column('POSEX', String(6), default=None, doc="""Sourced from VBAP-POSEX // Item Number of the Underlying Purchase Order""")
    KDMAT = Column('KDMAT', String(35), default=None, doc="""Sourced from VBAP-KDMAT // Material Number Used by Customer""")
    KBVER = Column('KBVER', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-KBVER // Allowed deviation in quantity (in percent)""")
    KEVER = Column('KEVER', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-KEVER // Days by which the quantity can be shifted""")
    VKGRU = Column('VKGRU', String(3), default=None, doc="""Sourced from VBAP-VKGRU // Repair Processing: Classification of Items""")
    VKAUS = Column('VKAUS', String(3), default=None, doc="""Sourced from VBAP-VKAUS // Usage Indicator""")
    GRKOR = Column('GRKOR', String(3), default=None, doc="""Sourced from VBAP-GRKOR // Delivery group (items are delivered together)""")
    FMENG = Column('FMENG', Boolean, default=None, doc="""Sourced from VBAP-FMENG // Quantity is Fixed""")
    UEBTK = Column('UEBTK', Boolean, default=None, doc="""Sourced from VBAP-UEBTK // Unlimited overdelivery allowed""")
    UEBTO = Column('UEBTO', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-UEBTO // Overdelivery Tolerance Limit""")
    UNTTO = Column('UNTTO', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-UNTTO // Underdelivery Tolerance Limit""")
    FAKSP = Column('FAKSP', String(2), default=None, doc="""Sourced from VBAP-FAKSP // Billing block for item""")
    ATPKZ = Column('ATPKZ', String(1), default=None, doc="""Sourced from VBAP-ATPKZ // Replacement part""")
    RKFKF = Column('RKFKF', String(1), default=None, doc="""Sourced from VBAP-RKFKF // Method of billing for CO/PPC orders""")
    SPART = Column('SPART', String(2), default=None, doc="""Sourced from VBAP-SPART // Division""")
    GSBER = Column('GSBER', String(4), default=None, doc="""Sourced from VBAP-GSBER // Business Area""")
    NETWR = Column('NETWR', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-NETWR // Net value of the order item in document currency""")
    WAERK = Column('WAERK', String(5), default=None, doc="""Sourced from VBAP-WAERK // SD Document Currency""")
    ANTLF = Column('ANTLF', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-ANTLF // Maximum Number of Partial Deliveries Allowed Per Item""")
    KZTLF = Column('KZTLF', String(1), default=None, doc="""Sourced from VBAP-KZTLF // Partial delivery at item level""")
    CHSPL = Column('CHSPL', Boolean, default=None, doc="""Sourced from VBAP-CHSPL // Batch split allowed""")
    KWMENG = Column('KWMENG', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-KWMENG // Cumulative Order Quantity in Sales Units""")
    LSMENG = Column('LSMENG', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-LSMENG // Cumulative required delivery qty (all dlv-relev.sched.lines)""")
    KBMENG = Column('KBMENG', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-KBMENG // Cumulative confirmed quantity in sales unit""")
    KLMENG = Column('KLMENG', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-KLMENG // Cumulative confirmed quantity in base unit""")
    VRKME = Column('VRKME', String(3), default=None, doc="""Sourced from VBAP-VRKME // Sales unit""")
    UMVKZ = Column('UMVKZ', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-UMVKZ // Numerator (factor) for conversion of sales quantity into SKU""")
    UMVKN = Column('UMVKN', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-UMVKN // Denominator (Divisor) for Conversion of Sales Qty into SKU""")
    BRGEW = Column('BRGEW', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-BRGEW // Gross Weight of the Item""")
    NTGEW = Column('NTGEW', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-NTGEW // Net Weight of the Item""")
    GEWEI = Column('GEWEI', String(3), default=None, doc="""Sourced from VBAP-GEWEI // Weight Unit""")
    VOLUM = Column('VOLUM', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-VOLUM // Volume of the item""")
    VOLEH = Column('VOLEH', String(3), default=None, doc="""Sourced from VBAP-VOLEH // Volume unit""")
    VBELV = Column('VBELV', String(10), default=None, doc="""Sourced from VBAP-VBELV // Originating document""")
    POSNV = Column('POSNV', String(6), default=None, doc="""Sourced from VBAP-POSNV // Originating item""")
    VGBEL = Column('VGBEL', String(10), default=None, doc="""Sourced from VBAP-VGBEL // Document number of the reference document""")
    VGPOS = Column('VGPOS', String(6), default=None, doc="""Sourced from VBAP-VGPOS // Item number of the reference item""")
    VOREF = Column('VOREF', Boolean, default=None, doc="""Sourced from VBAP-VOREF // Complete reference indicator""")
    UPFLU = Column('UPFLU', String(1), default=None, doc="""Sourced from VBAP-UPFLU // Update indicator for sales document document flow""")
    ERLRE = Column('ERLRE', String(1), default=None, doc="""Sourced from VBAP-ERLRE // Completion rule for quotation / contract""")
    LPRIO = Column('LPRIO', String(2), default=None, doc="""Sourced from VBAP-LPRIO // Delivery Priority""")
    WERKS = Column('WERKS', String(4), default=None, doc="""Sourced from VBAP-WERKS // Plant (Own or External)""")
    LGORT = Column('LGORT', String(4), default=None, doc="""Sourced from VBAP-LGORT // Storage Location""")
    VSTEL = Column('VSTEL', String(4), default=None, doc="""Sourced from VBAP-VSTEL // Shipping Point/Receiving Point""")
    ROUTE = Column('ROUTE', String(6), default=None, doc="""Sourced from VBAP-ROUTE // Route""")
    STKEY = Column('STKEY', String(1), default=None, doc="""Sourced from VBAP-STKEY // Origin of the bill of material""")
    STDAT = Column('STDAT', Date, default=None, doc="""Sourced from VBAP-STDAT // Key date of the bill of material""")
    STLNR = Column('STLNR', String(8), default=None, doc="""Sourced from VBAP-STLNR // Bill of material""")
    STPOS = Column('STPOS', String(5), default=None, doc="""Sourced from VBAP-STPOS // Bill of material item number VBAP not used""")
    AWAHR = Column('AWAHR', String(3), default=None, doc="""Sourced from VBAP-AWAHR // Order probability of the item""")
    ERDAT = Column('ERDAT', Date, default=None, doc="""Sourced from VBAP-ERDAT // Date on Which Record Was Created""")
    ERNAM = Column('ERNAM', String(12), default=None, doc="""Sourced from VBAP-ERNAM // Name of Person who Created the Object""")
    ERZET = Column('ERZET', Time, default=None, doc="""Sourced from VBAP-ERZET // Entry time""")
    TAXM1 = Column('TAXM1', String(1), default=None, doc="""Sourced from VBAP-TAXM1 // Tax classification material""")
    TAXM2 = Column('TAXM2', String(1), default=None, doc="""Sourced from VBAP-TAXM2 // Tax classification material""")
    TAXM3 = Column('TAXM3', String(1), default=None, doc="""Sourced from VBAP-TAXM3 // Tax classification material""")
    TAXM4 = Column('TAXM4', String(1), default=None, doc="""Sourced from VBAP-TAXM4 // Tax classification material""")
    TAXM5 = Column('TAXM5', String(1), default=None, doc="""Sourced from VBAP-TAXM5 // Tax classification material""")
    TAXM6 = Column('TAXM6', String(1), default=None, doc="""Sourced from VBAP-TAXM6 // Tax classification material""")
    TAXM7 = Column('TAXM7', String(1), default=None, doc="""Sourced from VBAP-TAXM7 // Tax classification material""")
    TAXM8 = Column('TAXM8', String(1), default=None, doc="""Sourced from VBAP-TAXM8 // Tax classification material""")
    TAXM9 = Column('TAXM9', String(1), default=None, doc="""Sourced from VBAP-TAXM9 // Tax classification material""")
    VBEAF = Column('VBEAF', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-VBEAF // Fixed shipping processing time in days (= setup time)""")
    VBEAV = Column('VBEAV', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-VBEAV // Variable shipping processing time in days""")
    VGREF = Column('VGREF', Boolean, default=None, doc="""Sourced from VBAP-VGREF // Preceding document has resulted from reference""")
    NETPR = Column('NETPR', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-NETPR // Net price""")
    KPEIN = Column('KPEIN', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-KPEIN // Condition pricing unit""")
    KMEIN = Column('KMEIN', String(3), default=None, doc="""Sourced from VBAP-KMEIN // Condition unit""")
    SHKZG = Column('SHKZG', Boolean, default=None, doc="""Sourced from VBAP-SHKZG // Returns Item""")
    SKTOF = Column('SKTOF', Boolean, default=None, doc="""Sourced from VBAP-SKTOF // Cash discount indicator""")
    MTVFP = Column('MTVFP', String(2), default=None, doc="""Sourced from VBAP-MTVFP // Checking Group for Availability Check""")
    SUMBD = Column('SUMBD', String(1), default=None, doc="""Sourced from VBAP-SUMBD // Summing up of requirements""")
    KONDM = Column('KONDM', String(2), default=None, doc="""Sourced from VBAP-KONDM // Material Pricing Group""")
    KTGRM = Column('KTGRM', String(2), default=None, doc="""Sourced from VBAP-KTGRM // Account assignment group for this material""")
    BONUS = Column('BONUS', String(2), default=None, doc="""Sourced from VBAP-BONUS // Volume rebate group""")
    PROVG = Column('PROVG', String(2), default=None, doc="""Sourced from VBAP-PROVG // Commission group""")
    EANNR = Column('EANNR', String(13), default=None, doc="""Sourced from VBAP-EANNR // European Article Number (EAN) - obsolete!!!!!""")
    PRSOK = Column('PRSOK', Boolean, default=None, doc="""Sourced from VBAP-PRSOK // Pricing is OK""")
    BWTAR = Column('BWTAR', String(10), default=None, doc="""Sourced from VBAP-BWTAR // Valuation Type""")
    BWTEX = Column('BWTEX', Boolean, default=None, doc="""Sourced from VBAP-BWTEX // Indicator: Separate valuation""")
    XCHPF = Column('XCHPF', Boolean, default=None, doc="""Sourced from VBAP-XCHPF // Batch management requirement indicator""")
    XCHAR = Column('XCHAR', Boolean, default=None, doc="""Sourced from VBAP-XCHAR // Batch management indicator (internal)""")
    LFMNG = Column('LFMNG', String(13), default=None, doc="""Sourced from VBAP-LFMNG // Minimum delivery quantity in delivery note processing""")
    STAFO = Column('STAFO', String(6), default=None, doc="""Sourced from VBAP-STAFO // Update group for statistics update""")
    WAVWR = Column('WAVWR', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-WAVWR // Cost in document currency""")
    KZWI1 = Column('KZWI1', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-KZWI1 // Subtotal 1 from pricing procedure for condition""")
    KZWI2 = Column('KZWI2', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-KZWI2 // Subtotal 2 from pricing procedure for condition""")
    KZWI3 = Column('KZWI3', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-KZWI3 // Subtotal 3 from pricing procedure for condition""")
    KZWI4 = Column('KZWI4', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-KZWI4 // Subtotal 4 from pricing procedure for condition""")
    KZWI5 = Column('KZWI5', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-KZWI5 // Subtotal 5 from pricing procedure for condition""")
    KZWI6 = Column('KZWI6', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-KZWI6 // Subtotal 6 from pricing procedure for condition""")
    STCUR = Column('STCUR', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-STCUR // Exchange rate for statistics (Exch.rate at time of creation)""")
    AEDAT = Column('AEDAT', Date, default=None, doc="""Sourced from VBAP-AEDAT // Changed On""")
    EAN11 = Column('EAN11', String(18), default=None, doc="""Sourced from VBAP-EAN11 // International Article Number (EAN/UPC)""")
    FIXMG = Column('FIXMG', Boolean, default=None, doc="""Sourced from VBAP-FIXMG // Delivery date and quantity fixed""")
    PRCTR = Column('PRCTR', String(10), default=None, doc="""Sourced from VBAP-PRCTR // Profit Center""")
    MVGR1 = Column('MVGR1', String(3), default=None, doc="""Sourced from VBAP-MVGR1 // Material group 1""")
    MVGR2 = Column('MVGR2', String(3), default=None, doc="""Sourced from VBAP-MVGR2 // Material group 2""")
    MVGR3 = Column('MVGR3', String(3), default=None, doc="""Sourced from VBAP-MVGR3 // Material group 3""")
    MVGR4 = Column('MVGR4', String(3), default=None, doc="""Sourced from VBAP-MVGR4 // Material group 4""")
    MVGR5 = Column('MVGR5', String(3), default=None, doc="""Sourced from VBAP-MVGR5 // Material group 5""")
    KMPMG = Column('KMPMG', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-KMPMG // Component quantity""")
    SUGRD = Column('SUGRD', String(4), default=None, doc="""Sourced from VBAP-SUGRD // Reason for material substitution""")
    SOBKZ = Column('SOBKZ', String(1), default=None, doc="""Sourced from VBAP-SOBKZ // Special Stock Indicator""")
    VPZUO = Column('VPZUO', String(1), default=None, doc="""Sourced from VBAP-VPZUO // Allocation Indicator""")
    PAOBJNR = Column('PAOBJNR', String(10), default=None, doc="""Sourced from VBAP-PAOBJNR // Profitability Segment Number (CO-PA)""")
    PS_PSP_PNR = Column('PS_PSP_PNR', String(8), default=None, doc="""Sourced from VBAP-PS_PSP_PNR // Work Breakdown Structure Element (WBS Element)""")
    AUFNR = Column('AUFNR', String(12), default=None, doc="""Sourced from VBAP-AUFNR // Order Number""")
    VPMAT = Column('VPMAT', String(18), default=None, doc="""Sourced from VBAP-VPMAT // Planning material""")
    VPWRK = Column('VPWRK', String(4), default=None, doc="""Sourced from VBAP-VPWRK // Planning plant""")
    PRBME = Column('PRBME', String(3), default=None, doc="""Sourced from VBAP-PRBME // Base unit of measure for product group""")
    UMREF = Column('UMREF', String(16), default=None, doc="""Sourced from VBAP-UMREF // Conversion factor: quantities""")
    KNTTP = Column('KNTTP', String(1), default=None, doc="""Sourced from VBAP-KNTTP // Account Assignment Category""")
    KZVBR = Column('KZVBR', String(1), default=None, doc="""Sourced from VBAP-KZVBR // Consumption Posting""")
    SERNR = Column('SERNR', String(8), default=None, doc="""Sourced from VBAP-SERNR // BOM explosion number""")
    OBJNR = Column('OBJNR', String(22), default=None, doc="""Sourced from VBAP-OBJNR // Object number at item level""")
    ABGRS = Column('ABGRS', String(6), default=None, doc="""Sourced from VBAP-ABGRS // Results Analysis Key""")
    BEDAE = Column('BEDAE', String(4), default=None, doc="""Sourced from VBAP-BEDAE // Requirements type""")
    CMPRE = Column('CMPRE', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-CMPRE // Item credit price""")
    CMTFG = Column('CMTFG', Boolean, default=None, doc="""Sourced from VBAP-CMTFG // ID for partial release of order item, credit block""")
    CMPNT = Column('CMPNT', Boolean, default=None, doc="""Sourced from VBAP-CMPNT // ID: Item with active credit function / relevant for credit""")
    CMKUA = Column('CMKUA', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-CMKUA // Credit data exchange rate for requested delivery date""")
    CUOBJ = Column('CUOBJ', String(18), default=None, doc="""Sourced from VBAP-CUOBJ // Configuration""")
    CUOBJ_CH = Column('CUOBJ_CH', String(18), default=None, doc="""Sourced from VBAP-CUOBJ_CH // Internal object number of the batch classification""")
    CEPOK = Column('CEPOK', String(1), default=None, doc="""Sourced from VBAP-CEPOK // Status expected price""")
    KOUPD = Column('KOUPD', Boolean, default=None, doc="""Sourced from VBAP-KOUPD // Condition update""")
    SERAIL = Column('SERAIL', String(4), default=None, doc="""Sourced from VBAP-SERAIL // Serial Number Profile""")
    ANZSN = Column('ANZSN', Integer, default=None, doc="""Sourced from VBAP-ANZSN // Number of serial numbers""")
    NACHL = Column('NACHL', Boolean, default=None, doc="""Sourced from VBAP-NACHL // Customer has not posted goods receipt""")
    MAGRV = Column('MAGRV', String(4), default=None, doc="""Sourced from VBAP-MAGRV // Material Group: Packaging Materials""")
    MPROK = Column('MPROK', String(1), default=None, doc="""Sourced from VBAP-MPROK // Status manual price change""")
    VGTYP = Column('VGTYP', String(1), default=None, doc="""Sourced from VBAP-VGTYP // Document category of preceding SD document""")
    PROSA = Column('PROSA', String(1), default=None, doc="""Sourced from VBAP-PROSA // ID for material determination""")
    UEPVW = Column('UEPVW', String(1), default=None, doc="""Sourced from VBAP-UEPVW // ID for higher-level item usage""")
    KALNR = Column('KALNR', String(12), default=None, doc="""Sourced from VBAP-KALNR // Cost Estimate Number for Cost Est. w/o Qty Structure""")
    KLVAR = Column('KLVAR', String(4), default=None, doc="""Sourced from VBAP-KLVAR // Costing Variant""")
    SPOSN = Column('SPOSN', String(4), default=None, doc="""Sourced from VBAP-SPOSN // BOM Item Number""")
    KOWRR = Column('KOWRR', String(1), default=None, doc="""Sourced from VBAP-KOWRR // Statistical values""")
    STADAT = Column('STADAT', Date, default=None, doc="""Sourced from VBAP-STADAT // Statistics date""")
    EXART = Column('EXART', String(2), default=None, doc="""Sourced from VBAP-EXART // Business Transaction Type for Foreign Trade""")
    PREFE = Column('PREFE', String(1), default=None, doc="""Sourced from VBAP-PREFE // Preference indicator in export/import""")
    KNUMH = Column('KNUMH', String(10), default=None, doc="""Sourced from VBAP-KNUMH // Number of condition record from batch determination""")
    CLINT = Column('CLINT', String(10), default=None, doc="""Sourced from VBAP-CLINT // Internal Class Number""")
    CHMVS = Column('CHMVS', String(3), default=None, doc="""Sourced from VBAP-CHMVS // Batches: Exit to quantity proposal""")
    STLTY = Column('STLTY', String(1), default=None, doc="""Sourced from VBAP-STLTY // BOM category""")
    STLKN = Column('STLKN', String(8), default=None, doc="""Sourced from VBAP-STLKN // BOM item node number""")
    STPOZ = Column('STPOZ', String(8), default=None, doc="""Sourced from VBAP-STPOZ // Internal counter""")
    STMAN = Column('STMAN', Boolean, default=None, doc="""Sourced from VBAP-STMAN // Inconsistent configuration""")
    ZSCHL_K = Column('ZSCHL_K', String(6), default=None, doc="""Sourced from VBAP-ZSCHL_K // Overhead key""")
    KALSM_K = Column('KALSM_K', String(6), default=None, doc="""Sourced from VBAP-KALSM_K // Costing Sheet""")
    KALVAR = Column('KALVAR', String(4), default=None, doc="""Sourced from VBAP-KALVAR // Costing Variant""")
    KOSCH = Column('KOSCH', String(18), default=None, doc="""Sourced from VBAP-KOSCH // Product allocation determination procedure""")
    UPMAT = Column('UPMAT', String(18), default=None, doc="""Sourced from VBAP-UPMAT // Pricing reference material of main item""")
    UKONM = Column('UKONM', String(2), default=None, doc="""Sourced from VBAP-UKONM // Material pricing group of main item""")
    MFRGR = Column('MFRGR', String(8), default=None, doc="""Sourced from VBAP-MFRGR // Material freight group""")
    PLAVO = Column('PLAVO', String(4), default=None, doc="""Sourced from VBAP-PLAVO // Planning delivery schedule instruction""")
    KANNR = Column('KANNR', String(35), default=None, doc="""Sourced from VBAP-KANNR // KANBAN/sequence number""")
    CMPRE_FLT = Column('CMPRE_FLT', Float, default=None, doc="""Sourced from VBAP-CMPRE_FLT // Item credit price""")
    ABFOR = Column('ABFOR', String(2), default=None, doc="""Sourced from VBAP-ABFOR // Form of payment guarantee""")
    ABGES = Column('ABGES', String(16), default=None, doc="""Sourced from VBAP-ABGES // Guaranteed (factor between 0 and 1)""")
    J_1BCFOP = Column('J_1BCFOP', String(10), default=None, doc="""Sourced from VBAP-J_1BCFOP // CFOP Code and Extension""")
    J_1BTAXLW1 = Column('J_1BTAXLW1', String(3), default=None, doc="""Sourced from VBAP-J_1BTAXLW1 // Tax law: ICMS""")
    J_1BTAXLW2 = Column('J_1BTAXLW2', String(3), default=None, doc="""Sourced from VBAP-J_1BTAXLW2 // Tax law: IPI""")
    J_1BTXSDC = Column('J_1BTXSDC', String(2), default=None, doc="""Sourced from VBAP-J_1BTXSDC // SD tax code""")
    WKTNR = Column('WKTNR', String(10), default=None, doc="""Sourced from VBAP-WKTNR // Value contract no.""")
    WKTPS = Column('WKTPS', String(6), default=None, doc="""Sourced from VBAP-WKTPS // Value contract item""")
    SKOPF = Column('SKOPF', String(18), default=None, doc="""Sourced from VBAP-SKOPF // Assortment module""")
    KZBWS = Column('KZBWS', String(1), default=None, doc="""Sourced from VBAP-KZBWS // Valuation of Special Stock""")
    WGRU1 = Column('WGRU1', String(18), default=None, doc="""Sourced from VBAP-WGRU1 // Material group hierarchy 1""")
    WGRU2 = Column('WGRU2', String(18), default=None, doc="""Sourced from VBAP-WGRU2 // Material group hierarchy 2""")
    KNUMA_PI = Column('KNUMA_PI', String(10), default=None, doc="""Sourced from VBAP-KNUMA_PI // Promotion""")
    KNUMA_AG = Column('KNUMA_AG', String(10), default=None, doc="""Sourced from VBAP-KNUMA_AG // Sales deal""")
    KZFME = Column('KZFME', String(1), default=None, doc="""Sourced from VBAP-KZFME // ID: Leading unit of measure for completing a transaction""")
    LSTANR = Column('LSTANR', String(1), default=None, doc="""Sourced from VBAP-LSTANR // Free goods delivery control""")
    TECHS = Column('TECHS', String(12), default=None, doc="""Sourced from VBAP-TECHS // Parameter Variant/Standard Variant""")
    MWSBP = Column('MWSBP', Numeric(15,3,3), default=None, doc="""Sourced from VBAP-MWSBP // Tax amount in document currency""")
    BERID = Column('BERID', String(10), default=None, doc="""Sourced from VBAP-BERID // MRP Area""")
    PCTRF = Column('PCTRF', String(10), default=None, doc="""Sourced from VBAP-PCTRF // Profit Center for Billing""")
    LOGSYS_EXT = Column('LOGSYS_EXT', String(10), default=None, doc="""Sourced from VBAP-LOGSYS_EXT // Logical system""")
    J_1BTAXLW3 = Column('J_1BTAXLW3', String(3), default=None, doc="""Sourced from VBAP-J_1BTAXLW3 // ISS Tax Law""")
    J_1BTAXLW4 = Column('J_1BTAXLW4', String(3), default=None, doc="""Sourced from VBAP-J_1BTAXLW4 // COFINS Tax Law""")
    J_1BTAXLW5 = Column('J_1BTAXLW5', String(3), default=None, doc="""Sourced from VBAP-J_1BTAXLW5 // PIS Tax Law""")
    STOCKLOC = Column('STOCKLOC', String(20), default=None, doc="""Sourced from VBAP-STOCKLOC // First Inventory-Managing Location""")
    SLOCTYPE = Column('SLOCTYPE', String(4), default=None, doc="""Sourced from VBAP-SLOCTYPE // Type of First Inventory-Managing Location""")
    MSR_RET_REASON = Column('MSR_RET_REASON', String(3), default=None, doc="""Sourced from VBAP-MSR_RET_REASON // Return Reason""")
    MSR_REFUND_CODE = Column('MSR_REFUND_CODE', String(3), default=None, doc="""Sourced from VBAP-MSR_REFUND_CODE // Returns Refund Code""")
    MSR_APPROV_BLOCK = Column('MSR_APPROV_BLOCK', String(1), default=None, doc="""Sourced from VBAP-MSR_APPROV_BLOCK // Approval Block""")
    NRAB_KNUMH = Column('NRAB_KNUMH', String(10), default=None, doc="""Sourced from VBAP-NRAB_KNUMH // Condition record number""")
    TRMRISK_RELEVANT = Column('TRMRISK_RELEVANT', String(2), default=None, doc="""Sourced from VBAP-TRMRISK_RELEVANT // Risk Relevancy in Sales""")
    SGT_RCAT = Column('SGT_RCAT', String(16), default=None, doc="""Sourced from VBAP-SGT_RCAT // Requirement Segment""")
    HANDOVERLOC = Column('HANDOVERLOC', String(10), default=None, doc="""Sourced from VBAP-HANDOVERLOC // Location for a physical handover of goods""")
    HANDOVERDATE = Column('HANDOVERDATE', String(8), default=None, doc="""Sourced from VBAP-HANDOVERDATE // Handover Date at the Handover Location""")
    HANDOVERTIME = Column('HANDOVERTIME', String(6), default=None, doc="""Sourced from VBAP-HANDOVERTIME // Handover time at the handover location""")
    TC_AUT_DET = Column('TC_AUT_DET', String(2), default=None, doc="""Sourced from VBAP-TC_AUT_DET // Tax Code Automatically Determined""")
    MANUAL_TC_REASON = Column('MANUAL_TC_REASON', String(2), default=None, doc="""Sourced from VBAP-MANUAL_TC_REASON // Manual Tax Code Reason""")
    FISCAL_INCENTIVE = Column('FISCAL_INCENTIVE', String(4), default=None, doc="""Sourced from VBAP-FISCAL_INCENTIVE // Tax Incentive Type""")
    TAX_SUBJECT_ST = Column('TAX_SUBJECT_ST', String(1), default=None, doc="""Sourced from VBAP-TAX_SUBJECT_ST // Tax Subject to Substituição Tributária""")
    FISCAL_INCENTIVE_ID = Column('FISCAL_INCENTIVE_ID', String(4), default=None, doc="""Sourced from VBAP-FISCAL_INCENTIVE_ID // Incentive ID""")
    SPCSTO = Column('SPCSTO', String(2), default=None, doc="""Sourced from VBAP-SPCSTO // Nota Fiscal Special Case for CFOP Determination""")
    AUFPL_OLC = Column('AUFPL_OLC', String(10), default=None, doc="""Sourced from VBAP-AUFPL_OLC // Routing number of operations in the order""")
    APLZL_OLC = Column('APLZL_OLC', String(8), default=None, doc="""Sourced from VBAP-APLZL_OLC // Internal counter""")
    FERC_IND = Column('FERC_IND', String(4), default=None, doc="""Sourced from VBAP-FERC_IND // Regulatory indicator""")
    KOSTL = Column('KOSTL', String(10), default=None, doc="""Sourced from VBAP-KOSTL // Cost Center""")
    FONDS = Column('FONDS', String(10), default=None, doc="""Sourced from VBAP-FONDS // Fund""")
    FISTL = Column('FISTL', String(16), default=None, doc="""Sourced from VBAP-FISTL // Funds Center""")
    FKBER = Column('FKBER', String(16), default=None, doc="""Sourced from VBAP-FKBER // Functional Area""")
    GRANT_NBR = Column('GRANT_NBR', String(20), default=None, doc="""Sourced from VBAP-GRANT_NBR // Grant""")
    IUID_RELEVANT = Column('IUID_RELEVANT', String(1), default=None, doc="""Sourced from VBAP-IUID_RELEVANT // IUID Relevant for Customer""")
    PRS_OBJNR = Column('PRS_OBJNR', String(22), default=None, doc="""Sourced from VBAP-PRS_OBJNR // Engagement mgmt: Object number""")
    PRS_SD_SPSNR = Column('PRS_SD_SPSNR', String(8), default=None, doc="""Sourced from VBAP-PRS_SD_SPSNR // Standard WBS Element for Project Inception via SD""")
    PRS_WORK_PERIOD = Column('PRS_WORK_PERIOD', String(7), default=None, doc="""Sourced from VBAP-PRS_WORK_PERIOD // Work Period (Internal Representation)""")
    PARGB = Column('PARGB', String(4), default=None, doc="""Sourced from VBAP-PARGB // Trading Partner's Business Area""")
    AUFPL_OAA = Column('AUFPL_OAA', String(10), default=None, doc="""Sourced from VBAP-AUFPL_OAA // Routing number of operations in the order""")
    APLZL_OAA = Column('APLZL_OAA', String(8), default=None, doc="""Sourced from VBAP-APLZL_OAA // Internal counter""")
    YAPPNUM = Column('YAPPNUM', String(15), default=None, doc="""Sourced from VBAP-YAPPNUM // Special Approval Number""")
    YCLMSTAT1 = Column('YCLMSTAT1', String(1), default=None, doc="""Sourced from VBAP-YCLMSTAT1 // Claim Status for Net Short Claims (ZNS doc type only)""")
    YCLMDATE1 = Column('YCLMDATE1', String(8), default=None, doc="""Sourced from VBAP-YCLMDATE1 // Date determined for claim status""")
    YCLMSTAT2 = Column('YCLMSTAT2', String(1), default=None, doc="""Sourced from VBAP-YCLMSTAT2 // Claim Status for Net Short Claims (ZNS doc type only)""")
    YCLMDATE2 = Column('YCLMDATE2', String(8), default=None, doc="""Sourced from VBAP-YCLMDATE2 // Date determined for claim status""")
    YCLEAN_CHARGE = Column('YCLEAN_CHARGE', Boolean, default=None, doc="""Sourced from VBAP-YCLEAN_CHARGE // Flag for cleaning charge %""")
    YYRIMDIAMETER = Column('YYRIMDIAMETER', String(7), default=None, doc="""Sourced from VBAP-YYRIMDIAMETER // Finished Tire Rim Diameter""")
    YYBASEPRNT = Column('YYBASEPRNT', String(15), default=None, doc="""Sourced from VBAP-YYBASEPRNT // Net Value in Document Currency""")
    YYNETPRNT = Column('YYNETPRNT', String(15), default=None, doc="""Sourced from VBAP-YYNETPRNT // Net Value in Document Currency""")
    YYNETPR = Column('YYNETPR', String(15), default=None, doc="""Sourced from VBAP-YYNETPR // Net Value in Document Currency""")
    YYARRIVAL_DATE = Column('YYARRIVAL_DATE', Date, default=None, doc="""Sourced from VBAP-YYARRIVAL_DATE // Arrival Date""")
    YYARRIVAL_TIME = Column('YYARRIVAL_TIME', String(6), default=None, doc="""Sourced from VBAP-YYARRIVAL_TIME // Arrival time""")
    YYZTOPDATE = Column('YYZTOPDATE', String(8), default=None, doc="""Sourced from VBAP-YYZTOPDATE // Date for pseudo terms""")
    YYZTP2DATE = Column('YYZTP2DATE', String(8), default=None, doc="""Sourced from VBAP-YYZTP2DATE // Date for pseudo terms""")
    YYZTOPTERMS = Column('YYZTOPTERMS', String(4), default=None, doc="""Sourced from VBAP-YYZTOPTERMS // Terms of Payment Key""")
    YYZTP2TERMS = Column('YYZTP2TERMS', String(4), default=None, doc="""Sourced from VBAP-YYZTP2TERMS // Terms of Payment Key""")
    YYMANUALTERMS = Column('YYMANUALTERMS', String(4), default=None, doc="""Sourced from VBAP-YYMANUALTERMS // Terms of Payment Key""")
    YYWERKS = Column('YYWERKS', String(4), default=None, doc="""Sourced from VBAP-YYWERKS // Original Plant""")
    YYMSTAV = Column('YYMSTAV', String(2), default=None, doc="""Sourced from VBAP-YYMSTAV // Cross-distribution-chain material status""")
    YYARRIVAL_DAT = Column('YYARRIVAL_DAT', String(8), default=None, doc="""Sourced from VBAP-YYARRIVAL_DAT // Arrival Date""")
    YORIGPROM_DAT = Column('YORIGPROM_DAT', String(8), default=None, doc="""Sourced from VBAP-YORIGPROM_DAT // Customer Promise Date""")
    YWGRU1 = Column('YWGRU1', String(18), default=None, doc="""Sourced from VBAP-YWGRU1 // Material group hierarchy 1""")
    YMTART = Column('YMTART', String(4), default=None, doc="""Sourced from VBAP-YMTART // Material Type""")
    YYDFS = Column('YYDFS', String(1), default=None, doc="""Sourced from VBAP-YYDFS // DFS flag sent through EDI on Wingfoot orders""")
    YYWAITLIST = Column('YYWAITLIST', String(1), default=None, doc="""Sourced from VBAP-YYWAITLIST // Wait List Indicator""")
    YYFAD = Column('YYFAD', Date, default=None, doc="""Sourced from VBAP-YYFAD // Final Acceptance Date""")
    YYORDD = Column('YYORDD', Date, default=None, doc="""Sourced from VBAP-YYORDD // Original Requested Delivery Date""")
    YYFRDD = Column('YYFRDD', Date, default=None, doc="""Sourced from VBAP-YYFRDD // First Requested Delivery Date""")
    YYFMAD = Column('YYFMAD', Date, default=None, doc="""Sourced from VBAP-YYFMAD // First Material Availability Date""")
    YYFGID = Column('YYFGID', Date, default=None, doc="""Sourced from VBAP-YYFGID // First Goods Issue Date""")
    YYPOSNR = Column('YYPOSNR', String(6), default=None, doc="""Sourced from VBAP-YYPOSNR // Original Item number""")

    sd_doc_id = synonym('VBELN')
    sd_doc_item_id = synonym('POSNR')
    material_id = synonym('MATNR')
    entered_material_id = synonym('MATWA')
    pricing_ref_material_id = synonym('PMATN')
    material_group_cd = synonym('MATKL')
    sd_item_descr = synonym('ARKTX')
    sd_item_ctgy_cd = synonym('PSTYV')
    item_type_cd = synonym('POSAR')
    item_relevant_for_delivery_ind = synonym('LFREL')
    billing_relevant_cd = synonym('FKREL')
    rej_reas_id = synonym('ABGRU')
    sls_to_base_uom_conversion_num = synonym('UMZIZ')
    sls_to_base_uom_conversion_denom = synonym('UMZIN')
    uom_cd = synonym('MEINS')
    deliv_rounding_qty = synonym('ABLFZ')
    delivery_group_cd = synonym('GRKOR')
    qty_fixed_ind = synonym('FMENG')
    block_cd = synonym('FAKSP')
    div_cd = synonym('SPART')
    doc_currency_net_value_qty = synonym('NETWR')
    sd_doc_currency_cd = synonym('WAERK')
    max_nbr_partial_deliveries = synonym('ANTLF')
    item_partial_delivery_cd = synonym('KZTLF')
    batch_split_allowed_ind = synonym('CHSPL')
    sales_uom_order_qty = synonym('KWMENG')
    required_delivery_qty = synonym('LSMENG')
    sales_uom_cnfrm_qty = synonym('KBMENG')
    base_uom_confirmed_qty = synonym('KLMENG')
    sls_uom_cd = synonym('VRKME')
    sls_uom_conversion_num = synonym('UMVKZ')
    sls_uom_conversion_denom = synonym('UMVKN')
    gross_wt = synonym('BRGEW')
    net_wt = synonym('NTGEW')
    weight_uom_cd = synonym('GEWEI')
    vol = synonym('VOLUM')
    volume_uom_cd = synonym('VOLEH')
    originating_doc_id = synonym('VBELV')
    originating_item_id = synonym('POSNV')
    reference_doc_id = synonym('VGBEL')
    reference_item_id = synonym('VGPOS')
    complete_reference_ind = synonym('VOREF')
    flow_table_update_ind = synonym('UPFLU')
    quote_completion_rule_cd = synonym('ERLRE')
    delivery_priority_cd = synonym('LPRIO')
    shipping_receiving_point_cd = synonym('VSTEL')
    route_id = synonym('ROUTE')
    doc_create_dt = synonym('ERDAT')
    doc_create_user_id = synonym('ERNAM')
    doc_create_tm = synonym('ERZET')
    net_price_qty = synonym('NETPR')
    availability_checking_group_id = synonym('MTVFP')
    material_pricing_grp_cd = synonym('KONDM')
    volume_rebate_grp_id = synonym('BONUS')
    pricing_is_ok_ind = synonym('PRSOK')
    separate_valuation_ind = synonym('BWTEX')
    batch_mgmt_required_ind = synonym('XCHPF')
    internal_batch_mgmt_ind = synonym('XCHAR')
    update_dt = synonym('AEDAT')
    deliv_dt_and_qty_fixed_ind = synonym('FIXMG')
    special_stock_cd = synonym('SOBKZ')
    allocation_cd = synonym('VPZUO')
    order_id = synonym('AUFNR')
    prod_grp_base_uom_cd = synonym('PRBME')
    reqts_type_cd = synonym('BEDAE')
    item_credit_price_qty = synonym('CMPRE')
    expected_price_status_cd = synonym('CEPOK')
    product_alloc_procedure_cd = synonym('KOSCH')
    special_stock_valuation_Cd = synonym('KZBWS')
    promotion_id = synonym('KNUMA_PI')
    mrp_area_id = synonym('BERID')
    cost_center_id = synonym('KOSTL')
    original_facility_id = synonym('YYWERKS')
    wait_list_ind = synonym('YYWAITLIST')
    final_acceptance_dt = synonym('YYFAD')
    orig_requested_delivery_dt = synonym('YYORDD')
    first_requested_delivery_dt = synonym('YYFRDD')
    first_material_availability_dt = synonym('YYFMAD')
    first_goods_issue_dt = synonym('YYFGID')
    orig_sd_item_id = synonym('YYPOSNR')


################################################################################




################################################################################

class SD_Reqts(SAP_Base):
    """\
    Table sourced from: VBBE
    Description: Sales Requirements: Individual Records
    """

    __tablename__ = "VBBE"

    VBELN = Column('VBELN', String(10), primary_key = True, doc="""Sourced from VBBE-VBELN // Sales Document""")
    POSNR = Column('POSNR', String(6), primary_key = True, doc="""Sourced from VBBE-POSNR // Sales Document Item""")
    ETENR = Column('ETENR', String(4), primary_key = True, doc="""Sourced from VBBE-ETENR // Delivery Schedule Line Number""")
    MATNR = Column('MATNR', String(18), default=None, doc="""Sourced from VBBE-MATNR // Material Number""")
    WERKS = Column('WERKS', String(4), default=None, doc="""Sourced from VBBE-WERKS // Plant""")
    BERID = Column('BERID', String(10), default=None, doc="""Sourced from VBBE-BERID // MRP Area""")
    MBDAT = Column('MBDAT', Date, default=None, doc="""Sourced from VBBE-MBDAT // Material Staging/Availability Date""")
    LGORT = Column('LGORT', String(4), default=None, doc="""Sourced from VBBE-LGORT // Storage Location""")
    CHARG = Column('CHARG', String(10), default=None, doc="""Sourced from VBBE-CHARG // Batch Number""")
    VBTYP = Column('VBTYP', String(1), default=None, doc="""Sourced from VBBE-VBTYP // SD document category""")
    BDART = Column('BDART', String(2), default=None, doc="""Sourced from VBBE-BDART // Requirement type""")
    PLART = Column('PLART', String(1), default=None, doc="""Sourced from VBBE-PLART // Planning type""")
    OMENG = Column('OMENG', Numeric(15,3,3), default=None, doc="""Sourced from VBBE-OMENG // Open Qty in Stockkeeping Units for Transfer of Reqmts to MRP""")
    VMENG = Column('VMENG', Numeric(15,3,3), default=None, doc="""Sourced from VBBE-VMENG // Confirmed quantity for availability check in SKU""")
    MEINS = Column('MEINS', String(3), default=None, doc="""Sourced from VBBE-MEINS // Base Unit of Measure""")
    VBELE = Column('VBELE', String(10), default=None, doc="""Sourced from VBBE-VBELE // Business document number""")
    POSNE = Column('POSNE', String(6), default=None, doc="""Sourced from VBBE-POSNE // Business item number""")
    ETENE = Column('ETENE', String(4), default=None, doc="""Sourced from VBBE-ETENE // Schedule line""")
    AWAHR = Column('AWAHR', String(3), default=None, doc="""Sourced from VBBE-AWAHR // Order probability of the item""")
    AUART = Column('AUART', String(4), default=None, doc="""Sourced from VBBE-AUART // Sales Document Type""")
    PROJN = Column('PROJN', String(16), default=None, doc="""Sourced from VBBE-PROJN // Old: Project number : No longer used --> PS_POSNR""")
    KUNNR = Column('KUNNR', String(10), default=None, doc="""Sourced from VBBE-KUNNR // Sold-to party""")
    NODIS = Column('NODIS', String(1), default=None, doc="""Sourced from VBBE-NODIS // Requirements record not relevant to MRP""")
    VPZUO = Column('VPZUO', String(1), default=None, doc="""Sourced from VBBE-VPZUO // Allocation Indicator""")
    VPMAT = Column('VPMAT', String(18), default=None, doc="""Sourced from VBBE-VPMAT // Planning material""")
    VPWRK = Column('VPWRK', String(4), default=None, doc="""Sourced from VBBE-VPWRK // Planning plant""")
    PRBME = Column('PRBME', String(3), default=None, doc="""Sourced from VBBE-PRBME // Base unit of measure for product group""")
    UMREF = Column('UMREF', String(16), default=None, doc="""Sourced from VBBE-UMREF // Conversion factor: quantities""")
    PZMNG = Column('PZMNG', Numeric(15,3,3), default=None, doc="""Sourced from VBBE-PZMNG // Planned allocation quantity for independent requirements""")
    KNTTP = Column('KNTTP', String(1), default=None, doc="""Sourced from VBBE-KNTTP // Account Assignment Category""")
    SOBKZ = Column('SOBKZ', String(1), default=None, doc="""Sourced from VBBE-SOBKZ // Special Stock Indicator""")
    KZVBR = Column('KZVBR', String(1), default=None, doc="""Sourced from VBBE-KZVBR // Consumption Posting""")
    SERNR = Column('SERNR', String(8), default=None, doc="""Sourced from VBBE-SERNR // BOM explosion number""")
    PSPEL = Column('PSPEL', String(8), default=None, doc="""Sourced from VBBE-PSPEL // WBS Element""")
    PLNKZ = Column('PLNKZ', String(1), default=None, doc="""Sourced from VBBE-PLNKZ // Planning Indicator""")
    CUOBJ = Column('CUOBJ', String(18), default=None, doc="""Sourced from VBBE-CUOBJ // Configuration""")
    MONKZ = Column('MONKZ', Boolean, default=None, doc="""Sourced from VBBE-MONKZ // Indicator: for assembly order procedures""")
    KZBWS = Column('KZBWS', String(1), default=None, doc="""Sourced from VBBE-KZBWS // Valuation of Special Stock""")
    TECHS = Column('TECHS', String(12), default=None, doc="""Sourced from VBBE-TECHS // Parameter Variant/Standard Variant""")
    SGT_RCAT = Column('SGT_RCAT', String(16), default=None, doc="""Sourced from VBBE-SGT_RCAT // Requirement Segment""")

    sd_doc_id = synonym('VBELN')
    sd_doc_item_id = synonym('POSNR')
    deliv_schd_ln_id = synonym('ETENR')
    material_id = synonym('MATNR')
    mrp_area_id = synonym('BERID')
    material_availability_dt = synonym('MBDAT')
    sd_doc_ctgy_cd = synonym('VBTYP')
    reqt_type_cd = synonym('BDART')
    planning_type_cd = synonym('PLART')
    sku_uom_open_qty = synonym('OMENG')
    sku_uom_confirmed_qty = synonym('VMENG')
    uom_cd = synonym('MEINS')
    schd_ln_id = synonym('ETENE')
    sd_hdr_type_cd = synonym('AUART')
    customer_id = synonym('KUNNR')
    allocation_cd = synonym('VPZUO')
    prod_grp_base_uom_cd = synonym('PRBME')
    special_stock_cd = synonym('SOBKZ')
    special_stock_valuation_Cd = synonym('KZBWS')


################################################################################




################################################################################

class SD_SchedLine(SAP_Base):
    """\
    Table sourced from: VBEP
    Description: Sales Document: Schedule Line Data
    """

    __tablename__ = "VBEP"

    VBELN = Column('VBELN', String(10), primary_key = True, doc="""Sourced from VBEP-VBELN // Sales Document""")
    POSNR = Column('POSNR', String(6), primary_key = True, doc="""Sourced from VBEP-POSNR // Sales Document Item""")
    ETENR = Column('ETENR', String(4), primary_key = True, doc="""Sourced from VBEP-ETENR // Delivery Schedule Line Number""")
    ETTYP = Column('ETTYP', String(2), default=None, doc="""Sourced from VBEP-ETTYP // Schedule line category""")
    LFREL = Column('LFREL', Boolean, default=None, doc="""Sourced from VBEP-LFREL // Item is relevant for delivery""")
    EDATU = Column('EDATU', Date, default=None, doc="""Sourced from VBEP-EDATU // Schedule line date""")
    EZEIT = Column('EZEIT', String(6), default=None, doc="""Sourced from VBEP-EZEIT // Arrival time""")
    WMENG = Column('WMENG', Numeric(15,3,3), default=None, doc="""Sourced from VBEP-WMENG // Order quantity in sales units""")
    BMENG = Column('BMENG', Numeric(15,3,3), default=None, doc="""Sourced from VBEP-BMENG // Confirmed Quantity""")
    VRKME = Column('VRKME', String(3), default=None, doc="""Sourced from VBEP-VRKME // Sales unit""")
    LMENG = Column('LMENG', Numeric(15,3,3), default=None, doc="""Sourced from VBEP-LMENG // Required quantity for mat.management in stockkeeping units""")
    MEINS = Column('MEINS', String(3), default=None, doc="""Sourced from VBEP-MEINS // Base Unit of Measure""")
    BDDAT = Column('BDDAT', Date, default=None, doc="""Sourced from VBEP-BDDAT // Requirement date (deadline for procurement)""")
    BDART = Column('BDART', String(2), default=None, doc="""Sourced from VBEP-BDART // Requirement type""")
    PLART = Column('PLART', String(1), default=None, doc="""Sourced from VBEP-PLART // Planning type""")
    VBELE = Column('VBELE', String(10), default=None, doc="""Sourced from VBEP-VBELE // Business document number""")
    POSNE = Column('POSNE', String(6), default=None, doc="""Sourced from VBEP-POSNE // Business item number""")
    ETENE = Column('ETENE', String(4), default=None, doc="""Sourced from VBEP-ETENE // Schedule line""")
    RSDAT = Column('RSDAT', Date, default=None, doc="""Sourced from VBEP-RSDAT // Earliest possible reservation date""")
    IDNNR = Column('IDNNR', String(10), default=None, doc="""Sourced from VBEP-IDNNR // Maintenance request""")
    BANFN = Column('BANFN', String(10), default=None, doc="""Sourced from VBEP-BANFN // Purchase Requisition Number""")
    BSART = Column('BSART', String(4), default=None, doc="""Sourced from VBEP-BSART // Order Type (Purchasing)""")
    BSTYP = Column('BSTYP', String(1), default=None, doc="""Sourced from VBEP-BSTYP // Purchasing Document Category""")
    WEPOS = Column('WEPOS', String(1), default=None, doc="""Sourced from VBEP-WEPOS // Confirmation status of schedule line (incl.ALE)""")
    REPOS = Column('REPOS', Boolean, default=None, doc="""Sourced from VBEP-REPOS // Invoice Receipt Indicator""")
    LRGDT = Column('LRGDT', Date, default=None, doc="""Sourced from VBEP-LRGDT // Return date for returnable packaging""")
    PRGRS = Column('PRGRS', String(1), default=None, doc="""Sourced from VBEP-PRGRS // Date type (day, week, month, interval)""")
    TDDAT = Column('TDDAT', String(8), default=None, doc="""Sourced from VBEP-TDDAT // Transportation Planning Date""")
    MBDAT = Column('MBDAT', Date, default=None, doc="""Sourced from VBEP-MBDAT // Material Staging/Availability Date""")
    LDDAT = Column('LDDAT', Date, default=None, doc="""Sourced from VBEP-LDDAT // Loading Date""")
    WADAT = Column('WADAT', Date, default=None, doc="""Sourced from VBEP-WADAT // Goods Issue Date""")
    CMENG = Column('CMENG', Numeric(15,3,3), default=None, doc="""Sourced from VBEP-CMENG // Corrected quantity in sales unit""")
    LIFSP = Column('LIFSP', String(2), default=None, doc="""Sourced from VBEP-LIFSP // Schedule line blocked for delivery""")
    GRSTR = Column('GRSTR', String(3), default=None, doc="""Sourced from VBEP-GRSTR // Group definition of structure data""")
    ABART = Column('ABART', String(1), default=None, doc="""Sourced from VBEP-ABART // Release type""")
    ABRUF = Column('ABRUF', String(10), default=None, doc="""Sourced from VBEP-ABRUF // Forecast Delivery schedule number""")
    ROMS1 = Column('ROMS1', Numeric(15,3,3), default=None, doc="""Sourced from VBEP-ROMS1 // Committed quantity""")
    ROMS2 = Column('ROMS2', Numeric(15,3,3), default=None, doc="""Sourced from VBEP-ROMS2 // Size 2""")
    ROMS3 = Column('ROMS3', Numeric(15,3,3), default=None, doc="""Sourced from VBEP-ROMS3 // Size 3""")
    ROMEI = Column('ROMEI', String(3), default=None, doc="""Sourced from VBEP-ROMEI // Unit of measure for sizes 1 to 3""")
    RFORM = Column('RFORM', String(2), default=None, doc="""Sourced from VBEP-RFORM // Formula key""")
    UMVKZ = Column('UMVKZ', Numeric(15,3,3), default=None, doc="""Sourced from VBEP-UMVKZ // Numerator (factor) for conversion of sales quantity into SKU""")
    UMVKN = Column('UMVKN', Numeric(15,3,3), default=None, doc="""Sourced from VBEP-UMVKN // Denominator (Divisor) for Conversion of Sales Qty into SKU""")
    VERFP = Column('VERFP', Boolean, default=None, doc="""Sourced from VBEP-VERFP // Availability confirmed automatically""")
    BWART = Column('BWART', String(3), default=None, doc="""Sourced from VBEP-BWART // Movement Type (Inventory Management)""")
    BNFPO = Column('BNFPO', String(5), default=None, doc="""Sourced from VBEP-BNFPO // Item Number of Purchase Requisition""")
    ETART = Column('ETART', String(1), default=None, doc="""Sourced from VBEP-ETART // Schedule line type EDI""")
    AUFNR = Column('AUFNR', String(12), default=None, doc="""Sourced from VBEP-AUFNR // Order Number""")
    PLNUM = Column('PLNUM', String(10), default=None, doc="""Sourced from VBEP-PLNUM // Planned order number""")
    SERNR = Column('SERNR', String(8), default=None, doc="""Sourced from VBEP-SERNR // BOM explosion number""")
    AESKD = Column('AESKD', String(17), default=None, doc="""Sourced from VBEP-AESKD // Customer Engineering Change Status""")
    ABGES = Column('ABGES', String(16), default=None, doc="""Sourced from VBEP-ABGES // Guaranteed (factor between 0 and 1)""")
    MBUHR = Column('MBUHR', Time, default=None, doc="""Sourced from VBEP-MBUHR // Material Staging Time (Local, Relating to a Plant)""")
    TDUHR = Column('TDUHR', Time, default=None, doc="""Sourced from VBEP-TDUHR // Transp. Planning Time (Local, Relating to a Shipping Point)""")
    LDUHR = Column('LDUHR', Time, default=None, doc="""Sourced from VBEP-LDUHR // Loading Time (Local Time Relating to a Shipping Point)""")
    WAUHR = Column('WAUHR', Time, default=None, doc="""Sourced from VBEP-WAUHR // Time of Goods Issue (Local, Relating to a Plant)""")
    AULWE = Column('AULWE', String(10), default=None, doc="""Sourced from VBEP-AULWE // Route Schedule""")
    HANDOVERDATE = Column('HANDOVERDATE', String(8), default=None, doc="""Sourced from VBEP-HANDOVERDATE // Handover Date at the Handover Location""")
    HANDOVERTIME = Column('HANDOVERTIME', String(6), default=None, doc="""Sourced from VBEP-HANDOVERTIME // Handover time at the handover location""")
    MBDAT_DRS = Column('MBDAT_DRS', Date, default=None, doc="""Sourced from VBEP-MBDAT_DRS // Material Availability Date Third-Party Order Planning""")

    sd_doc_id = synonym('VBELN')
    sd_doc_item_id = synonym('POSNR')
    deliv_schd_ln_id = synonym('ETENR')
    schd_ln_ctgy_cd = synonym('ETTYP')
    item_relevant_for_delivery_ind = synonym('LFREL')
    sched_line_dt = synonym('EDATU')
    sls_uom_order_qty = synonym('WMENG')
    cnfrm_qty = synonym('BMENG')
    sls_uom_cd = synonym('VRKME')
    sku_uom_required_qty = synonym('LMENG')
    uom_cd = synonym('MEINS')
    reqt_dt = synonym('BDDAT')
    reqt_type_cd = synonym('BDART')
    planning_type_cd = synonym('PLART')
    schd_ln_id = synonym('ETENE')
    prch_req_id = synonym('BANFN')
    prch_ord_type_cd = synonym('BSART')
    prch_doc_ctgy_cd = synonym('BSTYP')
    goods_receipt_ind = synonym('WEPOS')
    material_availability_dt = synonym('MBDAT')
    loading_dt = synonym('LDDAT')
    goods_issue_dt = synonym('WADAT')
    sales_uom_corrected_qty = synonym('CMENG')
    default_delivery_blk_cd = synonym('LIFSP')
    sls_uom_conversion_num = synonym('UMVKZ')
    sls_uom_conversion_denom = synonym('UMVKN')
    check_availability_ind = synonym('VERFP')
    im_matl_mvmnt_type_cd = synonym('BWART')
    prch_req_item_id = synonym('BNFPO')
    order_id = synonym('AUFNR')
    material_staging_tm = synonym('MBUHR')
    loading_tm = synonym('LDUHR')
    goods_issue_tm = synonym('WAUHR')
    route_schd_id = synonym('AULWE')


################################################################################




################################################################################

class SD_Flow(SAP_Base):
    """\
    Table sourced from: VBFA
    Description: Sales Document Flow
    """

    __tablename__ = "VBFA"

    VBELV = Column('VBELV', String(10), primary_key = True, doc="""Sourced from VBFA-VBELV // Preceding sales and distribution document""")
    POSNV = Column('POSNV', String(6), primary_key = True, doc="""Sourced from VBFA-POSNV // Preceding item of an SD document""")
    VBELN = Column('VBELN', String(10), primary_key = True, doc="""Sourced from VBFA-VBELN // Subsequent sales and distribution document""")
    POSNN = Column('POSNN', String(6), primary_key = True, doc="""Sourced from VBFA-POSNN // Subsequent item of an SD document""")
    VBTYP_N = Column('VBTYP_N', String(1), primary_key = True, doc="""Sourced from VBFA-VBTYP_N // Document category of subsequent document""")
    RFMNG = Column('RFMNG', Numeric(15,3,3), default=None, doc="""Sourced from VBFA-RFMNG // Referenced quantity in base unit of measure""")
    MEINS = Column('MEINS', String(3), default=None, doc="""Sourced from VBFA-MEINS // Base Unit of Measure""")
    RFWRT = Column('RFWRT', Numeric(15,3,3), default=None, doc="""Sourced from VBFA-RFWRT // Reference value""")
    WAERS = Column('WAERS', String(5), default=None, doc="""Sourced from VBFA-WAERS // Statistics currency""")
    VBTYP_V = Column('VBTYP_V', String(1), default=None, doc="""Sourced from VBFA-VBTYP_V // Document category of preceding SD document""")
    PLMIN = Column('PLMIN', String(1), default=None, doc="""Sourced from VBFA-PLMIN // Quantity is calculated positively, negatively or not at all""")
    TAQUI = Column('TAQUI', Boolean, default=None, doc="""Sourced from VBFA-TAQUI // ID: MM-WM transfer order confirmed""")
    ERDAT = Column('ERDAT', Date, default=None, doc="""Sourced from VBFA-ERDAT // Date on Which Record Was Created""")
    ERZET = Column('ERZET', Time, default=None, doc="""Sourced from VBFA-ERZET // Entry time""")
    MATNR = Column('MATNR', String(18), default=None, doc="""Sourced from VBFA-MATNR // Material Number""")
    BWART = Column('BWART', String(3), default=None, doc="""Sourced from VBFA-BWART // Movement Type (Inventory Management)""")
    BDART = Column('BDART', String(2), default=None, doc="""Sourced from VBFA-BDART // Requirement type""")
    PLART = Column('PLART', String(1), default=None, doc="""Sourced from VBFA-PLART // Planning type""")
    STUFE = Column('STUFE', Numeric(15,3,3), default=None, doc="""Sourced from VBFA-STUFE // Level of the document flow record""")
    LGNUM = Column('LGNUM', String(3), default=None, doc="""Sourced from VBFA-LGNUM // Warehouse Number / Warehouse Complex""")
    AEDAT = Column('AEDAT', Date, default=None, doc="""Sourced from VBFA-AEDAT // Changed On""")
    FKTYP = Column('FKTYP', String(1), default=None, doc="""Sourced from VBFA-FKTYP // Billing category""")
    BRGEW = Column('BRGEW', Numeric(15,3,3), default=None, doc="""Sourced from VBFA-BRGEW // Gross weight""")
    GEWEI = Column('GEWEI', String(3), default=None, doc="""Sourced from VBFA-GEWEI // Weight Unit""")
    VOLUM = Column('VOLUM', Numeric(15,3,3), default=None, doc="""Sourced from VBFA-VOLUM // Volume""")
    VOLEH = Column('VOLEH', String(3), default=None, doc="""Sourced from VBFA-VOLEH // Volume unit""")
    FPLNR = Column('FPLNR', String(10), default=None, doc="""Sourced from VBFA-FPLNR // Billing plan number / invoicing plan number""")
    FPLTR = Column('FPLTR', String(6), default=None, doc="""Sourced from VBFA-FPLTR // Item for billing plan/invoice plan/payment cards""")
    RFMNG_FLO = Column('RFMNG_FLO', Float, default=None, doc="""Sourced from VBFA-RFMNG_FLO // Referenced quantity in sales unit (float)""")
    RFMNG_FLT = Column('RFMNG_FLT', Float, default=None, doc="""Sourced from VBFA-RFMNG_FLT // Referenced quantity in base unit of measure (float)""")
    VRKME = Column('VRKME', String(3), default=None, doc="""Sourced from VBFA-VRKME // Sales unit""")
    ABGES = Column('ABGES', String(16), default=None, doc="""Sourced from VBFA-ABGES // Guaranteed (factor between 0 and 1)""")
    SOBKZ = Column('SOBKZ', String(1), default=None, doc="""Sourced from VBFA-SOBKZ // Special Stock Indicator""")
    SONUM = Column('SONUM', String(16), default=None, doc="""Sourced from VBFA-SONUM // Special Stock Number""")
    KZBEF = Column('KZBEF', Boolean, default=None, doc="""Sourced from VBFA-KZBEF // Indicator Inventory Management active""")
    NTGEW = Column('NTGEW', Numeric(15,3,3), default=None, doc="""Sourced from VBFA-NTGEW // Net Weight""")
    LOGSYS = Column('LOGSYS', String(10), default=None, doc="""Sourced from VBFA-LOGSYS // Logical system""")
    WBSTA = Column('WBSTA', String(1), default=None, doc="""Sourced from VBFA-WBSTA // Goods movement status""")
    CMETH = Column('CMETH', String(1), default=None, doc="""Sourced from VBFA-CMETH // Quantity Conversion Method""")
    MJAHR = Column('MJAHR', String(4), default=None, doc="""Sourced from VBFA-MJAHR // Material Document Year""")
    VBTYPEXT_V = Column('VBTYPEXT_V', String(4), default=None, doc="""Sourced from VBFA-VBTYPEXT_V // Extension of SD document category of preceding document""")
    VBTYPEXT_N = Column('VBTYPEXT_N', String(4), default=None, doc="""Sourced from VBFA-VBTYPEXT_N // Extension of Subsequent SD Document Category""")

    originating_doc_id = synonym('VBELV')
    originating_item_id = synonym('POSNV')
    sd_doc_id = synonym('VBELN')
    next_sd_doc_ctgy_cd = synonym('VBTYP_N')
    uom_cd = synonym('MEINS')
    currency_cd = synonym('WAERS')
    prior_sd_doc_ctgy_cd = synonym('VBTYP_V')
    doc_create_dt = synonym('ERDAT')
    doc_create_tm = synonym('ERZET')
    material_id = synonym('MATNR')
    im_matl_mvmnt_type_cd = synonym('BWART')
    reqt_type_cd = synonym('BDART')
    planning_type_cd = synonym('PLART')
    warehouse_nbr = synonym('LGNUM')
    update_dt = synonym('AEDAT')
    billing_ctgy_cd = synonym('FKTYP')
    gross_wt = synonym('BRGEW')
    weight_uom_cd = synonym('GEWEI')
    vol = synonym('VOLUM')
    volume_uom_cd = synonym('VOLEH')
    sls_uom_cd = synonym('VRKME')
    special_stock_cd = synonym('SOBKZ')
    net_wt = synonym('NTGEW')
    goods_movement_status_cd = synonym('WBSTA')
    material_doc_year = synonym('MJAHR')


################################################################################




################################################################################

class SD_BusData(SAP_Base):
    """\
    Table sourced from: VBKD
    Description: Sales Document: Business Data
    """

    __tablename__ = "VBKD"

    VBELN = Column('VBELN', String(10), primary_key = True, doc="""Sourced from VBKD-VBELN // Sales and Distribution Document Number""")
    POSNR = Column('POSNR', String(6), primary_key = True, doc="""Sourced from VBKD-POSNR // Item number of the SD document""")
    KONDA = Column('KONDA', String(2), default=None, doc="""Sourced from VBKD-KONDA // Price group (customer)""")
    KDGRP = Column('KDGRP', String(2), default=None, doc="""Sourced from VBKD-KDGRP // Customer group""")
    BZIRK = Column('BZIRK', String(6), default=None, doc="""Sourced from VBKD-BZIRK // Sales district""")
    PLTYP = Column('PLTYP', String(2), default=None, doc="""Sourced from VBKD-PLTYP // Price list type""")
    INCO1 = Column('INCO1', String(3), default=None, doc="""Sourced from VBKD-INCO1 // Incoterms (Part 1)""")
    INCO2 = Column('INCO2', String(28), default=None, doc="""Sourced from VBKD-INCO2 // Incoterms (Part 2)""")
    KZAZU = Column('KZAZU', Boolean, default=None, doc="""Sourced from VBKD-KZAZU // Order Combination Indicator""")
    PERFK = Column('PERFK', String(2), default=None, doc="""Sourced from VBKD-PERFK // Invoice dates (calendar identification)""")
    PERRL = Column('PERRL', String(2), default=None, doc="""Sourced from VBKD-PERRL // Invoice list schedule (calendar identification)""")
    MRNKZ = Column('MRNKZ', Boolean, default=None, doc="""Sourced from VBKD-MRNKZ // Manual invoice maintenance""")
    KURRF = Column('KURRF', Numeric(15,3,3), default=None, doc="""Sourced from VBKD-KURRF // Exchange rate for FI postings""")
    VALTG = Column('VALTG', String(2), default=None, doc="""Sourced from VBKD-VALTG // Additional value days""")
    VALDT = Column('VALDT', Date, default=None, doc="""Sourced from VBKD-VALDT // Fixed value date""")
    ZTERM = Column('ZTERM', String(4), default=None, doc="""Sourced from VBKD-ZTERM // Terms of Payment Key""")
    ZLSCH = Column('ZLSCH', String(1), default=None, doc="""Sourced from VBKD-ZLSCH // Payment Method""")
    KTGRD = Column('KTGRD', String(2), default=None, doc="""Sourced from VBKD-KTGRD // Account assignment group for this customer""")
    KURSK = Column('KURSK', Numeric(15,3,3), default=None, doc="""Sourced from VBKD-KURSK // Exchange Rate for Price Determination""")
    PRSDT = Column('PRSDT', Date, default=None, doc="""Sourced from VBKD-PRSDT // Date for pricing and exchange rate""")
    FKDAT = Column('FKDAT', Date, default=None, doc="""Sourced from VBKD-FKDAT // Billing date for billing index and printout""")
    FBUDA = Column('FBUDA', Date, default=None, doc="""Sourced from VBKD-FBUDA // Date on which services rendered""")
    GJAHR = Column('GJAHR', String(4), default=None, doc="""Sourced from VBKD-GJAHR // Fiscal Year""")
    POPER = Column('POPER', String(3), default=None, doc="""Sourced from VBKD-POPER // Posting period""")
    STCUR = Column('STCUR', Numeric(15,3,3), default=None, doc="""Sourced from VBKD-STCUR // Exchange rate for statistics""")
    MSCHL = Column('MSCHL', String(1), default=None, doc="""Sourced from VBKD-MSCHL // Dunning Key""")
    MANSP = Column('MANSP', String(1), default=None, doc="""Sourced from VBKD-MANSP // Dunning Block""")
    FPLNR = Column('FPLNR', String(10), default=None, doc="""Sourced from VBKD-FPLNR // Billing plan number / invoicing plan number""")
    WAKTION = Column('WAKTION', String(10), default=None, doc="""Sourced from VBKD-WAKTION // Promotion""")
    ABSSC = Column('ABSSC', String(6), default=None, doc="""Sourced from VBKD-ABSSC // Payment guarantee procedure""")
    LCNUM = Column('LCNUM', String(10), default=None, doc="""Sourced from VBKD-LCNUM // Financial doc. processing: Internal financial doc. number""")
    J_1AFITP = Column('J_1AFITP', String(2), default=None, doc="""Sourced from VBKD-J_1AFITP // Tax type""")
    J_1ARFZ = Column('J_1ARFZ', String(1), default=None, doc="""Sourced from VBKD-J_1ARFZ // Reason for zero VAT""")
    J_1AREGIO = Column('J_1AREGIO', String(3), default=None, doc="""Sourced from VBKD-J_1AREGIO // Region (State, Province, County)""")
    J_1AGICD = Column('J_1AGICD', String(2), default=None, doc="""Sourced from VBKD-J_1AGICD // Activity Code for Gross Income Tax""")
    J_1ADTYP = Column('J_1ADTYP', String(2), default=None, doc="""Sourced from VBKD-J_1ADTYP // Distribution Type for Employment Tax""")
    J_1ATXREL = Column('J_1ATXREL', String(10), default=None, doc="""Sourced from VBKD-J_1ATXREL // Tax relevant classification""")
    ABTNR = Column('ABTNR', String(4), default=None, doc="""Sourced from VBKD-ABTNR // Department number""")
    EMPST = Column('EMPST', String(25), default=None, doc="""Sourced from VBKD-EMPST // Receiving point""")
    BSTKD = Column('BSTKD', String(35), default=None, doc="""Sourced from VBKD-BSTKD // Customer purchase order number""")
    BSTDK = Column('BSTDK', Date, default=None, doc="""Sourced from VBKD-BSTDK // Customer purchase order date""")
    BSARK = Column('BSARK', String(4), default=None, doc="""Sourced from VBKD-BSARK // Customer purchase order type""")
    IHREZ = Column('IHREZ', String(12), default=None, doc="""Sourced from VBKD-IHREZ // Your Reference""")
    BSTKD_E = Column('BSTKD_E', String(35), default=None, doc="""Sourced from VBKD-BSTKD_E // Ship-to Party's Purchase Order Number""")
    BSTDK_E = Column('BSTDK_E', Date, default=None, doc="""Sourced from VBKD-BSTDK_E // Ship-to party's PO date""")
    BSARK_E = Column('BSARK_E', String(4), default=None, doc="""Sourced from VBKD-BSARK_E // Ship-to party purchase order type""")
    IHREZ_E = Column('IHREZ_E', String(12), default=None, doc="""Sourced from VBKD-IHREZ_E // Ship-to party character""")
    POSEX_E = Column('POSEX_E', String(6), default=None, doc="""Sourced from VBKD-POSEX_E // Item Number of the Underlying Purchase Order""")
    KURSK_DAT = Column('KURSK_DAT', String(8), default=None, doc="""Sourced from VBKD-KURSK_DAT // Translation Date""")
    KURRF_DAT = Column('KURRF_DAT', String(8), default=None, doc="""Sourced from VBKD-KURRF_DAT // Translation Date""")
    KDKG1 = Column('KDKG1', String(2), default=None, doc="""Sourced from VBKD-KDKG1 // Customer condition group 1""")
    KDKG2 = Column('KDKG2', String(2), default=None, doc="""Sourced from VBKD-KDKG2 // Customer condition group 2""")
    KDKG3 = Column('KDKG3', String(2), default=None, doc="""Sourced from VBKD-KDKG3 // Customer condition group 3""")
    KDKG4 = Column('KDKG4', String(2), default=None, doc="""Sourced from VBKD-KDKG4 // Customer condition group 4""")
    KDKG5 = Column('KDKG5', String(2), default=None, doc="""Sourced from VBKD-KDKG5 // Customer condition group 5""")
    WKWAE = Column('WKWAE', String(5), default=None, doc="""Sourced from VBKD-WKWAE // Value contract currency""")
    WKKUR = Column('WKKUR', Numeric(15,3,3), default=None, doc="""Sourced from VBKD-WKKUR // Exchange rate in value contract currency""")
    AKWAE = Column('AKWAE', String(5), default=None, doc="""Sourced from VBKD-AKWAE // Currency key for letter-of-credit procg in foreign trade""")
    AKKUR = Column('AKKUR', Numeric(15,3,3), default=None, doc="""Sourced from VBKD-AKKUR // Exchange rate for letter-of-credit procg in foreign trade""")
    AKPRZ = Column('AKPRZ', Numeric(15,3,3), default=None, doc="""Sourced from VBKD-AKPRZ // Depreciation percentage for financial document processing""")
    J_1AINDXP = Column('J_1AINDXP', String(5), default=None, doc="""Sourced from VBKD-J_1AINDXP // Inflation Index""")
    J_1AIDATEP = Column('J_1AIDATEP', Date, default=None, doc="""Sourced from VBKD-J_1AIDATEP // Indexing base date""")
    BSTKD_M = Column('BSTKD_M', String(35), default=None, doc="""Sourced from VBKD-BSTKD_M // Customer PO number as matchcode field""")
    DELCO = Column('DELCO', String(3), default=None, doc="""Sourced from VBKD-DELCO // Agreed delivery time""")
    FFPRF = Column('FFPRF', String(8), default=None, doc="""Sourced from VBKD-FFPRF // Dynamic Item Processor Profile""")
    BEMOT = Column('BEMOT', String(2), default=None, doc="""Sourced from VBKD-BEMOT // Accounting Indicator""")
    FAKTF = Column('FAKTF', String(2), default=None, doc="""Sourced from VBKD-FAKTF // Billing form""")
    RRREL = Column('RRREL', String(1), default=None, doc="""Sourced from VBKD-RRREL // Revenue recognition category""")
    ACDATV = Column('ACDATV', String(1), default=None, doc="""Sourced from VBKD-ACDATV // Proposed start date for accrual period""")
    VSART = Column('VSART', String(2), default=None, doc="""Sourced from VBKD-VSART // Shipping type""")
    TRATY = Column('TRATY', String(4), default=None, doc="""Sourced from VBKD-TRATY // Means-of-Transport Type""")
    TRMTYP = Column('TRMTYP', String(18), default=None, doc="""Sourced from VBKD-TRMTYP // Means of Transport""")
    SDABW = Column('SDABW', String(4), default=None, doc="""Sourced from VBKD-SDABW // Special processing indicator""")
    WMINR = Column('WMINR', String(10), default=None, doc="""Sourced from VBKD-WMINR // Product catalog number""")
    FKBER = Column('FKBER', String(16), default=None, doc="""Sourced from VBKD-FKBER // Functional Area""")
    PODKZ = Column('PODKZ', Boolean, default=None, doc="""Sourced from VBKD-PODKZ // Relevant for POD processing""")
    VKONT = Column('VKONT', String(12), default=None, doc="""Sourced from VBKD-VKONT // Contract Account Number""")
    DPBP_REF_FPLNR = Column('DPBP_REF_FPLNR', String(10), default=None, doc="""Sourced from VBKD-DPBP_REF_FPLNR // Billing plan number / invoicing plan number""")
    DPBP_REF_FPLTR = Column('DPBP_REF_FPLTR', String(6), default=None, doc="""Sourced from VBKD-DPBP_REF_FPLTR // Item for billing plan/invoice plan/payment cards""")
    REVSP = Column('REVSP', String(1), default=None, doc="""Sourced from VBKD-REVSP // Revenue Distribution Type""")
    REVEVTYP = Column('REVEVTYP', String(1), default=None, doc="""Sourced from VBKD-REVEVTYP // Revenue Event Type (Customizing)""")
    FARR_RELTYPE = Column('FARR_RELTYPE', String(10), default=None, doc="""Sourced from VBKD-FARR_RELTYPE // Revenue Accounting Type""")
    VTREF = Column('VTREF', String(20), default=None, doc="""Sourced from VBKD-VTREF // Reference Specifications from Contract""")
    J_1TPBUPL = Column('J_1TPBUPL', String(5), default=None, doc="""Sourced from VBKD-J_1TPBUPL // Branch Code""")
    PEROP_BEG = Column('PEROP_BEG', String(8), default=None, doc="""Sourced from VBKD-PEROP_BEG // Period of Performance Start Date""")
    PEROP_END = Column('PEROP_END', String(8), default=None, doc="""Sourced from VBKD-PEROP_END // Period of Performance End Date""")
    STCODE = Column('STCODE', Numeric(15,3,3), default=None, doc="""Sourced from VBKD-STCODE // LST CST applicability code""")
    FORMC1 = Column('FORMC1', String(3), default=None, doc="""Sourced from VBKD-FORMC1 // Form Type""")
    FORMC2 = Column('FORMC2', String(3), default=None, doc="""Sourced from VBKD-FORMC2 // Form Type""")
    STEUC = Column('STEUC', String(16), default=None, doc="""Sourced from VBKD-STEUC // Control code for consumption taxes in foreign trade""")
    COMPREAS = Column('COMPREAS', String(4), default=None, doc="""Sourced from VBKD-COMPREAS // Abbreviation for Complaints Reason""")
    MNDID = Column('MNDID', String(35), default=None, doc="""Sourced from VBKD-MNDID // Unique Referene to Mandate per Payment Recipient""")
    PAY_TYPE = Column('PAY_TYPE', String(1), default=None, doc="""Sourced from VBKD-PAY_TYPE // SEPA: Payment Type""")
    SEPON = Column('SEPON', String(1), default=None, doc="""Sourced from VBKD-SEPON // SEPA-Relevance""")
    MNDVG = Column('MNDVG', String(1), default=None, doc="""Sourced from VBKD-MNDVG // SEPA-Relevance""")

    sd_doc_id = synonym('VBELN')
    sd_doc_item_id = synonym('POSNR')
    customer_pricing_grp_cd = synonym('KONDA')
    customer_group_id = synonym('KDGRP')
    sales_district_id = synonym('BZIRK')
    incoterms_cd = synonym('INCO1')
    incoterms_desc = synonym('INCO2')
    pricing_dt = synonym('PRSDT')
    billing_dt = synonym('FKDAT')
    services_rendered_dt = synonym('FBUDA')
    fiscal_year = synonym('GJAHR')
    receiving_point_cd = synonym('EMPST')
    cust_prch_ord_nbr = synonym('BSTKD')
    cust_prch_ord_dt = synonym('BSTDK')
    cust_prch_ord_type_cd = synonym('BSARK')
    ship_to_cust_prch_ord_nbr = synonym('BSTKD_E')
    ship_to_cust_prch_ord_dt = synonym('BSTDK_E')
    ship_to_cust_prch_ord_type_cd = synonym('BSARK_E')
    cust_prch_ord_id = synonym('BSTKD_M')
    means_of_transportation_type_cd = synonym('TRATY')
    means_of_transportation = synonym('TRMTYP')
    special_processing_cd = synonym('SDABW')


################################################################################




################################################################################

class SD_ReleaseOrder(SAP_Base):
    """\
    Table sourced from: VBLB
    Description: Sales document: Release order data
    """

    __tablename__ = "VBLB"

    VBELN = Column('VBELN', String(10), primary_key = True, doc="""Sourced from VBLB-VBELN // Sales Document""")
    POSNR = Column('POSNR', String(6), primary_key = True, doc="""Sourced from VBLB-POSNR // Sales Document Item""")
    ABRLI = Column('ABRLI', String(4), primary_key = True, doc="""Sourced from VBLB-ABRLI // Internal delivery schedule number""")
    ABART = Column('ABART', String(1), primary_key = True, doc="""Sourced from VBLB-ABART // Release type""")
    DOCNUM = Column('DOCNUM', String(16), default=None, doc="""Sourced from VBLB-DOCNUM // IDoc number""")
    ABEFZ = Column('ABEFZ', Numeric(15,3,3), default=None, doc="""Sourced from VBLB-ABEFZ // Cumulative Quantity Received by Customer""")
    ABRAB = Column('ABRAB', Date, default=None, doc="""Sourced from VBLB-ABRAB // Dlv. sched. valid from""")
    ABRBI = Column('ABRBI', Date, default=None, doc="""Sourced from VBLB-ABRBI // SA rel. valid to""")
    LABNK = Column('LABNK', String(17), default=None, doc="""Sourced from VBLB-LABNK // Customer number for forecast / JIT dlv. sched.""")
    ABRDT = Column('ABRDT', Date, default=None, doc="""Sourced from VBLB-ABRDT // Delivery Schedule Date""")
    TERSL = Column('TERSL', String(1), default=None, doc="""Sourced from VBLB-TERSL // Date key for schedule line dates""")
    LFDKD = Column('LFDKD', Date, default=None, doc="""Sourced from VBLB-LFDKD // Date of last delivery posted by the customer""")
    LFNKD = Column('LFNKD', String(10), default=None, doc="""Sourced from VBLB-LFNKD // Last delivery confirmed by the customer""")
    ABFDA = Column('ABFDA', Date, default=None, doc="""Sourced from VBLB-ABFDA // Start of production go-ahead""")
    ABFDE = Column('ABFDE', Date, default=None, doc="""Sourced from VBLB-ABFDE // End of production go-ahead""")
    ABMDA = Column('ABMDA', Date, default=None, doc="""Sourced from VBLB-ABMDA // Start of material go-ahead""")
    ABMDE = Column('ABMDE', Date, default=None, doc="""Sourced from VBLB-ABMDE // End of material go-ahead""")
    ABLLI = Column('ABLLI', String(4), default=None, doc="""Sourced from VBLB-ABLLI // Last internal release order number""")
    HIFFZ = Column('HIFFZ', Numeric(15,3,3), default=None, doc="""Sourced from VBLB-HIFFZ // Highest cumulative production go-ahead quantity""")
    HIFFZLI = Column('HIFFZLI', String(4), default=None, doc="""Sourced from VBLB-HIFFZLI // Internal schedule no.for highest prod.go-ahead cml.qty""")
    HIMFZ = Column('HIMFZ', Numeric(15,3,3), default=None, doc="""Sourced from VBLB-HIMFZ // Highest cumulative material go-ahead quantity""")
    HIMFZLI = Column('HIMFZLI', String(4), default=None, doc="""Sourced from VBLB-HIMFZLI // Internal schedule number for highest mat.go-ahead cml.qty""")
    ERDAT = Column('ERDAT', Date, default=None, doc="""Sourced from VBLB-ERDAT // Date on Which Record Was Created""")
    ERZEI = Column('ERZEI', String(6), default=None, doc="""Sourced from VBLB-ERZEI // Entry time""")
    ERNAM = Column('ERNAM', String(12), default=None, doc="""Sourced from VBLB-ERNAM // Name of Person who Created the Object""")
    HILFZ = Column('HILFZ', Numeric(15,3,3), default=None, doc="""Sourced from VBLB-HILFZ // Highest delivery go-ahead cumulative quantity""")
    HILFZLI = Column('HILFZLI', String(4), default=None, doc="""Sourced from VBLB-HILFZLI // Internal schedule number for highest dlv.go-ahead cml.qty""")
    ABHOR = Column('ABHOR', Date, default=None, doc="""Sourced from VBLB-ABHOR // JIT horizon""")
    GJKUN = Column('GJKUN', String(4), default=None, doc="""Sourced from VBLB-GJKUN // Customer fiscal year""")
    VJKUN = Column('VJKUN', String(4), default=None, doc="""Sourced from VBLB-VJKUN // Customer fiscal year which is not yet closed""")
    AKMFZ = Column('AKMFZ', Numeric(15,3,3), default=None, doc="""Sourced from VBLB-AKMFZ // Actual cumulative material go-ahead quantity""")
    AKFFZ = Column('AKFFZ', Numeric(15,3,3), default=None, doc="""Sourced from VBLB-AKFFZ // Actual cumulative production go-ahead quantity""")
    AKLFZ = Column('AKLFZ', Numeric(15,3,3), default=None, doc="""Sourced from VBLB-AKLFZ // Actual cumulative delivery go-ahead quantity""")
    KRITB = Column('KRITB', String(1), default=None, doc="""Sourced from VBLB-KRITB // Key for high priority stock""")
    LABKY = Column('LABKY', String(1), default=None, doc="""Sourced from VBLB-LABKY // Requirements status key""")
    VBRST = Column('VBRST', String(14), default=None, doc="""Sourced from VBLB-VBRST // Customer point of consumption""")
    EDLLS = Column('EDLLS', String(20), default=None, doc="""Sourced from VBLB-EDLLS // Last dlv. note sent by ext. service agent to the customer""")
    EDLDT = Column('EDLDT', Date, default=None, doc="""Sourced from VBLB-EDLDT // Date of last delivery sent by external agent to customer""")
    LFMKD = Column('LFMKD', Numeric(15,3,3), default=None, doc="""Sourced from VBLB-LFMKD // Last delivery quantity received by the customer""")
    UMVKZ = Column('UMVKZ', Numeric(15,3,3), default=None, doc="""Sourced from VBLB-UMVKZ // Numerator (factor) for conversion of sales quantity into SKU""")
    UMVKN = Column('UMVKN', Numeric(15,3,3), default=None, doc="""Sourced from VBLB-UMVKN // Denominator (Divisor) for Conversion of Sales Qty into SKU""")
    USR01 = Column('USR01', String(35), default=None, doc="""Sourced from VBLB-USR01 // Additional data field 1 for delivery schedules""")
    USR02 = Column('USR02', String(35), default=None, doc="""Sourced from VBLB-USR02 // Additional data field 2 for delivery schedules""")
    USR03 = Column('USR03', String(35), default=None, doc="""Sourced from VBLB-USR03 // Additional data field 3 for delivery schedules""")
    USR04 = Column('USR04', String(10), default=None, doc="""Sourced from VBLB-USR04 // Additional data field 4 for delivery schedules""")
    USR05 = Column('USR05', String(10), default=None, doc="""Sourced from VBLB-USR05 // Additional data field 5 for delivery schedules""")
    CYEFZ = Column('CYEFZ', Numeric(15,3,3), default=None, doc="""Sourced from VBLB-CYEFZ // Cumulative quantity reached on date zero setting made""")
    CYDAT = Column('CYDAT', Date, default=None, doc="""Sourced from VBLB-CYDAT // Date on which cumulative received quantity set to zero""")
    MFLAUF = Column('MFLAUF', String(3), default=None, doc="""Sourced from VBLB-MFLAUF // Material go-ahead - validity period""")
    MFEIN = Column('MFEIN', String(1), default=None, doc="""Sourced from VBLB-MFEIN // Material go-ahead - unit validity period""")
    FFLAUF = Column('FFLAUF', String(3), default=None, doc="""Sourced from VBLB-FFLAUF // Production go-ahead  - validity period""")
    FFEIN = Column('FFEIN', String(1), default=None, doc="""Sourced from VBLB-FFEIN // Production go-ahead - Unit validity period""")
    ABRDT_ORG = Column('ABRDT_ORG', Date, default=None, doc="""Sourced from VBLB-ABRDT_ORG // Delivery schedule date of creation""")
    LFMAIS = Column('LFMAIS', String(20), default=None, doc="""Sourced from VBLB-LFMAIS // Last pick-up sheet sent by the customer""")
    MAIDT = Column('MAIDT', Date, default=None, doc="""Sourced from VBLB-MAIDT // Date of last pick-up sheet""")
    AEDAT = Column('AEDAT', Date, default=None, doc="""Sourced from VBLB-AEDAT // Changed On""")

    sd_doc_id = synonym('VBELN')
    sd_doc_item_id = synonym('POSNR')
    doc_create_dt = synonym('ERDAT')
    doc_create_user_id = synonym('ERNAM')
    jit_horizon = synonym('ABHOR')
    customer_fiscal_year = synonym('GJKUN')
    sls_uom_conversion_num = synonym('UMVKZ')
    sls_uom_conversion_denom = synonym('UMVKN')
    update_dt = synonym('AEDAT')


################################################################################




################################################################################

class SD_Partner(SAP_Base):
    """\
    Table sourced from: VBPA
    Description: Sales Document: Partner
    """

    __tablename__ = "VBPA"

    VBELN = Column('VBELN', String(10), primary_key = True, doc="""Sourced from VBPA-VBELN // Sales and Distribution Document Number""")
    POSNR = Column('POSNR', String(6), primary_key = True, doc="""Sourced from VBPA-POSNR // Item number of the SD document""")
    PARVW = Column('PARVW', String(2), primary_key = True, doc="""Sourced from VBPA-PARVW // Partner Function""")
    KUNNR = Column('KUNNR', String(10), default=None, doc="""Sourced from VBPA-KUNNR // Customer Number""")
    LIFNR = Column('LIFNR', String(10), default=None, doc="""Sourced from VBPA-LIFNR // Account Number of Vendor or Creditor""")
    PERNR = Column('PERNR', String(8), default=None, doc="""Sourced from VBPA-PERNR // Personnel Number""")
    PARNR = Column('PARNR', String(10), default=None, doc="""Sourced from VBPA-PARNR // Number of contact person""")
    ADRNR = Column('ADRNR', String(10), default=None, doc="""Sourced from VBPA-ADRNR // Address""")
    ABLAD = Column('ABLAD', String(25), default=None, doc="""Sourced from VBPA-ABLAD // Unloading Point""")
    LAND1 = Column('LAND1', String(3), default=None, doc="""Sourced from VBPA-LAND1 // Country Key""")
    ADRDA = Column('ADRDA', String(1), default=None, doc="""Sourced from VBPA-ADRDA // Address indicator""")
    XCPDK = Column('XCPDK', Boolean, default=None, doc="""Sourced from VBPA-XCPDK // Indicator: Is the account a one-time account?""")
    HITYP = Column('HITYP', String(1), default=None, doc="""Sourced from VBPA-HITYP // Customer hierarchy type""")
    PRFRE = Column('PRFRE', Boolean, default=None, doc="""Sourced from VBPA-PRFRE // Relevant for price determination ID""")
    BOKRE = Column('BOKRE', Boolean, default=None, doc="""Sourced from VBPA-BOKRE // Indicator: Customer Is Rebate-Relevant""")
    HISTUNR = Column('HISTUNR', String(2), default=None, doc="""Sourced from VBPA-HISTUNR // Level number within hierarchy""")
    KNREF = Column('KNREF', String(30), default=None, doc="""Sourced from VBPA-KNREF // Customer description of partner (plant, storage location)""")
    LZONE = Column('LZONE', String(10), default=None, doc="""Sourced from VBPA-LZONE // Transportation zone to or from which the goods are delivered""")
    HZUOR = Column('HZUOR', String(2), default=None, doc="""Sourced from VBPA-HZUOR // Assignment to Hierarchy""")
    STCEG = Column('STCEG', String(20), default=None, doc="""Sourced from VBPA-STCEG // VAT Registration Number""")
    PARVW_FF = Column('PARVW_FF', Boolean, default=None, doc="""Sourced from VBPA-PARVW_FF // Indicator 'further partners in this function' (VBPA2)""")
    ADRNP = Column('ADRNP', String(10), default=None, doc="""Sourced from VBPA-ADRNP // Person number""")
    KALE = Column('KALE', String(1), default=None, doc="""Sourced from VBPA-KALE // Maintain appointments in calendar""")

    sd_doc_id = synonym('VBELN')
    sd_doc_item_id = synonym('POSNR')
    partner_function_cd = synonym('PARVW')
    customer_id = synonym('KUNNR')
    addr_id = synonym('ADRNR')
    unloading_point = synonym('ABLAD')
    country_cd = synonym('LAND1')
    addr_ind = synonym('ADRDA')
    relevant_for_price_determ_ind = synonym('PRFRE')
    cust_rebate_rlvnt_ind = synonym('BOKRE')
    hierarchy_level_nbr = synonym('HISTUNR')
    transportation_zone_cd = synonym('LZONE')
    hierarchy_assignment_cd = synonym('HZUOR')
    home_addr_id = synonym('ADRNP')


################################################################################




################################################################################

class SD_HdrStatus(SAP_Base):
    """\
    Table sourced from: VBUK
    Description: Sales Document: Header Status and Administrative Data
    """

    __tablename__ = "VBUK"

    VBELN = Column('VBELN', String(10), primary_key = True, doc="""Sourced from VBUK-VBELN // Sales and Distribution Document Number""")
    RFSTK = Column('RFSTK', String(1), default=None, doc="""Sourced from VBUK-RFSTK // Reference document header status""")
    RFGSK = Column('RFGSK', String(1), default=None, doc="""Sourced from VBUK-RFGSK // Total reference status of all items""")
    BESTK = Column('BESTK', String(1), default=None, doc="""Sourced from VBUK-BESTK // Confirmation status""")
    LFSTK = Column('LFSTK', String(1), default=None, doc="""Sourced from VBUK-LFSTK // Delivery status""")
    LFGSK = Column('LFGSK', String(1), default=None, doc="""Sourced from VBUK-LFGSK // Overall delivery status for all items""")
    WBSTK = Column('WBSTK', String(1), default=None, doc="""Sourced from VBUK-WBSTK // Total goods movement status""")
    FKSTK = Column('FKSTK', String(1), default=None, doc="""Sourced from VBUK-FKSTK // Billing status""")
    FKSAK = Column('FKSAK', String(1), default=None, doc="""Sourced from VBUK-FKSAK // Billing status (order-related billing document)""")
    BUCHK = Column('BUCHK', String(1), default=None, doc="""Sourced from VBUK-BUCHK // Posting Status of Billing Document""")
    ABSTK = Column('ABSTK', String(1), default=None, doc="""Sourced from VBUK-ABSTK // Overall rejection status of all document items""")
    GBSTK = Column('GBSTK', String(1), default=None, doc="""Sourced from VBUK-GBSTK // Overall processing status of document""")
    KOSTK = Column('KOSTK', String(1), default=None, doc="""Sourced from VBUK-KOSTK // Overall picking / putaway status""")
    LVSTK = Column('LVSTK', String(1), default=None, doc="""Sourced from VBUK-LVSTK // Overall status of warehouse management activities""")
    UVALS = Column('UVALS', String(1), default=None, doc="""Sourced from VBUK-UVALS // Total incompletion status of all items in general""")
    UVVLS = Column('UVVLS', String(1), default=None, doc="""Sourced from VBUK-UVVLS // Total incompletion status of all items: Delivery""")
    UVFAS = Column('UVFAS', String(1), default=None, doc="""Sourced from VBUK-UVFAS // Total incompletion status of all items: Billing""")
    UVALL = Column('UVALL', String(1), default=None, doc="""Sourced from VBUK-UVALL // General incompletion status of the header""")
    UVVLK = Column('UVVLK', String(1), default=None, doc="""Sourced from VBUK-UVVLK // Header incompletion status concerning delivery""")
    UVFAK = Column('UVFAK', String(1), default=None, doc="""Sourced from VBUK-UVFAK // Header incompletion status with respect to billing""")
    UVPRS = Column('UVPRS', String(1), default=None, doc="""Sourced from VBUK-UVPRS // Document is incomplete with respect to pricing""")
    VBTYP = Column('VBTYP', String(1), default=None, doc="""Sourced from VBUK-VBTYP // SD document category""")
    VBOBJ = Column('VBOBJ', String(1), default=None, doc="""Sourced from VBUK-VBOBJ // SD document object""")
    AEDAT = Column('AEDAT', Date, default=None, doc="""Sourced from VBUK-AEDAT // Changed On""")
    FKIVK = Column('FKIVK', String(1), default=None, doc="""Sourced from VBUK-FKIVK // Billing totals status for intercompany billing""")
    RELIK = Column('RELIK', String(1), default=None, doc="""Sourced from VBUK-RELIK // Invoice list status of billing document""")
    UVK01 = Column('UVK01', String(1), default=None, doc="""Sourced from VBUK-UVK01 // Customer reserves 1: Header status""")
    UVK02 = Column('UVK02', String(1), default=None, doc="""Sourced from VBUK-UVK02 // Customer reserves 2: Header status""")
    UVK03 = Column('UVK03', String(1), default=None, doc="""Sourced from VBUK-UVK03 // Customer reserves 3: Header status""")
    UVK04 = Column('UVK04', String(1), default=None, doc="""Sourced from VBUK-UVK04 // Custmer reserves 4: Header status""")
    UVK05 = Column('UVK05', String(1), default=None, doc="""Sourced from VBUK-UVK05 // Customer reserves 5: Header status""")
    UVS01 = Column('UVS01', String(1), default=None, doc="""Sourced from VBUK-UVS01 // Customer reserves 1: Sum of all items""")
    UVS02 = Column('UVS02', String(1), default=None, doc="""Sourced from VBUK-UVS02 // Customer reserves 2: Sum of all items""")
    UVS03 = Column('UVS03', String(1), default=None, doc="""Sourced from VBUK-UVS03 // Customer reserves 3: Sum of all items""")
    UVS04 = Column('UVS04', String(1), default=None, doc="""Sourced from VBUK-UVS04 // Customer reserves 4: Sum of all items""")
    UVS05 = Column('UVS05', String(1), default=None, doc="""Sourced from VBUK-UVS05 // Customer reserves 5: Sum of all items""")
    PKSTK = Column('PKSTK', String(1), default=None, doc="""Sourced from VBUK-PKSTK // Overall packing status of all items""")
    CMPSA = Column('CMPSA', String(1), default=None, doc="""Sourced from VBUK-CMPSA // Status of static credit limit check""")
    CMPSB = Column('CMPSB', String(1), default=None, doc="""Sourced from VBUK-CMPSB // Status of dynamic credit limit check in the credit horizon""")
    CMPSC = Column('CMPSC', String(1), default=None, doc="""Sourced from VBUK-CMPSC // Status of credit check against maximum document value""")
    CMPSD = Column('CMPSD', String(1), default=None, doc="""Sourced from VBUK-CMPSD // Status of credit check against terms of payment""")
    CMPSE = Column('CMPSE', String(1), default=None, doc="""Sourced from VBUK-CMPSE // Status of credit check against customer review date""")
    CMPSF = Column('CMPSF', String(1), default=None, doc="""Sourced from VBUK-CMPSF // Status of credit check against open items due""")
    CMPSG = Column('CMPSG', String(1), default=None, doc="""Sourced from VBUK-CMPSG // Status of credit check against oldest open items""")
    CMPSH = Column('CMPSH', String(1), default=None, doc="""Sourced from VBUK-CMPSH // Status of credit check against highest dunning level""")
    CMPSI = Column('CMPSI', String(1), default=None, doc="""Sourced from VBUK-CMPSI // Status of credit check against financial document""")
    CMPSJ = Column('CMPSJ', String(1), default=None, doc="""Sourced from VBUK-CMPSJ // Status of credit check against export credit insurance""")
    CMPSK = Column('CMPSK', String(1), default=None, doc="""Sourced from VBUK-CMPSK // Status of credit check against payment card authorization""")
    CMPSL = Column('CMPSL', String(1), default=None, doc="""Sourced from VBUK-CMPSL // Status of credit check of reserves 4""")
    CMPS0 = Column('CMPS0', String(1), default=None, doc="""Sourced from VBUK-CMPS0 // Status of credit check for customer reserve 1""")
    CMPS1 = Column('CMPS1', String(1), default=None, doc="""Sourced from VBUK-CMPS1 // Status of credit check for customer reserve 2""")
    CMPS2 = Column('CMPS2', String(1), default=None, doc="""Sourced from VBUK-CMPS2 // Status of credit check for customer reserve 3""")
    CMGST = Column('CMGST', String(1), default=None, doc="""Sourced from VBUK-CMGST // Overall status of credit checks""")
    TRSTA = Column('TRSTA', String(1), default=None, doc="""Sourced from VBUK-TRSTA // Transportation planning status""")
    KOQUK = Column('KOQUK', String(1), default=None, doc="""Sourced from VBUK-KOQUK // Status of pick confirmation""")
    COSTA = Column('COSTA', String(1), default=None, doc="""Sourced from VBUK-COSTA // Confirmation status for ALE""")
    SAPRL = Column('SAPRL', String(4), default=None, doc="""Sourced from VBUK-SAPRL // SAP Release""")
    UVPAS = Column('UVPAS', String(1), default=None, doc="""Sourced from VBUK-UVPAS // Totals incomplete status for all items: packaging""")
    UVPIS = Column('UVPIS', String(1), default=None, doc="""Sourced from VBUK-UVPIS // Totals incomplete status for all items: Picking""")
    UVWAS = Column('UVWAS', String(1), default=None, doc="""Sourced from VBUK-UVWAS // Total incomplete status of all items: post goods movement""")
    UVPAK = Column('UVPAK', String(1), default=None, doc="""Sourced from VBUK-UVPAK // Header incomplete status for packaging""")
    UVPIK = Column('UVPIK', String(1), default=None, doc="""Sourced from VBUK-UVPIK // Header incomplete status for picking/putaway""")
    UVWAK = Column('UVWAK', String(1), default=None, doc="""Sourced from VBUK-UVWAK // Post header incomplete status for goods movement""")
    UVGEK = Column('UVGEK', String(1), default=None, doc="""Sourced from VBUK-UVGEK // UNUSED""")
    CMPSM = Column('CMPSM', String(1), default=None, doc="""Sourced from VBUK-CMPSM // Credit check data is obsolete""")
    DCSTK = Column('DCSTK', String(1), default=None, doc="""Sourced from VBUK-DCSTK // Delay status""")
    VESTK = Column('VESTK', String(1), default=None, doc="""Sourced from VBUK-VESTK // Handling Unit Placed in Stock""")
    VLSTK = Column('VLSTK', String(1), default=None, doc="""Sourced from VBUK-VLSTK // Distribution Status (Decentralized Warehouse Processing)""")
    RRSTA = Column('RRSTA', String(1), default=None, doc="""Sourced from VBUK-RRSTA // Revenue determination status""")
    BLOCK = Column('BLOCK', String(1), default=None, doc="""Sourced from VBUK-BLOCK // Indicator: Document preselected for archiving""")
    FSSTK = Column('FSSTK', String(1), default=None, doc="""Sourced from VBUK-FSSTK // Overall billing block status""")
    LSSTK = Column('LSSTK', String(1), default=None, doc="""Sourced from VBUK-LSSTK // Overall delivery block status""")
    SPSTG = Column('SPSTG', String(1), default=None, doc="""Sourced from VBUK-SPSTG // Overall blocked status""")
    PDSTK = Column('PDSTK', String(1), default=None, doc="""Sourced from VBUK-PDSTK // POD status on header level""")
    FMSTK = Column('FMSTK', String(1), default=None, doc="""Sourced from VBUK-FMSTK // Status Funds Management""")
    MANEK = Column('MANEK', String(1), default=None, doc="""Sourced from VBUK-MANEK // Manual Completion of Contract""")
    SPE_TMPID = Column('SPE_TMPID', String(1), default=None, doc="""Sourced from VBUK-SPE_TMPID // Temporary inbound delivery""")
    HDALL = Column('HDALL', Boolean, default=None, doc="""Sourced from VBUK-HDALL // Inbound delivery header not yet complete (on Hold)""")
    HDALS = Column('HDALS', Boolean, default=None, doc="""Sourced from VBUK-HDALS // At least one of ID items not yet complete (on Hold)""")
    CMPS_CM = Column('CMPS_CM', String(1), default=None, doc="""Sourced from VBUK-CMPS_CM // Status of Credit Check SAP Credit Management""")
    CMPS_TE = Column('CMPS_TE', String(1), default=None, doc="""Sourced from VBUK-CMPS_TE // Status of Technical Error SAP Credit Management""")
    VBTYP_EXT = Column('VBTYP_EXT', String(4), default=None, doc="""Sourced from VBUK-VBTYP_EXT // Extension of SD Document Category""")

    sd_doc_id = synonym('VBELN')
    total_reference_status_cd = synonym('RFGSK')
    cnfrm_sta_cd = synonym('BESTK')
    total_goods_movement_status_cd = synonym('WBSTK')
    other_billing_status_cd = synonym('FKSTK')
    order_billing_status_cd = synonym('FKSAK')
    bill_doc_posting_status_cd = synonym('BUCHK')
    overall_rej_sta_cd = synonym('ABSTK')
    sd_doc_overall_processing_statys_cd = synonym('GBSTK')
    overall_wm_status_cd = synonym('LVSTK')
    generally_incomplete_ind = synonym('UVALL')
    incomplete_delivery_ind = synonym('UVVLK')
    incomplete_billing_ind = synonym('UVFAK')
    incomplete_pricing_ind = synonym('UVPRS')
    sd_doc_ctgy_cd = synonym('VBTYP')
    sd_doc_object_cd = synonym('VBOBJ')
    update_dt = synonym('AEDAT')
    intercompany_billing_totals_status_cd = synonym('FKIVK')
    overall_item_packing_status_cd = synonym('PKSTK')
    overall_credit_check_status_cd = synonym('CMGST')
    transportation_planning_status_cd = synonym('TRSTA')
    distribution_status_cd = synonym('VLSTK')
    overall_bill_blk_status_cd = synonym('FSSTK')
    overall_blocked_status_cd = synonym('SPSTG')
    credit_mgmt_check_status_cd = synonym('CMPS_CM')


################################################################################




################################################################################

class SD_ItemStatus(SAP_Base):
    """\
    Table sourced from: VBUP
    Description: Sales Document: Item Status
    """

    __tablename__ = "VBUP"

    VBELN = Column('VBELN', String(10), primary_key = True, doc="""Sourced from VBUP-VBELN // Sales and Distribution Document Number""")
    POSNR = Column('POSNR', String(6), primary_key = True, doc="""Sourced from VBUP-POSNR // Item number of the SD document""")
    RFSTA = Column('RFSTA', String(1), default=None, doc="""Sourced from VBUP-RFSTA // Reference status""")
    RFGSA = Column('RFGSA', String(1), default=None, doc="""Sourced from VBUP-RFGSA // Overall status of reference""")
    BESTA = Column('BESTA', String(1), default=None, doc="""Sourced from VBUP-BESTA // Confirmation Status of Document Item""")
    LFSTA = Column('LFSTA', String(1), default=None, doc="""Sourced from VBUP-LFSTA // Delivery status""")
    LFGSA = Column('LFGSA', String(1), default=None, doc="""Sourced from VBUP-LFGSA // Overall delivery status of the item""")
    WBSTA = Column('WBSTA', String(1), default=None, doc="""Sourced from VBUP-WBSTA // Goods movement status""")
    FKSTA = Column('FKSTA', String(1), default=None, doc="""Sourced from VBUP-FKSTA // Billing status of delivery-related billing documents""")
    FKSAA = Column('FKSAA', String(1), default=None, doc="""Sourced from VBUP-FKSAA // Billing Status for Order-Related Billing Documents""")
    ABSTA = Column('ABSTA', String(1), default=None, doc="""Sourced from VBUP-ABSTA // Rejection status for SD item""")
    GBSTA = Column('GBSTA', String(1), default=None, doc="""Sourced from VBUP-GBSTA // Overall processing status of the SD document item""")
    KOSTA = Column('KOSTA', String(1), default=None, doc="""Sourced from VBUP-KOSTA // Picking status/Putaway status""")
    LVSTA = Column('LVSTA', String(1), default=None, doc="""Sourced from VBUP-LVSTA // Status of warehouse management activities""")
    UVALL = Column('UVALL', String(1), default=None, doc="""Sourced from VBUP-UVALL // General Incompletion Status of Item""")
    UVVLK = Column('UVVLK', String(1), default=None, doc="""Sourced from VBUP-UVVLK // Incompletion status of the item with regard to delivery""")
    UVFAK = Column('UVFAK', String(1), default=None, doc="""Sourced from VBUP-UVFAK // Item Incompletion Status with Respect to Billing""")
    UVPRS = Column('UVPRS', String(1), default=None, doc="""Sourced from VBUP-UVPRS // Pricing for item is incomplete""")
    FKIVP = Column('FKIVP', String(1), default=None, doc="""Sourced from VBUP-FKIVP // Intercompany Billing Status""")
    UVP01 = Column('UVP01', String(1), default=None, doc="""Sourced from VBUP-UVP01 // Customer reserves 1: Item status""")
    UVP02 = Column('UVP02', String(1), default=None, doc="""Sourced from VBUP-UVP02 // Customer reserves 2: Item status""")
    UVP03 = Column('UVP03', String(1), default=None, doc="""Sourced from VBUP-UVP03 // Item reserves 3: Item status""")
    UVP04 = Column('UVP04', String(1), default=None, doc="""Sourced from VBUP-UVP04 // Item reserves 4: Item status""")
    UVP05 = Column('UVP05', String(1), default=None, doc="""Sourced from VBUP-UVP05 // Customer reserves 5: Item status""")
    PKSTA = Column('PKSTA', String(1), default=None, doc="""Sourced from VBUP-PKSTA // Packing status of item""")
    KOQUA = Column('KOQUA', String(1), default=None, doc="""Sourced from VBUP-KOQUA // Confirmation status of picking/putaway""")
    COSTA = Column('COSTA', String(1), default=None, doc="""Sourced from VBUP-COSTA // Confirmation status for ALE""")
    CMPPI = Column('CMPPI', String(1), default=None, doc="""Sourced from VBUP-CMPPI // Status of credit check against financial document""")
    CMPPJ = Column('CMPPJ', String(1), default=None, doc="""Sourced from VBUP-CMPPJ // Status of credit check against export credit insurance""")
    UVPIK = Column('UVPIK', String(1), default=None, doc="""Sourced from VBUP-UVPIK // Incomplete status of item for picking/putaway""")
    UVPAK = Column('UVPAK', String(1), default=None, doc="""Sourced from VBUP-UVPAK // Incomplete status of item for packaging""")
    UVWAK = Column('UVWAK', String(1), default=None, doc="""Sourced from VBUP-UVWAK // Incomplete status of item regarding goods issue""")
    DCSTA = Column('DCSTA', String(1), default=None, doc="""Sourced from VBUP-DCSTA // Delay status""")
    RRSTA = Column('RRSTA', String(1), default=None, doc="""Sourced from VBUP-RRSTA // Revenue determination status""")
    VLSTP = Column('VLSTP', String(1), default=None, doc="""Sourced from VBUP-VLSTP // Decentralized whse processing""")
    FSSTA = Column('FSSTA', String(1), default=None, doc="""Sourced from VBUP-FSSTA // Billing block status for items""")
    LSSTA = Column('LSSTA', String(1), default=None, doc="""Sourced from VBUP-LSSTA // Delivery block status for item""")
    PDSTA = Column('PDSTA', String(1), default=None, doc="""Sourced from VBUP-PDSTA // POD status on item level""")
    MANEK = Column('MANEK', String(1), default=None, doc="""Sourced from VBUP-MANEK // Manual Completion of Contract""")
    HDALL = Column('HDALL', Boolean, default=None, doc="""Sourced from VBUP-HDALL // Inbound Delivery Item Not Yet Complete (on Hold)""")
    LTSPS = Column('LTSPS', String(1), default=None, doc="""Sourced from VBUP-LTSPS // Indicator : stockable type switched into standard product""")

    sd_doc_id = synonym('VBELN')
    sd_doc_item_id = synonym('POSNR')
    reference_status_cd = synonym('RFSTA')
    overall_reference_status_cd = synonym('RFGSA')
    itm_cnfrm_sta_cd = synonym('BESTA')
    delivery_status_cd = synonym('LFSTA')
    overall_item_delivery_status_cd = synonym('LFGSA')
    goods_movement_status_cd = synonym('WBSTA')
    deliv_billing_status_cd = synonym('FKSTA')
    billing_status_cd = synonym('FKSAA')
    sd_item_overall_processing_status_cd = synonym('GBSTA')
    wm_status_cd = synonym('LVSTA')
    generally_incomplete_ind = synonym('UVALL')
    incomplete_delivery_ind = synonym('UVVLK')
    incomplete_billing_ind = synonym('UVFAK')
    incomplete_pricing_ind = synonym('UVPRS')
    intercompany_billing_status_cd = synonym('FKIVP')
    item_packing_status_cd = synonym('PKSTA')
    delay_status_cd = synonym('DCSTA')
    bill_blk_status_cd = synonym('FSSTA')
    item_delivery_block_status_cd = synonym('LSSTA')


################################################################################




################################################################################

class SD_Incompletion(SAP_Base):
    """\
    Table sourced from: VBUV
    Description: Sales Document: Incompletion Log
    """

    __tablename__ = "VBUV"

    VBELN = Column('VBELN', String(10), primary_key = True, doc="""Sourced from VBUV-VBELN // Sales and Distribution Document Number""")
    POSNR = Column('POSNR', String(6), primary_key = True, doc="""Sourced from VBUV-POSNR // Item number of the SD document""")
    ETENR = Column('ETENR', String(4), primary_key = True, doc="""Sourced from VBUV-ETENR // Delivery Schedule Line Number""")
    PARVW = Column('PARVW', String(2), primary_key = True, doc="""Sourced from VBUV-PARVW // Partner Function""")
    TDID = Column('TDID', String(4), primary_key = True, doc="""Sourced from VBUV-TDID // Text ID""")
    TBNAM = Column('TBNAM', String(30), primary_key = True, doc="""Sourced from VBUV-TBNAM // Table for documents in sales and distribution""")
    FDNAM = Column('FDNAM', String(30), primary_key = True, doc="""Sourced from VBUV-FDNAM // Document field name""")
    FEHGR = Column('FEHGR', String(2), default=None, doc="""Sourced from VBUV-FEHGR // Incompletion procedure for sales document""")
    STATG = Column('STATG', String(2), default=None, doc="""Sourced from VBUV-STATG // Status group""")

    sd_doc_id = synonym('VBELN')
    sd_doc_item_id = synonym('POSNR')
    deliv_schd_ln_id = synonym('ETENR')
    partner_function_cd = synonym('PARVW')
    table_name = synonym('TBNAM')
    db_field_name = synonym('FDNAM')
    sd_doc_incomplete_proc_cd = synonym('FEHGR')


################################################################################




################################################################################

class IndexDeliveryDue(SAP_Base):
    """\
    Table sourced from: VEPVG
    Description: Delivery Due Index
    """

    __tablename__ = "VEPVG"

    VSTEL = Column('VSTEL', String(4), primary_key = True, doc="""Sourced from VEPVG-VSTEL // Shipping Point/Receiving Point""")
    LEDAT = Column('LEDAT', Date, primary_key = True, doc="""Sourced from VEPVG-LEDAT // Delivery Creation Date""")
    LPRIO = Column('LPRIO', String(2), primary_key = True, doc="""Sourced from VEPVG-LPRIO // Delivery Priority""")
    ROUTE = Column('ROUTE', String(6), primary_key = True, doc="""Sourced from VEPVG-ROUTE // Route""")
    SPDNR = Column('SPDNR', String(10), primary_key = True, doc="""Sourced from VEPVG-SPDNR // Forwarding agent""")
    WADAT = Column('WADAT', Date, primary_key = True, doc="""Sourced from VEPVG-WADAT // Goods Issue Date""")
    KUNWE = Column('KUNWE', String(10), primary_key = True, doc="""Sourced from VEPVG-KUNWE // Ship-to party""")
    VBELN = Column('VBELN', String(10), primary_key = True, doc="""Sourced from VEPVG-VBELN // Sales and Distribution Document Number""")
    LIFSP = Column('LIFSP', String(2), primary_key = True, doc="""Sourced from VEPVG-LIFSP // Delivery block for header or schedule line""")
    KUNNR = Column('KUNNR', String(10), default=None, doc="""Sourced from VEPVG-KUNNR // Sold-to party""")
    VKORG = Column('VKORG', String(4), default=None, doc="""Sourced from VEPVG-VKORG // Sales Organization""")
    VTWEG = Column('VTWEG', String(2), default=None, doc="""Sourced from VEPVG-VTWEG // Distribution Channel""")
    SPART = Column('SPART', String(2), default=None, doc="""Sourced from VEPVG-SPART // Division""")
    VKBUR = Column('VKBUR', String(4), default=None, doc="""Sourced from VEPVG-VKBUR // Sales Office""")
    VKGRP = Column('VKGRP', String(3), default=None, doc="""Sourced from VEPVG-VKGRP // Sales Group""")
    AUTLF = Column('AUTLF', Boolean, default=None, doc="""Sourced from VEPVG-AUTLF // Complete delivery defined for each sales order?""")
    BRGEW = Column('BRGEW', Numeric(15,3,3), default=None, doc="""Sourced from VEPVG-BRGEW // Open gross weight of all schedule lines for this key""")
    GEWEI = Column('GEWEI', String(3), default=None, doc="""Sourced from VEPVG-GEWEI // Weight Unit""")
    VOLUM = Column('VOLUM', Numeric(15,3,3), default=None, doc="""Sourced from VEPVG-VOLUM // Open volume of all schedule lines for this key""")
    VOLEH = Column('VOLEH', String(3), default=None, doc="""Sourced from VEPVG-VOLEH // Volume unit""")
    BEARZ = Column('BEARZ', Numeric(15,3,3), default=None, doc="""Sourced from VEPVG-BEARZ // Processing time in days""")
    ADRNR_AG = Column('ADRNR_AG', String(10), default=None, doc="""Sourced from VEPVG-ADRNR_AG // Address number of the sold-to party""")
    ADRNR_WE = Column('ADRNR_WE', String(10), default=None, doc="""Sourced from VEPVG-ADRNR_WE // Address number of the ship-to party""")
    AUART = Column('AUART', String(4), default=None, doc="""Sourced from VEPVG-AUART // Sales Document Type""")
    KZAZU = Column('KZAZU', Boolean, default=None, doc="""Sourced from VEPVG-KZAZU // Inverse Cumulated Indicator: Order Combination""")

    shipping_receiving_point_cd = synonym('VSTEL')
    delivery_note_create_dt = synonym('LEDAT')
    delivery_priority_cd = synonym('LPRIO')
    route_id = synonym('ROUTE')
    goods_issue_dt = synonym('WADAT')
    ship_to_customer_id = synonym('KUNWE')
    sd_doc_id = synonym('VBELN')
    default_delivery_blk_cd = synonym('LIFSP')
    customer_id = synonym('KUNNR')
    sales_org_cd = synonym('VKORG')
    distr_chan_cd = synonym('VTWEG')
    div_cd = synonym('SPART')
    sales_office_id = synonym('VKBUR')
    sales_group_id = synonym('VKGRP')
    gross_wt = synonym('BRGEW')
    weight_uom_cd = synonym('GEWEI')
    vol = synonym('VOLUM')
    volume_uom_cd = synonym('VOLEH')
    processing_tm = synonym('BEARZ')
    sold_to_addr_id = synonym('ADRNR_AG')
    ship_to_addr_id = synonym('ADRNR_WE')
    sd_hdr_type_cd = synonym('AUART')


################################################################################




################################################################################

class IndexDeliveryDueSTO(SAP_Base):
    """\
    Table sourced from: VETVG
    Description: Delivery Due Index for Stock Transfer
    """

    __tablename__ = "VETVG"

    VSTEL = Column('VSTEL', String(4), primary_key = True, doc="""Sourced from VETVG-VSTEL // Shipping Point/Receiving Point""")
    LEDAT = Column('LEDAT', Date, primary_key = True, doc="""Sourced from VETVG-LEDAT // Delivery Creation Date""")
    LPRIO = Column('LPRIO', String(2), primary_key = True, doc="""Sourced from VETVG-LPRIO // Delivery Priority""")
    ROUTE = Column('ROUTE', String(6), primary_key = True, doc="""Sourced from VETVG-ROUTE // Route""")
    SPDNR = Column('SPDNR', String(10), primary_key = True, doc="""Sourced from VETVG-SPDNR // Forwarding agent""")
    WADAT = Column('WADAT', Date, primary_key = True, doc="""Sourced from VETVG-WADAT // Goods Issue Date""")
    KUNWE = Column('KUNWE', String(10), primary_key = True, doc="""Sourced from VETVG-KUNWE // Ship-to party""")
    VBELN = Column('VBELN', String(10), primary_key = True, doc="""Sourced from VETVG-VBELN // Purchasing Document Number""")
    KUNNR = Column('KUNNR', String(10), default=None, doc="""Sourced from VETVG-KUNNR // Sold-to party""")
    VKORG = Column('VKORG', String(4), default=None, doc="""Sourced from VETVG-VKORG // Sales Organization""")
    VTWEG = Column('VTWEG', String(2), default=None, doc="""Sourced from VETVG-VTWEG // Distribution Channel""")
    SPART = Column('SPART', String(2), default=None, doc="""Sourced from VETVG-SPART // Division""")
    VKBUR = Column('VKBUR', String(4), default=None, doc="""Sourced from VETVG-VKBUR // Sales Office""")
    VKGRP = Column('VKGRP', String(3), default=None, doc="""Sourced from VETVG-VKGRP // Sales Group""")
    AUTLF = Column('AUTLF', Boolean, default=None, doc="""Sourced from VETVG-AUTLF // Complete delivery defined for each sales order?""")
    BRGEW = Column('BRGEW', Numeric(15,3,3), default=None, doc="""Sourced from VETVG-BRGEW // Open gross weight of all schedule lines for this key""")
    GEWEI = Column('GEWEI', String(3), default=None, doc="""Sourced from VETVG-GEWEI // Weight Unit""")
    VOLUM = Column('VOLUM', Numeric(15,3,3), default=None, doc="""Sourced from VETVG-VOLUM // Open volume of all schedule lines for this key""")
    VOLEH = Column('VOLEH', String(3), default=None, doc="""Sourced from VETVG-VOLEH // Volume unit""")
    BEARZ = Column('BEARZ', Numeric(15,3,3), default=None, doc="""Sourced from VETVG-BEARZ // Processing time in days""")
    ADRNR_AG = Column('ADRNR_AG', String(10), default=None, doc="""Sourced from VETVG-ADRNR_AG // Address number of the sold-to party""")
    ADRNR_WE = Column('ADRNR_WE', String(10), default=None, doc="""Sourced from VETVG-ADRNR_WE // Address number of the ship-to party""")
    AUART = Column('AUART', String(4), default=None, doc="""Sourced from VETVG-AUART // Order Type (Purchasing)""")
    RESWK = Column('RESWK', String(4), default=None, doc="""Sourced from VETVG-RESWK // Supplying (Issuing) Plant in Stock Transport Order""")

    shipping_receiving_point_cd = synonym('VSTEL')
    delivery_note_create_dt = synonym('LEDAT')
    delivery_priority_cd = synonym('LPRIO')
    route_id = synonym('ROUTE')
    goods_issue_dt = synonym('WADAT')
    ship_to_customer_id = synonym('KUNWE')
    sd_doc_id = synonym('VBELN')
    customer_id = synonym('KUNNR')
    sales_org_cd = synonym('VKORG')
    distr_chan_cd = synonym('VTWEG')
    div_cd = synonym('SPART')
    sales_office_id = synonym('VKBUR')
    sales_group_id = synonym('VKGRP')
    gross_wt = synonym('BRGEW')
    weight_uom_cd = synonym('GEWEI')
    vol = synonym('VOLUM')
    volume_uom_cd = synonym('VOLEH')
    processing_tm = synonym('BEARZ')
    sold_to_addr_id = synonym('ADRNR_AG')
    ship_to_addr_id = synonym('ADRNR_WE')
    sd_hdr_type_cd = synonym('AUART')
    sto_source_facility_id = synonym('RESWK')


################################################################################




################################################################################

class SchedAgrCustMatl(SAP_Base):
    """\
    Table sourced from: VLPKM
    Description: Scheduling agreements by customer material
    """

    __tablename__ = "VLPKM"

    KDMAT = Column('KDMAT', String(35), primary_key = True, doc="""Sourced from VLPKM-KDMAT // Material belonging to the customer""")
    KUNNR = Column('KUNNR', String(10), primary_key = True, doc="""Sourced from VLPKM-KUNNR // Sold-to party""")
    KNREF = Column('KNREF', String(30), primary_key = True, doc="""Sourced from VLPKM-KNREF // Customer description of partner (plant, storage location)""")
    ABLAD = Column('ABLAD', String(25), primary_key = True, doc="""Sourced from VLPKM-ABLAD // Unloading Point""")
    ABRVW = Column('ABRVW', String(3), primary_key = True, doc="""Sourced from VLPKM-ABRVW // Usage Indicator""")
    VKORG = Column('VKORG', String(4), primary_key = True, doc="""Sourced from VLPKM-VKORG // Sales Organization""")
    VTWEG = Column('VTWEG', String(2), primary_key = True, doc="""Sourced from VLPKM-VTWEG // Distribution Channel""")
    SPART = Column('SPART', String(2), primary_key = True, doc="""Sourced from VLPKM-SPART // Division""")
    AUART = Column('AUART', String(4), primary_key = True, doc="""Sourced from VLPKM-AUART // Sales Document Type""")
    VBELN = Column('VBELN', String(10), primary_key = True, doc="""Sourced from VLPKM-VBELN // Sales and Distribution Document Number""")
    POSNR = Column('POSNR', String(6), primary_key = True, doc="""Sourced from VLPKM-POSNR // Item number of the SD document""")
    ABGRU = Column('ABGRU', String(2), default=None, doc="""Sourced from VLPKM-ABGRU // Reason for rejection of quotations and sales orders""")
    KTEXT = Column('KTEXT', String(40), default=None, doc="""Sourced from VLPKM-KTEXT // Search term for product proposal""")

    customer_id = synonym('KUNNR')
    unloading_point = synonym('ABLAD')
    sales_org_cd = synonym('VKORG')
    distr_chan_cd = synonym('VTWEG')
    div_cd = synonym('SPART')
    sd_hdr_type_cd = synonym('AUART')
    sd_doc_id = synonym('VBELN')
    sd_doc_item_id = synonym('POSNR')
    rej_reas_id = synonym('ABGRU')


################################################################################




if __name__ == '__main__':
    engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/central', echo=True)

#    SAP_Base.metadata.drop_all(engine)
    SAP_Base.metadata.create_all(engine)


