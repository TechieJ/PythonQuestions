"""
Inputs: 
1. Non-empty array
2. Non-empty array

Ask: If second array is subsequence of first one.

Output: True / False

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that
are in the same order as they appear in the array.

Sample inputs
Input1 = [3, 5, -4, 8, 11, 1, -1, 6]
Input2 = [3, 8, 1]
Output = Input2 is subsequence of Input1

NOTE: A single element in array and array itself are both valid subsequence of the array.

I have provided multiple solutions for the same problem.
Only difference is the space and time complexity between the solutions.

"""

# Solution 1:
# Time Complexity: O(n) as we are traversing through main array once.
# Space Complexity: O(1)

def isValidSubsequence1(array, sequence):    
    seqStartIndex = 0
    for value in array:
        if value == sequence[seqStartIndex]:
            seqStartIndex += 1
            if seqStartIndex == len(sequence):
                break
    return seqStartIndex == len(sequence)

# Solution 2:
# Time Complexity: O(n) as we are traversing through main array once.
# Space Complexity: O(1)

def isValidSubsequence2(array, sequence):
    arrIdx = 0
    seqIdx = 0

    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)