"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once."""

#Solution 1
def singleNumber(nums: list[int]) -> int:
    hashmap = {}
    for i in nums:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    for i in hashmap:
        if hashmap[i] == 1:
            return i

#Solution 2
def singleNumber(nums: list[int]) -> int:
    numSet = set()
    for i in nums:
        if i in numSet:
            numSet.remove(i)
        else:
            numSet.add(i)
    return numSet.pop()

#Solution 3 - Worst but it works
def singleNumber(nums: list[int]) -> int:
    numSet = set(nums)
    for i in numSet:
        if nums.count(i) == 1:
            return i
        
#Solution 4 - Best
def singleNumber(nums: list[int]) -> int:
    return 2*sum(set(nums))-sum(nums)

