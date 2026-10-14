class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                # Return the index of the complement
                # and the current index
                return [seen[complement],i]

            # Store the current number and its index
            seen[num]=i
