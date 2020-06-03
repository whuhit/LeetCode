"""
@author: yangqiang
@contact: whuhit2020@gmail.com
@file: 面试题03.数组中重复的数字.py
@time: 2020-06-03 12:38
"""
"""
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findRepeatNumber(self, nums) -> int:
        d = dict()
        for element in nums:
            if element not in d:
                d[element] = 0
            else:
                return element
