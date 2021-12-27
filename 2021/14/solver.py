import argparse
from collections import defaultdict


def main():
    pass


def main2():
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fn", nargs="?", default="test.txt")
    fn = parser.parse_args().fn

    with open(fn) as f:
        matrix, actions = f.read().strip().split("\n\n")

    pts = []
    f = []
    for pt in matrix.splitlines():
        x, y = pt.split(",")
        pts.append((int(x), int(y)))

    for a in actions.splitlines():
        axis, num = a.replace("fold along ", "").split("=")
        f.append((axis, int(num)))
        # pts.append(xy)

    result = main()
    result2 = main2()
    print(f"the results is: \n  part 1 {result}; part 2 {result2}")
