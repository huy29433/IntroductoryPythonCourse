def main():
    hoehe = 20

    for i  in range(hoehe):
        count_of_stars = 1 + i * 2
        count_of_spaces = hoehe - i - 1
        print(count_of_spaces*" "+count_of_stars*"*")


if __name__ == "__main__":
    main()
