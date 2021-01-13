'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

 

Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        temp = head 
        
        arr = []
        count = 0
        while temp != None:
            count += 1
            
            if temp.val == 1:
                arr.append(count)
                
            temp = temp.next
            
        binarysum = 0
        
        for value in arr:
            
            binarysum += (2**(count-value))
            
        return binarysum