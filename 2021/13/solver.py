import argparse
from collections import defaultdict


def main(pts, folder):
    # x, y = zip(*pts)
    ax, where = folder
    # boundary = max(x) if ax == "x" else max(y)
    if ax == "x":
        new_pts = set([(2 * where - i[0], i[1]) for i in pts if i[0] > where])
        remain_pts = set([pt for pt in pts if pt[0] < where])
    else:
        new_pts = set([(i[0], 2 * where - i[1]) for i in pts if i[1] > where])
        remain_pts = set([pt for pt in pts if pt[1] < where])
    return len(remain_pts | new_pts)


def main2():
    return 0


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

    result = main(pts, f[0])
    result2 = main2()
    print(f"the results is: \n  part 1 {result}; part 2 {result2}")
