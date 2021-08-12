###################### OVERVIEW ###############################
Takes the QR code with encoded parameters brand, product, model, and serial
user waits on a nifty loading screen while it creates the contract.

Manual queries no longer work, you need to use the QR gen to get the encoded query.
Although you can use https://zxing.org/w/decode.jspx to get the raw QR text

######################## DEVELOPMENT TIMELINE #################################
V0_4_9_5 (current) : Adding loading screen for the duplicates, refactored some code, added 
error handling if the URL is modified

V0_5 Play with the gas price one last time to see if we can achieve faster contract generation. 

V0_5_5... final testing and bug fixes

V0_6 The version that will be used at the demo. 


Post demo?
-Add email landing page
-Refine the scilla contract to prevent duplicates from being made
-maybe add a "resale" option such that users can transfer the nft
-"Crawl" the blockchain looking for duplicates "properly"

#################### USAGE NOTES AND CONSTRAINTS ####################################
-Hosted at http://www.vaultqr.com

-Must generate the QR at http://www.vaultqrgen.com

-If you use '6DBL' for model (without quotes) then you get a link to that product page,
otherwise it just sends you to the bose website. This is because 6DBL is the only valid model number 
that we have in our database
