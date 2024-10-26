# -- DUPLICATE INTEGER -- 
from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = defaultdict()

        for num in nums:
            if num in result:
                return True
            else:
                result[num] = 1

        return False