#!/usr/bin/python3
# Author:Dalon Gao
# -*- coding: utf-8 -*-
# @Time    : 2018/3/11 20:41
# @Author  : Dallo Gao
# @Site    : 
# @File    : two-sum.py
# @Software: PyCharm
'''
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        results = {}
        for count, value in enumerate(nums):
            tmp = target - value
            if tmp in results:
                return [results[tmp], count]
            results[value] = count

if __name__ == '__main__':
    solution = Solution()
    test_list = [-1, -2, -3, -4, -5]
    test_target = -8
    print(solution.twoSum(test_list, test_target))
