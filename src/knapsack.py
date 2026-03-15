from dataclasses import dataclass
from typing import Optional

import perf

from rich import print


@dataclass
class Item:
    value: int
    weight: int
    id_: Optional[int] = -1


# might be useful for debugging
def _assign_ids(items: list[Item], starting_from=0):
    for i, item in enumerate(items):
        items[i].id_ = i + starting_from


@perf.measure
def knapsack_solve(items: list[Item], capacity: int):
    # outer lists = rows in this visualization https://youtu.be/cJ21moQpofY?t=363
    # first set of item states is 0 for empty
    states = [[0 for _ in range(capacity + 1)]]

    # the first row is full of zeros, so let's start with 1 using enumerate(items, 1)
    for i, item in enumerate(items, 1):
        # one could optimize this by using $\min(w)$ as a starting point instead
        states_item = []

        for cap in range(capacity + 1):
            perf.expensive_op()

            current_cell_value = 0
            if item.weight <= cap:
                current_cell_value = item.value

            # Backtracking: one up, own weight steps to the left; only possible if cap > item.weight
            backtracked_cell_value = 0
            if cap > item.weight:
                backtracked_cell_value = states[i - 1][cap - item.weight] + item.value

            value_above = states[i - 1][cap]

            current_cell_value = max(
                backtracked_cell_value, current_cell_value, value_above
            )

            print(
                f"backtracking [{i - 1}][{cap - item.weight}] = {backtracked_cell_value}"
            )
            print(
                f"i={i}; cap={cap} backtracking: {backtracked_cell_value} above: {value_above} final: {current_cell_value}"
            )

            states_item.append(current_cell_value)

        states.append(states_item)

    [print(i, s) for i, s in enumerate(states)]

    return states


def main():
    items = [Item(2, 3), Item(2, 1), Item(4, 3), Item(5, 4), Item(3, 2)]
    capacity = 7

    # let's start with 1, so 0 can be "void"
    _assign_ids(items, starting_from=1)
    print(items)

    print(knapsack_solve(items, capacity))


if __name__ == "__main__":
    main()
