import argparse
import heapq
from collections import defaultdict
from functools import reduce

VERSIONS = []
OPS = {
    0: sum,
    1: lambda iter: reduce(lambda x, y: x * y, iter),
    2: min,
    3: max,
    5: lambda x: int(x[0] > x[1]),
    6: lambda x: int(x[0] < x[1]),
    7: lambda x: int(x[0] == x[1]),
}


def main(data):
    _ = parse_packet(data, 0)
    return sum(VERSIONS)


def main2(data):
    return parse_packet(data, 0)[1]


def parse_literal(packet, i):
    ni = i
    res = []
    while True:
        res.append(packet[ni + 1:ni + 5])
        if packet[ni] == "0":
            return ni + 5, int("".join(res), 2)
        ni += 5


def parse_packet(packet, i):
    version, type_id = int(packet[i:i + 3], 2), int(packet[i + 3:i + 6], 2)
    VERSIONS.append(version)
    if type_id == 4:
        ni, val = parse_literal(packet, i + 6)
        return ni, val

    values = []
    len_type_id = packet[i + 6]
    if len_type_id == "0":
        total_len = int(packet[i + 7:i + 22], 2)
        ni = i + 22
        while ni < i + 22 + total_len:
            ni, val = parse_packet(packet, ni)
            values.append(val)
    else:
        packets = int(packet[i + 7:i + 18], 2)
        ni = i + 18
        for _ in range(packets):
            ni, val = parse_packet(packet, ni)
            values.append(val)

    return ni, OPS[type_id](values)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fn", nargs="?", default="test.txt")
    fn = parser.parse_args().fn

    with open(fn) as f:
        lines = f.read()
    print(lines)

    data = "".join(format(int(x, 16), "04b") for x in lines.replace("\n", ""))

    # print(coord, max(coord))
    result = main(data)
    result2 = main2(data)
    print(f"the results is: \n  part 1 {result}; part 2 {result2}")
