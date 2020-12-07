def main():
    ### 0x2800  # 0x2801 # 0x2802 ## 0x2803 #
    ### 2       #   3    #    3   #   2    #
    ### x_main  # y_main #        #        #
    ### ------  # -----  # x_func # y_func #

    def swap(x_func, y_func):
        temp = x_func;
        x_func = y_func;              # Aus C Kurs kopiert? -> ";"
        y_func = temp;

    # Driver code
    x_main = 2       # Adresse gespeichert, immutable object -> int(eger)
    y_main = 3
    swap(x_main, y_main)
    print(x_main)
    print(y_main)


if __name__ == "__main__":
    main()
