def main(pos_list):
    pl = pos_list
    min, max = min(pos_list), max(pos_list)
    result = {}
    for i in range(min, max, 1):
        result[i] = abs()
    return 1


if __name__ == "__main__":
    # fn = input("pls fill in filename to analysis:\n")
    fn = "test.txt"
    with open(fn) as f:
        lines = f.read().strip().split("\n")
    pos_list = list(map(int, lines[0].split(",")))
    result = main(pos_list)
    print(f"the results is: \n  part 1 {result}")
