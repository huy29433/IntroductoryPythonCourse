def integrator(func):
    def integrate(stop, N = 100, start = 0):
        steps = (stop - start) / N
        area = 0
        for i in range(N):
            y_left = func(i * steps + start)
            y_right = func((i * 2 * steps + start))

            area += min(y_right, y_left) * steps
        return area

    return integrate


def main():
    integral = integrator(lambda x : x)
    print(integral(2, 500))


if __name__ == "__main__":
    main()
