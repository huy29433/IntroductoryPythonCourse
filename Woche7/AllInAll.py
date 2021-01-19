import random

attributes = ["Leben", "Starke", "Intelligenz","Geschwindigkeit", "Charisma"]
ListePrufungen = []
ListeItems = []
MaxProgress = 5

def checkPrufung(Spielfig, Kategorie, Kosten):
    result = 0
    for i in range(Spielfig.attributes[Kategorie]):
        result += random.randint(0, 6)

    for item in Spielfig.bag:
        if item.Kategorie == Kategorie:
            result += item.Bonus

    if result >= Kosten:
        return True
    else:
        return False

class Spielfigur:
    def __init__(self, name):
        self.name = name

        self.attributes = dict()
        for att in attributes:
            self.attributes[att] = random.randint(3, 6)      # Jeder Spieler erhält einen eigenen Charakter

        self.bag = []
        self.bagsize = 5        # Eig auch als Klassenattribut verwendbar
                                # Gedankengang: Items die Rucksack erweitern hier möglich

        self.progress = 0
        self.mustWait = False

    def __str__(self):
        string = f"Name: \t {self.name} \n "
        for att in self.attributes:
            string += f"{att}: \t {self.attributes[att]} \n"
        string += f"Progress: \t {self.progress}\n"

        string += f"Im Rucksack: \n"
        for item in self.bag:
            string += f"{item}"

        return string

    def doPrufung(self, Prufung):
        if self.mustWait:
            self.mustWait = False
            return "Aussetzen"
        retValue = "Normal"
        print(f"Wollen Sie Folgende Prufung ablegen? \n {Prufung.Frage}")
        if input("y/n: ") == "y":
            if checkPrufung(self, Prufung.AufgabeJaKategorie, Prufung.AufgabeJaKosten):
                self.addItem(ListeItems[random.randint(0, len(ListeItems)-1)])
                self.progress += 2
                if self.progress >= MaxProgress:      # Als Funktion einbauen, Wiederholung!
                    print("Finished")
                    retValue = "Finished"
                else:
                    self.attributes["Leben"] -= 1
                    print(f"{self.name} wurde verletzt. HP ubrig: {self.attributes['Leben']}")
                    if self.attributes["Leben"] <= 0:
                        print("Charakter died")
                        retValue = "Died"
        else:
            if Prufung.AufgabeNeinKategorie == "Aussetzen":
                self.mustWait = True
                print(f"{self.name} muss aussetzen.")
            else:
                if checkPrufung(self, Prufung.AufgabeNeinKategorie, Prufung.AufgabeNeinKosten):
                    self.progress += 1
                    print(f"Nothing happened to {self.name}")
                    if self.progress >= MaxProgress:      # Als Funktion einbauen!
                        print("Finished")
                        retValue = "Finished"
                else:
                    self.mustWait = True #Hier evtl noch Leben abziehen?
                    print(f"{self.name} muss aussetzen.")
        return retValue

    def addItem(self, item):
        if len(self.bag) > self.bagsize:
            print("Rucksack voll")
        else:
            self.bag.append(item)
            print(f"{item} erhalten")


class Prufung:
    def __init__(
            self,
            Frage,
            TextJa,
            TextNein,
            AufgabeJaKategorie,
            AufgabeJaKosten,
            AufgabeNeinKategorie,
            AufgabeNeinKosten
    ):
        self.Frage = Frage
        self.TextJa = TextJa
        self.TextNein = TextNein
        self.AufgabeJaKategorie = AufgabeJaKategorie
        self.AufgabeJaKosten = AufgabeJaKosten
        self.AufgabeNeinKategorie = AufgabeNeinKategorie
        self.AufgabeNeinKosten = AufgabeNeinKosten


class Item:
    def __init__(self, Name, Kategorie, Bonus):
        self.Name = Name
        self.Kategorie = Kategorie
        self.Bonus = Bonus

    def __str__(self):
        return f"{self.Name} \t( {self.Kategorie} \t {self.Bonus} )"


def main():
    ListePrufungen.append(Prufung(
        "Text1",
        "Text1Ja",
        "Text1Nein",
        attributes[2],
        5,
        "Aussetzen",
        0
    ))
    ListePrufungen.append(Prufung(
        "Text2",
        "Text2Ja",
        "Text2Nein",
        attributes[4],
        2,
        "Aussetzen",
        0
    ))
    ListePrufungen.append(Prufung(
        "Text3",
        "Text3Ja",
        "Text3Nein",
        attributes[3],
        4,
        "Aussetzen",
        0
    ))

    ListeItems.append(
        Item("Item1", attributes[1], 4)
    )
    ListeItems.append(
        Item("Item2", attributes[2], 3)
    )
    ListeItems.append(
        Item("Item3", attributes[3], -5)
    )


    spieler = []
    spieler.append(Spielfigur("Dominik"))
    spieler.append(Spielfigur("Kinimod"))


    print(spieler[0])
    print("###")
    print(spieler[1])
    activePlayer = 0

    def aussetzen(name):
        print(f"{name} muss aussetzen")

    def normal(name):
        pass

    def finished(name):
        print(f"{name} has won")
        quit()

    def died(name):
        print(f"{name} has died")
        quit()

    ownSwitcher = {
        "Aussetzen": aussetzen,
        "Normal": normal,
        "Finished": finished,
        "Died": died
    }

    while True:
        print(f"{spieler[activePlayer].name} ist dran. \n Fortschritt: {spieler[activePlayer].progress} / {MaxProgress}")
        ownSwitcher[spieler[activePlayer].doPrufung(ListePrufungen[random.randint(0, len(ListePrufungen)-1)])](spieler[activePlayer].name)

        activePlayer += 1
        activePlayer = activePlayer % len(spieler)


if __name__ == "__main__":
    main()

# TODO: Finished Message wird von nächster Prüfung überdeckt
# aktiver Spieler muss angezeigt werden:
# Aussetzen anders einbauen, nicht erst in DoPrufung!
