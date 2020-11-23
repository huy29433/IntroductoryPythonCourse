def main():
    string = "My Hovercraft is full of eels"
    new_string = string.replace(" ", "")[1::2]  # Annahme: Leerzeichen zählen nicht als Buchstaben
    # new_string = string[1::2]   # Sonst so
    print(new_string)


if __name__ == "__main__":
    main()
