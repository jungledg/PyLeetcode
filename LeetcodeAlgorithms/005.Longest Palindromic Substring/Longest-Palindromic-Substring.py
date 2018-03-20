#!/usr/bin/python3
# Author:Dalon Gao
# -*- coding: utf-8 -*-
# @Time    : 2018/3/17 21:24
# @Author  : Dallo Gao
# @Site    : 
# @File    : Longest-Palindromic-Substring.py
# @Software: PyCharm
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # TODO simplify code
        record = 0
        r_str = ''
        for index in range(len(s)):
            single_left, single_right = self.singleNode(s, index)
            single_length = single_right - single_left
            if single_length >= record:
                record = single_length
                r_str = s[single_left:single_right + 1]
            double_left, double_right = self.doubleNode(s, index)
            double_length = double_right - double_left
            if double_length >= record:
                record = double_length
                r_str = s[double_left:double_right + 1]
        return r_str

    def singleNode(self, s, index):
        if index < 0 or index >= len(s):
            return 0, 0
        if index == 0 or index == len(s) - 1:
            return index, index
        left = index
        right = index
        while s[left] == s[right]:
            left -= 1
            right += 1
            if left < 0 or right >= len(s):
                break
        return left + 1, right - 1

    def doubleNode(self, s, index):
        if index < 0 or index >= len(s) - 1 or s[index] != s[index + 1]:
            return 0, 0
        left = index
        right = index + 1
        while s[left] == s[right]:
            left -= 1
            right += 1
            if left < 0 or right >= len(s):
                break
        return left + 1, right - 1


if __name__ == '__main__':
    solution = Solution()
    s = "babad"
    print(solution.longestPalindrome(s))
