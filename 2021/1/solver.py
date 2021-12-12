def main():
    with open("test.txt") as f:
        l = f.read().split("\n")
        l = [int(i) for i in l]
    cnt = 0
    for i in range(len(l) - 1):
        cnt = cnt + 1 if l[i + 1] > l[i] else cnt
    return cnt


if __name__ == "__main__":
    main()
