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
    result = {}
    for xy, num in tuple(coord.items()):
        if all(num < coord[adj] for adj in find_ajancent(xy)):
            low_pt.append(xy)

    for xy in low_pt:
        area = 1
        for adj in find_ajancent(xy):
            if coord[adj] < 9:
                area += 1
            else:
                break
        result[xy] = area
    print(result)
    return result


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
    print(f"the results is: \n  part 1 {result}; part 2 {result}")
