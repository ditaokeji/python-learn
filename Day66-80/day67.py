

class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
      nums.sort()
      length = len(nums)
      list = []
      min = float('inf')
      minIndex = 0
      for l in range(length):
       for m in range(l+1, length):
         for n in range(m+1, length):
           sum = nums[l] + nums[m] + nums[n] 
           if sum not in list:
             list.append(sum)
      for index,item in enumerate(list):
        if(min >= abs(target - item)):
          min = abs(target - item)
          minIndex = index
      return list[minIndex] 

solution = Solution()
res=solution.threeSumClosest([-1,2,1,-4], 1)
print(res)


class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        n = len(nums)
        res = float('inf')
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(res - target):
                    res = s
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    return res
        return res







