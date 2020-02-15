import turtle
t=turtle.Turtle()
t.shape("turtle")
#turtle.bgcolor("black")
t.speed(10)

colors=["red"]
t.fd(-200)

for x in range(400):
    t.pensize(20)
    t.fd(400)           #t.fd(x*3)
    t.right(144)  #91螺旋 170爆炸 50玫瑰 200八角星 250多瓣花 270正方 300正六边形 330近圆
    t.color(colors[x%1])
    t.width(x/50)

turtle.done()
