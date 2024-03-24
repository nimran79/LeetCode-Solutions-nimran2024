# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0] if len(lists) > 0 else None # return empty for null array of lists

    def merge2Lists(self, l1, l2):
        current = dummy = ListNode()
        while l1 and l2:    # When neither list is empty
            if l1.val <= l2.val:
                current.next = l1   # Append list1 node to merged list
                l1 = l1.next     # Move to the next node in list1
            else:
                current.next = l2   # Append list2 node to merged list
                l2 = l2.next     # Move to the next node in list2
            
            # Move the current pointer forward in the merged list
            current = current.next
      
        # Add any remaining nodes from list1 or list2 to the merged list
        # If one list is fully traversed, append the rest of the other list
        current.next = l1 if l1 else l2
    
        # The dummy node's next pointer points to the head of the merged list
        return dummy.next
        