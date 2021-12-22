def main(pos_list):
    pl = pos_list
    result = {}
    for i in range(min(pl), max(pl) + 1, 1):
        result[i] = sum([abs(q - i) for q in pl])
    print(result)
    return min(result.values())


if __name__ == "__main__":
    fn = input("pls fill in filename to analysis:\n")
    # fn = "test.txt"
    with open(fn) as f:
        lines = f.read().strip().split("\n")
    pos_list = list(map(int, lines[0].split(",")))
    result = main(pos_list)
    print(f"the results is: \n  part 1 {result}")
