'''
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
Example 3:

Input: root = [1]
Output: [1]
Example 4:

Input: root = [1,null,2]
Output: [1,2]
Example 5:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        
        if not root:
            return root
        
        queue = [root]
        res = []
      
        while queue:
            layer = []
            layervalues = []
            for i in range(len(queue)):
                Node = queue.pop(0)
                layer.append(Node)
                layervalues.append(Node.val)
                if Node.left:
                    queue.append(Node.left)
                if Node.right:
                    queue.append(Node.right)
                    
            res.append(max(layervalues))
                    
           
       
                
        return res
        