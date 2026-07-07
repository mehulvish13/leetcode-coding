class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f={}
        heap=[]
        for i in range(len(nums)):
            f[nums[i]]=f.get(nums[i],0)+1
        for ele,freq in f.items():
            curr=(freq,ele)
            if len(heap)<k:
                heapq.heappush(heap,curr)
                continue
            if curr[0]>heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap,curr)
        a=[]
        while heap:
            freq, ele = heapq.heappop(heap)
            a.append(ele)
        return a[:k]