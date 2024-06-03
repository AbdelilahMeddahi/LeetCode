from math import dist
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key= lambda x : dist(x,[0,0]))
        return points[:k]
