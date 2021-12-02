############# SETUP NOTES FOR PROFESSOR STORY #####
## Deployed on Ubuntu 20.04.2 LTS and with python 3.8.10
pip3 install -r requirements.txt
# start the local db testing and open a postgres terminal
sudo service postgresql start
sudo -u postgres psql
# Initialize the database and your user
# you can change the user/pass but you'll also have to change it in config.yaml
CREATE DATABASE testing;
CREATE USER story WITH ENCRYPTED PASSWORD 'nopass'; 
GRANT ALL PRIVILEGES ON DATABASE testing TO story;
Run the models.py file to run the migrations
# The database should be all set up, launch the application
python3 wsgi.py

############## USAGE NOTES and FAQ FOR PROFESSOR STORY #######################
## This is a big app, what should I be looking at?
The database folder is the most relevant. It contains our templates, logic, models, and
CRUD methods. Scan/mint.py calls database/CRUD.py to save freshly minted nfts

## How does it CRUD?
####C: The main feature of the app is creating NFTs by scanning QR codes. Normally,
you would use our generator (here: http://www.vaultqrgen.com) to make the QR
codes but since you're running the application locally the URL encoded in the QR
will not be correct. You could extract and modify the url to use with the localhost domain, but
it is less reliable. Here is a sample url:
http://www.vaultqr.com/scan?v=gAAAAABhqGdk07X6tQPY0TTOsQ2GS6txvjNme56lFQkz8RIA_KUjOvY_dgkkqzuW5A1o9KCeIW5Chtbb03Gu25-h06V8aNWPY_j0piWrOWR5NVcpFoXFuL5TxAq5WDuxB3aEg6dCAd2o

\
The easiest way to quickly add many entries is to run CRUD.py

####R: Reading occurs extensively when you view the NFT entries. Some database entries (like the info we
have on a certain company), are not displayed because it isnt relevant to the user. We would use this info
for internal purposes.

####U: The application updates the is_active NFT column. It adds the NFT to the database and sets
is_active=False. When the NFT is done being minted (which takes around 30-45sec), it sets
is_active=True and also sets the transaction hash. This is technically useful because if the NFT minting failed, is_active would remain False. 

####D: We want these NFTs to be permanent records, deleting entries doesn't really make sense.


###  Why does it look weird/inconsistent? ###
I spent a lot of time iinitially making it look nice and gave up. CSS is no fun

###     Why is this taking so long to install? Why are there dependency issues?  ###
Shoot me an email if there are issues. I have tested setup from start to finish on the clark library computers so it should work. The imports were giving me recurring issues though so if the 
application paths differently then I'd adjust those.





###################### OVERVIEW ###############################
Takes the QR code with encoded parameters brand, product, model, and serial
user waits on a nifty loading screen while it creates the contract.

Manual queries no longer work, you need to use the QR gen to get the encoded query.
Although you can use https://zxing.org/w/decode.jspx to get the raw QR text


#################### USAGE NOTES ####################################
-Hosted at http://www.vaultqr.com

-Must generate the QR at http://www.vaultqrgen.com
##################### 
REFACTOR NOTES
Fix the globals at some point (use flask_g)
