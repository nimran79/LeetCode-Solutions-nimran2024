class Solution:
    def __init__(self, w: List[int]):
        # Initialize an empty list to store cumulative weights
        self.cumulative_weights = [0]
        # Build up the cumulative weight list for later binary search
        # cumulative_weights[-1] represents the cumulative sum at the end
        for weights in w:
            self.cumulative_weights.append(self.cumulative_weights[-1] + weights)

    def pickIndex(self) -> int:
        # Generate a random number between 1 and the total sum of weights
        target = random.randint(1, self.cumulative_weights[-1])
        # Perform a binary search to find the target within the cumulative weights
        left, right = 1, len(self.cumulative_weights) - 1
        while left < right:
            # Calculate the middle index
            mid = (left + right) // 2
            # Since we want to find the first element that is not less than the target,
            # move the right pointer to mid if the middle cumulative weight is >= target
            if self.cumulative_weights[mid] >= target:
                right = mid
            # Otherwise, move the left pointer to one after the current middle
            else:
                left = mid + 1
        # The final index will be left - 1, since the cumulative_weights includes
        # an extra 0 at the beginning that we added during initialization
        return left - 1
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()