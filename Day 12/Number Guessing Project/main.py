import art
import random as rd

def verifica_guess(chute, segredo):
    if chute > segredo:
        return "Too High\nGuess Again"
    elif chute < segredo:
        return "Too Low\nGuess Again"
    else:
        return "Correct!"

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_number = rd.randint(1, 100)
difficult = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficult.lower() == "easy":
    attempts = 10
else:
    attempts = 5

vitoria = False
tentativas_iniciais = attempts

if difficult.upper() == "EASY":
    attempts = 10
else:
    attempts = 5

while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    resultado = verifica_guess(guess, random_number)
    if resultado == "Correct!":
        tentativas_usadas = tentativas_iniciais - attempts + 1
        print(f"ACERTOU! O número era {random_number}. Você usou {tentativas_usadas} tentativas.")
        vitoria = True
        break
    else:
        print(resultado)
    attempts -= 1
if not vitoria:
    print(f"Acabaram as tentativas :(.\n O numero era: {random_number}")


