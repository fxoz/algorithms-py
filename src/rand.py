import random


def digits(n: int = 500) -> list[int]:
    return [random.randint(0, 9) for _ in range(n)]
