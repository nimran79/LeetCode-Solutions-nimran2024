# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Creating a dummy node which helps to easily return the head of the merged list
        dummy = ListNode()
      
        # Current node is used to keep track of the end of the merged list
        current = dummy
      
        # Iterate while both lists have nodes
        while list1 and list2:
            # Choose the smaller value from either list1 or list2
            if list1.val <= list2.val:
                current.next = list1   # Append list1 node to merged list
                list1 = list1.next     # Move to the next node in list1
            else:
                current.next = list2   # Append list2 node to merged list
                list2 = list2.next     # Move to the next node in list2
          
            # Move the current pointer forward in the merged list
            current = current.next
      
        # Add any remaining nodes from list1 or list2 to the merged list
        # If one list is fully traversed, append the rest of the other list
        current.next = list1 if list1 else list2
      
        # The sentinel node's next pointer points to the head of the merged list
        return dummy.next
        