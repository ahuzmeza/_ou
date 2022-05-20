from flask_sqlalchemy import SQLAlchemy, sessionmaker, create_engine, Session
from flask_sqlalchemy import declarative_base
from . import db

con_username = 'guest'
con_password = 'password'
con_host = 'localhost'
con_db_name = '_ou_db'
# -------------------------------------------------
con_db = f'mysql+pymysql://{con_username}:{con_password}@{con_host}/{con_db_name}'.format()
engine = create_engine(con_db, echo=True)
session = sessionmaker(bind=engine)()
session = Session()
base = declarative_base()
base.metadata.create_all(engine)
   
