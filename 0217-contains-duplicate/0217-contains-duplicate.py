class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        f=set()
        for i in range(len(nums)):
            if nums[i] in f:
                return True
            else:
                f.add(nums[i])
        return False
