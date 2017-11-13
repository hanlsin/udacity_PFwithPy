import turtle

def draw_squre(turtle_name):
    for i in range (4):
        turtle_name.forward(100)
        turtle_name.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(7)

    for i in range(36):
        draw_squre(brad)
        brad.right(10)

    # draw circle
    # tom = turtle.Turtle()
    # tom.shape("turtle")
    # tom.color("purple")
    # tom.speed(2)
    # tom.circle(100)

    window.exitonclick()

draw_art()