from turtle import *
import turtle
turtle.tracer(0, 0)
left(90)


def tree(trunk, scaling, angle):
    width(2)
    if trunk > 2.30:
        # to paint forward by the trunk length
        forward(trunk)
        # scaling factor
        branch = trunk * scaling
        # f1
        left(angle)
        tree(branch, scaling, angle)
        right(angle)
        # f2
        right(angle)
        tree(branch, scaling, angle)
        left(angle)

        # to go back to point of split intersection when succeeding branches are too short (less than specified value)
        backward(trunk)


# to start at (0, -350) without tracing
penup()
goto(0, -300)
# to start tracing
pendown()
# to rotate left or counter-clockwise because function original stems out to the right
# left(90)

tree(150, 0.75, 30)

tracer(False)

exitonclick()
