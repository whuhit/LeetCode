"""
@author: yangqiang
@contact: whuhit2020@gmail.com
@file: 350.两个数组的交集2.py
@time: 2020-06-03 12:20
"""


"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。
进阶:

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-arrays-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def intersect(self, nums1, nums2):
        res = []
        if not nums1 or not nums2:
            return res
        for element in nums1:
            if element in nums2:
                res.append(element)
                nums2.remove(element)
        return res


if __name__ == '__main__':
    print(Solution().intersect([1, 2, 2, 1], [2, 2]))
