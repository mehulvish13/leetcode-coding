class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def fun(piles,speed):
            time=0
            for pile in piles:
                time=time+pile//speed
                if pile%speed!=0:
                    time+=1
            return time
        k=-1#bananas-per-hour eating speed$0
        l=1#lowest speed of pile
        r=max(piles)#piles[-1] is not always highest unless array is sorted. max(piles) is correct.
        while l<=r:
            mid=(l+r)//2#speed
            hour=fun(piles,mid)
            if hour>h:
                l=mid+1
            else:
                k=mid
                r=mid-1
        return k
        