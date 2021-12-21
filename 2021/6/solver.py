def main(fn):
    return fn


if __name__ == "__main__":
    # fn = input("pls fill in filename to analysis:\n")
    fn = "test.txt"
    with open(fn) as f:
        lines = f.read().strip().split("\n")
    result = main(fn)
    # result2 = main2(fn)
    print(f"the results is: \n  part 1 {result}")
