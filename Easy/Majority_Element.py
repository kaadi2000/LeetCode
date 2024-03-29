"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109"""

#Solution 1
def majorityElement(nums:list[int]) -> int:
    hashMap = {}
    for num in nums:
        if num in hashMap:
            hashMap[num] += 1
        else:
            hashMap[num] = 1
    for key in hashMap:
        if hashMap[key] > len(nums)//2:
            return key

#Solution 2
def majorityElement(nums:list[int]) -> int:
    nums.sort()
    return nums[len(nums)//2]

#Solution 3
def majorityElement(nums:list[int]) -> int:
    result = 0
    count  = 0
    for num in nums:
        if count == 0:
            result = num
            count +=1
        else:
            if result == num:
                count +=1
            else:
                count -=1
    return result

print(majorityElement([6, 5, 5]))