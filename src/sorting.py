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

            # Swap if current one bigger than right neighbor
            if arr[i] > arr[i + 1]:
                perf.expensive_op()
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                did_swap = True

        if not did_swap:
            break


@perf.measure  # $O(n^2)$
def sort_selection(arr: list) -> list:
    for shift in range(len(arr) - 1):
        idx_smallest = shift

        for i in range(shift + 1, len(arr)):
            if arr[i] < arr[idx_smallest]:
                idx_smallest = i

        if idx_smallest != shift:
            perf.expensive_op()
            arr[shift], arr[idx_smallest] = arr[idx_smallest], arr[shift]


@perf.measure  # $ O(n^2) \text{\quad Best case: } O(n)$
def sort_insert(arr: list) -> list:
    for i in range(1, len(arr)):
        curr = arr[i]

        # i's left neighbor
        left = i - 1

        # while in bounds && left value greater than current
        while left >= 0 and arr[left] > curr:
            perf.expensive_op()
            # set right neighbor of left to value of left
            arr[left + 1] = arr[left]
            # print(f"[{left + 1}] = {arr[left]}")

            # move one step left
            left -= 1

        # set right neighbor to current val
        arr[left + 1] = curr

    return arr


def _merge(left: list, right: list) -> list:
    sorted_list = []

    i = j = 0

    while i < len(left) and j < len(right):
        perf.expensive_op()

        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


@perf.measure
def sort_merge(arr: list) -> list:
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    left_half = sort_merge(arr[:mid])
    right_half = sort_merge(arr[mid:])

    return _merge(left_half, right_half)


@perf.measure
def sort_heap(arr: list) -> list:
    pass


@perf.measure
def sort_quick(arr: list) -> list:
    pass


@perf.measure
def sort_radix(arr: list) -> list:
    pass


def main():
    for func in [sort_merge]:
        v = [0, 6, 9, 1, 3, 3, 7]
        v_orig = deepcopy(v)

        out = func(v)
        v_new = out or v

        print(
            f"[bold blue]{func.__name__}():[/bold blue] - {'In Place' if out is None else 'NOT In Place'}"
        )
        print(v_new)

        assert v_new == sorted(v_orig), "Did not sort correctly!"


if __name__ == "__main__":
    main()
