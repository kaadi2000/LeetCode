"""Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105"""

def TrappedWater(height: list[int]) -> int:
    n = len(height)
    leftHeight = [0] * n
    rightHeight = [0] * n
    leftHeight[0] = height[0]
    for i in range(1, n):
        leftHeight[i] = max(leftHeight[i-1], height[i])
    rightHeight[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        rightHeight[i] = max(rightHeight[i+1], height[i])
    result = 0
    for i in range(n):
        result += min(leftHeight[i], rightHeight[i]) - height[i]
    return result


print(TrappedWater([0,1,0,2,1,0,1,3,2,1,2,1]))