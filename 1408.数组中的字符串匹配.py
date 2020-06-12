# -*- coding: utf-8 -*-
# @Time    : 2020-06-12 22:06
# @Author  : yangqiang
# @FileName: 1408.数组中的字符串匹配.py
# @Blog    ：http://zhifei.online
#
# 给你一个字符串数组 words ，数组中的每个字符串都可以看作是一个单词。请你按 任意 顺序返回 words 中是其他单词的子字符串的所有单词。
#
# 如果你可以删除 words[j] 最左侧和/或最右侧的若干字符得到 word[i] ，那么字符串 words[i] 就是 words[j] 的一个子字符串。
#
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/string-matching-in-an-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def stringMatching(self, words):
        words = sorted(words,key=lambda i:len(i))
        res = []
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i] in words[j]:
                    res.append(words[i])
                    break
        return res

