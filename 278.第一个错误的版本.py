# -*- coding: utf-8 -*-
# @Time    : 2020-06-17 21:10
# @Author  : yangqiang
# @FileName: 278.第一个错误的版本.py
# @Blog    ：http://zhifei.online

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool


def isBadVersion(version):
    pass


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right - 1:
            if isBadVersion((left + right) // 2):
                right = (left + right) // 2
            else:
                left = (left + right) // 2
        return left if isBadVersion(left) else right
