# -*- coding: utf-8 -*-
# @Time    : 2020-06-04 22:48
# @Author  : yangqiang
# @FileName: 几个数之和.py
# @Blog    ：http://zhifei.online
import numpy as np

# 给定一个数组，和一个目标值，数组中若存在数字组合之和等于目标值则返回True，否则返回False
arr = [2, 3, 4, 12, 5, 2, 9]


def fun1(arr, i, s):
    """
    递归
    :param arr:
    :param i:
    :param s:
    :return:
    """
    if s == 0:
        return True
    elif i == 0:
        return arr[i] == s
    elif arr[i] > s:
        return fun1(arr, i - 1, s)
    else:
        return fun1(arr, i - 1, s - arr[i]) or fun1(arr, i - 1, s)


def fun2(arr, s):
    """
    动态规划：重叠子问题 保存中间结果
    :param arr:
    :param s:
    :return:
    """
    subsets = np.zeros((len(arr), s + 1), dtype=bool)
    subsets[:, 0] = True
    subsets[0, :] = False
    subsets[0, arr[0]] = True
    for i in range(1, len(arr)):
        for j in range(1, s + 1):
            if arr[i] > s:
                subsets[i, j] = subsets[i - 1, j]
            else:
                a = subsets[i - 1, j - arr[i]]
                b = subsets[i - 1, j]
                subsets[i, j] = a or b
    return subsets[-1, -1]


print(fun2(arr, 37))
