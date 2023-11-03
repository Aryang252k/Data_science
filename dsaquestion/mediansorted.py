class Solution():
    def findMedianSortedArrays(self, num1: list[int],num2: list[int])->float:
        num1.extend(num2)
        num1.sort()
        s=len(num1)
        if s%2!=0:
           return float(num1[int(s/2)])
        else:
           a=int(s/2)
           return float((num1[a-1]+num1[a])/2)



s1=Solution()
m=s1.findMedianSortedArrays([1,2,3,5,4],[6,7,8,9,10])
print(m)