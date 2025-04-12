import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def rotate_angle_right():
    turtle_instance.right(100)

def rotate_angle_left():
    turtle_instance.left(100)


drawing_board.listen()
drawing_board.onkey(fun= turtle_forward,key="space")
drawing_board.onkey(fun= rotate_angle_right,key="2")
drawing_board.onkey(fun= rotate_angle_left,key="1")


turtle.mainloop()