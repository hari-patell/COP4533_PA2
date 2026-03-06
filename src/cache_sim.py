from collections import deque, OrderedDict


def parse_input(filename: str) -> tuple[int, list[int]]:
    with open(filename) as f:
        lines = f.readlines()
    k, m = map(int, lines[0].split())
    requests = [int(x) for x in lines[1].split()]
    return k, requests


def fifo(k: int, requests: list[int]) -> int:
    cache = set()
    order = deque()
    misses = 0
    for x in requests:
        if x in cache:
            continue
        misses += 1
        if len(cache) == k:
            evict = order.popleft()
            cache.discard(evict)
        order.append(x)
        cache.add(x)
    return misses


def lru(k: int, requests: list[int]) -> int:
    cache = OrderedDict()
    misses = 0
    for x in requests:
        if x in cache:
            cache.move_to_end(x)
            continue
        misses += 1
        if len(cache) == k:
            cache.popitem(last=False)
        cache[x] = None
    return misses


if __name__ == "__main__":
    k, requests = parse_input("data/example.in")
    print("FIFO :", fifo(k, requests))
    print("LRU  :", lru(k, requests))
