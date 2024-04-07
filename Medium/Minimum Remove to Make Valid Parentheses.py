"""Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter."""
from collections import deque

def minumumToMakeValid(s:str) -> str:
    temp = []
    count = 0
    for i in s:
        count += (i == '(')-(i == ')')
        if count >= 0:
            temp.append(i)
        else: 
            count = 0
    count =0
    queue = []
    for i in temp[::-1]:
        count += (i == '(')-(i == ')')
        if count <=0:
            queue.append(i)
        else: 
            count =0
        print(count, i)
    return ''.join(queue[::-1])

print(minumumToMakeValid("(a(b(c)d)"))