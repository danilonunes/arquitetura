from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

_basedir = os.path.abspath(os.path.dirname(__file__))

engine = create_engine('sqlite:///' + os.path.join(_basedir, '3camadas.db'),
                        echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()
