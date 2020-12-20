def fizzBuzzGame(dictionaryList,  end):
    returnList = []
    for number in range(1, end):
        string = ""
        for i in dictionaryList:
            if number % i == 0:
                string += dictionaryList[i]
        if string != "":
            returnList.append(string)
        else:
            returnList.append(number)
    return returnList


def main():
    # FizzBuzz
    gameDict = {
        3: "Fizz",
        5: "Buzz"
    }
    for i in fizzBuzzGame(gameDict, 100):
        print(i)


if __name__ == "__main__":
    main()
