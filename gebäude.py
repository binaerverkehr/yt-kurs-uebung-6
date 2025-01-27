from geometrie import *


def haus(hoehe, breite, basisfarbe, dachfarbe):

    # Position vor Haus
    x, y = pos()
    pendown()

    rechteck(hoehe, breite, basisfarbe)
    left(90)
    forward(hoehe)
    right(90)

    dreieck(breite, dachfarbe)

    penup()
    goto(x, y)
    pendown()

    # Türbreite, Hoehe
    h, b = hoehe * 0.4, breite * 0.15
    penup()
    forward(breite / 2 - b / 2)
    pendown()
    # Position
    tür(hoehe=h, breite=b)


def tür(hoehe=80, breite=40, türfarbe="tan"):
    rechteck(breite=breite, laenge=hoehe, fuellfarbe=türfarbe)
