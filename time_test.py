def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp

def newSort(L):
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
# add selSort() and newSort() as above

def testSelSort():
    L = [3,6,8,23,67,87,88,45,6,55,32,10,11,45,9]
    selSort(L)

def testNewSort():
    L = [3,6,8,23,67,87,88,45,6,55,32,10,11,45,9]
    newSort(L)

if __name__ == "__main__":

    L = [3,6,8,23,67,87,88,45,6,55,32,10,11,45,9]

    from timeit import Timer
    t = Timer("testNewSort()", "from __main__ import newSort, testNewSort")
    print("newSort:{}".format(t.timeit(number=100000)))

    t = Timer("testSelSort()", "from __main__ import selSort, testSelSort")
    print("selSort:{}".format(t.timeit(number=100000)))
