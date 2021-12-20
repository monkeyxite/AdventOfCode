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
    for i in num:
        for b in bl:
            b.match(i)
            pprint(b.m)
            b.win()
    return num


class Board:
    """docstring for Board."""

    def __init__(self, num_list):
        self.num = [int(i) for i in num_list]
        self.m = []

    def __repr__(self):
        return str(self.num)

    def match(self, n):
        self.m.append(self.num.index(n))

    def win(self):
        return False


def main2(fn):
    return fn


if __name__ == "__main__":
    fn = input("pls fill in filename to analysis:\n")
    result = main(fn)
    result2 = main2(fn)
