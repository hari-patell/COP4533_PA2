def parse_input(filename: str) -> tuple[int, list[int]]:
    with open(filename) as f:
        lines = f.readlines()
    k, m = map(int, lines[0].split())
    requests = [int(x) for x in lines[1].split()]
    return (k, requests)
