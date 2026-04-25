#
# Author: Rohtash Lakra
#
from flask_sqlalchemy import SQLAlchemy

from framework.db.connector import SQLite3Connector

db = SQLAlchemy()
connector = SQLite3Connector()
