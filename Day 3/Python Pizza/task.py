print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

valor = 0
if extra_cheese == "Y":
    valor += 1
if pepperoni == "Y":
    if size == "S":
        valor += 2
    else:
        valor += 3

if size == "S":
    valor += 15
elif size == "M":
    valor += 20
else:
    valor += 25

print(f"Your final bill is: ${valor}.")


