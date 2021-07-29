###################### OVERVIEW ###############################
Takes the QR code with encoded parameters brand, product, model, and serial
user waits on a nifty loading screen while it creates the contract.

Manual queries no longer work, you need to use the QR gen to get the encoded query.

That model number represents a real product and we search our database for it so do not change otherwise the program will fail.

######################## DEVELOPMENT TIMELINE #################################
V0_4_7... fix the url tripling bug

V0_5 Touch up the loading page to scale its size up for mobile devices; also add VAULT below it (name is now PAV) Polish the results page (change blue font, increase gradient darkness). Play with the gas price to see if we can achieve faster contract generation. 

V0_5_5... final testing and bug fixes

V0_6 The version that will be used at the demo. 


Post demo?
-Add email landing page
-Refine the scilla contract to prevent duplicates from being made
-maybe add a "resale" option such that users can transfer the nft

#################### USAGE NOTES AND CONSTRAINTS ####################################
-Hosted at http://www.vaultqr.com

-Must generate the QR at http://www.vaultqrgen.com

-If you use '6DBL' for model (without quotes) then you get a link to that product page,
otherwise it just sends you to the bose website. This is because 6DBL is the only valid model number 
that we have in our database

-You must make the contract unique in some way. If you generate a contract that is exactly the same,
the Ziliqa blockchain will NOT create a duplicate by default (it does provide the address to the previously
made contract, however). This is extremely useful and we can use this to our advantage in the future. 
Anyways, make sure you use a unique serial # each time.
