def main():
    file = open("praktische_Physik.txt", 'rb')
    file.readlines() # seek(0, 2)
    print(f"Size is {file.tell()} Bytes")
    file.close()


if __name__ == "__main__":
    main()
