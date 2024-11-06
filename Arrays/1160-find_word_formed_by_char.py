'''
Problem: Find words that can be formed by characters

Difficulty: Easy

Topic: Arrays

Description: You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

'''

def countCharacters(words,chars):
    #count how many of each character are in chars and store in dictionary
    char_count = {}
    for char in chars:
        #if the char is found in the dictionary:
        if char in char_count:
            #add to the counter of that char
            char_count[char] += 1
        else:
            #if not, initialize the counter to 1
            char_count[char] = 1

    total_length = 0

    #For each word in the list:
    for word in words:
        can_form_word = True
        word_count = {}

        #count how many of each characters are in word and store in dictionary
        for char in word:
            if char in word_count:
                word_count[char] += 1
            else:
                word_count[char] = 1

        #for each character in the word
        for char in word:
            #if the number of character needed in the word is higher than the available characters in chars
            if word_count[char] > char_count.get(char, 0):
                #the word cannot be formed
                can_form_word = False
                break

        #if the word can be formed
        if can_form_word:
            total_length += len(word)
            
    return total_length
        


words = ["cat","bt","hat","tree","hat"]
chars = "atach"
print(countCharacters(words, chars))
