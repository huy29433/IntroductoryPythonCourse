def main():
    A = []
    A.append(A)
    A.append(2)

    print(A)
    print(len(A))
    print(len(A[0]))
    print(len(A[0][0]))

    A[0][0] = 1
    print(A)


if __name__ == "__main__":
    main()
