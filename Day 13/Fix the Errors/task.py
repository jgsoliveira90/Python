try:
    age = int(input("How old are you?"))
except ValueError:
    print("Invalid number, Try again!")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
