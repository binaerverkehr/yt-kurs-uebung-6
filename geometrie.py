from turtle import *


# Funktion zum Zeichnen eines Quadrats
# Parameter:
# - laenge: Seitenlänge des Quadrats
# - fuellfarbe: Füllfarbe des Quadrats (optional)
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


# Funktion zum Zeichnen eines Rechtecks
# Parameter:
# - laenge: Höhe des Rechtecks
# - breite: Breite des Rechtecks
# - fuellfarbe: Füllfarbe des Rechtecks (optional)
def rechteck(laenge, breite, fuellfarbe=None):

    if fuellfarbe:
        color(fuellfarbe)
        begin_fill()

    forward(breite)
    left(90)
    forward(laenge)
    left(90)
    forward(breite)
    left(90)
    forward(laenge)
    left(90)

    if fuellfarbe:
        end_fill()


# Funktion zum Zeichnen eines gleichseitigen Dreiecks
# Parameter:
# - laenge: Seitenlänge des Dreiecks
# - fuellfarbe: Füllfarbe des Dreiecks (optional)
def dreieck(laenge, fuellfarbe=None):
    if fuellfarbe:
        color(fuellfarbe)
        begin_fill()
    for i in range(3):
        forward(laenge)
        left(120)
    if fuellfarbe:
        end_fill()


# Funktion zum Zeichnen eines Kreises
# Parameter:
# - laenge: Schrittweite für die Kreiskonstruktion
# - fuellfarbe: Füllfarbe des Kreises (optional)
def kreis(laenge, fuellfarbe=None):
    if fuellfarbe:
        color(fuellfarbe)
        begin_fill()
    for i in range(120):
        forward(laenge)
        left(3)
    if fuellfarbe:
        end_fill()
