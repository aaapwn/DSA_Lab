"""ISINTERSECT(A, B, C)"""

from time import time
import random

def isIntersect1(A, B, C):
    """Big-O = N^2"""
    isSame = None
    ans = False
    for i in A:
        for j in B:
            if i == j:
                if i in C:
                    ans = True
    return ans
    # f(n) = n^2
    # f(n) = O(n^2)

def isIntersect2(A, B, C):
    """Big-O = N^3"""
    ans = False
    for i in A:
        for j in B:
            for k in C:
                if i == j == k:
                    ans = True
    return ans
    # f(n) = n^3 + 2
    # f(n) = O(n^3)

def randomList(n):
    A = [random.randint(1, n*100) for _ in range(n)]
    B = [random.randint(1, n*100) for _ in range(n)]
    C = [random.randint(1, n*100) for _ in range(n)]
    return A, B, C

def analyze_algorithms(n):
    testCase = randomList(n)
    stime = time()
    ans = isIntersect1(testCase[0], testCase[1], testCase[2])
    etime = time()
    print("isIntersect(%d)" %n)
    print("isIntersect1 : Answer = "+str(ans)+", Time = "+str(etime-stime)+"s")
    stime = time()
    ans = isIntersect2(testCase[0], testCase[1], testCase[2])
    etime = time()
    print("isIntersect2 : Answer = "+str(ans)+", Time = "+str(etime-stime)+"s")
    print("---------------------------------")

def testProgram():
    print("case1 :")
    print("Intersect1 =", isIntersect1([50, 20, 80], [40, 30, 20], [20, 70, 90]))
    print("Intersect2 =", isIntersect2([50, 20, 80], [40, 30, 20], [20, 70, 90]))
    print()
    print("case2 :")
    print("Intersect1 =", isIntersect1([40, 60, 80, 100], [10, 30, 50, 60], [10, 20, 30, 40]) )
    print("Intersect2 =", isIntersect2([40, 60, 80, 100], [10, 30, 50, 60], [10, 20, 30, 40]) )

analyze_algorithms(100)
analyze_algorithms(1000)
analyze_algorithms(10000)
analyze_algorithms(100000)
