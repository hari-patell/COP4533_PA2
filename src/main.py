import sys
from cache_sim import parse_input, fifo, lru

def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else "data/example.in"
    k, requests = parse_input(path)
    print("FIFO :", fifo(k, requests))
    print("LRU  :", lru(k, requests))


if __name__ == "__main__":
    main()
