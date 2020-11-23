def main():
    matrix = []
    matrix.append([1,2,3])
    matrix.append([4,5,6])
    matrix.append([7,8,9])

    for line in matrix:
        for elem in line:
            print(f"{elem:^5} ", end='')
        print("")

    # mit 3 print Befehlen:
    print("###")
    print("Mit 3 Befehlen")
    print(f"{matrix[0][0]:^5} {matrix[0][1]:^5} {matrix[0][2]:^5}")
    print(f"{matrix[1][0]:^5} {matrix[1][1]:^5} {matrix[1][2]:^5}")
    print(f"{matrix[2][0]:^5} {matrix[2][1]:^5} {matrix[2][2]:^5}")
    print("###")

    matrix[1] = [10,11,12]  # Ändern einer Zeile
    matrix[0][0] = 13       # Ändern einer Zahl

    print()
    for line in matrix:
        for elem in line:
            print(f"{elem:^5} ", end='')
        print("")


if __name__ == "__main__":
    main()
