import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

_basedir = os.path.abspath(os.path.dirname(__file__))

engine = create_engine('sqlite:///' + os.path.join(_basedir, '3camadas.db'),
                        echo=False)

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()
