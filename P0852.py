# Time: O(n)
# Space: O(1)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left,right=1,len(arr)-2
        while left<right:
            mid=(left+right)//2
            if arr[mid]>arr[mid+1]:
                right=mid
            else:
                left=mid+1
        return left
