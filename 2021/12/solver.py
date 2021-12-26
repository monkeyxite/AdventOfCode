import argparse
from collections import defaultdict


def main():
    return dfs("start", set())


def main2():
    return dfs("start", set(), dual_visit=True)


# dfs alg refer to
# - https://github.com/michaeljgallagher/Advent-of-Code/blob/master/2021/12.py
def dfs(node, seen, dual_visit=False):
    if node == "end":
        return 1
    if node == "start" and seen:
        return 0
    if node.islower() and node in seen:
        # print(seen)
        if dual_visit:
            dual_visit = False
        else:
            return 0
    path = 0
    seen = seen | {node}
    # seen = seen.add(node) if seen else {node}
    for neibourg in edges[node]:
        path += dfs(neibourg, seen, dual_visit)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fn", nargs="?", default="test.txt")
    fn = parser.parse_args().fn

    with open(fn) as f:
        lines = f.read().strip().split("\n")

    edges = defaultdict(list)
    for line in lines:
        node1, node2 = line.split("-")
        edges[node1].append(node2)
        edges[node2].append(node1)

    result = main()
    result2 = main2()
    print(f"the results is: \n  part 1 {result}; part 2 {result2}")
