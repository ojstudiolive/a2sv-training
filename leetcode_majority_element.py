class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_num = len(nums)//2
        for num in nums:
            count = sum(1 for m in nums if m==num)
            if count > majority_num:
                return num
