#14. Longest Common Prefix --leetcode
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

class Solution:
    def longestCommonPrefix(self, A) :
        st = ''
        while True:
            if all(A[0][len(st)] == A[i][len(st)] for i in range(len(A))):
                st+= A[0][len(st)]
            else:
                return st
				
				
class Solution1:
    def longestCommonPrefix(self, A) :
        i = 0
        st = ''
        print("hello")
        while True:
            
            if len(A[0]) <= i:
                return st
            
            tmp = A[0][i]
            
            for x in A:
                if len(x) <=i:
                    return st
                if x[i] != tmp:
                    return st

                
            st+= tmp
            i+=1
            
            
ss = Solution1()
print(ss.longestCommonPrefix(["flower","flow","flight"]))