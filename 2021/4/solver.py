from pprint import pprint


def main(fn):
    with open(fn) as f:
        l = f.read().split("\n\n")
        num, boards = l[0], l[1:]
    num = [int(i) for i in num.strip().split(",")]
    bl = []
    for i in boards:
        b = Board(i.strip().split())
        bl.append(b)
    pprint(bl)
    pprint(num)
    return num


class Board:
    """docstring for Board."""
    def __init__(self, num_list):
        self.num = [int(i) for i in num_list]

    def __repr__(self):
        return str(self.num)


def main2(fn):
    return fn


if __name__ == "__main__":
    fn = input("pls fill in filename to analysis:\n")
    result = main(fn)
    result2 = main2(fn)
