#!/usr/bin/env python

class Solution(object):
    """
    leetcode easy question
    """
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative_num = x < 0
        if negative_num:
            x = abs(x)
        digit_str = str(x)
        digit_arr = list(digit_str)
        digit_arr.reverse()
        if negative_num:
            digit_arr.insert(0, '-')
        reversed_str = ''.join(digit_arr)
        result = int(reversed_str)
        if negative_num:
            if result < -2147483648:
                result = 0
        else:
            if result > 2147483647:
                result = 0
        return result

sol = Solution()
assert 321 == sol.reverse(123)
assert -321 == sol.reverse(-123)
assert 0 == sol.reverse(2147483647)
