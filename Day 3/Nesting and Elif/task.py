print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Qual sua idade? "))
    if age <= 18:
        print("meia")
    elif age >1:
        print("cheia")
else:
    print("Sorry you have to grow taller before you can ride.")
