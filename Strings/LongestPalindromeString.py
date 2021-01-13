'''
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"
 
Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),


'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        maxlen = 0
        largestPalindromeString = ""
        for i in range(len(s)):
            
            for j in range(1,len(s)+1):
                temp = s[i:j]
                
                if temp == temp[::-1]:
                    maxlen = max(len(temp),maxlen)
                    
                    if maxlen == len(temp):
                        largestPalindromeString = temp
        return largestPalindromeString
                        
                    
                
        