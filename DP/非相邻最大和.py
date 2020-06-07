# -*- coding: utf-8 -*-
# @Time    : 2020-06-04 22:12
# @Author  : yangqiang
# @FileName: 非相邻最大和.py
# @Blog    ：http://zhifei.online

# 动态规划

arr = [1, 2, 3, 4, 5, 4, 2, 1, 9, 8]


def fun1(arr, i):
    """
    递归方式：递归形式、出口
    :param arr:
    :return:
    """
    if i == 0:
        return arr[0]
    elif i == 1:
        return max(arr[:2])
    else:
        return max(arr[i] + fun1(arr, i - 2), fun1(arr, i - 1))


def fun2(arr):
    """
    动态规划：状态定义、转移方程、初始条件
    :param arr:
    :return:
    """
    opt = [0] * len(arr)
    opt[0] = arr[0]
    opt[1] = max(arr[:2])
    for i in range(2, len(arr)):
        opt[i] = max(opt[i - 2] + arr[i], opt[i - 1])
    return max(opt)


print(fun2(arr, 9))
