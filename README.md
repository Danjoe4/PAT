Takes the QR code with parameters brand, product, model, and serial
directs the user to a nifty loading screen while it creates the contract 
then returns its bech32 address. 

Manual queries no longer work, you need to use the QR gen to get the encoded query. This is V0_4, we added decoding. 

That model number represents a real product and we search our database for it so do not change otherwise the program will fail. Overall, V03 is a success. Slight reprioritization of goals, see below:

Separate REPO
V0_2_5 QR code url is obfuscated

MAIN REPO
V0_5 Touch up the loading page to scale its size up for mobile devices; also add VAULT below it (name is now PAV) Polish the results page (change blue font, increase gradient darkness). Play with the gas price to see if we can achieve faster contract generation

V0_5_5 MEETING: Decide if we need an initial landing page where the user enters their email

V0_6 Final testing, add error handling. 


Post demo?
-Refine the scilla contract to prevent duplicates from being made
-maybe add a "resale" option such that users can transfer the nft

########################################################
Hosted at www.vaultqr.com (soon)

USEAGE NOTES:
Must generate the QR at http://danjoe4.pythonanywhere.com/
If you use '6DBL' for model (without quotes) then you get a link to that product page,
otherwise it sends you to the bose website because 6DBL is the only valid model number 
that we have in our database
