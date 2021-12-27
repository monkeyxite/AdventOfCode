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


def main2(pts, folders):
    for folder in folders:
        print(folder)
        ax, where = folder
        if ax == "x":
            new_pts = set([(2 * where - i[0], i[1]) for i in pts
                           if i[0] > where])
            remain_pts = set([pt for pt in pts if pt[0] < where])
        else:
            new_pts = set([(i[0], 2 * where - i[1]) for i in pts
                           if i[1] > where])
            remain_pts = set([pt for pt in pts if pt[1] < where])
        pts = remain_pts | new_pts

    x, y = zip(*pts)
    boundary = (max(x), max(y))
    matrix = [["."] * (boundary[0] + 1) for i in range(boundary[1] + 1)]
    for x, y in pts:
        print(x, y)
        matrix[y][x] = "#"
    for row in matrix:
        print("".join(row))

    return pts


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
    result2 = main2(pts, f)
    print(f"the results is: \n  part 1 {result}; part 2 {result2}")
