import perf

from copy import deepcopy
from rich import print


@perf.measure  # $O(n^2$)
def sort_bubble(arr: list) -> list:
    while True:
        did_swap = False

        for i, _ in enumerate(arr):
            if i == len(arr) - 1:
                continue

            if arr[i] > arr[i + 1]:
                perf.expensive_op()
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                did_swap = True

        if not did_swap:
            break


@perf.measure  # $O(n^2)$
def sort_selection(arr: list):
    for shift in range(len(arr) - 1):
        idx_smallest = shift

        for i in range(shift + 1, len(arr)):
            if arr[i] < arr[idx_smallest]:
                idx_smallest = i

        if idx_smallest != shift:
            perf.expensive_op()
            arr[shift], arr[idx_smallest] = arr[idx_smallest], arr[shift]


@perf.measure  # $ O(n^2) \text{\quad Best case: } O(n)$
def sort_insert(arr: list):
    for i in range(1, len(arr) - 1):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            perf.expensive_op()
            arr[j + 1] = arr[j]
            j -= 1

        perf.expensive_op()
        arr[j + 1] = key


def main():
    sort_func = sort_insert  # ? Change as needed.

    v = [0, 6, 9, 1, 3, 3, 7]
    v_orig = deepcopy(v)
    sort_func(v)
    assert v == sorted(v_orig), "Did not sort correctly!"
    print(v)


if __name__ == "__main__":
    main()
