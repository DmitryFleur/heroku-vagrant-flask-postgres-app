#!/usr/bin/python

import os.path
import sys

cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.abspath(cwd + '/../'))

from migrate.versioning import api
from migrate.exceptions import DatabaseAlreadyControlledError

from app import app, db

db.create_all()
try:
    if not os.path.exists(app.config['SQLALCHEMY_MIGRATE_REPO']):
        api.create(app.config['SQLALCHEMY_MIGRATE_REPO'], 'database repository')
        api.version_control(app.config['SQLALCHEMY_DATABASE_URI'],
                            app.config['SQLALCHEMY_MIGRATE_REPO'])
    else:
        api.version_control(app.config['SQLALCHEMY_DATABASE_URI'],
                            app.config['SQLALCHEMY_MIGRATE_REPO'],
                            api.version(app.config['SQLALCHEMY_MIGRATE_REPO']))
except DatabaseAlreadyControlledError:
    pass
