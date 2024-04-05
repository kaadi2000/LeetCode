"""Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6."""

def findKthPositiveNumber(arr: list[int], k: int) -> int:
    result = arr[0] - 1
    lastPositive = arr[0]
    if result == k:
        return result
    elif result > k:
        return k
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] - 1 < k - result:
            result += arr[i+1] - arr[i] - 1
            lastPositive = arr[i+1]
        else:
            return arr[i] + k - result
    if k - result > 0:
        return arr[-1] + k - result
    
print(findKthPositiveNumber([1,2,3,4], 2))
print(findKthPositiveNumber([2,3,4,7,11], 5))
print(findKthPositiveNumber([2], 1))