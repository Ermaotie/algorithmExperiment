def recursiveMergeSort(numList):
    if len(numList) <= 1:
        return numList
    mid = len(numList) // 2
    left = recursiveMergeSort(numList[:mid])
    right = recursiveMergeSort(numList[mid:])
    return merge(left, right)


def recursiveQuickSort(numlist):
    if not len(numlist):
        return []
    else:
        division = numlist[0]
        left = recursiveQuickSort([x for x in numlist[1:] if x < division])
        right = recursiveQuickSort([x for x in numlist[1:] if x >= division])
    return left + [division] + right


def nonRecursiveMergeSort(numList):
    i = 1
    while(i < len(numList)):
        low = 0
        while low < len(numList):
            mid = low + i
            height = min(low + 2 * i, len(numList))
            if mid < height:
                left = numList[low:mid]
                right = numList[mid:height]

                j, k = 0, 0
                result = []
                while(j < mid-low and k < height-mid):
                    if left[j]<right[k]:
                        result.append(left[j])
                        j += 1
                    else:
                        result.append(right[k])
                        k +=1
                result += left[j:]
                result += right[k:]
                numList[low:height] = result
            low += 2 * i
        i *= 2
    return numList


def nonRecursiveQuickSort(array):
    stack = []
    stack.append(0)
    stack.append(len(array))
    while stack:
        low = stack.pop()
        high = stack.pop()
        if high - low <= 0:
            continue
        x = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        stack.extend([low, i, i + 2, high])
    return array


def merge(left, right):
    """合并两个已排序好的列表，产生一个新的已排序好的列表"""
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def test():
    data = [47, 4, 1, 43, 568, 2, 34, 967, 2567, 345, 1236, 12378, 8]
    RMS = recursiveMergeSort(data)
    print("the result of RMS")
    print(RMS)

    print("the result of NRMS")
    print(nonRecursiveMergeSort(data))

    print("the result of RQS")
    print(recursiveQuickSort(data))

    print("the result of NRQS")
    print(nonRecursiveQuickSort(data))


if __name__ == "__main__":
    test()
