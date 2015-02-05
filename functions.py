def countEvens(A):
    numOfEvens = 0
    for num in A:
        if num % 2 == 0:
            numOfEvens += 1
    return numOfEvens

def myMin(A):
    minNum = A[0]
    for num in A:
        if num < minNum:
            minNum = num
    return minNum

def myMax(A):
    maxNum = A[0]
    for num in A:
        if num > maxNum:
            maxNum = num
    return maxNum

def median(A):
    A.sort()
    if len(A) % 2 == 1:
        medianIndex = int((len(A) - 1) / 2)
        medianNum = A[medianIndex]
    else:
        medianLeftIndex = int(len(A) / 2 - 1)
        medianRightIndex = int(len(A) / 2)
        medianNum = (A[medianLeftIndex] + A[medianRightIndex]) / 2
    return medianNum

def secondBiggest(A):
    biggestNum = max(A)
    while max(A) == biggestNum:
        A.remove(biggestNum)
    secondBiggestNum = max(A)
    return secondBiggestNum

def dot(A, B):
    dotProduct = 0
    for index in range(len(A)):
        dotProduct += A[index] * B[index]
    return dotProduct

def LIS(A):
    LIS = []
    for index in range(len(A)):
        if index != 0:
            if A[index-1] < A[index]:
                increasingSublist.append(A[index])
            elif len(LIS) <= len(increasingSublist):
                LIS = increasingSublist
                increasingSublist = [A[index]]
        else:
            increasingSublist = [A[index]]
    return LIS

def intersect1(A, B):
    intersection = []
    for numA in A:
        for numB in B:
            if numA == numB:
                intersection.append(numA)
    return intersection

def intersect2(A, B):
    A.sort()
    B.sort()
    intersection = []
    indexA = 0
    indexB = 0
    aLength = len(A)
    bLength = len(B)
    while indexA<aLength and indexB<bLength:
        numA = A[indexA]
        numB = B[indexB]
        if numA == numB:
            intersection.append(A[numA])
            indexA += 1
            indexB += 1
        elif numA > numB:
            indexB += 1
        else:
            indexA += 1
    return intersection

def binarySearch(A, start, stop, target):
    if stop < start:
        return False
    middle = A[(start + stop)//2]
    if A[middle] == target:
        return A[middle]
    elif A[middle] > target:
        return binarySearch(A, middle, stop, target)
    else:
        return binarySearch(A, start, middle, target)

def fib(n):
    fibList = [1,1]
    for num in range(n):
        if num > 1:
            fibList.append(fibList[-1]+fibList[-2])
    nthNum = fibList[n-1]
    return nthNum

