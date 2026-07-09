import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]#max heap store -ve values
        for w in stones:
            heapq.heappush(heap,-w)
        while len(heap)>1:
            x=-heapq.heappop(heap)#poped ele is -2 then to store in x we store -(-2)
            y=-heapq.heappop(heap)
            dif=abs(x-y)#calculating the diff
            if dif!=0:#if its not 0 then push into heap
                heapq.heappush(heap,-dif)#then again push the-ve of dif 
        if len(heap)==0:
            return 0
        else:
            return -heap[0]