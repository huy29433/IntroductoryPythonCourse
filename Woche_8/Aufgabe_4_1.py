import csv


def main():
    gameScores = dict()
    with open("gameScores.txt") as f:
        csvFile = csv.reader(f)
        names = next(csvFile)   # Liest erste Zeile aus -> Namen für Dictionary

        for name in names:
            gameScores[name] = 0

        for line in csvFile:
            for index, score in enumerate(line):
                gameScores[names[index]] += int(score)

    for key in gameScores:
        print(f"{key} hat {gameScores[key]} Punkte")


if __name__ == "__main__":
    main()
