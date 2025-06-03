def life_in_weeks(idade):
    noventa = 4680
    idadeEmSemanas = idade * 52
    tempoRestante = noventa - idadeEmSemanas
    print(f"You have {tempoRestante} weeks left.")

tempo = int(input("Qual sua idade?\n"))
life_in_weeks(tempo)