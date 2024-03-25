from heapq import heapify, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # using min_heap
        heap = []
        for num in nums:
            # push all the elements onto a min-heap
            heapq.heappush(heap, num)
            
            # pop from the heap when the size exceeds k
            # Since it's min_heap popping removes the smallest element
            if len(heap) > k:
                heapq.heappop(heap)
        
        # top of the heap is the smallest element in min_heap
        return heap[0]
        