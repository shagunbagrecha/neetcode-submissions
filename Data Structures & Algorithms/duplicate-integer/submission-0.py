class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elements = defaultdict(int)
        for num in nums:
            if num in elements:
                return True
            elements[num] = 0
        return False
        