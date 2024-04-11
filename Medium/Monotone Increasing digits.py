"""An integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.

Given an integer n, return the largest number that is less than or equal to n with monotone increasing digits.

 

Example 1:

Input: n = 10
Output: 9
Example 2:

Input: n = 1234
Output: 1234
Example 3:

Input: n = 332
Output: 299
 

Constraints:

0 <= n <= 109"""

def monotoneIncreasingDigits(n: int) -> int:
    digits = [int(x) for x in str(n)]

    i = len(digits) - 1

    while i > 0:
        if digits[i] < digits[i-1]:
            digits[i-1] -= 1
            for i in range(i,len(digits)):
                digits[i] = 9
        i -= 1
    return int("".join([str(x) for x in digits]))
    
print(monotoneIncreasingDigits(123456))
print(monotoneIncreasingDigits(123465))
print(monotoneIncreasingDigits(12928))
