###################### OVERVIEW ###############################
Takes the QR code with encoded parameters brand, product, model, and serial
user waits on a nifty loading screen while it creates the contract.

Manual queries no longer work, you need to use the QR gen to get the encoded query.
Although you can use https://zxing.org/w/decode.jspx to get the raw QR text


#################### USAGE NOTES AND CONSTRAINTS ####################################
-Hosted at http://www.vaultqr.com

-Must generate the QR at http://www.vaultqrgen.com
##################### 
REFACTOR NOTES
The dup_checker.csv and relevant methods, mostly found in scan/views are to be deprecated once
we get the database online.
Fix the globals at some point