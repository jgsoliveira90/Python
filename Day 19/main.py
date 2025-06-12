import turtle as tt
import random as rd

screen = tt.Screen()
screen.setup(500, 400)
aposta = screen.textinput("Aposte em qual tartaruga vai vencer.", "Escolha uma cor dentre as cores do arco Iris")

eixoY = 0
turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]


def cria_tartaruga(color, eixoY):
    t = tt.Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.goto(x=-230, y=eixoY)
    turtles.append(t)


for i in range(7):
    color = rd.choice(colors)
    cria_tartaruga(color, eixoY)
    colors.remove(color)
    eixoY = eixoY+30

acabou_a_corrida = True

while acabou_a_corrida:
    for x in turtles:
        if x.xcor() > 230:
            acabou_a_corrida = False
            if aposta == x.pencolor():
                print("VOCE ACERTOU A COR!")
            else:
                print(f"Acabou a corrida das turtles, o vencedor foi: {x.pencolor()}")

        dist = rd.randint(0, 15)
        x.forward(dist)


screen.exitonclick()