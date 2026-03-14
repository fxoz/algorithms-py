import contextvars

from time import perf_counter
from rich import print

_add_counter = contextvars.ContextVar("add_counter", default=None)


def expensive_op():
    c = _add_counter.get()
    if c is not None:
        c[0] += 1


def measure(func):
    func_prefix = f"[magenta]\\[{func.__name__}] [/]"
    start = perf_counter()

    def inner(*args, **kwargs):
        token = None
        counter = _add_counter.get()

        if counter is None:
            counter = [0]
            token = _add_counter.set(counter)

        result = func(*args, **kwargs)

        if token is not None:
            print(f"{func_prefix}[yellow italic]Expensive operations: {counter[0]}[/]")
            _add_counter.reset(token)

        print(
            f"{func_prefix}[yellow italic]Execution time (ms): {(perf_counter() - start) * 1000:.2f}[/]"
        )

        return result

    return inner
