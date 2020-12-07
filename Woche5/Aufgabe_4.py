def nFach_for(f, count, x):
    value = None
    for i in range(count):
        if value == None:
            value = f(x)
        else:
            value = f(value)
    return value


def nFach_for2(f, count, x):
    value = x
    for i in range(count):
        value = f(value)
    return value


def nFach(f, count, x):
    count = count - 1
    if count == 0:
        return f(x)
    else:
        return f(nFach(f, count, x))


def main():
    f = lambda x: x + 1
    g = lambda x: 2 * x

    print(f"nFach: {nFach(f, 3, 0)}")
    print(f"nFach: {nFach(g, 3, 2)}")

    print(f"nFach: {nFach_for(f, 3, 0)}")
    print(f"nFach: {nFach_for(g, 3, 2)}")

    print(f"nFach: {nFach_for2(f, 3, 0)}")
    print(f"nFach: {nFach_for2(g, 3, 2)}")


if __name__ == "__main__":
    main()
