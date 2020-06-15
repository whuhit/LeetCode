# -*- coding: utf-8 -*-
# @Time    : 2020-06-15 21:34
# @Author  : yangqiang
# @FileName: 260.只出现一次的数字3.py
# @Blog    ：http://zhifei.online

# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
#
# 示例 :
#
# 输入: [1,2,1,3,2,5]
# 输出: [3,5]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/single-number-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from collections import Counter
class Solution:
    def singleNumber(self, nums):
        hashmap = Counter(nums)
        return [x for x in hashmap if hashmap[x] == 1]
