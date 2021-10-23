    # adding inputs to get the desired value
money_str = input("Insert the total amount of money you have: ")
apple_str = input("Insert the price of an apple: ")

    # converting the string into float (with decimals)
moneyAmount = float(money_str)
applePrice = float(apple_str)

    # dividing the total money to the apple price, to get the number of apples you can buy
totalApple = moneyAmount // applePrice

    # multiplying the total apple you can buy to the apple price, to get the total apple price
totalApplePrice = totalApple * applePrice

    # subtracting the total money to the total apple price, to get the total change
totalChange = moneyAmount - totalApplePrice

    # printing the total apple you can buy and the total change
print("You can buy ", totalApple, "apples and your change is ", str(totalChange) + ".")
        # str(variable) is to convert the variable into a string to add the period without any space
