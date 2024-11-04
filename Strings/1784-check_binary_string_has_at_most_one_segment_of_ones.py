'''
Problem: Check if binary string has at most one segment of ones

Difficulty: Easy

Topic: Strings

Description: Given a binary string s ​​​​​without leading zeros, 
return true​​​ if s contains at most one contiguous segment of ones. 
Otherwise, return false.

 

Example 1:

Input: s = "1001"
Output: false
Explanation: The ones do not form a contiguous segment.
Example 2:

Input: s = "110"
Output: true
'''

def checkOnesSegment(s):
    # If the string "01" is present, it means there is more than one segment of ones.
    return "01" not in s

s = "1000101011"
print(checkOnesSegment(s))