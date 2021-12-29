import argparse
import heapq
from collections import defaultdict


def main(coord):
    target = max(coord)
    passed = set()
    working = [(0, (0, 0))]

    while working:
        cost, last_pos = heapq.heappop(working)
        if last_pos == target:
            return cost
        elif last_pos in passed:
            continue
        else:
            passed.add(last_pos)

        for next_pos in find_ajancent(last_pos):
            if next_pos in coord:
                heapq.heappush(working, (cost + coord[next_pos], next_pos))


def find_ajancent(xy):
    yield xy[0] + 1, xy[1]
    yield xy[0] - 1, xy[1]
    yield xy[0], xy[1] + 1
    yield xy[0], xy[1] - 1


def main2():
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fn", nargs="?", default="test.txt")
    fn = parser.parse_args().fn

    with open(fn) as f:
        lines = f.read().strip().split("\n")

    coord = {}
    for y, line in enumerate(lines):
        for x, num in enumerate(line):
            coord[(x, y)] = int(num)

    print(coord, max(coord))
    result = main(coord)
    # result2 = main()
    print(f"the results is: \n  part 1 {result}; part 2 {result}")
