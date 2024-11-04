'''
Problem: Percentage of Letter in String

Difficulty: Easy

Topic: String manipulation

Description: Given a string s and a character letter, 
return the percentage of characters in s that equal letter rounded down to the nearest whole percent.

 
Example 1:

Input: s = "foobar", letter = "o"
Output: 33
Explanation:
The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded down, 
so we return 33.
Example 2:

Input: s = "jjjj", letter = "k"
Output: 0
Explanation:
The percentage of characters in s that equal the letter 'k' is 0%, so we return 0.
'''

def percentageLetter(s, letter):
    counter = 0
    #loop the string
    for char in s:
        if char == letter:
            #add tocounter if letter is in the string
            counter += 1
    if counter != 0:
        #return %
        return int((counter / len(s)) * 100)
    return 0

s = "foobar"
letter = "o"

print(percentageLetter(s,letter))