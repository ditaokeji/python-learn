 class ListNode:
      def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def longestPalindrome(self, s: str) -> str:
      max = 0
      result = ''
      for index, chat in enumerate(s):
        palindrome = ""
        isPalindrome = True 
        left = right =  index
        while isPalindrome:
           left-=1 
           right+=1 
           start=0 if left<=0 else left  
           end=len(s)-1 if right > len(s) else right+1
           leftStrRange = s[start:index]
           rightStrRange = s[index:end]
           strRange = s[start:end]
           if strRange == strRange[::-1] or leftStrRange == leftStrRange[::-1] or rightStrRange == rightStrRange[::-1]:
              isPalindrome = True 
              palindrome = strRange 
           else:
              isPalindrome = False 
        if len(result)<len(palindrome):
           result = palindrome  

      return result
    
    def convert(self, s:str, numRows: int) -> str:
      arr = [[] for x in range(numRows)]
      for index, chat in enumerate(s):
          num = index % (numRows*2 - 2)        
          level = 0
          if num > numRows - 1:
              level = numRows*2 - num - 2
          else:
              level = num % numRows 
          arr[level].append(chat)
      flat_arr = [str(item) for sublist in arr for item in sublist]
      return ''.join(flat_arr)
    
    def isPalindrome(self, x: int) -> bool:
      if(x<0):
        return False
      raw = str(x)
      for index, item in enumerate(raw):
        if item != raw(len(raw)-index):
          return False 
      return True 
    
    def intToRoman(self, num: int) -> str:
        roman_map = {
          1: 'I',
          4: 'IV',
          5: 'V',
          9: 'IX',
          10: 'X',
          40: 'XL',
          50: 'L',
          90: 'XC',
          100: 'C',
          400: 'CD',
          500: 'D',
          900: 'CM',
          1000: 'M',
        }
        roman = []
        while num > 0:
          temp_value = ""
          temp_int = 0
          for key, value in roman_map.items():
            if key <= num:
               temp_value = value
               temp_int = key;
          roman.append(temp_value)
          num = num - temp_int 
      return ''.join(roman)
    
    def romanToInt(self, s: str) -> int:
        roman_map = {
          'I': 1,
          'IV': 4,
          'V': 5,
          'IX': 9,
          'X': 10,
          'XL': 40,
          'L': 50,
          'XC': 90,
          'C': 100,
          'CD': 400,
          'D': 500,
          'CM': 900,
          'M': 1000,
       }
       result = 0
       while len(s) > 0:
          chat = s[:2]
          count = 2
         if chat not in roman_map:
            chat = s[:1]
            count = 1
        result += roman_map[chat] 
        s = s[count:] 
      return result

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      dummy  = ListNode(0)
      target = dummy  
      while list1 and list2:
        if list1.val >= list2.val:
          target.next = list2 
          target.next.next = list1  
        else:
          target.next = list1 
          target.next.next = list2
        list1 = list1.next 
        list2 = list2.next
        target.next = target.next.next
      return dummy.next

solution = Solution()      
str1 = solution.convert('PAYPALISHIRING',3)
str2 = solution.romanToInt('MCMXCIV')

l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
str3 = solution.mergeTwoLists(l1,l2)
print(str2)

from typing import Optional,List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 使用列表生成链表
def generate_linked_list(nums):
    if not nums:
        return None
    head = ListNode(nums[0])
    current = head
    for i in range(1, len(nums)):
        current.next = ListNode(nums[i])
        current = current.next
    return head

nums = [1,2,3,4,5]
linked_list = generate_linked_list(nums)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      target = head
      temp = target
      len1 = 0
      while temp:
           len1 += 1
           temp = temp.next
      temp = res = ListNode(0)
      temp.next = target
      len2 = 0
      while temp:
          if len2 == len1 - n:
             temp.next = temp.next.next
          temp = temp.next
          len2 += 1
          if not temp:
              break
      return res.next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        list = []
        for item in lists:
           while item:
               list.append(item.val)
               item = item.next
        list.sort()
        target = temp = ListNode(0)
        for it in list:
           temp.next = ListNode(it)
           temp = temp.next
        return target.next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        target = iter = ListNode(0)
        while temp:
           odd_node = temp.next
           even_node = temp
           odd_node.next = even_node
           iter.next = odd_node
           iter = iter.next.next
           temp = temp.next.next
        return target

# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6



solution = Solution()
solution.swapPairs(generate_linked_list([1,2,3,4]))





        


















