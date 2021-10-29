"""
Inputs: 
1. Non-empty array of distinct integers 
2. Integer representing a target sum

If any two integers sum up to the target sum then return them in the array in any order.

Output: List of 2 integers summin up to the target sum. If None found then return empty list.

NOTE: You cannot add single integer twice to return the target sum.

Sample inputs
Input1 = [3, 5, -4, 8, 11, 1, -1, 6]
Input2 = 10
Output = [11, -1]

I have provided multiple solutions for the same problem.
Only difference is the space and time complexity between the solutions.

"""

# Solution 1: Traverse array in 2 for loops to find 1st and 2nd number.
# Time Complexity: O(n*n) as we are using 2 for loops.
# Space complexity: O(1) as we are not storing most of elements again in some variable and we have
# used contant space.

def twoNumberSum1(array, targetSum):

    for idx, value1 in enumerate(array, start=1):
        for value2 in array[idx:]:
            if value1+value2 == targetSum:
                return [value1, value2]
    return []

# Solution 2: Use hash table and use it to store each element of array to find the potential match.
# Time Complexity: O(n) as we are traversing array only once and for each number we are calculating
# for potential match and thats just constant time operation and we are accessing values in a 
# hash table which is gonna run in constant time.
# Space complexity: O(n) as we are storing values in hash table and we are storing most of the values
# in a hash table.

def twoNumberSum2(array, targetSum):
    hashArray = {}
    for value in array:
        potentialMatch = targetSum - value
        if potentialMatch in hashArray:
            return [potentialMatch, value]
        else:
            hashArray[value] = True
    return []

# Solution 3: Sort the array. Add left and right values of array and compare with target sum. Keep
# moving pointers towards each other till we get the match.
# Time Complexity: O(nlogn) as we are using 1 for loop and sorting. Quicksort, Mergesort or HeapSort will
# take O(nlogn) time and single for loop will take O(n).
# Space complexity: O(1) as we have not used any additional space like hash table and we have used
# few variable which is having constant values.

def twoNumberSum3(array, targetSum):
    array.sort()
    leftpointer = 0
    rightpointer = len(array)-1

    while(leftpointer < rightpointer):

        currentSum = array[leftpointer] + array[rightpointer]
        if currentSum == targetSum:
            return [array[leftpointer], array[rightpointer]]
        elif currentSum < targetSum:
            leftpointer += 1
        else:
            rightpointer -= 1
    return []