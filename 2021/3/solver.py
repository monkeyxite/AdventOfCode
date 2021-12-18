from copy import copy


def main(fn):
    with open(fn) as f:
        l = f.read().splitlines()
    ll = [list(i) for i in l]
    gamma, epsilon = [], []
    for i in range(len(ll[0])):
        gamma.append([int(q[i]) for q in ll])
    g = ["1" if i.count(1) >= i.count(0) else "0" for i in gamma]
    e = ["0" if i.count(1) >= i.count(0) else "1" for i in gamma]
    return int("".join(g), 2) * int("".join(e), 2), g, e


def main2(fn):
    with open(fn) as f:
        l = f.read().splitlines()
    pos = len(l[0]) - 1
    ll = [int(i, 2) for i in l]
    filtered_ll = copy(ll)
    while pos > 0:
        cur = [(i & (1 << pos)) >> pos for i in filtered_ll]
        total = len(cur)
        if total <= 2:
            break
        if sum(cur) >= total / 2:
            filtered_ll = list(
                filter(lambda i: (i & (1 << pos)) >> pos == 1, filtered_ll)
            )
        else:
            filtered_ll = list(
                filter(lambda i: (i & (1 << pos)) >> pos == 0, filtered_ll)
            )
        pos -= 1
    o_r = list(filter(lambda i: (i & (1 << pos)) >> pos == 1, filtered_ll))[0]

    pos = len(l[0]) - 1
    filtered_ll2 = copy(ll)
    while pos > 0:
        cur2 = [(i & (1 << pos)) >> pos for i in filtered_ll2]
        total2 = len(cur2)
        if total2 == 2:
            filtered_ll2 = list(
                filter(lambda i: (i & (1 << pos)) >> pos == 0, filtered_ll2)
            )
            break
        if total2 == 1:
            break
        if sum(cur2) >= total2 / 2:
            filtered_ll2 = list(
                filter(lambda i: (i & (1 << pos)) >> pos == 0, filtered_ll2)
            )
        else:
            filtered_ll2 = list(
                filter(lambda i: (i & (1 << pos)) >> pos == 1, filtered_ll2)
            )
        pos -= 1
    c_r = filtered_ll2[0]
    return o_r * c_r


if __name__ == "__main__":
    fn = input("pls fill in filename to analysis:\n")
    result = main(fn)
    result2 = main2(fn)
    print(f"the results is: \n  part 1 {result[0]}; part2 {result2}")
