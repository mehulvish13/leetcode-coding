class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for x,y in points:
            dis=-(x**2+y**2)#1-0 ka sq and 3-0 ka 2 1^2 and 3^2
            if len(heap)<k:
                heapq.heappush(heap,(dis,[x,y]))
                continue
            if dis>heap[0][0]:#heap[0][0] ka top means largest
                heapq.heapreplace(heap, (dis, [x, y]))
        a=[]
        while heap:
            _, ele = heapq.heappop(heap)
            a.append(ele)
        return a[:k]
'''
For every point

    distance = x² + y²

    Make distance negative

    If heap size < k

        Push

    Else

        If new distance > heap top

            Replace

Return all points'''