import turtle
p=turtle.Turtle()
p.pensize(6)
p.speed(0)
p.color('pink','pink')
p.left(90)
for i in range(4):
    p.begin_fill()
    p.circle(200,90)
    p.left(90)
    p.circle(200,90)
    p.end_fill()
turtle.done()
