import argparse


def main():
    guess_v_range = ((1, int(x_max) + 1), (int(y_min) - 1, abs(int(y_min))))
    print(guess_v_range)
    result = 0
    right_v = []
    for i in range(guess_v_range[0][0], guess_v_range[0][1]):
        for q in range(guess_v_range[1][0], guess_v_range[1][1]):
            pos = start
            init_v = v = (i, q)
            high = 0
            # print(f"init v: {v}")
            while True:
                pos = (pos[0] + v[0], pos[1] + v[1])
                v = v_changing(v)
                high = pos[1] if pos[1] > high else high
                if pos[0] in target[0] and pos[1] in target[1]:
                    if init_v not in right_v:
                        right_v.append(init_v)
                    # print( f"hit target via {pos} with {high} @ {v} with init v {init_v}")
                    result = high if high > result else result
                    break
                elif pos[0] > int(x_max) or pos[1] < int(y_min):
                    break
                else:
                    continue
    return result, right_v


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

    target = (range(int(x_min),
                    int(x_max) + 1), range(int(y_min),
                                           int(y_max) + 1))
    start = [0, 0]

    # print(coord, max(coord))
    result = main()
    result2 = main2()
    print(f"the results is: \n  part 1 {result[0]}; part 2 {len(result[1])}")
