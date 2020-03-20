#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import settings

Base = declarative_base()

DB_USER = settings.DB_USER
DB_PASSWORD = settings.DB_PASSWORD
DB_HOST = settings.DB_HOST
DB_NAME = settings.DB_NAME

DB_URL = "mysql://{0}:{1}@{2}:3306".format(DB_USER, DB_PASSWORD, DB_HOST)

ECHO_LOG = True
engine = create_engine(
  DB_URL, echo=ECHO_LOG
)

existing_databases = engine.execute("SHOW DATABASES;")
existing_databases = [d[0] for d in existing_databases]

if DB_NAME not in existing_databases:
    engine.execute("CREATE DATABASE {0} DEFAULT CHARACTER SET 'utf8' ".format(DB_NAME))

DB_URL = "mysql://{0}:{1}@{2}:3306/{3}?charset=utf8mb4&use_unicode=1".format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

engine = create_engine(
    DB_URL, echo=ECHO_LOG, convert_unicode=True
)

Session = sessionmaker(bind=engine)
session = Session()
