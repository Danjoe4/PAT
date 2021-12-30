""" contains CRUD (create, read, update, delete) functions for the database
"""
from sqlalchemy import Table
from connect import db_session
from models import Identifiers, Company, Model, NFT


####################### create ####################################
def add_new_nft_record(company_name, model_no, serial_no, 
date_time, is_active, trx_hash=None,  client_cookie='None'):
    """ Add a new nft record to the database. Loose_add is for testing purposes. 
    Normally all our companies and models should be created beforehand. 
    """
    nft = NFT(client_cookie = client_cookie, trx_hash = trx_hash, 
    date_time = date_time, is_active = is_active)
    db_session.add(nft)
    identifiers = Identifiers(company_name=company_name, model_no=model_no, 
    serial_no=serial_no, nft_info=nft.id)
    db_session.add(identifiers)
    
    db_session.commit()
    return nft, db_session

def add_model_info(company, model_no, product_name, url):
    """ Adds/updates info for a model/product
    """
    exists = db_session.query(Model).filter_by(company_name=company, model_no=model_no).first()
    if exists:
        exists.product_name = product_name
        exists.url = url
        exists.commit()
    else:
        new_entry = Model(company_name=company, model_no=model_no, product_name=product_name, url=url)
        db_session.add(new_entry)
        db_session.commit()
    



def retrieve_all_model_info(company, model_no):
    """ Retrieves company name, model number, product name, and url
    """
    model = db_session.query(Model).filter_by(company=company, model_no=model_no).first()
    return model

def retrive_model_name(company, model_no):
    """ retrieve the product name for a specific model
    """
    model = retrieve_all_model_info(company, model_no)
    return model.product_name

def retrieve_model_url(company, model_no):
    """ Retrieve the url the product is sold at
    """
    model = retrieve_all_model_info(company, model_no)
    return model.product_name


def get_results(result_type=None, search_string=None):
    if search_string == "":
        search_string = None

    if result_type == None:
        if search_string == None:
            out = db_session.query(Identifiers).all()
            return out
        else:
            out = db_session.query(Identifiers).filter_by(company_name=search_string).all()
            if out == []:
                out = db_session.query(Identifiers).filter_by(model_no=search_string).all()
            if out == []:
                out = db_session.query(Identifiers).all()
            return out
        



if __name__ == "__main__":
    #add_new_company("Bose")
    import random
    for repeat in range(3):
        for company in ["Facebook", "Apple", "Amazon", "Netflix", "Google"]:
            add_new_nft_record(company, 
            random.choice(["Earbuds", "Brain Chip", "Something-Verse", "243422"]), 
            random.choice(["XSCNS32423598", "NoTaReAlsErIaL#", "DASASD325433","SOMESERIAL123"]), 
            "2020-01-01", False)
    #add_model_info(f"Testcompany{i}", f"testmodel{i}", f"mymodelname{i}", "someurl{i}")
