# -*- coding: utf-8 -*-
# @Time    : 2020-06-02 23:05
# @Author  : yangqiang
# @FileName: 面试题50.第一个只出现一次的字符.py
# @Blog    ：http://zhifei.online

"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:

s = "abaccdeff"
返回 "b"

s = ""
返回 " "

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def firstUniqChar(self, s: str) -> str:
        # for c in s:
        #     if s.count(c) == 1:
        #         return c
        # return ' '
        dic = dict()
        for c in s:
            dic[c] = not c in dic
        for k, v in dic.items():
            if v: return k
        return ' '


if __name__ == '__main__':
    print(Solution().firstUniqChar("abaccdeff"))
