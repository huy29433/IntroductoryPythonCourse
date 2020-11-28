def main():
    vector_a = [3, 2, 1, 5, 7, 2, -1]
    vector_b = [-7, 3, 7, 5, 6, 8, 1]

    Skalarprodukt = 0
    for a,b in zip(vector_a, vector_b):
        Skalarprodukt += a*b

    print(Skalarprodukt)


if __name__ == "__main__":
    main()
