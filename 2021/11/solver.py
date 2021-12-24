import argparse

SCORE = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

SCORE2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}
BRACKETS = {"[": "]", "(": ")", "{": "}", "<": ">"}


def main(lines):
    result = []
    for line in lines:
        pair_stack = []
        for i in line:
            if i in BRACKETS.keys():
                pair_stack.append(i)
            else:
                if i == BRACKETS[pair_stack[-1]]:
                    pair_stack.pop()
                else:
                    result.append(SCORE[i])
                    # print(f"{i} found with {SCORE[i]} pnts")
                    break
    return sum(result)


def main2(lines):
    result = []
    result2 = []
    for line in lines:
        pair_stack = []
        for i in line:
            if i in BRACKETS.keys():
                pair_stack.append(i)
            else:
                if i == BRACKETS[pair_stack[-1]]:
                    pair_stack.pop()
                else:
                    result.append(SCORE[i])
                    break
        else:
            result2.append(pair_stack)
    # score = [sum([SCORE2[BRACKETS[i]] for i in line]) for line in result2]
    # print(result2, len(result2))
    score_list = []
    for line in result2:
        score = 0
        if line == []:
            break
        for i in line[::-1]:
            # print(
            #     f"{score} w {BRACKETS[i]} becomes {5 * score + SCORE2[BRACKETS[i]]})"
            # )
            score = 5 * score + SCORE2[BRACKETS[i]]
        score_list.append(score)
    # print(sorted(score_list))
    return sorted(score_list)[len(score_list) // 2]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fn", nargs="?", default="test.txt")
    fn = parser.parse_args().fn

    with open(fn) as f:
        lines = f.read().strip().split("\n")

    result = main(lines)
    result2 = main2(lines)
    # result2 = main2(total, sources)
    print(f"the results is: \n  part 1 {result}; part 2 {result2}")
