import argparse
from collections import defaultdict


def main(c):
    step = 100
    # coord = defaultdict(lambda: 0, c)
    coord = c
    print("intial status")
    print(coord.values())
    print("\n".join([
        "".join(list(map(str, coord.values()))[i * 10:i * 10 + 10])
        for i in range(10)
    ]))

    num = 0
    for i in range(1, step + 1, 1):
        flashing = []
        for k, v in tuple(coord.items()):
            # print(f"step{i} for {k} with {v}")
            coord[k] += 1
            if coord[k] > 9:
                flashing.append(k)

        while flashing:
            pt = flashing.pop()

            if coord[pt] == 0:
                continue
            num += 1
            # print(f"{pt} flashed in step {i}")
            coord[pt] = 0

            for others in find_ajancent(pt):
                if others in coord.keys() and coord[others] != 0:
                    coord[others] += 1
                    if coord[others] > 9:
                        flashing.append(others)
                        # print(f" find {others} should flash in step{i}")

        print(f"step{i}:")
        print("\n".join([
            "".join(list(map(str, coord.values()))[i * 10:i * 10 + 10])
            for i in range(10)
        ]))
    return num


def main2(c):
    pass


# generator with adj pt including 45d
def find_ajancent(xy):
    for i in (-1, 0, 1):
        for q in (-1, 0, 1):
            yield xy[0] + i, xy[1] + q


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
    # result2 = main2(coord)
    print(f"the results is: \n  part 1 {result}; part 2 {result}")
