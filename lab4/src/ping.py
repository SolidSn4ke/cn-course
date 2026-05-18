from matplotlib import pyplot as plt
from math import ceil


def main():
    x = [100, 200, 500, 1000, 2500, 5000, 10000, 20000, 30000]
    y = list(map(lambda e: ceil(e / 1500), x))

    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    main()
