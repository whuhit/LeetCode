# -*- coding: utf-8 -*-
# @Time    : 2020-06-29 23:28
# @Author  : yangqiang
# @FileName: 215.数组中的第K个最大元素.py
# @Blog    ：http://zhifei.online


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums,reverse=True)[k-1]
