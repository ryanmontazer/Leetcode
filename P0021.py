# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=list1
        curr2=list2
        head=ListNode(0)
        curr=head
        while True:
            if curr1 is None and curr2 is None:
                return head.next
            elif curr1 is None and curr2 is not None:
                curr.next=curr2
                curr=curr.next
                curr2=curr2.next
            elif curr2 is None and curr1 is not None:
                curr.next=curr1
                curr=curr.next
                curr1=curr1.next 
            elif curr1 is not None and curr2 is not None:
                if curr1.val<=curr2.val:
                    curr.next=curr1
                    curr=curr.next
                    curr1=curr1.next
                else:
                    curr.next=curr2
                    curr=curr.next
                    curr2=curr2.next
