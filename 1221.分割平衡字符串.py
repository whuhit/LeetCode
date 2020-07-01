# -*- coding: utf-8 -*-
# @Time    : 2020-07-01 23:32
# @Author  : yangqiang
# @FileName: 1221.分割平衡字符串.py
# @Blog    ：http://zhifei.online


def balancedStringSplit(s):
    if not s:
        return 0
    res = 0
    i = 2
    while i <= len(s):
        if s[:i].count("L") == i // 2:
            res += 1
            s = s[i:]
            i = 2
        else:
            i += 2
    return res


def balancedStringSplit2(s):
    cnt = 0
    balance = 0;
    for i in range(len(s)):
        if s[i] == 'L':
            balance -= 1
        if s[i] == 'R':
            balance += 1
        if balance == 0:
            cnt += 1
    return cnt

print(balancedStringSplit("RL"))
