def main():
    string = "Legen Sie eine String-Variable an. Bestimmen Sie, welches" \
             " Schriftzeichen jeweils wie oft in diesem Text vorkommt."

    # string = string.lower()
    unique_letters = set(string)        # Berücksichtigt Groß-/Kleinschreibung, falls vorherige Zeile kommentiert

    print(unique_letters)

    count_of_letters = dict()
    for letter in unique_letters:
        count_of_letters[letter] = 0

    for letter in string:
        count_of_letters[letter] += 1

    for letter in sorted(count_of_letters):
        print(f"'{letter}'{count_of_letters[letter]:5}")


if __name__ == "__main__":
    main()
