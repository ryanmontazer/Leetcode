class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length=len(nums)
        i=1
        for j in range(1,length):
            if nums[j] != nums[j-1]:
                nums[i]=nums[j]
                i+=1
        return i
