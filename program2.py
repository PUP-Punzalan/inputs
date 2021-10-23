    # printing simple guide of prices
print("Apple = 20 pesos & Orange = 25 pesos")

    # adding inputs to get the desired amount
apple_str = input("How many apple you want to buy? Enter a value: ")
orange_str = input("How many orange you want to buy? Enter a value: ")

    # converting string into integers
appleVal = int(apple_str)
orangeVal = int(orange_str)

    # multiplying the integers to the price to get the amount
apple = appleVal * 20
orange = orangeVal * 25

    # adding apple and orange to get the total amount
total = apple + orange

    # printing the total amount
print("The total amount is", str(total) + ".")
        # str(variable) is to convert the variable into a string to add the period without any space
