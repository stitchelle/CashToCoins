def calc_coins():
    dollarAmount = 8.69 * 100

    piggyBank = {
        "pennies": 0,
        "nickels": 0,
        "dimes": 0,
        "quarters": 0
    }

    
    remainder_after_quarters = dollarAmount % 25

    how_many_quarters = (dollarAmount - remainder_after_quarters)/25

    remainder_after_dimes = remainder_after_quarters % 10

    how_many_dimes = (remainder_after_quarters - remainder_after_dimes) / 10

    remainder_after_nickels = remainder_after_dimes % 5
    
    how_many_nickels = (remainder_after_dimes - remainder_after_nickels) / 5

    remainder_after_pennies = remainder_after_nickels % 1

    how_many_pennies = (remainder_after_nickels - remainder_after_pennies) /1

    print("quarters",how_many_quarters)
    print("remainder after quarters",remainder_after_quarters)
    print("dimes", how_many_dimes)
    print("remainder after dime",remainder_after_dimes)
    print("nickels", how_many_nickels)
    print("remainder after nickels", remainder_after_nickels)
    print("pennies", how_many_pennies)
    print("quarters", how_many_quarters,"dimes", how_many_dimes,"nickels", how_many_nickels,"pennies", how_many_pennies)

# Your magic Python code here

calc_coins()