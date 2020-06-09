# -*- coding: utf-8 -*-
# @Time    : 2020-06-09 22:33
# @Author  : yangqiang
# @FileName: 661.图片平滑器.py
# @Blog    ：http://zhifei.online


class Solution:
    def imageSmoother(self, M):
        h = len(M)
        w = len(M[0])
        # res = [[0]*w]*h # 不能这么写，改变一个元素会把其他元素也改掉
        ress = []
        for i in range(h):
            res = []
            for j in range(w):
                count = 0
                sum_ = 0
                for x in (-1,0,1):
                    for y in (-1,0,1):
                        if i+x>=0 and i+x <= h-1 and j+y>=0 and j+y<=w-1:
                            count += 1
                            sum_ += M[i+x][j+y]
                # res[i][j] = sum_//count
                res.append(sum_//count)
            ress.append(res)
        return ress


M = [[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]]

# print(res)
