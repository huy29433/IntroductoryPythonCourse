def integrate(func, start, stop, N):
    steps = (stop - start) / N
    area = 0
    for i in range(N):
        y_left = func(i*steps+start)
        y_right = func((i*2*steps+start))

        area += min(y_right, y_left) * steps
    return area


def integrator(func, precision = 100, start = 0):
    return lambda x: integrate(func = func, stop = x, start = start, N = precision)

def main():
    func_test = lambda x: x
    print(func_test(1))
    print(func_test(2))

    print(integrator(func_test))
    print(integrator(func_test, precision= 100000)(2))


if __name__ == "__main__":
    main()
