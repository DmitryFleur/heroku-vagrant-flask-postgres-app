#!/usr/bin/env python

import os.path
import sys

cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.abspath(cwd + '/../'))

from migrate.versioning import api

from app import app


v = api.db_version(app.config['SQLALCHEMY_DATABASE_URI'],
                   app.config['SQLALCHEMY_MIGRATE_REPO'])
api.downgrade(app.config['SQLALCHEMY_DATABASE_URI'],
              app.config['SQLALCHEMY_MIGRATE_REPO'], v - 1)
print 'Current database version: ' + str(api.db_version(app.config['SQLALCHEMY_DATABASE_URI'],
                                         app.config['SQLALCHEMY_MIGRATE_REPO']))
