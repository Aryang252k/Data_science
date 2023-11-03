class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    newls=list()
    for i in range(len(nums)):
      for j in range(i+1,len(nums)):
       if (nums[i]+nums[j])==target:
         newls.extend([i,j])
         return newls
  

n=Solution()
l=[3,3,4,6,8]
nl=n.twoSum(l,11)

print(nl)