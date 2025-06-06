import art
import game_data as gd
import random as rd

def escolher_conta(data):
    """Sorteia e remove uma conta aleatória da lista."""
    indice = rd.randint(0, len(data) - 1)
    return data.pop(indice)

def exibir_conta(conta, posicao):
    """Exibe as informações de uma conta."""
    print(f"{posicao}: {conta['name']}, {conta['description']}, {conta['country']}")

def comparar(conta1, conta2, escolha):
    """Compara follower_count e retorna True se a escolha estiver correta."""
    if escolha == 1:
        return conta1['follower_count'] >= conta2['follower_count']
    else:
        return conta2['follower_count'] >= conta1['follower_count']

print(art.logo)
quantidade_de_acertos = 0

data = gd.data.copy()
conta_atual = escolher_conta(data)

while len(data) > 0:
    conta_proxima = escolher_conta(data)
    exibir_conta(conta_atual, "1")
    print(art.vs)
    exibir_conta(conta_proxima, "2")

    resposta = int(input("Qual você acha que tem mais seguidores no Instagram?: 1 ou 2?\n"))

    if comparar(conta_atual, conta_proxima, resposta):
        quantidade_de_acertos += 1
        print(f"Você acertou! quantidade de acertos até o momento: {quantidade_de_acertos}")
        conta_atual = conta_proxima
    else:
        print("ERROU!")
        break

print(f"Você teve: {quantidade_de_acertos} acertos")