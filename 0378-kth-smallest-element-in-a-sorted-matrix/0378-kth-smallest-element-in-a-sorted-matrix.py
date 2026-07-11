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
# Approach 1: Flatten & Sort (Brute Force)

# This is the most straightforward approach. Since we need the nth smallest element overall, we can flatten the 2D matrix into a 1D array, sort the array in ascending order, and return the element at index $k-1$.

# from typing import List

# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         flat_list = []
        
#         # Flatten the 2D matrix into a 1D list
#         for row in matrix:
#             flat_list.extend(row)
            
#         # Sort the flattened list
#         flat_list.sort()
        
#         # Return the k-th element (0-indexed, so we look at k - 1)
#         return flat_list[k - 1]


# Complexity

# Time Complexity: $\mathcal{O}(n^2 \log(n^2)) = \mathcal{O}(n^2 \log n)$

# Flattening the $n \times n$ matrix takes $\mathcal{O}(n^2)$ time.

# Sorting an array of size n $n^2$ takes $\mathcal{O}(n^2 \log(n^2))$ time.

# Space Complexity: $\mathcal{O}(n^2)$ to store the flattened array of size $n^2$.

# Approach 2: Max-Heap of Size $k$

# Instead of storing and sorting all $n^2$ elements, we can maintain a max heap of size $k$. As we iterate through the matrix, we push elements onto the heap. If the heap size exceeds it, we pop the largest element. At the end of the iteration, the top of our max-heap will be the nth smallest element.

# To implement a max-heap in Python, we negate values because Python's heapq is a min-heap by default.

# import heapq
# from typing import List

# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         max_heap = []
        
#         for r in range(len(matrix)):
#             for c in range(len(matrix[0])):
#                 val = matrix[r][c]
#                 # Push negative value to simulate max-heap behavior
#                 heapq.heappush(max_heap, -val)
                
#                 # If the heap exceeds size k, pop the largest element
#                 if len(max_heap) > k:
#                     heapq.heappop(max_heap)
                    
#         # The top of the max-heap is our kth smallest element (re-negated)
#         return -max_heap[0]


# Complexity

# Time Complexity: $\mathcal{O}(n^2 \log k)$

# Iterating through all $n^2$ elements takes $\mathcal{O}(n^2)$ loops.

# Each heap insertion/extraction takes $\mathcal{O}(\log k)$ time since the heap size is capped.

# Space Complexity: $\mathcal{O}(k)$ to maintain a heap of size $k$.

# Approach 3: Min-Heap / K-Way Merge (Optimal for Small $k$)

# Since every row in the matrix is already sorted, we can treat this problem as merging $n$ sorted lists.

# We initialize a min-heap containing the first element of each row. We then pop the smallest element from the heap. If there is a next element in the same row, we push it into the heap. We repeat this pop-and-push sequence many $k$ times. The "th" popped element is our answer.

# import heapq
# from typing import List

# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         n = len(matrix)
#         min_heap = []
        
#         # Initialize heap with the first element of each row
#         # Store as: (value, row_index, column_index)
#         # We only need to check up to min(n, k) rows
#         for r in range(min(n, k)):
#             heapq.heappush(min_heap, (matrix[r][0], r, 0))
            
#         # Pop from the heap k-1 times
#         for _ in range(k - 1):
#             val, r, c = heapq.heappop(min_heap)
            
#             # If there is another element in the same row, push it to the heap
#             if c + 1 < n:
#                 heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
                
#         # The k-th pop gives us the k-th smallest element
#         return heapq.heappop(min_heap)[0]


# Complexity

# Time Complexity: $\mathcal{O}(X \log X + k \log X)$ where $X = \min(n, k)$

# Initializing the heap with $X$ elements takes $\mathcal{O}(X \log X)$ time.

# We perform $k$ pop/push operations, each taking $\mathcal{O}(\log X)$ time.

# For the complexity simplifies to $\mathcal{O}(k \log k)$. For the worst-case, it becomes $\mathcal{O}(n \log n + n^2 \log n) = \mathcal{O}(n^2 \log n)$.

# Space Complexity: $\mathcal{O}(\min(n, k))$ to store the heap elements.

# Approach 4: Binary Search on Value Range (Highly Optimal)

# Instead of searching by row/column index, we can perform a binary search on the value range of the matrix. The minimum possible value is ___, matrix[0][0] and the maximum is ___.

# For any candidate value mid:

# We count how many elements in the matrix are less than or equal to it.

# Because the rows and columns are sorted, we can count this in $\mathcal{O}(n)$ time using a saddleback search starting from the bottom-left corner of the matrix.

# Based on the count:

# If the count is $\ge k$, then the nth smallest element is less than or equal to mid (we search left).

# If the count is $< k$, then the nth smallest element must be strictly greater than mid (we search right).

# from typing import List

# class Solution:
#     def countLessOrEqual(self, matrix: List[List[int]], target: int) -> int:
#         """
#         Counts the number of elements in the sorted matrix that are <= target
#         using a saddleback search starting from the bottom-left corner.
#         """
#         n = len(matrix)
#         count = 0
        
#         # Start at the bottom-left corner
#         row = n - 1
#         col = 0
        
#         while row >= 0 and col < n:
#             if matrix[row][col] <= target:
#                 # If current element is <= target, then all elements 
#                 # above it in this column are also <= target.
#                 count += (row + 1)
#                 # Move to the next column to look for larger elements
#                 col += 1
#             else:
#                 # If current element is > target, move up to a smaller element
#                 row -= 1
                
#         return count

#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         n = len(matrix)
        
#         # Search range boundaries
#         low = matrix[0][0]
#         high = matrix[n - 1][n - 1]
        
#         while low < high:
#             mid = (low + high) // 2
            
#             # Count elements <= mid
#             if self.countLessOrEqual(matrix, mid) >= k:
#                 # The target is in the left half (including mid)
#                 high = mid
#             else:
#                 # The target is strictly in the right half
#                 low = mid + 1
                
#         return low


# Complexity

# Time Complexity: $\mathcal{O}(n \log(\text{Max} - \text{Min}))$



# Comparison Cheat Sheet

# Approach

# Time Complexity

# Space Complexity

# Best For

# Interview Rating

# 1. Flatten & Sort

# $\mathcal{O}(n^2 \log n)$

# $\mathcal{O}(n^2)$

# Quick, direct implementation

# ⭐⭐

# 2. Max-Heap (size $k$)

# $\mathcal{O}(n^2 \log k)$

# $\mathcal{O}(k)$

# Simple streaming alternative

# ⭐⭐⭐

# 3. Min-Heap (K-Way)

# $\mathcal{O}(k \log (\min(n, k)))$

# $\mathcal{O}(\min(n, k))$

# Small value of $k$ relative to $n^2$

# ⭐⭐⭐⭐⭐

# 4. Binary Search

# $\mathcal{O}(n \log(\text{Max} - \text{Min}))$

# $\mathcal{O}(1)$

# Large matrices / Strict space constraints

# ⭐⭐⭐⭐⭐

# 💡 Interview Tips

# Clarify Constraints: Ask your interviewer about the dimensions of the matrix $n$ and its value. If it $k$ is extremely small (e.g.), Approach 3 (Min-Heap) is actually faster than Binary Search. If so, Approach 4 (Binary Search) is vastly superior.

# Master Saddleback Search: The utility function countLessOrEqual is the core of the binary search strategy. Be prepared to explain why starting from the bottom-left (or top-right) allows you to make binary decisions (move up or move right) in $\mathcal{O}(n)$ time instead of scanning the entire matrix.

# Floating vs. Integer Matrix: In integer-only matrices, standard binary search splits perfectly. If the interviewer asks about a floating-point matrix, remind them you'd adjust the search loop termination to a precision tolerance, for example.