# `algorithms-py` - Various Algorithms, Implemented in Python

## Strongly Suggested VS Code Extension

[Comment Formula](https://marketplace.visualstudio.com/items?itemName=howcasperwhat.comment-formula) adds LaTeX formatting to comments, making displaying mathematical formulas inside of code possible.

## API

### `perf`

The `perf` module I wrote makes it trivial to measure any algorithm's performance:

```py
@perf.measure
def my_function():
    for i in range(100):
        perf.expensive_op() # counter++
        # perform heavy calculations, etc.
```

The rest will be handled automatically - no `print()` needed!

Result:

```py
[my_function] Expensive operations: 100
```

## `rand`

`rand.digits(n)` returns a list of `n` digits from 0-9:

```py
rand.digits(n=5)
# [9, 2, 3, 8, 7]
```


## Glossary

- `iter` = iterative functions that utilize loops.
- `recu` = recursive functions that call themselves. Their use can be controversial, especially in Python, since the interpreter limits recursion depth by default. Also can be more prone to errors and use more overhead. Sometimes easier to write, in my personal opinion.
