# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 18:50:51 2015

@author: Robert Smith
"""

from setuptools import setup, find_packages

setup(
    name="data_model",
    version = "0.0.1",
    packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests", "*.egg-info"]),
    author = "Robert Smith",
    author_email = "rob_smith@goodyear.com",
    description = "common sqlalchemy data model",
    install_requires = ['sqlalchemy', 'psycopg2', 'pyodbc'],
    test_suite = 'tests'
)


