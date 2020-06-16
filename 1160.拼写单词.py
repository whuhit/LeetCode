# -*- coding: utf-8 -*-
# @Time    : 2020-06-16 22:30
# @Author  : yangqiang
# @FileName: 1160.拼写单词.py
# @Blog    ：http://zhifei.online

class Solution:
    def know(self, word, chars):
        lc = list(chars)
        for c in word:
            if c not in lc:
                return False
            else:
                lc.remove(c)
        return True

    def countCharacters(self, words, chars) -> int:
        res = 0
        for word in words:
            if self.know(word, chars):
                res += len(word)
        return res


words = ["cat", "bt", "hat", "tree"]
chars = "atach"

print(Solution().countCharacters(words, chars))
