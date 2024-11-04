'''
Problem: Minimum number of operations to convert time

Difficulty: Easy

Topic: Strings

Description: You are given two strings current and correct representing two 24-hour times.

24-hour times are formatted as "HH:MM", 
where HH is between 00 and 23, and MM is between 00 and 59. 
The earliest 24-hour time is 00:00, and the latest is 23:59.

In one operation you can increase the time current by 1, 5, 15, or 60 minutes. 
You can perform this operation any number of times.

Return the minimum number of operations needed to convert current to correct.

 
Example 1:

Input: current = "02:30", correct = "04:35"
Output: 3
Explanation:
We can convert current to correct in 3 operations as follows:
- Add 60 minutes to current. current becomes "03:30".
- Add 60 minutes to current. current becomes "04:30".
- Add 5 minutes to current. current becomes "04:35".
It can be proven that it is not possible to convert current to correct in fewer than 3 operations.
Example 2:

Input: current = "11:00", correct = "11:01"
Output: 1
Explanation: We only have to add one minute to current, 
so the minimum number of operations needed is 1.
'''

#The approach:
#Dealing with HH first, so that the h is the same, deal from 23 to 00
#Deal with minutes after
#Always save the number of steps
#1 / 5 / 15 / 60 min

def convertTime(current, correct):

    #convert current into total minutes
    h_current = int(current[0] + current[1]) * 60
    m_current = int(current[3] + current[4])
    tot_minutes_current = h_current + m_current

    #convert correct into total minutes
    h_correct = int(correct[0] + correct[1]) * 60
    m_correct = int(correct[3] + correct[4])
    tot_minutes_correct = h_correct + m_correct

    #calculate difference in minutes
    difference = tot_minutes_correct - tot_minutes_current
    operations = 0

    #if there is difference
    while difference != 0:
        #if difference is at least 60
        if difference >= 60:
            #increment operations by the number of times 60 minutes fits into the difference
            operations += difference // 60
            #update difference with the remainder of dividing by 60
            difference %= 60
        elif difference >= 15:
            operations += difference // 15
            difference %= 15
        elif difference >= 5:
            operations += difference // 5
            difference %= 5
        elif difference >= 1:
            operations += difference // 1
            difference %= 1
    return operations
    
    

current = "02:30"
correct = "02:35"

print(convertTime(current,correct))