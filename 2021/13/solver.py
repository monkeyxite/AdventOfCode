import argparse
from collections import defaultdict


def main():
    return 0


def main2():
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fn", nargs="?", default="test.txt")
    fn = parser.parse_args().fn

    with open(fn) as f:
        matrix, actions = f.read().strip().split("\n\n")

    pts = []
    for pt in matrix:
        xy = pt.split(", ")
        pts.append(xy)

    print(pts)
    result = main()
    result2 = main2()
    print(f"the results is: \n  part 1 {result}; part 2 {result2}")
