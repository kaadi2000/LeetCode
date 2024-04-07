"""Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.

 

Example 1:

Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
Example 2:

Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit. 
 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters and/or digits."""

def secondLargets(s: str) -> int:
    arr = []
    for i in range(len(s)) :
        if s[i].isnumeric():
            arr.append(s[i])
        else :
            pass
    arr = list(set(arr))
    arr.sort()
    if len(arr) < 2 :
        return -1
    a = int(arr[-2])
    return a

print(secondLargets("ck077"))