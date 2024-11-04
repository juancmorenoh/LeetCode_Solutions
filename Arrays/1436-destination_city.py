'''
Problem: Destination city

Difficulty: Easy

Topic: Arrays

Description: You are given the array paths, 
where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. 
Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, 
therefore, there will be exactly one destination city.


Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".
Example 3:

Input: paths = [["A","Z"]]
Output: "Z"
'''

def destCity(paths):
    #sets are better then lists in this case
    outgoing_path = set()
    destination_candidate = set()

    for path in paths: #for each element in paths
        outgoing_path.add(path[0]) #add the first to this set
        destination_candidate.add(path[1])#add the second to the other set
    destination_city = destination_candidate - outgoing_path#find the difference, the city that is in destination but not in outgoing
    #(this return a set)
    return destination_city.pop()#return the string in the set

paths = [["A","Z"]]
print(destCity(paths))