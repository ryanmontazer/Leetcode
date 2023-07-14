# Time: O(n log(k))
# Space: O(k)
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap=[]
        for i in range(len(points)):
            distance=sqrt(points[i][0]**2+points[i][1]**2)
            heapq.heappush(max_heap,[-distance,points[i][0],points[i][1]])
            if len(max_heap)>k:
                heapq.heappop(max_heap)
        for element in max_heap:
            element.pop(0)
        return max_heap
