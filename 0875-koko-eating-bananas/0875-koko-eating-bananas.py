class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def fun(speed):#condition function
            time=0
            for pile in piles:
                time=time+(pile+speed-1)//speed
            return time
        k=-1#bananas-per-hour eating speed$0
        l=1#lowest speed of pile
        r=max(piles)#piles[-1] is not always highest unless array is sorted. max(piles) is correct.
        while l<=r:
            mid=(l+r)//2#speed
            hour=fun(mid)
            if hour>h:
                l=mid+1#❌ Speed too slow. so Need a larger speed,Move Right.
            else:#hours <= h #speed works butTry finding a smaller speed.
                k=mid
                r=mid-1
        return k
        