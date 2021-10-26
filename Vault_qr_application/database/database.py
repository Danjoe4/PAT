import psycopg2
from flask_sqlalchemy import SQLAlchemy





class DatabaseMethods:
    def __init__(self):
        # probably have something like self.db_location = file.db
        self.db = sqlite3.connect(self.db_location)
    

    def _exists(self) -> bool:
        """ 
        """


    def retrieve_trxn_addr(self):
        """ Search the database and return the tranaction address
        """
        pass


    def add_new_nft_record(self):
        pass



if __name__ == "__main__":
# you can use past queries from dup_checker.csv for testing
    pass