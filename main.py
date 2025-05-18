# Importiere die benötigten Funktionen aus den Modulen
from gebäude import haus, tür
from natur import *

# Setze die Zeichengeschwindigkeit auf Maximum für schnelleres Rendering
speed(0)

# Zeichne zwei Häuser mit unterschiedlichen Größen und Farben
# Erstes Haus: Groß, beige mit schwarzem Dach
penup()  # Hebe den Stift an
goto(-400, 0)  # Gehe zur Position für das erste Haus

haus(200, 300, "pale goldenrod", "black")  # Zeichne großes Haus

penup()  # Hebe den Stift an
goto(-200, -50)  # Gehe zur Position für das zweite Haus
pendown()  # Setze den Stift ab

haus(150, 200, "green", "red")  # Zeichne kleineres Haus

penup()  # Hebe den Stift an
goto(100, -50)  # Gehe zur Position für die Bäume
pendown()  # Setze den Stift ab

# Zeichne drei Baumreihen mit unterschiedlichen Grüntönen

x, y = pos()  # Speichere aktuelle Position
baum_reihe(3)  # Erste Baumreihe mit Standardgrün
penup()
goto(x - 60, y)  # Gehe zur Position für die zweite Baumreihe
pendown()
x, y = pos()
baum_reihe(3, color="dark green")  # Zweite Baumreihe in Dunkelgrün
penup()
goto(x - 60, y)  # Gehe zur Position für die dritte Baumreihe
pendown()
baum_reihe(3, color="sea green")  # Dritte Baumreihe in Meeresgrün

# Zeichne drei Blumenreihen mit unterschiedlichen Farben
x, y = pos()  # Speichere aktuelle Position
blumen_reihe()  # Erste Blumenreihe mit Standardfarben
penup()
goto(x + 20, y)  # Gehe zur Position für die zweite Blumenreihe
pendown()
blumen_reihe(farbe_mitte="blue")  # Zweite Blumenreihe mit blauer Mitte
penup()
goto(x + 40, y)  # Gehe zur Position für die dritte Blumenreihe
pendown()
blumen_reihe(farbe_mitte="red")  # Dritte Blumenreihe mit roter Mitte

# Warte auf Mausklick zum Beenden
exitonclick()
