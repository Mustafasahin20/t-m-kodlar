import turtle

t=turtle.Pen()

def up():
    t.color('red')
    t.forward(8)
    t.turtle=Turtle(shape='classic')


def down():
    t.color('black')
    t.backward(8)
    t.turtle=Turtle(shape='arrow')

def left():
    t.color('blue')
    t.left(8)
    t.turtle=Turtle(shape='turtle')

def right():
    t.color('yellow')
    t.right(8)
    t.turtle=Turtle(shape='circle')

def uc():
    t.penup()

def indir():
    t.pendown

def doldur():
    t.begin_fill

def birak():
    t.end_fill


def daire():
    yaricap=int(turtle.numinput('daire çapı','yaroçap giriniz:'))
    t.circle(yaricap)


turtle.onkeypress(up,'w')
turtle.onkeypress(down,'s')
turtle.onkeypress(left,'a')
turtle.onkeypress(right,'d')
turtle.onkeypress(uc,'e')
turtle.onkeypress(indir,'q')
turtle.onkeypress(doldur,'z')
turtle.onkeypress(birak,'x')
turtle.onkeypress(daire,'c')

turtle.listen()
















    
