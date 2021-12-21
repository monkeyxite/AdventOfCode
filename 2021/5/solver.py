from pprint import pprint


def main(fromto_xy, matrix):
    ftl, m = fromto_xy, matrix
    line = []
    for ft in ftl:
        f, t = ft[0], ft[1]
        if f[0] == t[0]:
            # gap = (list(range(t[0], t[1] + 1, 1)) if t[0] >= t[1] else list(
            #     range(t[1], t[0] + 1, 1)))
            gap = range(f[1], t[1] +
                        1, 1) if t[1] >= f[1] else range(t[1], f[1] + 1, 1)
            for i in gap:
                line.append((t[0], i))

        elif f[1] == t[1]:
            gap = range(f[0], t[0] +
                        1, 1) if t[0] >= f[0] else range(t[0], f[0] + 1, 1)
            for i in gap:
                line.append((i, t[1]))
        else:
            print(f"the {ft} is not a straight line")
    for xy in line:
        m[xy[0]][xy[1]] += 1
    cnt = 0
    for i in m:
        for q in i:
            cnt = cnt + 1 if q > 1 else cnt
    print(m)
    return cnt


def main2(fn):
    return "p2"


if __name__ == "__main__":
    fn = input("pls fill in filename to analysis:\n")
    # fn = "test.txt"
    with open(fn) as f:
        lines = f.read().strip().split("\n")

    fromto = [i.split(" -> ") for i in lines]
    fromto_xy = [(list(map(int,
                           i[0].split(","))), list(map(int, i[1].split(","))))
                 for i in fromto]
    matrix = [[0 for i in range(1000)] for q in range(1000)]
    print(matrix, len(matrix), len(matrix[0]))

    result = main(fromto_xy, matrix)
    result2 = main2(fn)
    print(f"the results is: \n  part 1 {result}; part2 {result2}")
