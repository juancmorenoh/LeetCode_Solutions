'''
Problem: Diffewrence Between element sum and 
digit sum of an array

Difficulty: Easy

Topic: Arrays

Description:You are given a positive integer array nums.

The element sum is the sum of all the elements in nums.
The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.

Note that the absolute difference between two integers x and y is defined as |x - y|.

 

Example 1:

Input: nums = [1,15,6,3]
Output: 9
Explanation: 
The element sum of nums is 1 + 15 + 6 + 3 = 25.
The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
The absolute difference between the element sum and digit sum is |25 - 16| = 9.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Explanation:
The element sum of nums is 1 + 2 + 3 + 4 = 10.
The digit sum of nums is 1 + 2 + 3 + 4 = 10.
The absolute difference between the element sum and digit sum is |10 - 10| = 0.
'''

def differenceOfSum(nums):
    element_sum = 0
    digit_sum = 0
    for num in nums: #for each element of array
        element_sum += num #add to element_sum
        for digit in str(num): #convert each number to string to access each digit
            digit_sum += int(digit) #convert back to integer and add to digit_sum

    return element_sum - digit_sum #return difference

nums = [1,15,6,3]
print(differenceOfSum(nums))