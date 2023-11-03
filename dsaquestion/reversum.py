class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        temp1,temp2 = l1,l2
        ls1 = list()
        ls2 = list()
        ls1.append(temp1.val)
        while temp1 is not None :
             ls1.append(temp1.val)
             temp1=temp1.next
          
        ls2.append(temp2.val)
        while temp2 is not None:
             ls2.append(temp2.val)
             temp2=temp2.next

        st1=0
        st2=0
        
        for i in range(len(ls1)-1,-1,-1):
             st1=st1*10+ls1[i]
        for i in range(len(ls2)-1,-1,-1):
             st2=st2*10+ls2[i]
        sum1=st1+st2
    
        stsum=str(sum1)
        ls3=list()
        for i in stsum:
             ls3.append(int(i))
        le=len(ls3)
        head=ListNode(ls3[le-1])
        temp=head
        for i in range(le-2,-1,-1):
             temp.next=ListNode(ls3[i])
             temp=temp.next
          
        return head
   


l=ListNode(3)
l.next=ListNode(4)
l.next.next=ListNode(4)
la=ListNode(2)
la.next=ListNode(3)
la.next.next=ListNode(5)

S=Solution()
a=S.addTwoNumbers(l,la)

temp1=a

while temp1.next is not None :
    print(temp1.val)
    temp1=temp1.next