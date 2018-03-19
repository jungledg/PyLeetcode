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
        a = "123"
        re_s = a[::-1]

    def _LCS(self, str1, str2):
        list_a = list(str1)
        list_b = list(str2)
        list_ab = [[0 for i in range(len(list_a) + 1)] for j in range(len(list_b) + 1)]
        for i, count_a in enumerate(list_a):
            for j, count_b in enumerate(list_b):
                # todo i==0,j==0
                if i == j:
                    list_ab[i][j] = list_ab[i - 1][j - 1] + 1

        pass
