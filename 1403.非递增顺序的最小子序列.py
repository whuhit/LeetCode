# -*- coding: utf-8 -*-
# @Time    : 2020-06-29 23:44
# @Author  : yangqiang
# @FileName: 1403.非递增顺序的最小子序列.py
# @Blog    ：http://zhifei.online

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        sum_ = sum(nums)
        nums = sorted(nums,reverse=True)
        res = []
        sum_2 = 0
        for i in nums:
            res.append(i)
            sum_2 += i
            if sum_2 > sum_ //2:
                break
        return res

