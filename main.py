from gebäude import haus, tür
from natur import *

speed(0)


# haus
penup()
goto(-400, 0)

haus(200, 300, "pale goldenrod", "black")

penup()
goto(-200, -50)
pendown()

haus(150, 200, "green", "red")

penup()
goto(100, -50)
pendown()

# bäume

x, y = pos()
baum_reihe(3)
penup()
goto(x - 60, y)
pendown()
x, y = pos()
baum_reihe(3, color="dark green")
penup()
goto(x - 60, y)
pendown()
baum_reihe(3, color="sea green")

# blumen
x, y = pos()
blumen_reihe()
penup()
goto(x + 20, y)
pendown()
blumen_reihe(farbe_mitte="blue")
penup()
goto(x + 40, y)
pendown()
blumen_reihe(farbe_mitte="red")


exitonclick()
