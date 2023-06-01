class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # creating a set to remove duplicates from the list
        num_set = set()
        
        #looping through each element in list
        for num in nums:
            #checking if num appears in set
            if num in num_set:
                return True
            else:
                #adding num back to set because it was removed initially
                num_set.add(num)
