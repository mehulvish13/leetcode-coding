class Solution:
    def addDigits(self, num: int) -> int:

        while num>=10:

            a=num%10
            b=num//10
            num=a+b
        return num
        # while num >= 10:
        #     res = 0
        #     while num:
        #         num, d = divmod(num, 10)
        #         res += d
        #     num = res
        # return num