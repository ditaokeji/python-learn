class Solution(object):
    def longestPalindrome(self, s: str) -> str:
      max = 0
      for index, chat in enumerate(s):
        palindrome = ""
        isPalindrome = True 
        left = right =  index
        while isPalindrome:
           left-=1 
           right+=1 
           start=0 if left<=0 else left  
           end=len(s)-1 if right > len(s) else right+1
           strRange = s[start:end]
           if strRange == strRange[::-1]:
              isPalindrome = True 
           else:
              isPalindrome = False 
        if len(palindrome)<len(strRange):
           palindrome = strRange 

      return palindrome



solution = Solution()      
len = solution.longestPalindrome("babad")
print(len)
























