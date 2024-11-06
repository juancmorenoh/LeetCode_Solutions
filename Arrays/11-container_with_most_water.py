'''
Problem: Container with most water

Difficulty: Medium

Topic: Array

Description: You are given an integer array height of length n. 
There are n vertical lines drawn such that 
the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 
Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1
'''

def maxArea(height):
    max_volume = 0 
    i = 0 #left pointer
    j = len(height) - 1 #right pointer
    
    #true until the two pointers meet
    while i < j:
        #calculate volume between the two pointers
        volume = min(height[i], height[j]) * (j - i)
        #store the max volume
        max_volume = max(max_volume, volume)
        
        #move the pointer to the center of the shorter height of the 2 pointers
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    
    return max_volume

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))