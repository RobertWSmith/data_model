# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 18:50:51 2015

@author: Robert Smith
"""

from setuptools import setup, find_packages

setup(
    name="data_model",
    version = "0.0.3",
    packages = find_packages(exclude=["alembic", "build", "config", "*.tests", "*.tests.*", "tests.*", "tests", "*.egg-info", "*__pycache__", "dist", "alembic.ini", "generate_sap_model.py"]),
    author = "Robert Smith",
    author_email = "rob_smith@goodyear.com",
    description = "common sqlalchemy data model",
    install_requires = ['sqlalchemy >= 1.0.9', 'psycopg2', 'pyodbc', 'architect', 'pyyaml >= 3.11'],
    test_suite = 'tests'
)

