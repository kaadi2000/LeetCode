"""Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
 

Constraints:

1 <= columnNumber <= 231 - 1"""

import string


def excelSheetColumn(columnNumber: int) -> str:
    masterList = list(string.ascii_uppercase)
    result = ""
    while columnNumber > 0:
        columnNumber -= 1
        result = masterList[columnNumber % 26] + result
        columnNumber //= 26
    return result

print(excelSheetColumn(1))
print(excelSheetColumn(28))
print(excelSheetColumn(701))
print(excelSheetColumn(2147483647))