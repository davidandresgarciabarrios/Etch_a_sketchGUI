from turtle import Turtle, Screen

pointer = Turtle()
screen = Screen()


# Move the turtle forward by 10 units
def move_forwards():
    pointer.forward(10)


# Move the turtle backward by 10 units
def move_backwards():
    pointer.backward(10)


# Turn the turtle left by 10 degrees
def turn_left():
    pointer.setheading(pointer.heading() + 10)


# Turn the turtle right by 10 degrees
def turn_right():
    pointer.setheading(pointer.heading() - 10)


# Clear the drawing and reset the turtle position
def clear():
    pointer.clear()
    pointer.penup()
    pointer.home()
    pointer.pendown()


# Set up key bindings
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

# Exit on click
screen.exitonclick()
