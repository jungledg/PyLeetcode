#!/usr/bin/python3
# Author:Dalon Gao
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 23:30
# @Author  : Dallo Gao
# @Site    : 
# @File    : Substring Without Repeating Characters.py
# @Software: PyCharm

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        record_lenth = 0
        for num, ch in enumerate(s):
            if ch not in d:
                d[ch] = num
            else:
                old_mark = d[ch]
                for key in list(d.keys()):
                    if d[key] <= old_mark:
                        del(d[key])
                d[ch] = num
            long = len(d)
            if long > record_lenth:
                record_lenth = long
        return record_lenth

if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("pwwkewww"))
