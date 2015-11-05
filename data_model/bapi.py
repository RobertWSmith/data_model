# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:14:09 2015

@author: Robert Smith
"""

from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, Numeric, Text, Time, Float, ForeignKey
from sqlalchemy.orm import relationship, synonym
#from .custom_type import CoerceDate, CoerceTime, CoerceBoolean, CoerceNumeric, CoerceInteger



class _SchemaBase(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    @declared_attr
    def __table_args__(cls):
        return {'schema': 'bapi'}

    id = Column(Integer, primary_key=True, autoincrement=True)


BAPI_Base = declarative_base(name="BAPI_Base", cls=_SchemaBase)



