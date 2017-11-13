import turtle

def draw_k(turtle_name):
    t_st = [turtle_name.pos(), turtle_name.heading()]
    turtle_name.seth(-90)
    turtle_name.forward(200)
    turtle_name.backward(100)
    turtle_name.left(45)
    turtle_name.forward(120)
    turtle_name.backward(120)
    turtle_name.left(90)
    turtle_name.forward(120)
    turtle_name.backward(120)

    turtle_name.penup()
    turtle_name.goto(t_st[0])
    turtle_name.setheading(t_st[1])
    turtle_name.pendown()

def draw_c(turtle_name):
    turtle_name.seth(180)
    turtle_name.forward(100)
    turtle_name.left(90)
    turtle_name.forward(200)
    turtle_name.left(90)
    turtle_name.forward(100)

def draw_kc():
    window = turtle.Screen()
    window.bgcolor("white")

    bill = turtle.Turtle()
    bill.shape("turtle")
    bill.color("blue")
    bill.speed(50)

    draw_k(bill)
    bill.penup()
    bill.forward(250)
    bill.pendown()
    draw_c(bill)

    window.exitonclick()

draw_kc()