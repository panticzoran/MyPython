# Turtle program

import turtle

playgroundWindow = turtle.Screen()
playgroundWindow.bgcolor("darkblue")
playgroundWindow.title("Mala i velika kornjača")

malaKornjaca = turtle.Turtle()
malaKornjaca.color("yellow")
malaKornjaca.pensize(3)

velikaKornjaca = turtle.Turtle()
velikaKornjaca.color("orange")
velikaKornjaca.pensize(6)

lenght = 15
ugao = 90

for longer in range(6):

  for i in range(4):

    drawLenght = lenght + lenght * longer

    malaKornjaca.forward(drawLenght)
    malaKornjaca.left(ugao)
    velikaKornjaca.forward(drawLenght * 2)
    velikaKornjaca.right(ugao)

playgroundWindow.mainloop()
