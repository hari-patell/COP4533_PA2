import sys
from cache_sim import parse_input, fifo, lru, optff

def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else "../data/example.in"

    try:
        k, requests = parse_input(path)
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        sys.exit(1)
    print("FIFO  :", fifo(k, requests))
    print("LRU   :", lru(k, requests))
    print("OPTFF :", optff(k, requests))


if __name__ == "__main__":
    main()
