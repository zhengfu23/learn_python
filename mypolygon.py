import turtle
import math


def polyline(t, n, length, angle):
    """Draws n line segmments with the given length and
    angle (in degrees) between them. t is a turtle.
    """
    for i in range(n):
        t.fd(length)
        t.rt(angle)


def polygon(t, n, length):
    angle = 360/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    t.lt(step_angle / 2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def circle(t, r):
    arc(t, r, 360)


def square(t, length):
    polygon(t, 4, length)


if __name__ == '__main__':
    bob = turtle.Turtle()

    radius = 100
    bob.pu()
    bob.fd(radius)
    bob.lt(90)
    bob.pd()
    circle(bob, radius)

    turtle.mainloop()
