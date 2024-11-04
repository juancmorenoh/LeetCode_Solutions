'''
Problem: Number of studentt unable to eat lunch

Difficulty: Easy

Topic: Arrays

Description:The school cafeteria offers circular and square sandwiches at lunch break,
 referred to by numbers 0 and 1 respectively. 
 All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. 
The sandwiches are placed in a stack. At each step:

If the student at the front of the queue prefers the sandwich on the top of the stack, 
they will take it and leave the queue.
Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich 
and are thus unable to eat.

You are given two integer arrays students and sandwiches 
where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack 
(i = 0 is the top of the stack) and students[j] 
is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). 
Return the number of students that are unable to eat.

 

Example 1:

Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
Output: 0 
Explanation:
- Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
Hence all students are able to eat.
Example 2:

Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
Output: 3

'''
#-Sandwich never changes, only students.
#-If Student and Sandwich matches, we remove both from both lists
#-If Student and sandwich does not match, move current student to end
#Constantly check that at least 1 student in the list matches the first sandwich

def countStudents(students,sandwiches):
    student_count = len(students)
    i = 0
    
    while i < student_count:
        #check if any student matches sandwich at the top of the stack
        if sandwiches[0] in students:
            #if student and sandwich match
            if students[i] == sandwiches[0]:
                #remove both from the list
                students.pop(i)
                sandwiches.pop(0) 
                student_count -= 1
                print("Student is fed")
            #if they don't match           
            else:
                #move student at the end of the list
                student_pref = students.pop(i)
                students.append(student_pref)
                print("Student is goes at the end of the line")
        #if no student wants the first sandwich, break the loop
        else:
            print("No student wants this sandwich")  
            break     
        
    return student_count   


students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]

print(countStudents(students,sandwiches))