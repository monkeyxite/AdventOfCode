def main(fn):
    with open(fn) as f:
        l = f.read().splitlines()
    ll = [i.split() for i in l]
    for i in ll:
        if i[0] == "forward":
            o[0] += int(i[1])
        elif i[0] == "down":
            o[1] += int(i[1])
        elif i[0] == "up":
            o[1] -= int(i[1])
        else:
            raise AssertionError(f"Unexpected action {i[0]} detected!")
    return o[0] * o[1]


def main2(fn):
    with open(fn) as f:
        l = f.read().splitlines()
    ll = [i.split() for i in l]
    for i in ll:
        if i[0] == "forward":
            o[0] += int(i[1])
            o[1] += o[2] * int(i[1])
        elif i[0] == "down":
            # o[1] += int(i[1])
            o[2] += int(i[1])
        elif i[0] == "up":
            # o[1] -= int(i[1])
            o[2] -= int(i[1])
        else:
            raise AssertionError(f"Unexpected action {i[0]} detected!")
    return o[0] * o[1]


if __name__ == "__main__":
    o = [0, 0, 0]  # x(horizontal), depth, aim
    fn = input("pls fill in filename to analysis:\n")
    result = main(fn)
    o = [0, 0, 0]  # x(horizontal), depth, aim
    result2 = main2(fn)
    print(f"the results is: \n  part 1 {result}; part2 {result2}")
