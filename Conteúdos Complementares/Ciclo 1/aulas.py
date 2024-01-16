import turtle

Screen = turtle.Screen()
t = turtle.Turtle()


t.shape('turtle')
t.turtlesize(2,2,3)
t.pensize(5)

def drawFigure(lados, tamanho):
    angulo = 360/lados
    for i in range(lados):
        t.forward(tamanho)
        t.left(angulo)

    return 1

t.speed(0)

drawFigure(360,1)

# for i in range(3,11):
#     drawFigure(i,100)

t.penup()
t.forward(1000)

turtle.done()
