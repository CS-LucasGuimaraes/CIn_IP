import turtle

Screen = turtle.Screen()
t = turtle.Turtle()


t.shape('turtle')
t.turtlesize(2,2,3)
t.pensize(5)
t.speed(0)


def drawFigure(lados, tamanho):
    angulo = 360/lados
    for i in range(lados):
        t.forward(tamanho)
        t.left(angulo)

    return 1

def drawRow(x,size):
    for i in range(x):
        drawFigure(4,size)  
        t.forward(size)


def drawGraph(x, y, size):
    for i in range(y):
        drawRow(x,size)
        t.back(size*x)

        if i != (y-1):
            t.right(90)
            t.forward(size)
            t.left(90)

x = 8
y = 4
size = 50

drawGraph(x,y,size)

t.penup()
t.forward(10000)

turtle.done()
