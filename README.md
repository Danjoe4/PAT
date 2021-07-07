Takes the QR code with parameters brand, product, model, and serial
directs the user to a nifty loading screen while it creates the contract 
then returns its bech32 address. 

NEW query format is http://djbroderick.xyz/send?serial=RANDOSERIALXNAFD42069&product=headphones&brand=bose&model=7DAV

That model number represents a real product and we search our database for it so do not change otherwise the program will fail. Overall, V03 is a success. Slight reprioritization of goals, see below:

Separate REPO
V0_1 Create the QR code generator, with an obfuscated query string to prevent tampering and make our product seem more like "magic"

MAIN REPO
V0_5 Touch up the loading page to scale its size up for mobile devices. Polish the results page (change blue font, increase gradient darkness). Play with the gas price to see if we can achieve faster contract generation

V0_5_5 MEETING: Decide if we need an initial landing page where the user enters their email

V0_6 Final testing, add error handling. 


Post demo?
-Refine the scilla contract to prevent duplicates from being made
-maybe add a "resale" option such that users can transfer the nft