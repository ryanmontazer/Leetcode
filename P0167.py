class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length=len(numbers)
        left,right=0,length-1
        while left<right:
            if numbers[left]+numbers[right]==target:
                return [left+1,right+1]
            elif numbers[left]+numbers[right]>target:
                right-=1
            elif numbers[left]+numbers[right]<target:
                left+=1
        return [-1,-1]
