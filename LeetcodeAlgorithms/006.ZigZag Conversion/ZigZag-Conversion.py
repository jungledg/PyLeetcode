#!/usr/bin/python3
# Author:Dalon Gao
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 23:54
# @Author  : Dallo Gao
# @Site    : 
# @File    : ZigZag-Conversion.py
# @Software: PyCharm
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2 or len(s) <= numRows:
            return s
        re = ''
        for i in range(numRows):
            count = i
            while count < len(s):
                re += s[count]
                if i == 0 or i == (numRows - 1):
                    count += 2*numRows - 2
                else:
                    count += 2 * (numRows - i) - 2
                    if count >= len(s):
                        break
                    re += s[count]
                    count += 2*i

        return re

if __name__ == '__main__':
    solution = Solution()
    print(solution.convert("ABCDE", 4))
