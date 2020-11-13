def ist_schaltjahr(year):
    schaltjahr = False

    if year % 4 == 0 and year % 100 == 0:
        schaltjahr = True
    elif year % 100 == 0 or year % 4 != 0:
        schaltjahr = False
    elif year % 4 == 0:
        schaltjahr = True
    else:
        schaltjahr = False

        return schaltjahr

