import matplotlib.pyplot as plt
import numpy as np
from enum import Enum

sign = lambda x: (1 if x > 0 else -1 if x < 0 else 0)

letter_to_bin = {"к": 0b11001010, "а": 0b11000000}


class EncodingMethod(Enum):
    RZ = "rz"
    NRZ = "nrz"
    AMI = "ami"
    MANCHESTER = "manchester"


def gen(method: EncodingMethod, data: bytes):
    if method == EncodingMethod.RZ:
        return gen_rz(data)
    elif method == EncodingMethod.NRZ:
        return gen_nrz(data)
    elif method == EncodingMethod.AMI:
        return gen_ami(data)
    elif method == EncodingMethod.MANCHESTER:
        return gen_manchester(data)
    else:
        raise ValueError("Unknown encoding method")


def gen_nrz(data: str):
    n = 0

    for i in range(len(data)):
        bit = int(data[i])

        color = "blue" if bit == 1 else "red"

        plt.plot([n, n + 1], [bit, bit], color=color, linewidth=2)

        if i + 1 < len(data):
            next_bit = int(data[i + 1])

            if bit != next_bit:
                plt.plot([n + 1, n + 1], [bit, next_bit], color="black", linewidth=2)

        n += 1

    plt.ylim(-0.5, 1.5)
    plt.xlim(0, len(data))
    plt.yticks([0, 1], ["0", "1"])
    plt.grid(axis="x", linestyle="--", alpha=0.4)

    for x in range(len(data) + 1):
        plt.axvline(x, linestyle="--", color="gray", linewidth=0.8, alpha=0.5)

    plt.show()


def gen_rz(data: str):
    n = 0

    for i in range(len(data)):
        bit = 1 if int(data[i]) == 1 else -1

        color = "blue" if bit == 1 else "red"

        plt.plot([n, n + 0.5], [bit, bit], color=color, linewidth=2)
        plt.plot([n + 0.5, n + 0.5], [bit, 0], color="black", linewidth=2)
        plt.plot([n + 0.5, n + 1], [0, 0], color="black", linewidth=2)

        if i + 1 < len(data):
            next_bit = 1 if int(data[i + 1]) == 1 else -1
            plt.plot([n + 1, n + 1], [0, next_bit], color="black", linewidth=2)
        n += 1

    plt.ylim(-1.5, 1.5)
    plt.xlim(0, len(data))
    plt.yticks([0, 1], ["0", "1"])
    plt.grid(axis="x", linestyle="--", alpha=0.4)

    for x in range(len(data) + 1):
        plt.axvline(x, linestyle="--", color="gray", linewidth=0.8, alpha=0.5)

    plt.show()


def gen_ami(data: str):
    n = 0
    prev = -1

    for i in range(len(data)):
        bit = -sign(prev) * int(data[i])

        color = "blue" if abs(bit) == 1 else "red"

        plt.plot([n, n + 1], [bit, bit], color=color, linewidth=2)

        if i + 1 < len(data):
            prev = bit if bit != 0 else prev
            next_bit = -sign(prev) * int(data[i + 1])

            plt.plot([n + 1, n + 1], [bit, next_bit], color="black", linewidth=2)
        n += 1

    plt.ylim(-1.5, 1.5)
    plt.xlim(0, len(data))
    plt.yticks([-1, 0, 1], ["-1", "0", "1"])
    plt.grid(axis="x", linestyle="--", alpha=0.4)

    for x in range(len(data) + 1):
        plt.axvline(x, linestyle="--", color="gray", linewidth=0.8, alpha=0.5)

    plt.show()


def gen_manchester(data: str):
    def invert(bit):
        return 1 - bit

    n = 0

    for i in range(len(data)):
        bit = int(data[i])

        color = "blue" if bit == 1 else "red"

        plt.plot([n, n + 0.5], [bit, bit], color="black", linewidth=2)
        plt.plot([n + 0.5, n + 0.5], [bit, invert(bit)], color=color, linewidth=2)
        plt.plot(
            [n + 0.5, n + 1], [invert(bit), invert(bit)], color="black", linewidth=2
        )

        if i + 1 < len(data):
            next_bit = int(data[i + 1])

            if bit == next_bit:
                plt.plot(
                    [n + 1, n + 1], [invert(bit), next_bit], color="black", linewidth=2
                )
        n += 1

    plt.ylim(-0.5, 1.5)
    plt.xlim(0, len(data))
    plt.yticks([0, 1], ["0", "1"])
    plt.grid(axis="x", linestyle="--", alpha=0.4)

    for x in range(len(data) + 1):
        plt.axvline(x, linestyle="--", color="gray", linewidth=0.8, alpha=0.5)

    plt.show()


def main():
    msg = "каа"
    data = "".join([f"{letter_to_bin[c]:08b}" for c in msg])
    # data = "110011010011001100111111"
    gen(EncodingMethod.MANCHESTER, data)


if __name__ == "__main__":
    main()
