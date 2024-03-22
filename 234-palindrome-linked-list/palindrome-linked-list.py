# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers, slow moves one step at a time, fast moves two steps
        slow = fast = head
        
        # Move fast pointer to the end of the list, and slow to the middle node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
      
        # Reverse the second half of the list
        prev_node = None
        while slow:
            next_node = slow.next
            slow.next = prev_node
            prev_node = slow
            slow = next_node
        
        # 'prev_node' now points to the head of the reversed second half.
        # Compare the first half and the reversed second half
        while head and prev_node:  # Compare first and second half
            if head.val != prev_node.val:
                return False
            head = head.next
            prev_node = prev_node.next 
      
        # If all nodes matched, it's a palindrome
        return True
        