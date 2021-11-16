#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
print("Welocome to the tip calculator. :) ")
bill = input("What was the total bill?\n $ ")
tip = input("How much tip would you like to give?\n 10, 12 or 15?\n")
people = input("How many people to split the bill??\n")
new_bill = float(bill)
new_tip = int(tip)
new_people = int(people)
split = ((new_bill + new_bill * (new_tip/100))/new_people)
new_split = round(split,1)
print(new_split)
print(f"Each person should pay: $ {new_split}")


#Write your code below this line 👇