import turtle as tt
import random as rd

tim = tt.Turtle()
tim.shape("turtle")
tt.colormode(255)
tim.pensize(2)
tim.speed("fastest")
tim.penup()
num_linhas = 10
num_colunas = 10
espaco = 90

# Começa no canto superior esquerdo
start_x = - (num_colunas // 2) * espaco
start_y = (num_linhas // 2) * espaco

tim.setpos(start_x, start_y)

# def desenhar(numero_de_lados):
#     angulo = 360/numero_de_lados
#     for _ in range(numero_de_lados):
#         tim.forward(100)
#         tim.right(angulo)
#
# def aleatorio():
#     angulo = rd.choice([0, 90, 180, 270])
#     tim.forward(40)
#     tim.setheading(angulo)
#
# def desenhar_circulo():
#     heading = tim.heading()
#     tim.setheading(heading + 10)
#     tim.circle(100)

# for i in range(3,11):
#     r = rd.randint(0, 255)
#     g = rd.randint(0, 255)
#     b = rd.randint(0, 255)
#     tim.pencolor(r, g, b)
#     aleatorio()

for linha in range(num_linhas):
    for coluna in range(num_colunas):
        r = rd.randint(0, 255)
        g = rd.randint(0, 255)
        b = rd.randint(0, 255)
        tim.pencolor(r, g, b)
        tim.dot(20)
        tim.forward(espaco)

    tim.setpos(start_x, start_y - espaco * (linha + 1))

tt.Screen().exitonclick()




















tt.Screen().exitonclick()