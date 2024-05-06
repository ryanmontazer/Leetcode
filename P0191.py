# Time: O(32)
# Space: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        result=0
        while n>0:
            result+=n%2
            n=n>>1
        return result
