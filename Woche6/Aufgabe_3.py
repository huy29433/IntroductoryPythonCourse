# Lambda - Funktion verwenden

def main():
    data = [(7, 3), (5, 5), (8, 2), (9, 1), (6, 4)]

    data.sort(key = lambda element: (element[0]**2 + element[1]**2)**0.5)
    print(data)


if __name__ == "__main__":
    main()
