import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq=Counter(s)#counting charater frequnecy
        max_freq = max(freq.values())
        if max_freq>(len(s)+1)//2:
            return ''
        ans=[]#initialise the ans array
        #build max heap
        heap=[]
        for char ,count in freq.items():
            heapq.heappush(heap,(-count,char))
        
        while len(heap)>1:
            #popping most freqent char
            cnt1,ch1=heapq.heappop(heap)
            cnt2,ch2=heapq.heappop(heap)
            ans.append(ch1)
            ans.append(ch2)
            # since count is -ve then inc the counts
            cnt1+=1
            cnt2+=1
            #pushing back isstill remaining
            if cnt1<0:
                heapq.heappush(heap, (cnt1, ch1))
            if cnt2<0:
                heapq.heappush(heap, (cnt2, ch2))

        if heap:#not empty
            ans.append(heap[0][1])#add max element
        return ''.join(ans)
# Complete Trace
# Iteration	Heap Before	Pop	ans	Counts After +1	Heap After Push
# 1	a3 b2 c1	a,b	ab	a2 b1	a2 c1 b1
# 2	a2 c1 b1	a,b	abab	a1 b0	a1 c1
# 3	a1 c1	a,c	ababac	a0 c0	empty