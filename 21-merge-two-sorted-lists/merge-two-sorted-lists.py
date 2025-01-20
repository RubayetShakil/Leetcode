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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1=count(list1)
        c2=count(list2)
        i=j=0
        h=ListNode(None)
        head=h
        while list1!=None and list2!=None:
            if list1.val>=list2.val:
                head.next=ListNode(list2.val)
                j+=1
                list2=list2.next
            else:
                head.next=ListNode(list1.val)
                i+=1
                list1=list1.next
            head=head.next

        while i<c1:
            head.next=ListNode(list1.val)
            list1=list1.next
            head=head.next
            i+=1
        while j<c2:
            head.next=ListNode(list2.val)
            list2=list2.next
            head=head.next
            j+=1
        return h.next

