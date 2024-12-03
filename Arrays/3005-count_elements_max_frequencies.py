'''
Problem: Count elements maximium frequencies

Difficulty: Easy

Topic: Arrays

Description: You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.

 

Example 1:

Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.
Example 2:

Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.

'''

def maxFrequencyElements(list):
    freq = {}
    
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # Step 2: Find the maximum frequency
    max_freq = max(freq.values())
    
    # Step 3: Sum the frequencies of elements that have the maximum frequency
    total_freq = sum(count for count in freq.values() if count == max_freq)
    
    return total_freq

nums = [1,2,2,3,1,4]

print(maxFrequencyElements(nums))