import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

'''
#basic
turtle_instance = turtle.Turtle()
turtle_instance.forward(100)
turtle_instance_2 = turtle.Turtle()
turtle_instance_2.left(180)
turtle_instance_2.forward(100)

#square
turtle_instance = turtle.Turtle()
for i in range(4):
    turtle_instance.forward(50)
    turtle_instance.left(90)


#star
turtle_instance = turtle.Turtle()
for i in range(5):
    turtle_instance.left(144)
    turtle_instance.forward(100)

'''


#polygon
turtle_instance = turtle.Turtle()
num_sides = 6
angle = 360.0 / num_sides
side_lenght = 100

for i in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(side_lenght)




turtle.done()