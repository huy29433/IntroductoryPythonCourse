def main():
    with open("praktische_Physik.txt") as f:
        lines = f.readlines()

  #  file = open("praktische_Physik.txt")
   # lines = file.readlines()
    #file.close()

    countLetters = 0
    countWords = 0
    countLines = len(lines) # Leere Zeilen werden mitgelesen

    for line in lines:
        countWords += len(line.split(" "))
        countLetters += len(line)

    print(f"Letters: {countLetters}")
    print(f"Words: {countWords}")
    print(f"Lines: {countLines}")


if __name__ == "__main__":
    main()
