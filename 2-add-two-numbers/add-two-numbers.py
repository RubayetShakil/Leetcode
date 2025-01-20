# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def count(head):
    x=0
    while head!=None:
        x+=1
        head=head.next
    return x


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i=j=x=0
        c1=count(l1)
        c2=count(l2)
        h=ListNode(None)
        head=h

        while l1!=None and l2!=None:
            sum=l1.val+l2.val+x
            if sum>9:
                s=str(sum)
                sum=int(s[1])
                x=1
            else:
                x=0
            head.next=ListNode(sum)
            head=head.next
            l1=l1.next
            l2=l2.next
            i+=1
            j+=1

        while i<c1:
            sum=x+l1.val
            if sum>9:
                s=str(sum)
                sum=int(s[1])
                x=1
            else:
                x=0
            head.next=ListNode(sum)
            head=head.next
            l1=l1.next
            i+=1
        while j<c2:
            sum=x+l2.val
            if sum>9:
                s=str(sum)
                sum=int(s[1])
                x=1
            else:
                x=0
            head.next=ListNode(sum)
            head=head.next
            l2=l2.next
            j+=1
        if x!=0:
            head.next=ListNode(x)

        return h.next

            



            

            
            
            
            


        