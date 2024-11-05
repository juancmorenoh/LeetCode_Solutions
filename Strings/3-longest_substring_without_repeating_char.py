'''
Problem: Longest substring without repeating characters

Difficulty: Medium

Topic: Strings

Description: Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

def lengthOfLongestSubstring(s):
    char_set = set()
    start = 0
    counter = 0

    for i in range(len(s)):
        #if current char is in the set, remove it until not found anymore
        #increment the start of the new substring by 1
        while s[i] in char_set:
            char_set.remove(s[start])
            start += 1
        #(if char not in the set)
        #add it to the set
        char_set.add(s[i])
        #update the counter for the length of the substring
        counter = max(counter, i - start +1)

    return counter


s = "pwwkew"
print(lengthOfLongestSubstring(s))