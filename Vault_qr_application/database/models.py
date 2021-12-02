""" Creates SQLalchemy db models. Run this file without launching the application """

from sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime, Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from connect import Base

Base = declarative_base()


class Identifiers(Base):
    """ Table of all the identifiers/components of the NFTs """
    __tablename__ = 'identifiers'
    company_name = Column(String(100), primary_key=True)
    model_no = Column(String(100), primary_key=True)
    serial_no = Column(String(100), primary_key=True)
    nft_info = Column(Integer, ForeignKey('nft.id'))
    

class Company(Base):
    """ Table of all companies and their models thatwe're servicing. """
    __tablename__ = 'company'
    company_name = Column(String(100), primary_key=True)
    start_of_service = Column(DateTime)
    end_of_service = Column(DateTime, nullable=True)


class Model(Base):
    """ Table of different products that we're servicing. """
    __tablename__ = 'model'
    company_name = Column(String(100), primary_key=True)
    model_no = Column(String(100), primary_key=True)
    product_name = Column(String(100))
    url = Column(String(200))


class NFT(Base):
    """ Other info associated with the NFT. Client cookie for retrieving the NFT. Date minted. 
    If the NFT is active (ie. true if tradable, false if it has been burned) """
    __tablename__ = 'nft'
    id = Column(Integer, primary_key=True, autoincrement=True)
    client_cookie = Column(String(100))
    trx_hash = Column(String(200))
    date_time = Column(DateTime)
    is_active = Column(Boolean)


def migrate():
    """ Creates the database """
    from connect import db_string
    db = create_engine(db_string)

    Session = sessionmaker(db)  
    session = Session()
    Base.metadata.create_all(db)


if __name__ == "__main__":
    migrate()
    
    # remove backpopulate and make creation of records independent/consistent
    # finish crud methods
    # register db on application
    # fix templates