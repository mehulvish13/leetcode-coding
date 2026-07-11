class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        heap=[]
        for i, row in enumerate(matrix):
            for j, ele in enumerate(row):
                heapq.heappush(heap,ele)
        for i in range(k-1):
            heapq.heappop(heap)
        a=heapq.heappop(heap)
        return a