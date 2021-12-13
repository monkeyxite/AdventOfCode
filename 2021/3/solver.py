def main(fn):
    with open(fn) as f:
        l = f.read().splitlines()
    ll = [list(i) for i in l]
    gamma,epsilon = [],[]
    for i in range(len(ll[0])):
        gamma.append( [int(q[i]) for q in ll])
    g = ["1" if i.count(1)>=i.count(0) else "0" for i in gamma ]
    e = ["0" if i.count(1)>=i.count(0) else "1" for i in gamma ]
    return int("".join(g), 2) * int("".join(e),2)

def main2(fn):
    pass 

if __name__ == "__main__":
    o = [0, 0, 0]  # x(horizontal), depth, aim
    fn = input("pls fill in filename to analysis:\n")
    result = main(fn)
    print(f"the results is: \n  part 1 {result}; part2 {result}")
