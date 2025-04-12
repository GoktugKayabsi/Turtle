import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("Turtle Python")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")

def shrinkingsquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size -  5

shrinkingsquare(150)
shrinkingsquare(130)
shrinkingsquare(110)
shrinkingsquare(90)
shrinkingsquare(70)
shrinkingsquare(50)
shrinkingsquare(30)
shrinkingsquare(10)
