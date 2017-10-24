# This script searches for a missing number in a given array, where the numbers
# are sorted in increased order.
# Example: [1, 2, 4, 5] - Missing number is 3.

import math

def findMissing(arr):
    """
    This version works with arrays which may not start with one.
    It searches for the smallest and the largest number, then calculates the
    sum of all the number which should be between them.
    From that sum it removes the sum of the currently present numbers.
    """
    smin = arr[0]
    smax = arr[0]
    missing = 0

    for i in range(1, len(arr)):
        if arr[i] < smin:
            smin = arr[i]
        if arr[i] > smax:
            smax = arr[i]

    expectedSum = 0
    sumArr = 0
    
    for i in range(smin, smax + 1):
        expectedSum += i

    for i in arr:
        sumArr += i


    if expectedSum != sumArr:
        return expectedSum - sumArr
    else:
        return "There is a no missing number."


"""
# This is the second version of this script
# It works only with arrays starting with one.

def missingNumber(arr):
    n = len(arr) + 1
    total_sum = 0
    expectedSum = math.factorial(n) 
    for i in range(len(arr)):
        total_sum += arr[i]
    return expectedSum - total_sum   
"""
