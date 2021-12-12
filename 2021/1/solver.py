def main(fn):
    with open(fn) as f:
        l = f.read().split("\n")
        print(l)
        l = [int(i) for i in l if i]
    l2 = [sum(l[i:i+2]) for i in range(len(l)-2)]
    return cmp(l),cmp(l2)



def cmp(l):
    cnt = 0
    for i in range(len(l) - 1):
        cnt = cnt + 1 if l[i + 1] > l[i] else cnt
    return cnt

if __name__ == "__main__":
    fn = input("pls fill in filename to analysis:\n")
    result = main(fn)
    print(f"the results is {result}")
