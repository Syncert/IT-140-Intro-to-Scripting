#output total change with fewest coins
coins = int(input("Enter the amount"))

dollar = 100
quarter = 25
dime = 10
nickel = 5
penny = 1

if coins == 0:
    print("No change")
else:


    if (coins // dollar) > 0:
        if (coins // dollar) == 1:
            print("{} Dollar".format(str(coins // dollar)))
            coins = coins - ((coins // dollar) * dollar)
        else:
            print("{} Dollars".format(str(coins // dollar)))
            coins = coins - ((coins // dollar) * dollar)
    #   print("new coins {}".format(coins))
    if (coins // quarter) > 0:
        if (coins // quarter) == 1:
            print("{} Quarter".format(str(coins // quarter)))
            coins = coins - ((coins // quarter) * quarter)
        else:
            print("{} Quarters".format(str(coins // quarter)))
            coins = coins - ((coins // quarter) * quarter)
    #   print("New coins {}".format((coins)))
    if (coins // dime) > 0:
        if (coins // dime) == 1:
            print("{} Dime".format(str(coins // dime)))
            coins = coins - ((coins // dime) * dime)
        else:
            print("{} Dimes".format(str(coins // dime)))
            coins = coins - ((coins // dime) * dime)
    #    print("New coins {}".format((coins)))
    if (coins // nickel) > 0:
        if (coins // nickel) == 1:
            print("{} Nickel".format(str(coins // nickel)))
            coins = coins - ((coins // nickel) * nickel)
        else:
            print("{} Nickels".format(str(coins // nickel)))
            coins = coins - ((coins // nickel) * nickel)
    #    print("New coins {}".format((coins)))
    if (coins // penny) > 0:
        if (coins // penny) == 1:
            print("{} Penny".format(str(coins // penny)))
            coins = coins - ((coins // penny) * penny)
        else:
            print("{} Pennies".format(str(coins // penny)))
            coins = coins - ((coins // penny) * penny)        
    #    print("New coins {}".format((coins)))