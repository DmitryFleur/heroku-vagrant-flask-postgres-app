import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL',
                                                       'postgresql://vagrant:vagrant@127.0.0.1/vagrant')
app.config['SQLALCHEMY_MIGRATE_REPO'] = os.path.join(basedir, 'migrations')
db = SQLAlchemy(app)


from apps.account import models


@app.route('/')
def hello():
    return 'Hello World!'
