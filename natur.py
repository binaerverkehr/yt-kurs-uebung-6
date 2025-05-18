from geometrie import *


# Funktion zum Zeichnen einer einzelnen Blume
# Parameter:
# - stielhoehe: Höhe des Blumenstiels (Standard: 30)
# - stielbreite: Breite des Blumenstiels (Standard: 3)
# - farbe_blueten: Farbe der Blütenblätter (Standard: pink)
# - farbe_mitte: Farbe der Blütenmitte (Standard: gelb)
def blume(stielhoehe=30, stielbreite=3, farbe_blueten="pink", farbe_mitte="yellow"):
    speed(0)
    # Stiel
    color("green")
    rechteck(stielhoehe, stielbreite, "green")

    # Position für die Blüte (über dem Stiel)
    left(90)
    forward(stielhoehe)
    right(90)

    # Blütenblätter
    color(farbe_blueten)
    pensize(2)  # Dickere Linien für die Blütenblätter
    for i in range(6):  # Reduziert auf 6 Blütenblätter
        # Größeres, ovales Blütenblatt
        begin_fill()
        circle(20, 60)  # Erster Teil des Blatts
        left(120)
        circle(20, 60)  # Zweiter Teil des Blatts
        left(120)
        end_fill()
        left(60)  # 360° / 6 = 60° für gleichmäßige Verteilung

    # Blütenmitte
    pensize(1)  # Zurück zur normalen Linienstärke
    color(farbe_mitte)
    begin_fill()
    circle(10)  # Größerer, einfacher Kreis für die Mitte
    end_fill()


# Funktion zum Zeichnen eines einzelnen Baums
# Parameter:
# - stammhoehe: Höhe des Baumstamms (Standard: 100)
# - stammbreite: Breite des Baumstamms (Standard: 20)
# - farbe: Farbe der Baumkrone (Standard: grün)
def baum(stammhoehe=100, stammbreite=20, farbe="green"):
    speed(0)
    # Stamm
    color("brown")
    rechteck(stammhoehe, stammbreite, "brown")

    # Position für die Baumkrone (mittig über dem Stamm)
    left(90)
    forward(stammhoehe)
    right(90)
    backward(stammbreite * 2)

    # Baumkrone (3 Dreiecke übereinander)
    kronenbreite = stammbreite * 5
    abstand = stammhoehe / 3  # Abstand zwischen den Dreiecken

    for i in range(3):
        dreieck(kronenbreite, farbe)
        # Nach oben für nächstes Dreieck
        penup()
        left(90)
        forward(abstand)
        right(90)
        pendown()
        # Nächstes Dreieck etwas kleiner
        # kronenbreite = kronenbreite * 0.7


# Funktion zum Zeichnen einer Reihe von Bäumen
# Parameter:
# - anzahl: Anzahl der zu zeichnenden Bäume
# - versatz_x: Horizontaler Abstand zwischen den Bäumen (Standard: 30)
# - versatz_y: Vertikaler Abstand zwischen den Bäumen (Standard: -30)
# - color: Farbe der Baumkronen (Standard: grün)
def baum_reihe(anzahl, versatz_x=30, versatz_y=-30, color="green"):
    speed(0)
    for i in range(anzahl):
        x, y = pos()
        baum(120, 25, farbe=color)
        penup()
        goto(x + versatz_x, y + versatz_y)
        pendown()


# Funktion zum Zeichnen einer Reihe von Blumen
# Parameter:
# - anzahl: Anzahl der zu zeichnenden Blumen (Standard: 3)
# - versatz_x: Horizontaler Abstand zwischen den Blumen (Standard: -20)
# - versatz_y: Vertikaler Abstand zwischen den Blumen (Standard: -20)
# - farbe_blueten: Farbe der Blütenblätter (Standard: pink)
# - farbe_mitte: Farbe der Blütenmitte (Standard: gelb)
def blumen_reihe(
    anzahl=3, versatz_x=-20, versatz_y=-20, farbe_blueten="pink", farbe_mitte="yellow"
):
    speed(0)
    for i in range(3):
        x, y = pos()
        blume(farbe_blueten=farbe_blueten, farbe_mitte=farbe_mitte)
        penup()
        goto(x + versatz_x, y + versatz_y)
        pendown()
