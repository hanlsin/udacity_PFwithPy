import turtle

def draw_leaf(turtle_name):
    for i in range(2):
        turtle_name.forward(50)
        turtle_name.right(60)
        turtle_name.forward(50)
        turtle_name.right(120)

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("white")

    tom = turtle.Turtle()
    tom.shape("turtle")
    tom.color("blue")
    tom.speed(50)

    for i in range(72):
        draw_leaf(tom)
        tom.right(5)

    tom.right(90)
    tom.forward(150)

    window.exitonclick()

draw_flower()