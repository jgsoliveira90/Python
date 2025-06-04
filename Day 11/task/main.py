import random as rd
import art

print(art.logo)

def soma(n1, n2):
    return n1 + n2

def comprarCarta(cartas):
    indice = rd.randrange(len(cartas))
    return cartas.pop(indice)

cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4

while True:
    dealer = 0
    mao = 0

    dealer = comprarCarta(cartas)
    dealer = soma(dealer, comprarCarta(cartas))
    mao = comprarCarta(cartas)
    mao = soma(mao, comprarCarta(cartas))

    estourou = False
    vitoria = False

    # Loop do jogador
    while True:
        if mao > 21:
            print(f"Você estourou com: {mao}")
            estourou = True
            break
        elif mao == 21:
            print(f"Você Ganhou com: {mao}")
            vitoria = True
            break
        resposta = input(f"Você tem: {mao}, deseja parar ou comprar mais? Digite S para comprar\n")
        if resposta != "S":
            break
        nova_carta = comprarCarta(cartas)
        print(f"Você comprou um: {nova_carta}\n")
        mao = soma(mao, nova_carta)

    if estourou or vitoria:
        print(f"Sua mao: {mao} \n Mao do dealer: {dealer}")
        break

    # Loop do Dealer
    while dealer < 17:
        dealer = soma(dealer, comprarCarta(cartas))

    print(f"Sua mão: {mao} | Mão do dealer: {dealer}")

    if dealer > 21:
        print(f"Dealer estourou com {dealer}! Parabéns!")
    elif mao > dealer:
        print("Parabéns!")
    elif mao == dealer:
        print("Empate!")
    else:
        print("Better luck next time!")

    break