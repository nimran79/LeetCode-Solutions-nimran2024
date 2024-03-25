# Time: O(n), Space: O(n)
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        seen = []

        while p:
            seen.append(p)
            p = p.parent
        
        while q:
            if q in seen:
                return q    # return result when p & q meet
            q = q.parent
