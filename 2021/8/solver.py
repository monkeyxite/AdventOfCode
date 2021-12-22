import argparse


def main(s):
    samples = s
    counter = 0
    for i in samples:
        if len(i) in [2, 3, 4, 7]:
            counter += 1
    return counter


def main2(s, cb):
    samples = s
    codebook = cb
    result = []
    for i in samples:
        for q in codebook.keys():
            if set(i) == set(q):
                result.append(codebook[q])
            else:
                print(f"{i} doesn't match the codebook")
    print(result, len(result))
    comb = [
        1000 * result[i] + 100 * result[i + 1] + 10 * result[i + 2] +
        result[i + 3] for i in range(0, len(result), 4)
    ]
    print(comb)
    return sum(comb)


def decoding(sources):
    postion_holder = ["", "", "", "", "", "", ""]
    c7 = set(list(filter(lambda i: len(i) == 3, sources))[0])
    c1 = set(list(filter(lambda i: len(i) == 2, sources))[0])
    c8 = set(list(filter(lambda i: len(i) == 7, sources))[0])
    c4 = set(list(filter(lambda i: len(i) == 4, sources))[0])
    c253 = list(map(set, list(filter(lambda i: len(i) == 5, sources))))
    c3 = list(filter(lambda i: len(i&c1)==2, c253))[0]
    c069 = list(map(set, list(filter(lambda i: len(i) == 6, sources)))
    c6 = list(filter(lambda i: len(i&c1)==1, c069))[0]
    postion_holder[6] = c7 - c1
    postion_holder[2] = c6 & c1
    postion_holder[1] = c1-(c6 & c1)
    postion_holder[6] = c1-(c6 & c1)
    return postion_holder


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fn", nargs="?", default="test.txt")
    fn = parser.parse_args().fn

    postion_holder = ["", "", "", "", "", "", ""]
    codebook = {
        8: (1, 2, 3, 4, 5, 6, 0),
        5: (2, 3, 5, 6, 0),
        2: (1, 3, 4, 6, 0),
        3: (1, 2, 3, 6, 0),
        7: (6, 1, 2),
        9: (1, 2, 3, 5, 6, 0),
        6: (2, 3, 4, 5, 6, 0),
        4: (1, 2, 5, 0),
        0: (1, 2, 3, 4, 5, 6),
        1: (1, 2),
    }
    with open(fn) as f:
        lines = f.read().strip().split("\n")

    samples = []
    sources = []
    for line in lines:
        samples.extend(line.split("|")[1].split())
        sources.extend(line.split("|")[0].split())

    print(samples)
    result = main(samples)
    result2 = main2(samples, codebook)
    print(f"the results is: \n  part 1 {result}; part 2 {result2}")
