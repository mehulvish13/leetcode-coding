import heapq
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n=len(s)
        ans = [''] * n
        for i in range(n):
            ans[indices[i]] = s[i]
        return ''.join(ans)
# my approach
        # heap=[]
        # n=len(s)
        # res=[]
        # for i in range(n):
        #     heapq.heappush(heap,(indices[i],s[i]))#store(4,'c')
        #     #i,s[i] never do these it sotres from 0 to n but the indice of that string 
        # while heap:
        #     res.append(heapq.heappop(heap)[1])
        # return ''.join(res)
    