import argparse


def main(s):
    samples = s
    counter = 0
    for i in samples:
        if len(i) in [2, 3, 4, 7]:
            counter += 1
    return counter


def main2():
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fn", nargs="?", default="test.txt")
    fn = parser.parse_args().fn

    codebook = {
        0: "abcdfg",
        1: "cf",
        2: "acdeg",
        3: "acdfg",
        4: "bcdf",
        5: "abdfg",
        6: "abdefg",
        7: "acf",
        8: "abcdefg",
        9: "abcdfg",
    }

    with open(fn) as f:
        lines = f.read().strip().split("\n")

    samples = []
    for line in lines:
        samples.extend(line.split("|")[1].split())
    print(samples)
    result = main(samples)
    print(f"the results is: \n  part 1 {result}; part 2 {result}")
