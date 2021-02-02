import csv
import matplotlib.pyplot as plt


class Spectroscopy:
    def __init__(self, file=None):
        self.plotReady = False
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot()

        self.wavenumbers = []
        self.intensities = []

        self.title = ""

        self.minima = dict()

        if file is not None:
            self.loadFile(file)

    def loadFile(self, file):
        self.plotReady = False
        with open(file, newline='') as f:
            csvFile = csv.reader(f, delimiter=' ')
            for i in csvFile:
                if i[0][:7] == "##TITLE":
                    self.title = i[0].split("=")[1]
                elif i[0][:6] == "##END=":
                    break
                elif i[0][:2] == "##":
                    continue
                else:
                    self.wavenumbers.append(float(i[0]))
                    self.intensities.append(float(i[1]))  # TODO: Teilen durch größten Wert der Spalte oder Reihe?
        for id, int in enumerate(self.intensities):
            self.intensities[id] = int / max(self.intensities)

    def preparePlots(self):
        plt.xlim(max(self.wavenumbers), min(self.wavenumbers))


        self.ax.set_title(self.title)
        plt.xlabel("wavenumber / cm^-1")
        plt.ylabel("Intensity / 1")

        self.ax.plot(self.wavenumbers, self.intensities)

        self.findMinima2()
        self.plotMinima()
        self.plotReady = True

    def show(self):
        if not self.plotReady:
            self.preparePlots()
        plt.show()

    def findMinima2(self, genauigkeit = 5):
        # TODO: Noch nicht ganz korrekt, findet erstes Minima nicht größte
        
        val_before = 0
        for id, intensity in enumerate(self.intensities):
            if id > len(self.intensities) - genauigkeit:
                break
            for i in range(id, id+genauigkeit):
                val_before = self.intensities[i-genauigkeit]
                val_actual = self.intensities[i]

                # Linda: ab hier bis 77 sollte glaube ich auch eingerückt sein
                
            if val_actual > val_before and dir == -1:
                self.minima[self.wavenumbers[id-genauigkeit//2]] = self.intensities[id-genauigkeit//2]
                print(self.wavenumbers[id-genauigkeit//2])
                dir = 1
            elif val_actual < val_before:
                dir = -1
            else:
                dir = 0

    def findMinima(self):
        # Glätten möglich -> z.B. Savitzky-Golay aus Scipy-Modul für Spektren.

        # TODO: Wie Minima richtig finden?
        # Meine Methode findet falsche Position ...

        skip = 0
        for id, (intensity) in enumerate(self.intensities):
            genauigkeit = 3
            if skip >= 0:
                skip -= 1
                continue
            if (id < genauigkeit):
                continue
            if id >= len(self.intensities)-(2*genauigkeit):
                continue

            int_before = 0
            int_actual = 0
            int_after = 0
            for i in range(id, id+genauigkeit):
                int_before += self.intensities[i-genauigkeit]/genauigkeit
                int_actual += self.intensities[i]/genauigkeit
                int_after += self.intensities[i+genauigkeit]/genauigkeit

            if int_actual < int_before and int_actual < int_after:
                self.minima[self.wavenumbers[int(id+genauigkeit/2)]] = intensity
                skip = genauigkeit


    def plotMinima(self):
        for minima in self.minima:
           self.ax.arrow(minima+1, self.minima[minima]-0.2, -1, 0.2, shape='full')


def main():
    #caffeine = Spectroscopy("caffeine.jdx")
    #caffeine.show()

    ethanol = Spectroscopy("ethanol.jdx")
    ethanol.show()


if __name__ == "__main__":
    main()
