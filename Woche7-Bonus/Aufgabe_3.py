# Pi nach Monte Carlo berechnen
import random


def piNachMonteCarlo(N = 100):
    radiusOfCircle = 1
    counterPairsInCircle = 0
    for i in range(N):
        x_coord = random.uniform(0, radiusOfCircle)
        y_coord = random.uniform(0, radiusOfCircle)

        if (x_coord**2 + y_coord**2) < radiusOfCircle:
            counterPairsInCircle += 1

    return counterPairsInCircle/N*4


def main():
    print(piNachMonteCarlo())
    print(piNachMonteCarlo(100000))


if __name__ == "__main__":
    main()
