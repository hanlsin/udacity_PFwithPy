import turtle

def draw_green_t(turtle_name):
    turtle_name.fillcolor("lightgreen")
    turtle_name.begin_fill()
    for i in range(3):
        turtle_name.forward(200)
        turtle_name.left(120)
    turtle_name.end_fill()

def draw_inner_t(turtle_name, length, depth):
    if depth == 0:
        return

    turtle_name.forward(length)
    turtle_name.left(60)

    turtle_name.fillcolor("white")
    turtle_name.begin_fill()
    t_sts = [[None]] * 3
    for i in range(3):
        t_sts[i] = [turtle_name.pos(), turtle_name.heading()]
        turtle_name.forward(length)
        turtle_name.left(120)
    turtle_name.end_fill()

    for t_st in t_sts:
        turtle_name.penup()
        turtle_name.goto(t_st[0])
        turtle_name.pendown()
        turtle_name.setheading(t_st[1] - 60)
        draw_inner_t(turtle_name, length / 2, depth - 1)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")

    ann = turtle.Turtle()
    ann.shape("turtle")
    ann.color("blue")
    ann.speed(50)

    draw_green_t(ann)

    draw_inner_t(ann, 200 / 2, 3)

    window.exitonclick()

draw_art()