def main(fn):
    return "p1"


def main2(fn):
    return "p2"


if __name__ == "__main__":
    # fn = input("pls fill in filename to analysis:\n")
    fn = "test.txt"
    result = main(fn)
    result2 = main2(fn)
    print(f"the results is: \n  part 1 {result}; part2 {result2}")
