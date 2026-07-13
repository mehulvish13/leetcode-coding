class Solution:
    def checkRecord(self, s: str) -> bool:
        # =====False when===
        # The student was absent ('A') for strictly fewer than 2 days total.
        # (len('A') >= 2 and 'A' in s) meaning 2 or more 'A'==

        # The student was never late ('L') for 3 or more consecutive days.
        # =='LLL' in s 

        if s.count('A')>= 2 or 'LLL' in s :
            return False
        else:
            return True