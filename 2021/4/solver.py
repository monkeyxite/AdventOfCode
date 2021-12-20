from pprint import pprint


def main(num, bl):
    ord = 0
    for i in num:
        for b in bl:
            b.match(i)
            if b.winner:
                pass
            else:
                if b.win(wl):
                    ord += 1
                    result = (
                        i * sum(set(b.num) - set(num[:num.index(i) + 1])),
                        f" {i} * {sum(set(b.num)-set(num[:num.index(i)+1]))}",
                    )
                    b.update_after_winning(i, ord, result)
    result1 = list(filter(lambda i: i.win_order == 1, bl))[0]
    result2 = list(filter(lambda i: i.win_order == len(bl), bl))[0]
    return result1, result2


class Board:
    """docstring for Board."""
    def __init__(self, num_list):
        self.num = [int(i) for i in num_list]
        self.m = set()
        self.winner = False
        self.win_order = False
        self.win_num = False
        self.win_result = False

    def __repr__(self):
        return f"{self.num} win {self.win_order} with {self.win_num} and the result is {self.win_result}"

    def match(self, n):
        try:
            self.m.add(self.num.index(n))
        except ValueError:
            print(f"not found {n}")

    def win(self, wl):
        wl = wl
        result = list(filter(lambda i: i.issubset(self.m), wl))
        return True if result else False

    def update_after_winning(self, num, ord, result):
        self.winner = True
        self.win_num = num
        self.win_order = ord
        self.win_result = result


def winlist_gen():
    win_list = []
    for g in range(5):
        win_list.append({i + 5 * g for i in range(5)})
        win_list.append({i + g for i in range(0, 25, 5)})
    return win_list


if __name__ == "__main__":
    # fn = "test.txt"
    fn = input("pls fill in filename to analysis:\n")

    with open(fn) as f:
        l = f.read().split("\n\n")
        num, boards = l[0], l[1:]
    num = [int(i) for i in num.strip().split(",")]
    bl = []
    for i in boards:
        b = Board(i.strip().split())
        bl.append(b)

    wl = winlist_gen()
    result = main(num, bl)
    print(
        f"part1 the reuslt is {result[0].win_result}; 2 is {result[1].win_result}"
    )
