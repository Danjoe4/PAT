from base64 import urlsafe_b64decode
import binascii
import yaml

# encryption
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64 


class Decrypt:
    def __init__(self) -> None:
        pass


    def set_default_salt_and_password(self) -> None:
        with open("config.yaml") as f_stream:
            config_file = yaml.load(f_stream, yaml.FullLoader)

        self.salt = bytes(config_file["encryption_salt_1"], encoding='utf8')
        self.password = bytes(config_file["encryption_password_1"], encoding='utf8')


    def _derive_encryption_key(self):
        """ Helper to decrypt. Uses our salt and password to derive the key
        """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=10000)
        key = base64.urlsafe_b64encode(kdf.derive(self.password))
        return key


    def decrypt(self, encrypted_str) -> list:
        """ Helper function to init. Takes the encrypted string and 
        sets the brand, product, model, serial appropriately.
        """
        ENCRYPTION_KEY_1 = self._derive_encryption_key()
        f = Fernet(ENCRYPTION_KEY_1)
        string_params = f.decrypt(encrypted_str.encode("utf-8"))
        print("decrypted bytes: ")
        print(string_params)
        list_params = list(string_params.decode("utf-8").split(','))
        print(list_params)
        return list_params



class DatabaseMethods:
    def __init__(self):
        # probably have something like self.db_location = file.db 
        pass
    

    def _exists(self) -> bool:
        """ 
        """


    def retrieve_trxn_addr(self):
        """ Search the database and return the tranaction address
        """
        pass


    def add_new_nft_record(self):
        pass




class Query(Decrypt, DatabaseMethods):
    """ An instance of the user query. 
    """
    def __init__(self, encrypted_str):
        self.encrypted_string = encrypted_str
        self.set_default_salt_and_password 
        self.brand, self.product, self.model, self.serial = self.decrypt(encrypted_str)
        self.is_duplicate = None 


    def is_duplicate(self):
        """ Has this code been scanned before
        """
        if self.is_duplicate is None:
            self.is_duplicate = self._exists()
        return self.is_duplicate


    def print_query(self):
        print("The values in this query are as follows:")
        print("brand: " + self.brand)
        print("product: " + self.product)
        print("model: " + self.model)
        print("serial: " + self.serial)
        print("duplicate (T or F): " + self.is_duplicate)
        
            



if __name__ == "__main__":
    # you can use past queries from dup_checker.csv for testing, please add comments if 
    # you change the Query or DatabaseMethods classes