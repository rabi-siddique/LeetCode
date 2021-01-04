'''
Write a function to delete a node in a singly-linked list. You will not be given access to 
the head of the list, instead you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should 
become 4 -> 1 -> 9 after calling your function.


Since we do not have access to the node before the one we want to delete, 
we cannot modify the next pointer of that node in any way. Instead, 
we have to replace the value of the node we want to delete with the value in 
the node after it, and then delete the node after it.

'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        
        
        