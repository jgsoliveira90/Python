def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def div(n1, n2):
    return n1 / n2

def mlt(n1, n2):
    return n1 * n2

operations = {
    "+":add,
    "-":sub,
    "/":div,
    "*":mlt,

}

first_number = int(input("What is the first number?\n"))
result = first_number
while True:
    operator = input("What is the mathematical operator (a choice of +, -, * or /)?\n")
    another_number = int(input("What is the next number?\n"))
    result = operations[operator](result, another_number)
    print(f"The result is: {result}\n")

    respostaPergunta = input("Would you like to continue with the previous result? (Y or N)\n")
    if respostaPergunta == "N":
        print("Fim da calculadora!")
        break


