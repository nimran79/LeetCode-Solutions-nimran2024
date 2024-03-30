# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flatten_list(nested_list):
            items  = []
            for item in nested_list:
                # If element is an integer, add it to the final list
                if item.isInteger():
                    items.append(item.getInteger())
                # Otherwise, get the nested list for next step of recursion
                else:
                    # using extend so that only flattened elements are added 
                    items.extend(flatten_list(item.getList()))  
                
            return items 
        
        # A list to store the flattened elements
        self.queue = collections.deque(flatten_list(nestedList))
        
    def next(self) -> int:
        # Returns the next integer in the flattened list, popleft for FIFO 
        return self.queue.popleft()
    
    def hasNext(self) -> bool:
        # Check if there are more integers in the queue
         return len(self.queue) != 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())