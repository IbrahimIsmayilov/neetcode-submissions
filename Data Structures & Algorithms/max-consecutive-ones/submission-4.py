class Solution:
    # Steps: 
    # 1. Make 2 variables to keep track of the current consecutive 1s and the maximum consecutive 1s recorded while iterating the list. Start iterating the list from the beginning of the list
    # 2. Increment count if the element being iterated is a 1. Else, check if the count of consecutive 1s is the maximum amount, update if so, and reset count. 
    # 3. Add a final check once the for loop finishes to update max count if the iteratiion finished while counting consecutive 1s. Return the maxiumum count of consecutive 1s.
    
    # Overview: In the list nums, return the maximum number of consecutive 1s in the list. 
    # Time Complexity: O(n), where n represents the length of the lust nums
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for num in nums:
            count = count + 1 if num else 0
            max_count = max(count, max_count)

        return max_count