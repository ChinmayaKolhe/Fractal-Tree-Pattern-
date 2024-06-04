import turtle as tu

roo = tu.Turtle()  
wn = tu.Screen() 
wn.bgcolor("black") 
wn.title("Fractal Tree Pattern")
roo.left(90) 
roo.speed(940) 


def draw(l): 
    if (l < 10):
        return
    else:

        roo.pensize(2) 
        roo.pencolor("yellow") 
        roo.forward(l)  
        roo.left(30) 
        draw(3 * l / 4)  
        roo.right(60) 
        draw(3 * l / 4) 
        roo.left(30) 
        roo.pensize(2)
        roo.backward(l)  


draw(10)  
roo.right(90)
roo.speed(10000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("magenta")
        roo.forward(l)
        roo.left(30)
        draw(3 * l / 4)
        roo.right(60)
        draw(3 * l / 4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(10)

roo.left(270)
roo.speed(10000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("red") 
        roo.forward(l)
        roo.left(30)
        draw(3 * l / 4)
        roo.right(60)
        draw(3 * l / 4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(10)

roo.right(90)
roo.speed(10000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor('#FFF8DC')  
        roo.forward(l)
        roo.left(30)
        draw(3 * l / 4)
        roo.right(60)
        draw(3 * l / 4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(10)




def draw(l):
    if (l < 10):
        return
    else:

        roo.pensize(3)
        roo.pencolor("lightgreen")  
        roo.forward(l)
        roo.left(30)
        draw(4 * l / 5)
        roo.right(60)
        draw(4 * l / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)


draw(20)

roo.right(90)
roo.speed(10000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(3)
        roo.pencolor("red")  
        roo.forward(l)
        roo.left(30)
        draw(4 * l / 5)
        roo.right(60)
        draw(4 * l / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)


draw(20)

roo.left(270)
roo.speed(10000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(3)
        roo.pencolor("yellow")  
        roo.forward(l)
        roo.left(30)
        draw(4 * l / 5)
        roo.right(60)
        draw(4 * l / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)


draw(20)

roo.right(90)
roo.speed(10000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(3)
        roo.pencolor('#FFF8DC')
        roo.forward(l)
        roo.left(30)
        draw(4 * l / 5)
        roo.right(60)
        draw(4 * l / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)


draw(20)


def draw(l):
    if (l < 10):
        return
    else:

        roo.pensize(2)
        roo.pencolor("cyan")  
        roo.forward(l)
        roo.left(30)
        draw(6 * l / 7)
        roo.right(60)
        draw(6 * l / 7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(30)

roo.right(90)
roo.speed(10000)


def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("yellow")  
        roo.forward(l)
        roo.left(30)
        draw(6 * l / 7)
        roo.right(60)
        draw(6 * l / 7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(30)

roo.left(270)
roo.speed(10000)


def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("magenta") 
        roo.forward(l)
        roo.left(30)
        draw(6 * l / 7)
        roo.right(60)
        draw(6 * l / 7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(30)

roo.right(90)
roo.speed(10000)



def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor('#FFF8DC')
        roo.forward(l)
        roo.left(30)
        draw(6 * l / 7)
        roo.right(60)
        draw(6 * l / 7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(30)
wn.exitonclick()