from turtle import *

def quadrat(laenge, fuellfarbe=None):

    if fuellfarbe:
        color(fuellfarbe)
        begin_fill()

    i = 0
    while i < 4:
        forward(laenge)
        left(90)
        i = i + 1
    
    if fuellfarbe:
        end_fill()


def dreieck(laenge, fuellfarbe=None):
    if fuellfarbe:
        color(fuellfarbe)
        begin_fill()
    for i in range(3):
        forward(laenge)
        left(120)
    if fuellfarbe:
        end_fill()


def kreis(laenge, fuellfarbe=None):
    if fuellfarbe:
        color(fuellfarbe)
        begin_fill()
    for i in range(120):
        forward(laenge)
        left(3)
    if fuellfarbe:
        end_fill()