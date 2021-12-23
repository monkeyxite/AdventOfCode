import argparse


def main(s):
    samples = s
    counter = 0
    for i in samples:
        if len(i) in [2, 3, 4, 7]:
            counter += 1
    return counter


def main2(t, s):
    total = [["".join(sorted(q)) for q in i] for i in t]
    sources = s
    result = []
    for i in range(len(sources)):
        codebook = decoding(sources[i])
        print(codebook)
        print(total[i])
        comb = [codebook[q] for q in total[i]]
        result.append(comb[0] * 1000 + comb[1] * 100 + comb[2] * 10 + comb[3])
    print(result)
    return sum(result)


def decoding(sources):
    sources = tuple(sources)
    c7 = list(filter(lambda i: len(i) == 3, sources))[0]
    c1 = list(filter(lambda i: len(i) == 2, sources))[0]
    c8 = list(filter(lambda i: len(i) == 7, sources))[0]
    c4 = list(filter(lambda i: len(i) == 4, sources))[0]
    # 3
    c253 = list(filter(lambda i: len(i) == 5, sources))
    c3 = list(filter(lambda i: len(set(i) & set(c1)) == 2, c253))[0]
    c25 = list(filter(lambda i: len(set(i) & set(c1)) != 2, c253))

    # 6
    c069 = list(filter(lambda i: len(i) == 6, sources))
    c6 = list(filter(lambda i: len(set(i) & set(c1)) == 1, c069))[0]
    c09 = list(filter(lambda i: len(set(i) & set(c1)) != 1, c069))

    # 09&3 == 4 -> 0
    # 09&3 == 5 -> 9
    c0 = list(filter(lambda i: len(set(i) & set(c3)) == 4, c09))[0]
    c9 = list(filter(lambda i: len(set(i) & set(c3)) == 5, c09))[0]
    # 25&9 5 -> 5
    # 25&9 4 -> 2
    c5 = list(filter(lambda i: len(set(i) & set(c9)) == 5, c25))[0]
    c2 = list(filter(lambda i: len(set(i) & set(c9)) == 4, c25))[0]

    cb = dict(
        zip(
            map(lambda i: "".join(sorted(i)),
                [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9]),
            range(10),
        ))
    return cb


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fn", nargs="?", default="test.txt")
    fn = parser.parse_args().fn

    with open(fn) as f:
        lines = f.read().strip().split("\n")

    samples = []
    sources = []
    total = []
    for line in lines:
        samples.extend(line.split("|")[1].split())
        sources.append(line.split("|")[0].split())
        total.append(line.split("|")[1].split())

    result = main(samples)
    result2 = main2(total, sources)
    print(f"the results is: \n  part 1 {result}; part 2 {result2}")
