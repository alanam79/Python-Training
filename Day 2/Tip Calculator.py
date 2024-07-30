#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6 (1.12 represents 100% of the bill amount (the original amount) plus 12% more)

#Format(ROUND) the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# print("Welcome to the tip calculator!\n")
# bill = input("What was the total bill? $ ")
# tip = input("How much tip would you like to give? 10, 12, or 15? ")
# peopleToSplit = input("How many people to split the bill? ")

# bill_float = float(bill) # could have added float to the function (bill = (float(input("What was the total bill? $ ")))
# tip_float = float(tip) #could have added float/int to the function (tip = (float(input("How much tip would you like to give? 10, 12,
# toSplit = int(peopleToSplit) #could have added int to the function (peopleToSplit = (int(input("How many people to split the bill? ")))

# # By including 1 in the formula, you ensure that the calculation accounts for both the original bill and the tip, 
# # giving you the correct total amount each person needs to pay.
# eachToPay = bill_float / toSplit * (1 + tip_float / (100))


# eachToPayRounded = round(eachToPay, 2) # The 2 is how many decimal points we want to round to
# eachToPayRounded = "{:.2f}".format(eachToPay) # this alows python to format the number to 2 decimal places even if the number is a whole number, instead of showing $33.6 it would show $33.60 (for example)

# print(f"Each person should pay: ${eachToPayRounded}")

