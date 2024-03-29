"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'."""

def isValid(s: str) -> bool:
    stack = []
    openParathesis = ["(", "[", "{"]
    parathesis = {"{": "}", "(" : ")", "[" : "]", "}" : "{", ")": "(",  "]" : "["}
    for i in s:
        if i in openParathesis:
            stack.append(i)
        else:
            if len(stack) <= 0:
                return False
            if (parathesis[i] != stack.pop()):
                return False
    if(len(stack) > 0):
        return False
    else:
        return True
    
# Valid_Paranthesis.py

print(isValid("()")) # True
print(isValid("()[]{}")) # True
print(isValid("(]")) # False
print(isValid("([)]")) # False
print(isValid("{[]}")) # True