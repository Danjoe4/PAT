""" Utilizes models.py. Establishes a connection to the database.
"""
from sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime, Boolean, Float, engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

### messy config, will refactor into config.py #####
import yaml 
with open("config.yaml") as f_stream:
    config_file = yaml.load(f_stream, yaml.FullLoader)
PSQL_DB = config_file['postgres_db_name']
PSQL_USER = config_file["postgres_user_name"]
PSQL_PASSWORD = config_file["postgres_user_password"]
db_string = f"postgresql://localhost/{PSQL_DB}?user={PSQL_USER}&password={PSQL_PASSWORD}"
###############################

## other connection stuff, ideally we define this within a specific context in the future
engine = create_engine(db_string)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    """define our models"""
    from .models import User, NFT, Transaction, NFT_Transaction
    Base.metadata.create_all(bind=engine)




if __name__ == "__main__":
# test connection
    init_db()