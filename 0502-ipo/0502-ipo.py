import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n=len(profits)
        a=[]
        for i in range(n):
            a.append((capital[i],profits[i]))
        a.sort()
        i=0
        heap=[]
        while k:
            while i<n:
                if a[i][0]>w:
                    break
                heapq.heappush(heap,-a[i][1])
                i+=1
            if len(heap)==0:
                return w
            w=w+(-heap[0])
            heapq.heappop(heap)
            k-=1
        return w