import base64 
import yaml

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Query:
    """ Takes the encrypted url string to create an instance of the user query. 
    """
    def __init__(self, encrypted_str):
        self.encrypted_str = encrypted_str
        self.set_default_salt_and_password()
        self.brand, self.product, self.model, self.serial = self.decrypt(encrypted_str)

    def __str__(self):
        return f"""The values in this query are as follows: \n
        Encrypted string: {self.encrypted_str} \n
        brand: {self.brand} \n
        product: {self.product} \n 
        model: {self.model} \n
        serial: {self.serial} """

    def set_default_salt_and_password(self) -> None:
        with open("config.yaml") as f_stream:
            config_file = yaml.load(f_stream, yaml.FullLoader)

        self.salt = bytes(config_file["encryption_salt_1"], encoding='utf8')
        self.password = bytes(config_file["encryption_password_1"], encoding='utf8')

    def decrypt(self, encrypted_str) -> list:
        """ Takes the encrypted string and 
        sets the brand, product, model, serial appropriately.
        """
        ENCRYPTION_KEY_1 = self._derive_encryption_key()
        f = Fernet(ENCRYPTION_KEY_1)
        string_params = f.decrypt(encrypted_str.encode("utf-8"))
        list_params = list(string_params.decode("utf-8").split(','))
        return list_params

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