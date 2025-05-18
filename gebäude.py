from geometrie import *


# Funktion zum Zeichnen eines Hauses
# Parameter:
# - hoehe: Höhe des Hauses (ohne Dach)
# - breite: Breite des Hauses
# - basisfarbe: Farbe der Hauswände
# - dachfarbe: Farbe des Dachs
def haus(hoehe, breite, basisfarbe, dachfarbe):
    # Speichere Startposition für spätere Verwendung
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


# Funktion zum Zeichnen einer Tür
# Parameter:
# - hoehe: Höhe der Tür (Standard: 80)
# - breite: Breite der Tür (Standard: 40)
# - türfarbe: Farbe der Tür (Standard: hellbraun)
def tür(hoehe=80, breite=40, türfarbe="tan"):
    rechteck(breite=breite, laenge=hoehe, fuellfarbe=türfarbe)
