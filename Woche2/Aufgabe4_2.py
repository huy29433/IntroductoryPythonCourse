def ist_schaltjahr(year):
    schaltjahr = False
    if year % 4 == 0:
        if year % 400 == 0:
            schaltjahr = True
        elif year % 100 == 0:
            schaltjahr = False
        else:
            schaltjahr = True
#    else:                      # Der besseren Lesbarkeit halber würde ich diese Zeilen hinzuschreiben
#         schaltjahr = False    # Funktionstechnisch sind sie aber überflüssig -> Was ist zu empfehlen?
    return schaltjahr

# Die Lesbarkeit ist hier auf jeden Fall auch noch ohne die Zeilen gegeben.
# Leicht effizienter ist erst Teilbarkeit durch 400, dann 100, dann 4 zu prüfen (weil die eine jeweils die nächste impliziert)
# und am lesbarsten insgesamt mit and und or:

if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    return True
else:
    return False

# die Funktion gibt dir im Falle einer großen Verschachtelung einen Lesbarkeitsvorteil, mit der and/or Lösung brauchst du diesen nicht
# und musst damit keinen Speicherplatz auf die Funktion verschwenden.

year = int(input("Jahr: "))

result_string = f"Das Jahr {year} ist "

if not ist_schaltjahr(year):
    result_string += "k"

result_string += "ein Schaltjahr"
print(result_string)
