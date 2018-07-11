import turtle
import math


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.rt(90)


def polygon(t, n, length):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.rt(angle)


def circle(t, r):
    circumference = 2 * math.pi * r
    n = 720
    length = circumference / n
    polygon(t, n, length)


def arc(t, r, angle):
    for i in range(angle):
        t.fd(2*math.pi*r/360)
        t.rt(1)


bob = turtle.Turtle()
circle(bob, r=50)
