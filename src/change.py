# German: Wechselgeldproblem

import perf
from rich import print

pieces = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]
pieces.reverse()


@perf.measure  # $\mathcal{O}(n)$ with $n$ being the number of pieces
def change(inp: float) -> dict[int, int]:
    remainder = inp * 100
    res = {}
    for value in pieces:
        perf.expensive_op()
        if value <= remainder:
            mult = remainder // value
            res[value] = int(mult)
            remainder -= value * mult

    return res


def main():
    inp = float(input("-> Input EUR float: "))
    print("> Output pcs: ")
    print(change(inp))

    for piece in pieces:
        pass


if __name__ == "__main__":
    main()
