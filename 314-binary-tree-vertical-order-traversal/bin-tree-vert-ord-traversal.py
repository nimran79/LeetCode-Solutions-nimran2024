class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty, return an empty list.
        if not root:
            return []

        # Initialize a double-ended queue to hold nodes (tuples) along with their horizontal distances.
        queue = collections.deque([(0, root)])
        # Use a default dictionary to map horizontal distances to list of node values.
        column_items = collections.defaultdict(list)

        # To keep track of min and max dict keys
        min_x = float('inf')
        max_x = float('-inf')
  
        result = []  # define a result variable
      
        # Perform a breadth-first search
        while queue:
            x, current_node  = queue.popleft()
            # Append the node's value to the list of its respective horizontal distance.
            column_items[x].append(current_node.val)

            # Update min-max keys
            min_x = min(min_x, x)
            max_x = max(max_x, x)

            # If the left child exists, add it to the queue with the horizontal distance decremented.
            if current_node.left:
                 queue.append((x - 1, current_node.left))
            # If the right child exists, add it to the queue with the horizontal distance incremented.
            if current_node.right:
                queue.append((x + 1, current_node.right))

        # Rearrange the nodes from left to right
        for level in range (min_x, max_x + 1):
            result.append(column_items[level])

        return result
