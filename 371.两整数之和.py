# -*- coding: utf-8 -*-
# @Time    : 2020-06-20 23:50
# @Author  : yangqiang
# @FileName: 371.两整数之和.py
# @Blog    ：http://zhifei.online

# 不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

#在位运算操作中，异或的一个重要特性是无进位加法。

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 异或就是无进位相加
        MASK = 0x100000000
        # 整型最大值
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        while b != 0:
            # 计算进位
            carry = (a & b) << 1
            # 取余范围限制在 [0, 2^32-1] 范围内
            a = (a ^ b) % MASK
            b = carry % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)
