"""
@author: yangqiang
@contact: whuhit2020@gmail.com
@file: 342.4的幂.py
@time: 2020-06-06 23:30
"""
"""
给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。

示例 1:

输入: 16
输出: true
示例 2:

输入: 5
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-four
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        while num >= 4:
            if num % 4 == 0:
                num /= 4
            else:
                return False
        if num != 1:
            return False
        return True
