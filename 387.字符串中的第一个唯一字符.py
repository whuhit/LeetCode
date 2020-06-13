# -*- coding: utf-8 -*-
# @Time    : 2020-06-13 23:45
# @Author  : yangqiang
# @FileName: 387.字符串中的第一个唯一字符.py
# @Blog    ：http://zhifei.online

# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

# 示例：
#
# s = "leetcode"
# 返回 0
#
# s = "loveleetcode"
# 返回 2

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        for key in d:
            if d[key] == 1:
                return s.index(key)
        return -1
