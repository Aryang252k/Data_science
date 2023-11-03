#Input: s = "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3.
#Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
class Solution:
 def lengthOfLongestSubstring(self, st: str) -> str:
    max_length=start=0
    sr=temp=''
    for i in range(len(st)):
      for j in range(i+1,len(st)-1):
        if st[i]==st[j]:
          sr+=st[i]
        else:
           
           sr+=st[j]
          # print(sr)
           start+=1
           temp1=max_length
           max_length=max(max_length,start)
           if max_length > temp1:
              temp=sr
            
           start=0
        #print(temp)
   
    start=0
    print(temp)
    
    for i in range(len(temp)-1,0):
       if temp[start]==temp[i]:
         start+=1

    if  len(temp)==start:
       return temp
 
                  
               
               

st="cbbd"
sta=Solution()
n=sta.lengthOfLongestSubstring(st)
print(n)


