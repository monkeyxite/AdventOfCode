import argparse
from collections import Counter


def main(init, pts):
    init_status = []
    for i in range(len(init) - 1):
        init_status.append(init[i:i + 2])
    counter = Counter(init_status)

    # p, addin = zip(*pts)
    step = 10

    for _ in range(step):
        new_counter = Counter()
        for k, v in counter.items():
            if k in pts.keys():
                print(f"found {k}")
                new_counter[k[0] + pts[k]] += v
                new_counter[pts[k] + k[1]] += v
            print(counter)
            print(new_counter)
        counter = new_counter

    result = Counter()
    for i in counter.keys():
        result.update({i[0]: counter[i], i[1]: counter[i]})

    print(sum(result.values()) / 2 + 1)


def main2():
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fn", nargs="?", default="test.txt")
    fn = parser.parse_args().fn

    with open(fn) as f:
        init, pattern = f.read().strip().split("\n\n")

    pts = {}
    for pt in pattern.splitlines():
        p, addin = pt.split(" -> ")
        pts[p] = addin

    result = main(init, pts)
    result2 = main2()
    print(f"the results is: \n  part 1 {result}; part 2 {result2}")
