Takes the QR code with parameters serial, product, brand,
directs the user to a nifty loading screen while it creates the contract 
then returns its bech32 address. 

query format is http://djbroderick.xyz/send?serial=040075Z62443247AC&product=headphones&brand=bose

A brief outline of features to be added:
V0_3 A nicely formatted results page complete with a link to the product page (and viewblock)
V0_4 Touch up the loading page to scale its size up for mobile devices
     Add an initial landing page where the user enters their email
V0_5 Add encryption to the query string to prevent tampering
     Create the QR code generator
V0_6 Refine the scilla contract to prevent duplicates from being made
        - maybe add a "resale" option such that users can transfer the nft