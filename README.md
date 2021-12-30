###################### OVERVIEW ###############################
Takes the QR code with encoded parameters brand, product, model, and serial
user waits on a nifty loading screen while it creates the contract.

Manual queries no longer work, you need to use the QR gen to get the encoded query.
Although you can use https://zxing.org/w/decode.jspx to get the raw QR text


#################### USAGE NOTES ####################################
-Hosted at http://www.vaultqr.com

-Must generate the QR at http://www.vaultqrgen.com
##################### 
To do NOTES
fix config (load from env), factor out of smaller files
fix the database folder 
create admin section and auth
consider adding flask-admin
Fix the globals at some point (use flask_g)
