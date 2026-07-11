class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap=[]
        m=len(mat)
        n=len(mat[0])
        for i in range(m):
            a=0
            for j in range(n):
                if mat[i][j]==1:
                    a+=1
            heapq.heappush(heap,(a,i))
        ans=[]
        for i in range(k):
            x,y=heapq.heappop(heap)
            ans.append(y)
        return ans
# Approach 1: Simple Summation + Sorting (Cleanest)

# This is the most intuitive and readable approach. It leverages Python's built-in sorting behavior, which naturally handles tie-breakers when sorting lists of tuples.

# Python Code

# from typing import List

# class Solution:
#     def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
#         # Store tuples of (soldier_count, row_index)
#         rows = []
        
#         for i, row in enumerate(mat):
#             # sum(row) works because soldiers (1) always precede civilians (0)
#             rows.append((sum(row), i))
            
#         # Sort rows. Python sorts tuples element-by-element:
#         # First, by sum(row) ascending.
#         # Second, by index ascending (acts as the perfect tie-breaker!)
#         rows.sort()
        
#         # Extract the original indices of the first k elements
#         return [index for _, index in rows[:k]]

# Time Complexity: $\mathcal{O}(m \cdot n + m \log m)$

# Calculating the sum of each row of length $n$ takes $\mathcal{O}(m \cdot n)$ time.

# Sorting $m$ elements takes $\mathcal{O}(m \log m)$ time.

# Space Complexity: $\mathcal{O}(m)$ to store the array of $m$ tuples.

# Approach 2: Simple Summation + Min Heap


# Python Code

# import heapq
# from typing import List

# class Solution:
#     def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
#         heap = []
        
#         # Populate the heap with (soldier_count, row_index)
#         for i, row in enumerate(mat):
#             heapq.heappush(heap, (sum(row), i))
            
#         ans = []
#         # Pop the k smallest elements (weakest rows) from the heap
#         for _ in range(k):
#             _, index = heapq.heappop(heap)
#             ans.append(index)
            
#         return ans
# Time Complexity: $\mathcal{O}(m \cdot n + m \log m)$ (In Python, individual heappush operations take log-time. Pop takes $\mathcal{O}(k \log m)$).

# Approach 3: Binary Search + Sorting (Optimal Counting)
# Python Code

# from typing import List

# class Solution:
#     def countSoldiers(self, row: List[int]) -> int:
#         # Standard binary search to find the index of the first 0
#         left = 0
#         right = len(row)
        
#         while left < right:
#             mid = (left + right) // 2
#             # If current element is 1, the first 0 is further right
#             if row[mid] == 1:
#                 left = mid + 1
#             # If current element is 0, the first 0 is here or to the left
#             else:
#                 right = mid
                
#         # 'left' will point to the count of 1s in the row
#         return left
#     def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
#         rows = []
#         for i, row in enumerate(mat):
#             # Count soldiers efficiently using binary search
#             soldiers = self.countSoldiers(row)
#             rows.append((soldiers, i))
#         # Sort by soldier count, then by index
#         rows.sort()
#         # Get indices of the k weakest rows
#         return [index for _, index in rows[:k]]
# Complexity

# Time Complexity: $\mathcal{O}(m \log n + m \log m)$


# Approach 4: Binary Search + Min Heap

# This approach combines the $\mathcal{O}(\log n)$ binary search counting technique with a standard min-heap for selection.
# Python Code
# import heapq
# from typing import List

# class Solution:
#     def countSoldiers(self, row: List[int]) -> int:
#         left = 0
#         right = len(row)
        
#         while left < right:
#             mid = (left + right) // 2
#             if row[mid] == 1:
#                 left = mid + 1
#             else:
#                 right = mid
#         return left

#     def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
#         heap = []
        
#         for i, row in enumerate(mat):
#             soldiers = self.countSoldiers(row)
#             # Push into the min heap
#             heapq.heappush(heap, (soldiers, i))
            
#         ans = []
#         # Pull out the k weakest items
#         for _ in range(k):
#             _, index = heapq.heappop(heap)
#             ans.append(index)
            
#         return ans
# Complexity
# Time Complexity: $\mathcal{O}(m \log n + m \log m)$

# Approach 5: Binary Search + Max Heap of Size $k$ (Optimal for Large Datasets)

# To implement a max-heap in Python, we negate the values because Python's heapq is a min-heap by default.

# import heapq
# from typing import List

# class Solution:
#     def countSoldiers(self, row: List[int]) -> int:
#         left, right = 0, len(row)
#         while left < right:
#             mid = (left + right) // 2
#             if row[mid] == 1:
#                 left = mid + 1
#             else:
#                 right = mid
#         return left
#     def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
#         heap = []
#         for i, row in enumerate(mat):
#             soldiers = self.countSoldiers(row)
#             # Since heapq is a min-heap, we push negative values
#             # to simulate a max-heap. 
#             # We negate both values: (-soldiers, -index)
#             # This ensures that the strongest row (highest soldiers, highest index)
#             # rises to the top of the heap to be evicted first.
#             heapq.heappush(heap, (-soldiers, -i))
#             # If our candidate list exceeds size k, evict the strongest row
#             if len(heap) > k:
#                 heapq.heappop(heap)
#         ans = []
#         # The heap now contains the k weakest rows, but unsorted and negated.
#         while heap:
#             soldiers, index = heapq.heappop(heap)
#             # Revert the negation of the index
#             ans.append(-index)
#         # Since we popped from a max-heap, the weakest element is at the end of ans.
#         # Reverse the array to order from weakest to strongest.
#         return ans[::-1]
# Time Complexity: $\mathcal{O}(m \log n + m \log k)$

# Approach 6: Pythonic One-Liner
# from typing import List
# class Solution:
#     def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
#         # Sort row indices directly using a custom key
#         return sorted(range(len(mat)), key=lambda i: (sum(mat[i]), i))[:k]