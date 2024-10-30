class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numSet = set(nums)
        
        for num in nums:
            if (num - 1) not in numSet:
                counter = 1
                while(num + counter) in numSet:
                    counter += 1
                res = max(res, counter)

        return res