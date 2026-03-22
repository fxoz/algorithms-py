import perf


@perf.measure
def fib_iter(n: int) -> int:
    prev = prev_prev = 1

    res = 1
    for i in range(2, n - 1):
        perf.expensive_op()

        res += prev + prev_prev
        prev_prev = prev
        prev = res

    return res


@perf.measure  # $\mathcal{O}(2^n)$
def fib_recu(n: int) -> int:
    perf.expensive_op()

    if n < 3:
        return 1

    return fib_recu(n - 1) + fib_recu(n - 2)


def main():
    print(fib_iter(int(input("-> "))))


if __name__ == "__main__":
    main()
