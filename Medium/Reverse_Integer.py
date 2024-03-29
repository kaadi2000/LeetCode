"""Given a signed 32-bit integer num, return num with its digits reversed. If reversing num causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Enumample 1:

Input: num = 123
Output: 321
Enumample 2:

Input: num = -123
Output: -321
Enumample 3:

Input: num = 120
Output: 21
 

Constraints:

-231 <= num <= 231 - 1"""

def reverse(num: int) -> int:
    negativeFlag = False if num < 0 else True
    num = abs(num)
    result = int(str(num)[::-1]) if negativeFlag else int(str(num)[::-1]) * -1
    return 0 if (result > 2**31 - 1 or result < 2**31 * -1 + 1) else result


print(reverse(123))
print(reverse(-123))
print(reverse(120))