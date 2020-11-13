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


year = int(input("Jahr: "))

result_string = f"Das Jahr {year} ist "

if not ist_schaltjahr(year):
    result_string += "k"

result_string += "ein Schaltjahr"
print(result_string)
