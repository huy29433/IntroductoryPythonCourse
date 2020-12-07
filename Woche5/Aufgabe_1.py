def quersumme_2(number):
    pass


def quersumme(number):
    if number < 0:
        number *= -1
    return_value = 0
    while number != 0:
        return_value += number % 10
        number = number // 10       # Ganzzahl-division

    return return_value


def main():
    print(f"Quersumme ist: {quersumme(int(input('Zu berechnende Zahl: ')))}")


if __name__ == "__main__":
    main()
