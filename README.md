# COP4533 PA2

## How to run

From the project root:

```bash
python src/main.py
```

To test the cache input parser with the example file:

```bash
python -c "from src.cache_sim import parse_input; print(parse_input('data/example.in'))"
```

Expected output: `(3, [1, 2, 3, 4, 1, 2, 5, 1, 2, 3])`

To run test files:
```bash
python src/main.py tests/example1.in
python src/main.py tests/test1.in
python src/main.py tests/test2.in
python src/main.py tests/test3.in
python src/main.py tests/test4.in
python src/main.py tests/bestoptff.in
```
