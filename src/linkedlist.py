from rich import print
from typing import Optional

import perf
import rand


class Node:
    def __init__(self, val: int, next: Optional[Node] = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        text = f"{self.val}"

        if self.next:
            text += f" -> {str(self.next)}"
        else:
            text += "."

        return text


@perf.measure  #  $n$
def from_list_recu(vals: list[int], reverse: bool = False) -> Node:
    perf.expensive_op()

    if len(vals) == 1:  # the last one doesn't have a 'next'
        return Node(val=vals[0], next=None)

    # Remove last item if reverse, otherwise first item
    val = vals.pop(-1 if reverse else 0)
    return Node(val=val, next=from_list_recu(vals))


@perf.measure  #  $n$
def from_list_iter(vals: list[int], reverse: bool = False) -> Node:
    prev = None
    for i, _ in enumerate(vals):
        perf.expensive_op()
        prev = Node(vals[i if reverse else len(vals) - i - 1], prev)

    return prev


@perf.measure  # $n$
def traverse(node: Node) -> list:
    vals = []

    while node.next:
        perf.expensive_op()
        vals.append(node.val)
        node = node.next
    vals.append(node.val)

    return vals


@perf.measure  # $2n$
def reverse(head: Node):
    return from_list_iter(traverse(head), reverse=True)


def main():
    # ll = Node(1, Node(2, Node(3)))

    ll = from_list_iter([1, 2, 3, 4, 5], True)

    print(ll)

    ll_reveresed = reverse(ll)

    print(ll_reveresed)


if __name__ == "__main__":
    main()
