import random as rd
import art

print(art.logo)

def soma_mao(mao):
    total = sum(mao)
    ases = mao.count(1)
    while ases > 0 and total + 10 <= 21:
        total += 10
        ases -= 1
    return total

def tem_blackjack(mao):
    return len(mao) == 2 and 1 in mao and 10 in mao

def comprar_carta(cartas):
    indice = rd.randrange(len(cartas))
    return cartas.pop(indice)

cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4

mao = [comprar_carta(cartas), comprar_carta(cartas)]
dealer = [comprar_carta(cartas), comprar_carta(cartas)]

jogo_ativo = True

# Checagem de Blackjack inicial
if tem_blackjack(mao) and tem_blackjack(dealer):
    print(f"Suas cartas: {mao}, BLACKJACK!")
    print(f"Cartas do dealer: {dealer}, BLACKJACK!")
    print("EMPATE!")
    jogo_ativo = False
elif tem_blackjack(mao):
    print(f"Suas cartas: {mao}, BLACKJACK!")
    print(f"Cartas do dealer: {dealer}")
    print("WINNER WINNER CHICKEN DINNER!")
    jogo_ativo = False
elif tem_blackjack(dealer):
    print(f"Suas cartas: {mao}")
    print(f"Cartas do dealer: {dealer}, BLACKJACK!")
    print("BLACKJACK! A CASA SEMPRE VENCE")
    jogo_ativo = False
else:
    print(f"Dealer está mostrando: {dealer[0]}")
    print(f"Suas cartas: {mao}, total: {soma_mao(mao)}")

if jogo_ativo:
    estourou = False
    vitoria = False

    # Loop do jogador
    while True:
        somaMao = soma_mao(mao)
        if somaMao > 21:
            print(f"Você estourou com: {somaMao}")
            estourou = True
            break
        elif somaMao == 21:
            print(f"Você fez 21!")
            vitoria = True
            break
        resposta = input(f"Você tem: {mao}, somando: {somaMao}, deseja parar ou comprar mais? Digite S para comprar\n")
        if resposta.upper() != "S":
            break
        nova_carta = comprar_carta(cartas)
        print(f"Você comprou um: {nova_carta}\n")
        mao.append(nova_carta)

    if not estourou and not vitoria:
        print(f"O dealer revela as cartas: {dealer}, total: {soma_mao(dealer)}")
        # Loop do Dealer
        while soma_mao(dealer) < 17:
            dealer.append(comprar_carta(cartas))
            print(f"Dealer compra: {dealer[-1]}. Mão do dealer: {dealer}, total: {soma_mao(dealer)}")

        somaMao = soma_mao(mao)
        somaMaoDealer = soma_mao(dealer)
        print(f"Suas cartas: {mao}, total: {somaMao} | Cartas do dealer: {dealer}, total: {somaMaoDealer}")

        if somaMaoDealer > 21:
            print("Dealer estourou! Parabéns, você ganhou!")
        elif somaMao > somaMaoDealer:
            print("Parabéns, você ganhou!")
        elif somaMao == somaMaoDealer:
            print("Empate!")
        else:
            print("Better luck next time!")
    else:
        somaMao = soma_mao(mao)
        somaMaoDealer = soma_mao(dealer)
        print(f"Suas cartas: {mao}, total: {somaMao} | Cartas do dealer: {dealer}, total: {somaMaoDealer}")