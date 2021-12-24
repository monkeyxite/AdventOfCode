import argparse
from collections import defaultdict


def main(c):
    result = 0
    coord = defaultdict(lambda: 9999, c)
    for xy, num in tuple(coord.items()):
        if all(num < coord[adj] for adj in find_ajancent(xy)):
            result += num + 1
    return result


def main2(c):
    result = []
    coord = defaultdict(lambda: 9999, c)
    low_pt = []
    passed_pt = []
    result = {}
    for xy, num in tuple(coord.items()):
        if all(num < coord[adj] for adj in find_ajancent(xy)):
            low_pt.append(xy)

    for xy in low_pt:
        passed_pt = []
        find_area(xy, coord, passed_pt)
        result[xy] = len(passed_pt)
    result = sorted(result.values())

    return result[-1] * result[-2] * result[-3]


def find_area(xy, c, passed_pt):
    coord = c
    if xy not in passed_pt:
        passed_pt.append(xy)
    for adj in find_ajancent(xy):
        if coord[adj] < 9 and adj not in passed_pt:
            passed_pt.append(adj)
            find_area(adj, coord, passed_pt)
        else:
            pass


def find_ajancent(xy):
    yield xy[0] + 1, xy[1]
    yield xy[0] - 1, xy[1]
    yield xy[0], xy[1] + 1
    yield xy[0], xy[1] - 1


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

    result = main(coord)
    result2 = main2(coord)
    # result2 = main2(total, sources)
    print(f"the results is: \n  part 1 {result}; part 2 {result2}")
