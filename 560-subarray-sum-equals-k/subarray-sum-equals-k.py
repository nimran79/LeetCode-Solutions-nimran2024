class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums: 
            return 0

        # Initialize a counter to keep track of the cumulative sums encountered
        prefix_dict = collections.defaultdict(int)
        prefix_dict[0] = 1

        # 'count_subarrays' will store the total count of subarrays that sum up to 'k'
        count_subarrays = 0
        # 'prefix_sum' holds the sum of numbers seen so far
        prefix_sum = 0

        for num in nums:
            prefix_sum += num

            # If there is a previous cumulative sum such that current_sum - k is equal
            # to that previous sum, then a subarray ending at the current position would sum to 'k'
            if prefix_sum - k in prefix_dict:
                count_subarrays += prefix_dict[prefix_sum - k]
            
            # Increase the count of the current prefix sum by 1 in the counter
            prefix_dict[prefix_sum] += 1

        return count_subarrays

        