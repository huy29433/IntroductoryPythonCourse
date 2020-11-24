def main():

    # Inhalt:   # ----  # ----  # ----  # ----  # ----  # ----  #
    # Adresse:  # 0x00  # 0x01  # 0x02  # 0x03  # 0x04  # 0x05  #
    #
    #
    A = []              # A enthält Adresse (z.B. 0x01)
    # Inhalt:   # ----  # []  # ----  # ----  # ----  # ----  #
    # Adresse:  # 0x00  # 0x01  # 0x02  # 0x03  # 0x04  # 0x05  #
    A.append(A)         # Der Liste wird Adresse von A angehängt

    # Inhalt:   # ----  #[0x01] # ----  # ----  # ----  # ----  #
    # Adresse:  # 0x00  # 0x01  # 0x02  # 0x03  # 0x04  # 0x05  #

    print(A)            # Auflösung der Elemente klappt nicht, da immer wieder auf Adresse 0x01 geschaut wird
    print(len(A))       # Die Liste ist aber immer noch nur 1 Element lang, da die Liste eine (besser gesagt: sich
                        # selbst als) Liste (usw.) enthält
    print(len(A[0]))    # Auch das erste Element der Liste A ist nur 1 lang, da diese auch wiederum eine Liste einer
                        # Liste (...) enthält
    print(len(A[0][0])) # Auch das erste Element der Liste A ist nur 1 lang, da diese auch wiederum eine Liste einer
                        # Liste (...) enthält

    A[0][0] = 1         # Gehe in Element 0 der Adresse 0x01 (->0x01), gehe auch dort in Element 0 (->0x01)
                        # Setze dieses Element auf 1
            # Inhalt:   # ----  #  [1]  # ----  # ----  # ----  # ----  #
    # Adresse:  # 0x00  # 0x01  # 0x02  # 0x03  # 0x04  # 0x05  #
    print(A)            # Referenzierung auf sich selbst gelöst, nur noch 1 in Liste enthalten


if __name__ == "__main__":
    main()
