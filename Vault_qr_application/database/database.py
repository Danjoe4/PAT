<<<<<<< HEAD
import psycopg2
from flask_sqlalchemy import SQLAlchemy


=======
>>>>>>> 4d6ca8bf2da8fcb960669527cae9eb79898037e1



class DatabaseMethods:
    def __init__(self):
<<<<<<< HEAD
        # probably have something like self.db_location = file.db
        self.db = sqlite3.connect(self.db_location)
=======
        # probably have something like self.db_location = file.db 
        pass
>>>>>>> 4d6ca8bf2da8fcb960669527cae9eb79898037e1
    

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