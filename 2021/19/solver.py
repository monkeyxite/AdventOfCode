import argparse
from collections import Counter, deque
from itertools import product

def main():
    result = find_beacons()[0]
    return len(result)

def main2():
    offsets = find_beacons()[1]
    res = 0
    for a, b in product(offsets, offsets):
        cur = sum(abs(x - y) for x, y in zip(a, b))
        res = max(res, cur)
    return res

def align(scanner_a, scanner_b):
    points = []
    offset = []
    solved_axes = set()
    for dim in range(3):
        cur = [beacon[dim] for beacon in scanner_a]
        for axis, flip in product((0, 1, 2), (1, -1)):
            if axis in solved_axes:
                continue
            orient = [beacon[axis]*flip for beacon in scanner_b]
            shift = [b - a for (a, b) in product(cur, orient)]
            in_common, count = Counter(shift).most_common(1)[0]
            if count >= 12:
                break
        if count < 12:
            return False, False
        solved_axes.add(axis)
        points.append([v - in_common for v in orient])
        offset.append(in_common)
    return list(zip(*points)), offset


def find_beacons():
    res = set()
    stack = [scanners[0]]
    q = deque(scanners[1:])
    offsets = []
    while stack:
        scanner_a = stack.pop()
        for _ in range(len(q)):
            scanner_b = q.popleft()
            updated, offset = align(scanner_a, scanner_b)
            if updated:
                stack.append(updated)
                offsets.append(offset)
            else:
                q.append(scanner_b)
        res |= set(scanner_a)
    # print(len(res))
    return res, offsets

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fn", nargs="?", default="test.txt")
    fn = parser.parse_args().fn

    with open(fn) as f:
        lines = f.read()

    scanners = []
    for line in lines.split('\n\n'):
        beacons = []
        for beacon in line.splitlines()[1:]:
            beacons.append(tuple(map(int, beacon.split(','))))
        scanners.append(beacons)

    result = main()
    result2 = main2()
    print(f"the results is: \n  part 1 {result}; part 2 {result2}")
