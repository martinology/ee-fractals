from turtle import *
import turtle
import random


turtle.tracer(0, 0)


def tree(trunk, scaling, angle, randomness=0):

    if trunk > 10:

        width(trunk/8)
        forward(trunk)
        # scaling factor
        branch = trunk * scaling
        if randomness > 0:
            # adds variation to the length of the branch
            branch *= random.uniform(0.9, 1.1)
        # adds variation to angle by adding a random value in a set with mean = 0 and standard dev = randomness
        angle_left = angle + random.gauss(0, randomness)
        angle_right = angle + random.gauss(0, randomness)

        left(angle_left)
        tree(branch, scaling, angle, randomness)
        right(angle_left)

        right(angle_right)
        tree(branch, scaling, angle, randomness)
        left(angle_right)

        # to go back to point o fsplit intersection when succeeding branches are too short (less than 10)
        backward(trunk)


# to start at (0, -275) without tracing
penup()
goto(0, -275)

pendown()
# to rotate left or counter-clockwise because function stems out to the right
left(90)

tree(100, 0.83, 20, 10)

tracer(True)

exitonclick()
