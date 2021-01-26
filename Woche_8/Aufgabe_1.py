class defaultDict(dict):
    def __init__(self, defValue):
        self.defValue = defValue

    def __getitem__(self, item):
    #    if item in self.keys():
      #      return super().__getitem__(item)
       # else:
     #       return self.defValue
        try:            # if auch möglich
            return super().__getitem__(item)
        except KeyError:
            self[item] = self.defValue
            return self[item]


def main():
    dd = defaultDict("def Value")
    print(dd["a"])
    dd["Key2"] = "abc"
    print(dd["Key2"])


if __name__ == "__main__":
    main()