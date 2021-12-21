def main(fl, days):
    fish_list, days = fl, days
    for i in range(days):
        for f in fish_list:
            nf = f.live_for_oneday()
            if nf:
                fish_list.append(nf)
        # print(f"after d{i+1}: {fish_list}")
    return fl


def main2(fl, days):
    from collections import Counter

    fish_list = [f.days for f in fl]
    fc = Counter(fish_list)
    print(fc)
    for i in range(days):
        new_fc = {}
        for k, v in fc.items():
            new_fc[k - 1] = v

    return 10


class Fish:
    def __init__(self, *days):
        if not days:
            self.days = 9
        else:
            self.days = days[0]

    def __repr__(self):
        return f"F{self.days}!"

    def live_for_oneday(self):
        self.days -= 1
        if self.days == -1:
            # reset fish lifecycle
            self.days = 6
            new_fish = Fish()
            return new_fish
        else:
            return False


if __name__ == "__main__":
    fn = input("pls fill in filename to analysis:\n")
    # fn = "test.txt"
    with open(fn) as f:
        lines = f.read().strip().split("\n")

    days_list = lines[0].split(",")
    fish_list = [Fish(int(i)) for i in days_list]
    days = 18
    # print(fish_list)

    result = main2(fish_list, days)
    # if days < 80:
    #     result = main(fish_list, days)
    # else:
    #     result = main2(fish_list, days)
    # result2 = main2(fn)
    print(f"the results is: \n  part 1 {result}")
