"""SUMMATION(N)"""

from time import time

def summation1(n):
    """summation type 1"""
    ans = 0
    for i in range(1, n+1):
        ans += i
    return ans
    # f(n) = n+1
    # f(n) = O(n)

def summation2(n):
    """summation type 2"""
    return (n*(n+1))/2
    # f(n) = O(1)

def analyze_algorithms(n):
    stime = time()
    ans = summation1(n)
    etime = time()
    print("Summation(%d)" %n)
    print("Summation1 : Answer = "+str(ans)+", Time = "+str(etime-stime)+"s")
    stime = time()
    ans = summation2(n)
    etime = time()
    print("Summation2 : Answer = "+str(ans)+", Time = "+str(etime-stime)+"s")
    print("---------------------------------")

analyze_algorithms(100)
analyze_algorithms(10000)
analyze_algorithms(1000000)
analyze_algorithms(100000000)
analyze_algorithms(10000000000)
