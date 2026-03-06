# Greedy Algorithms

Implementation of LRU, FIFO, and OPTFF caching algorithms.

**Authors:** Hari-Krishna Patel (UFID: 89949738), Hunter Stewart (UFID: 43812980)

## Input Format

**Input file type:** Input files must use the `**.in`** extension (e.g., `example.in`, `1.in`, etc). Input file must contain k (cache size), m (number of requests), and a subsequent sequence of requests.

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

On macOS, the Python 3 interpreter is usually available as `python3`.  
On many Linux/Windows setups, or if you've configured your system so `python` points to Python 3, you can use `python` instead.  
Equivalent commands with both options are shown below.

### From the project root:

```bash
# macOS (typical)
python3 src/main.py

# Linux/Windows or if `python` is Python 3
python src/main.py
```

### To run test files from the project root:

```bash
# macOS (typical)
python3 src/main.py tests/example.in
python3 src/main.py tests/test1.in
python3 src/main.py tests/test2.in
python3 src/main.py tests/test3.in
python3 src/main.py tests/test4.in
python3 src/main.py tests/bestoptff.in

# Linux/Windows or if `python` is Python 3
python src/main.py tests/example.in
python src/main.py tests/test1.in
python src/main.py tests/test2.in
python src/main.py tests/test3.in
python src/main.py tests/test4.in
python src/main.py tests/bestoptff.in
```

### To add and run your own test files, follow this format:

```
# macOS (typical)
python3 src/main.py tests/<filename>.in

# Linux/Windows or if `python` is Python 3
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


| Input File | k   | m   | FIFO | LRU | OPTFF |
| ---------- | --- | --- | ---- | --- | ----- |
| test1.in   | 3   | 50  | 10   | 10  | 6     |
| test2.in   | 3   | 60  | 9    | 9   | 6     |
| test3.in   | 4   | 60  | 7    | 7   | 6     |
| test4.in   | 5   | 54  | 7    | 6   | 6     |


**Observations**

- **OPTFF** consistently returns the fewest misses, as expected from an optimal offline algorithm.
- As cache size increases, the gap between **OPTFF** and **FIFO/LRU** misses shrinks, since more items fit in cache.
- **FIFO** and **LRU** perform similarly in these tests, with only one case where LRU outperforms FIFO.

---

## Question 2: Bad Sequence for LRU (and FIFO)

Here is a sequence where **OPTFF performs strictly better** than both LRU and FIFO for k = 3.


| Input File   | k   | m   | FIFO | LRU | OPTFF |
| ------------ | --- | --- | ---- | --- | ----- |
| bestoptff.in | 3   | 12  | 12   | 12  | 6     |


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

---

## Question 3: Proving OPTFF is Optimal

We want to show that Belady's algorithm (OPTFF) never does worse than any other offline algorithm on the same request sequence. We'll prove this using an exchange argument.

**Setup:**

Let OPT refer to OPTFF and let A be any offline algorithm that knows the full request sequence. Both start with the same cache of size *k*. We want to show:

misses(OPT) ≤ misses(A)

The idea is that if A ever makes a different eviction choice than OPT, we can "fix" that choice to match OPT without making things worse.

**The Exchange Argument:**

Assume OPT and A agree on the first *i − 1* requests and have identical cache contents up to that point. At request *r_i*, both have a miss and need to evict something. Say A evicts item *x* and OPT evicts item *y*. Since OPT always evicts the item whose next use is farthest in the future, *x* must be needed no later than *y*.

Now create a modified version of A, call it A', that evicts *y* instead of *x* at this step (matching OPT). After this, A' has *x* in its cache where A has *y*, and vice versa. We check what happens going forward:

- **x is never requested again:** It doesn't matter whether we kept *x* or *y* — *x* would never be useful anyway. A' does no worse than A.
- **x is requested before y:** A' still has *x* in cache, so it hits. A doesn't have *x*, so it misses. Later when *y* comes up, A' misses on *y* while A hits. So we get one extra hit and one extra miss compared to A — they cancel out. At this point, when A' brings *y* back in, we have it evict *x*. Now both A and A' have the same cache contents again and behave identically from here on. So A' has no more total misses than A.
- **y is requested before x:** This can't actually happen. OPT evicts the farthest-in-future item, so *y*'s next use has to be at least as far away as *x*'s. That means *x* comes first, not *y*.

In every case, A' does no worse than A.

**Finishing Up:**

We can keep applying this argument — every time A makes an eviction choice that differs from OPT, we swap it to match OPT without increasing the miss count. After each swap the caches re-sync, so we can repeat the process. Eventually A becomes OPT. Since each swap never increased the misses:

misses(OPT) ≤ misses(A)

So OPTFF is optimal among all offline algorithms.