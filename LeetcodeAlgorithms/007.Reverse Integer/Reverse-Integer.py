#!/usr/bin/python3
# Author:Dalon Gao
# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 22:08
# @Author  : Dallo Gao
# @Site    : 
# @File    : Reverse-Integer.py
# @Software: PyCharm

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = True
        if x < 0:
            flag = False
        x = abs(x)
        x_str = str(x)
        x_str = x_str[::-1]
        res = int(x_str)
        if res > (2 ** 31):
            res = 0
        if flag is False:
            return -res
        else:
            return res


if __name__ == '__main__':
    solution = Solution()
    a = "abc"
    print(a[::-1])
    print(2**32)
    print(solution.reverse(1563847412))
