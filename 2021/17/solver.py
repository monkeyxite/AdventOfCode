import argparse


def main():
    guess_v_range = ((0, int(x_max)), (int(y_min), -int(y_min)))
    print(guess_v_range)
    result = 0
    for i in range(guess_v_range[0][0], guess_v_range[0][1]):
        for q in range(guess_v_range[1][0], guess_v_range[1][1]):
            pos = start
            v = [i, q]
            while True:
                new_pos = (pos[0] + i, pos[1] + q)
                v = v_changing(v)

    pass


def main2():
    pass


def v_changing(v):
    v_x, v_y = v
    if v_x > 0:
        v_x += -1
    elif v_x < 0:
        v_x += 1
    else:
        v_x = 0

    v_y += -1
    return (v_x, v_y)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fn", nargs="?", default="test.txt")
    fn = parser.parse_args().fn

    with open(fn) as f:
        lines = f.read()

    _, Target = lines.split(": ")
    x, y = Target.split(", ")
    x_min, x_max = x.replace("x=", "").split("..")
    y_min, y_max = y.replace("y=", "").split("..")

    target = (range(int(x_min), int(x_max)), range(int(y_min), int(y_max)))
    start = [0, 0]

    # print(coord, max(coord))
    result = main()
    result2 = main2()
    print(f"the results is: \n  part 1 {result}; part 2 {result}")
