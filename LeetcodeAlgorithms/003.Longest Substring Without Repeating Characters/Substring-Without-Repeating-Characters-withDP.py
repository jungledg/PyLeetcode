#!/usr/bin/python3
# Author:Dalon Gao
# -*- coding: utf-8 -*-
# @Time    : 2018/3/17 21:04
# @Author  : Dallo Gao
# @Site    : 
# @File    : Substring-Without-Repeating-Characters-withDP.py
# @Software: PyCharm
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("pwwkewww"))
