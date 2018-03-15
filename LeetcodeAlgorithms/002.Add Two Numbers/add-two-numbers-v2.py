#!/usr/bin/python3
# Author:Dalon Gao
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 23:32
# @Author  : Dallo Gao
# @Site    : 
# @File    : add-two-numbers-v2.py
# @Software: PyCharm

# Definition for singly-linked list.
import copy


# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    global results

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        self.new_add(l1, l2, False)
        return l1

    def new_add(self, l1, l2, flag=False):
        sum1 = 0
        if l1 is not None:
            sum1 += l1.val
        if l2 is not None:
            sum1 += l2.val
        if flag:
            sum1 += 1
        val = sum1
        flag = False
        if sum1 > 9:
            val = sum1 % 10
            flag = True
        if l1.next is None and l2.next is not None:
            l1.next = l2.__class__(0)
        elif l1.next is not None and l2.next is None:
            l2.next = l1.__class__(0)
        elif l1.next is None and l2.next is None and flag is True:
            l2.next = l1.__class__(0)
            l1.next = l2.__class__(0)
        l1.val = val
        l2.val = val
        if l1.next is not None or l2.next is not None or flag is True:
            self.new_add(l1.next, l2.next, flag=flag)
