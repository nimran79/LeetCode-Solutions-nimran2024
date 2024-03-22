class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # First push all data in stack, and then traverse linked list and keep poping element from stack one by one, so stack will give you element from last.
        list_vals = []
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        curr = head
        while curr and curr.val == stack.pop():
            curr = curr.next
        return curr is None
