class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i=0
        while  i<len(arr)-1 and arr[i+1]-arr[i]>0:
            i=i+1
        if i==0 or i==len(arr)-1:
            return False
        while i<len(arr)-1 and arr[i+1]-arr[i]<0:
            i=i+1
        return i==len(arr)-1
