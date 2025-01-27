from geometrie import *


def haus(hoehe, breite, basisfarbe, dachfarbe):
    rechteck(hoehe, breite, basisfarbe)
    left(90)
    forward(hoehe)
    right(90)

    dreieck(breite, dachfarbe)


speed(0)

penup()
goto(50, 0)
pendown()

haus(200, 300, "black", "pink")

penup()
goto(-250,0)
pendown()


haus(150, 50, "green", "red")


exitonclick()