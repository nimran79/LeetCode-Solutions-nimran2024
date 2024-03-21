# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        curr_node = head
        next_node  = None
        
        while curr_node is not None:
            # Save the next node
            next_node = curr_node.next

            # Reverse the link so that current_node.next points to the node before it
            curr_node.next = prev_node
            prev_node = curr_node

            # Move to the next node in the original linked list
            curr_node = next_node

        # prev_node now points to the head of the reversed list
        return prev_node
        