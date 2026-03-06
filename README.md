# Greedy Algorithms

Implementation of LRU, FIFO, and OPTFF caching algorithms.

**Authors:** Hari-Krishna Patel (UFID: 89949738), Hunter Stewart (UFID: 43812980)

## Input Format

**Input file type:** Input files must use the **`.in`** extension (e.g., `example.in`, `1.in`, etc). Input file must contain k (cache size), m (number of requests), and a subsequent sequence of requests.

**Structure:**

```
k m
<m number of requests>
```

See `tests/example.in` for reference.

## Output format

Prints the cache miss amount for all three caching algorithms.

```
FIFO  : a
LRU   : b
OPTFF : c
```

## How to run

### From the project root:

```bash
python src/main.py
```

### To test the cache input parser with the example file:

```bash
python -c "from src.cache_sim import parse_input; print(parse_input('data/example.in'))"
```

Expected output: `(3, [1, 2, 3, 4, 1, 2, 5, 1, 2, 3])`

### To run test files from the project root:

```bash
python src/main.py tests/example.in
python src/main.py tests/test1.in
python src/main.py tests/test2.in
python src/main.py tests/test3.in
python src/main.py tests/test4.in
python src/main.py tests/bestoptff.in
```

### To add and run your own test files, follow this format:

```
python src/main.py tests/<filename>.in
```

### Clearing output files

To remove all `.out` files from `/tests`:

```bash
rm tests/*.out
```
