# Sieb des Erathostenenes
# Keine sehr elegante Lösung, aber funktioniert

import datetime


def main():
    start = datetime.datetime.now()     # Evtl eine Möglichkeit, die notwendige Zeit zu bestimmen. Kann aber vmtl ignoriert werden.
    numberList = [1 for i in range(0, 10000000)]

    for i in range(int(len(numberList)**0.5)):      # Theoretisch muss man nur
                                                    # bis sqrt(N) gehen, oder?
        if i < 2:
            numberList[i] = 0
            continue
        elif numberList[i] == 0:
            continue
        else:
            for j in range(0, len(numberList), i):
                if j <= i:
                    continue
                numberList[j] = 0

    print(datetime.datetime.now()-start)        # 10.000.000 : Etwa 4 Sekunden
    #print(numberList)

    for i in range(len(numberList)):
       if numberList[i]:
            print(i)


if __name__ == "__main__":
    main()
