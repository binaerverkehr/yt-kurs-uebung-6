from geometrie import *


def haus(laenge, breite, basisfarbe, dachfarbe):
    rechteck(laenge, breite, basisfarbe)
    left(90)
    forward(laenge)
    right(90)

    dreieck(laenge, dachfarbe)


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