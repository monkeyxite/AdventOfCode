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
            if b.win(wl):
                pprint(f"{b} wins @ {i}")
                result = (
                    i * sum(set(b.num) - set(num[:num.index(i) + 1])),
                    f" {i} * {sum(set(b.num)-set(num[:num.index(i)+1]))}",
                )
                break
        else:
            continue
        break
    return result


class Board:
    """docstring for Board."""
    def __init__(self, num_list):
        self.num = [int(i) for i in num_list]
        self.m = set()

    def __repr__(self):
        return str(self.num)

    def match(self, n):
        try:
            self.m.add(self.num.index(n))
        except ValueError:
            print(f"not found {n} in {self}")

    def win(self, wl):
        wl = wl
        result = list(filter(lambda i: i.issubset(self.m), wl))
        return True if result else False


def winlist_gen():
    win_list = []
    for g in range(5):
        win_list.append({i + 5 * g for i in range(5)})
        win_list.append({i + g for i in range(0, 25, 5)})
    return win_list


wl = winlist_gen()


def main2(fn):
    return fn


if __name__ == "__main__":
    fn = input("pls fill in filename to analysis:\n")
    result = main(fn)
    print(f"part1 the reuslt is {result}; ")
    result2 = main2(fn)
