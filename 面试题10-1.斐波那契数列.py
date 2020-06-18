# -*- coding: utf-8 -*-
# @Time    : 2020-06-18 23:26
# @Author  : yangqiang
# @FileName: 面试题10-1.斐波那契数列.py
# @Blog    ：http://zhifei.online

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        res = [0, 1]
        for i in range(1, n):
            res.append(res[-1] + res[-2])
        return res[-1] % 1000000007
