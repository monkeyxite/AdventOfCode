def main(fromto_xy, matrix):
    ftl, m = fromto_xy, matrix
    line = []
    part2_line = []
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
        # For part2
        elif (f[0] - t[0]) == (f[1] - t[1]) or (f[0] - t[0]) == -(f[1] - t[1]):
            # print(f"found 45d line {f} -> {t}")
            y_gap = (range(f[1], t[1] + 1, 1) if t[1] >= f[1] else range(
                f[1], t[1] - 1, -1))
            x_gap = (range(f[0], t[0] + 1, 1) if t[0] >= f[0] else range(
                f[0], t[0] - 1, -1))
            for i in range(len(x_gap)):
                part2_line.append((x_gap[i], y_gap[i]))
        else:
            print(f"the {ft} is not a 45 degree/vertical/horizontal line")
    for xy in line:
        m[xy[0]][xy[1]] += 1
    cnt = 0
    for i in m:
        for q in i:
            cnt = cnt + 1 if q > 1 else cnt
    # print(f"the 45d lines are {part2_line}")
    for xy in part2_line:
        m[xy[0]][xy[1]] += 1
    p2_cnt = 0
    for i in m:
        for q in i:
            p2_cnt = p2_cnt + 1 if q > 1 else p2_cnt
    # print(m)
    return cnt, p2_cnt


if __name__ == "__main__":
    fn = input("pls fill in filename to analysis:\n")
    # fn = "test.txt"
    with open(fn) as f:
        lines = f.read().strip().split("\n")
    fromto = [i.split(" -> ") for i in lines]
    fromto_xy = [(list(map(int,
                           i[0].split(","))), list(map(int, i[1].split(","))))
                 for i in fromto]
    # TODO dynamically generating the right size of the matrix
    matrix = [[0 for i in range(1000)] for q in range(1000)]
    # matrix = [[0 for i in range(10)] for q in range(10)]
    result = main(fromto_xy, matrix)
    # result2 = main2(fn)
    print(f"the results is: \n  part 1 {result[0]}; part2 {result[1]}")
