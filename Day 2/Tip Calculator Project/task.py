print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total_com_tip = bill + (bill * tip/100);
result = total_com_tip / people;
final_result = round(result,2)

print(f"Each person should pay: {final_result}")


