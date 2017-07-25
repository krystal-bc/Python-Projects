import turtle


def draw_square(turtle):
    for i in range(1,5):
        turtle.forward(100)
        turtle.right(90)

def draw_circle(turtle):
        turtle.circle(100)

window = turtle.Screen()
#window.bgcolor("red")
brad = turtle.Turtle()
brad.shape("turtle")
brad.color("dark green")
brad.speed(2)
for i in range(1,37):
    draw_square(brad)
    brad.right(10)
brad.color("green")
for i in range(1,37):
    draw_circle(brad)
    brad.right(10)
window.exitonclick()
    

