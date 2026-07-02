class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def fun(piles,n,mid):
            time=0
            for i in range(n):
                time=time+piles[i]//mid
                if piles[i]%mid!=0:
                    time+=1
            return time
        n=len(piles)
        k=-1#bananas-per-hour eating speed$0
        l=1#lowest speed of pile
        r=max(piles)#piles[-1] is not always highest unless array is sorted. max(piles) is correct.
        while l<=r:
            mid=(l+r)//2#speed
            hour=fun(piles,n,mid)
            if hour>h:
                l=mid+1
            else:
                k=mid
                r=mid-1
        return k
        