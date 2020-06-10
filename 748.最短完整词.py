# -*- coding: utf-8 -*-
# @Time    : 2020-06-10 21:51
# @Author  : yangqiang
# @FileName: 748.最短完整词.py
# @Blog    ：http://zhifei.online
#
# 如果单词列表（words）中的一个单词包含牌照（licensePlate）中所有的字母，那么我们称之为完整词。在所有完整词中，最短的单词我们称之为最短完整词。
#
# 单词在匹配牌照中的字母时不区分大小写，比如牌照中的 "P" 依然可以匹配单词中的 "p" 字母。
#
# 我们保证一定存在一个最短完整词。当有多个单词都符合最短完整词的匹配条件时取单词列表中最靠前的一个。
#
# 牌照中可能包含多个相同的字符，比如说：对于牌照 "PP"，单词 "pair" 无法匹配，但是 "supper" 可以匹配。
#
#  
#
# 示例 1：
#
# 输入：licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
# 输出："steps"
# 说明：最短完整词应该包括 "s"、"p"、"s" 以及 "t"。对于 "step" 它只包含一个 "s" 所以它不符合条件。同时在匹配过程中我们忽略牌照中的大小写。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shortest-completing-word
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def isPlate(self, s1, s2):
        x2 = []
        for c in s2:
            if c.isalpha():
                x2.append(c.lower())
        x1 = []
        for c in s1:
            x1.append(c)
        for c in x2:
            if c in x1:
                x1.remove(c)
            else:
                return False
        return True

    def shortestCompletingWord(self, licensePlate, words):
        num = 16
        res = ""
        for word in words:
            if len(word) >= num:
                continue
            if self.isPlate(word, licensePlate):
                num = len(word)
                res = word
        return res


res = Solution().shortestCompletingWord(
    "1s3 PSt", ["step", "steps", "stripe", "stepple"])

print(res)
