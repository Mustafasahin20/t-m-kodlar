import turtle

t=turtle.Turtle(shape='classic')
t.pensize(8)

t.circle(50)
t.penup()
t.setposition(120,0)
t.pendown()
t.color('red')
t.circle(50)

t.penup()
t.setposition(-120,0)
t.pendown()
t.color('blue')
t.circle(50)

t.penup()
t.setposition(60,-60)
t.pendown()
t.color('green')
t.circle(50)

t.penup()
t.setposition(-60,-60)
t.pendown()
t.color('yellow')
t.circle(50)
