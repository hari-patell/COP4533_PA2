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

# Written Response
## Question 1: Empirical Comparison

Below are the empirical results for four input files.  
Each file contains at least 50 requests.

| Input File | k | m  | FIFO | LRU | OPTFF |
|------------|---|----|------|-----|--------|
| test1.in   | 3 | 50 | 10   | 10  | 6      |
| test2.in   | 3 | 60 | 9    | 9   | 6      |
| test3.in   | 4 | 60 | 7    | 7   | 6      |
| test4.in   | 5 | 54 | 7    | 6   | 6      |

**Observations**

- **OPTFF** consistently returns the fewest misses, as expected from an optimal offline algorithm.
- As cache size increases, the gap between **OPTFF** and **FIFO/LRU** misses shrinks, since more items fit in cache.
- **FIFO** and **LRU** perform similarly in these tests, with only one case where LRU outperforms FIFO.

---

## Question 2: Bad Sequence for LRU (and FIFO)

Here is a sequence where **OPTFF performs strictly better** than both LRU and FIFO for \(k = 3\).

| Input File   | k | m  | FIFO | LRU | OPTFF |
|--------------|---|----|------|-----|--------|
| bestoptff.in | 3 | 12 | 12   | 12  | 6      |

**Input**  
3 12  
1 2 3 4 1 2 3 4 1 2 3 4

**Explanation**

With 4 distinct items and a cache size of 3:
- **FIFO** and **LRU** both evict the oldest or least recently used item, which is always the one needed next.
  - When they get to item 4, item 1 is evicted even though it is the subsequent request.
  - This causes **every request to be a miss** for FIFO and LRU
- **OPTFF** looks ahead and evicts the page whose next use is farthest in the future.
  - This allows OPTFF to keep the pages that will be reused soon, cutting the number of misses in half.

This request example demonstrates that OPTFF can outperform both FIFO and LRU.

