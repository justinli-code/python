import turtle
t=turtle.Turtle()
t.shape("turtle")
turtle.bgcolor("black")
t.speed(0)

t.color("orange")
t.pensize(650)
t.left(90)
t.fd(1)

t.color("yellow")
t.pensize(540)
t.fd(-1)

t.color("black")
t.pensize(1)

    
t.penup()
t.color("green")
t.goto(200,30)
t.pendown()
t.pensize(50)
t.fd(1)

t.penup()
t.goto(-200,-30)
t.pendown()
t.pensize(50)
t.fd(1)

t.penup()
t.goto(-130,150)
t.pendown()
t.pensize(50)
t.fd(1)

t.penup()
t.goto(130,160)
t.pendown()
t.pensize(50)
t.fd(1)

t.penup()
t.goto(-130,-150)
t.pendown()
t.pensize(50)
t.fd(1)

t.penup()
t.goto(130,-140)
t.pendown()
t.pensize(50)
t.fd(1)

t.penup()
t.goto(0,230)
t.pendown()
t.pensize(50)
t.fd(1)

t.penup()
t.goto(0,-200)
t.pendown()
t.pensize(50)
t.fd(1)



t.color("red")
t.penup()
t.goto(30,100)
t.pendown()
t.pensize(50)
t.fd(1)

t.penup()
t.goto(-200,40)
t.pendown()
t.pensize(50)
t.fd(1)

t.penup()
t.goto(-100,-200)
t.pendown()
t.pensize(50)
t.fd(1)

t.penup()
t.goto(90,200)
t.pendown()
t.pensize(50)
t.fd(1)

t.penup()
t.goto(-60,-100)
t.pendown()
t.pensize(50)
t.fd(1)

t.penup()
t.goto(60,-100)
t.pendown()
t.pensize(50)
t.fd(1)

t.penup()
t.goto(-60,100)
t.pendown()
t.pensize(50)
t.fd(1)

t.penup()
t.goto(100,0)
t.pendown()
t.pensize(50)
t.fd(1)

t.color("blue")
t.penup()
t.goto(0,0)
t.pendown()
t.pensize(70)
t.fd(1)

t.color("black")
t.pensize(5)
for x in range(8):
    t.fd(325)
    t.fd(-325)
    t.left(45)



turtle.done()
