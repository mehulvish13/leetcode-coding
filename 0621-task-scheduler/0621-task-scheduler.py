import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):

        # Count frequency of every task
        freq = Counter(tasks)

        # Max heap of frequencies
        # Python has min heap, so store negative frequencies
        heap = [-f for f in freq.values()]
        heapq.heapify(heap)

        # Stores tasks in cooldown
        # (remaining_frequency, available_time)
        cooldown = []

        # Current CPU time
        time = 0

        # Continue until every task is completed
        while heap or cooldown:

            # Every iteration = one unit of CPU time
            time += 1

            # If some task is available, execute it
            if heap:

                # Remove task with highest remaining frequency
                f = heapq.heappop(heap)

                # One occurrence executed
                # Example:
                # -3 -> -2
                # -2 -> -1
                # -1 -> 0 (finished)
                f += 1

                # If task still remains,
                # send it to cooldown instead of heap
                if f != 0:
                    # Available again after n intervals
                    cooldown.append((f, time + n))

            # Check whether first cooldown task is ready
            # Cooldown list is naturally sorted by available time
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(heap, cooldown[0][0])
                cooldown.pop(0)

        return time
        # freq = Counter(tasks)
        # maxFreq = max(freq.values())
        # maxCount = 0
        # for f in freq.values():
        #     if f == maxFreq:
        #         maxCount += 1
        # return max(len(tasks), (maxFreq - 1) * (n + 1) + maxCount)