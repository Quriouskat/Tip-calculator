#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print ("Welcome to the tip calculator!")
message = input("what was the total bill? $")
bill = float(message)  
tip = int(input("How much would you like to give? 10, 12 or 15? $"))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill
individual_bill = bill_with_tip / people
final_bill = round(individual_bill, 2)
final_bill = "{:.2f}" .format(final_bill)
print(f"Each person should pay: ${final_bill}")