import math


def integrate(func, start, stop, N):
    rangeOfIntegral = stop - start;
    stepWidth = rangeOfIntegral / N
    areaOfIntegral = 0
    xValue = start
    while xValue <= stop:
        areaOfIntegral += func(xValue) * stepWidth
        xValue += stepWidth
    return areaOfIntegral


def main():
    print(integrate(math.exp, 0, 1, 10000))


if __name__ == "__main__":
    main()
