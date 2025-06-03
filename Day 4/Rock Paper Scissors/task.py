import random as rd

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

numeroAleatorio = rd.randint(0,2)
print(numeroAleatorio)
escolha = int(input("Escolha entre Pedra(0), Papel(1), Tesoura(2)"))
lista_PedraPapelTesoura = [rock, paper, scissors]
print(f"Sua escolha foi: \n {lista_PedraPapelTesoura[escolha]}")
print(f"Escolha do computador foi: \n {lista_PedraPapelTesoura[numeroAleatorio]}")

pedraContraPapel = (escolha == 0 and numeroAleatorio == 1)
pedraContraTesoura = (escolha == 0 and numeroAleatorio == 2)
papelContraTesoura = (escolha == 1 and numeroAleatorio == 2)
papelContraPedra = (escolha == 1 and numeroAleatorio == 0)
tesouraContraPedra = (escolha == 2 and numeroAleatorio == 0)
tesouraContraPapel = (escolha == 2 and numeroAleatorio == 1)

if escolha == numeroAleatorio:
    print("EMPATE")
elif pedraContraPapel or papelContraTesoura or tesouraContraPedra:
    print("PERDEU")
elif tesouraContraPapel or papelContraPedra  or pedraContraTesoura:
    print("GANHOU")