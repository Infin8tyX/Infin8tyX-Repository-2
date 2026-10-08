Costco_Item = [
    {
        "name": "Verity",
        "price": 3145.99,
        "Department": "high class valuables",
        "description": "Hey, its him, its VERITY, ask him anything"
    },
    {
        "name": "IPhone Duo",
        "price": 1999.99,
        "Department": "Technology",
        "Description": "The all new folding IPhone!"
    },
    {
        "name": "Mr. Whalen statue",
        "price": 499.99,
        "Department": "Art",
        "Description": "Statue of Mr Whalen"
    }
]

order = input("Hello, welcome to Costco, would you like a Verity AI, an IPhone Duo, or a statue of Mr. Whalen?")
if order =="Verity AI":
    print(Costco_Item[0])
    confirmverity = input("would you like to buy this item?")
    if confirmverity == "yes":
        print("Okay, that will be $3145.99")
        if confirmverity == "no":
            print("THEN WHY WOULD YOU ASK, VERITY IS LITERALLY THE BEST THING EVER, ARE YOU GOING TO BUY ANYTHING ELSE")
if order == "IPhone Duo":
    print(Costco_Item[1])
    confirmiphone = input("Would you like to buy this item?")
    if confirmiphone == "yes":
        print("Okay, that will be $1999.99")
        if confirmiphone == "no":
            print("Okay, would you like to buy anything else?")
if order == "Mr Whalen statue":
    print(Costco_Item[2])
    confirmstatue = input("Would you like to buy this item?")
    if confirmstatue == "yes":
        print("Okay, that will be $499.99")
        if confirmstatue == "no":
            print("Okay, would you like to buy anything else?")