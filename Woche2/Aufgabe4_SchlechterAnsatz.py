year = int(input("Geben Sie ein Jahr ein, zur Ueberpruefung, ob Schaltjahr"))

#

if year % 400:
    print(f"{year} ist ein Schaltjahr")
elif year % 100:
    print(f"{year} ist kein Schaltjahr")
elif year % 4:
    print(f"{year} ist ein Schaltjahr")
else:
    print(f"{year} ist kein Schaltjahr")

# Hier ist Redundanz vorhanden

# aber keine allzu schlimme. Geht aber tatsächlich kürzer, siehe andere Version.
