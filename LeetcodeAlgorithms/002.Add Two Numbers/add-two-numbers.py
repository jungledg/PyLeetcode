#!/usr/bin/python3
# Author:Dalon Gao
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 22:13
# @Author  : Dallo Gao
# @Site    : 
# @File    : add-two-numbers.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1.pre = None
        l2.pre = None
        self.result(l1)
        tmp1 = l1
        while tmp1.next is not None:
            tmp1 = tmp1.next
        first = 0
        while tmp1 is not None:
            first = first * 10 + int(tmp1.val)
            tmp1 = tmp1.pre

        self.result(l2)
        tmp2 = l2
        while tmp2.next is not None:
            tmp2 = tmp2.next
        second = 0

        while tmp2 is not None:
            second = second * 10 + int(tmp2.val)
            tmp2 = tmp2.pre
        enough = first + second
        unit = enough % 10
        while enough > 0:

            pass
        return

    def result(self, node):
        if node.next is not None:
            next = self.result(node=node.next)
            next.pre = node
        return node


if __name__ == '__main__':
    solution = Solution()
    l1 = ListNode("2")
    l2 = ListNode("4")
    l3 = ListNode("3")
    l4 = ListNode("5")
    l5 = ListNode("6")
    l6 = ListNode("4")
    l1.next = l2
    l2.next = l3
    l4.next = l5
    l5.next = l6
    print(solution.addTwoNumbers(l1=l1, l2=l4))
