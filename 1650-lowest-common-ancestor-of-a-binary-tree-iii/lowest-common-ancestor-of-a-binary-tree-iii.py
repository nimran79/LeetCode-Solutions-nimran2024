class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # Start both pointers at the given nodes.
        pointer_p = p
        pointer_q = q
      
        # Continue traversing up the tree until both pointers meet at the common ancestor.
        while pointer_p != pointer_q:
            # If pointer_a has a parent, move to the parent; otherwise, go to the other node's initial position.
            pointer_p = pointer_p.parent if pointer_p.parent else q
          
            # Do the same for pointer_b, going to the initial position of node_p if there's no parent.
            pointer_q = pointer_q.parent if pointer_q.parent else p
      
        # Once they meet, both pointer is the same and that's the lowest common ancestor.
        return pointer_p
