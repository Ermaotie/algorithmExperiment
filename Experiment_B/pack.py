import numpy as np


def pack(vlist, wlist, totalWeight, totalLength):
    resArr = np.zeros((totalLength+1, totalWeight+1), dtype=int)
    for i in range(1, totalLength+1):
        for j in range(1, totalWeight+1):
            if wlist[i] <= j:
                resArr[i, j] = max(resArr[i - 1, j - wlist[i]] + vlist[i], resArr[i - 1, j])
            else:
                resArr[i, j] = resArr[i - 1, j]
    return resArr[-1, -1]


def test():
    v = [0, 1000, 60, 100, 120,20000]
    w = [0, 30, 10, 20, 30,40]
    weight = 50
    n = 5

    print("01pack:")
    print(pack(v,w,weight,n))


if __name__ == "__main__":
    test()
