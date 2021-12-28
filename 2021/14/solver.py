import argparse
from collections import Counter


def main(init, pts, step):
    init_status = []
    for i in range(len(init) - 1):
        init_status.append(init[i : i + 2])
    counter = Counter(init_status)

    # p, addin = zip(*pts)

    for _ in range(step):
        result = Counter()
        print(f"step{_}:")
        new_counter = Counter()
        for k, v in counter.items():
            # print(new_counter)
            if k in pts.keys():
                # print(f"found {k}")
                new_counter[k[0] + pts[k]] += v
                new_counter[pts[k] + k[1]] += v
                result.update({k[0]: v})
                result.update({pts[k]: v})
            # print(new_counter)
        counter = new_counter
    result[init[-1]] += 1
    # print(sum(new_counter.values()))
    print(result)
    mm = sorted(result.values())
    return mm[-1] - mm[0]

    # start, stop = init[0], init[1]
    # for k, v in result:
    #     if k in [start, stop]:
    #         result[k] = int((v + 1) / 2)
    #     else:
    #         result[k] = int(v / 2)

    # for i in counter.keys():
    #     result.update({i[0]: counter[i], i[1]: counter[i]})


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

    result = main(init, pts, 10)
    result2 = main(init, pts, 40)
    print(f"the results is: \n  part 1 {result}; part 2 {result2}")
