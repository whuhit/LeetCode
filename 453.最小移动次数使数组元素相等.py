# -*- coding: utf-8 -*-
# @Time    : 2020-06-11 23:50
# @Author  : yangqiang
# @FileName: 453.最小移动次数使数组元素相等.py
# @Blog    ：http://zhifei.online
#
# 给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动将会使 n - 1 个元素增加 1。
#
#  
#
# 示例:
#
# 输入:
# [1,2,3]
#
# 输出:
# 3
#
# 解释:
# 只需要3次移动（注意每次移动会增加两个元素的值）：
#
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def minMoves(self, nums) -> int:
        return sum(nums)-len(nums)*min(nums)

# 纯数学计算就能算出来。
#
# x为次数，最终数组元素为y，原始数组最小数为min，
# 则 1、y=min+x
# 2、x *(n-1)+sum(nums) = y*len(nums)