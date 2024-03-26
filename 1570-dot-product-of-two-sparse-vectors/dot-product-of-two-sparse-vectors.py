class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = []
        # Create tuples with <index,value> pairs
        # This will run for both sparse vectors during initialization
        for index, value in enumerate(nums):
            if value != 0:
                self.pairs.append([index, value])
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_product = 0
        p, q = 0, 0

        while p < len(self.pairs) and q < len(vec.pairs):
            # Compare the key of the p-th element of 1st vector with 
            # the key of the q-th element of the 2nd vector
            if self.pairs[p][0] == vec.pairs[q][0]:
                # Since keys matched, perform dot product
                dot_product += self.pairs[p][1] * vec.pairs[q][1]
                p += 1
                q += 1
            elif self.pairs[p][0] < vec.pairs[q][0]:
                p += 1
            else:
                q += 1

        return dot_product
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
