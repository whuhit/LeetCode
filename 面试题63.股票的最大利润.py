# -*- coding: utf-8 -*-
# @Time    : 2020-06-04 20:25
# @Author  : yangqiang
# @FileName: 面试题63.股票的最大利润.py
# @Blog    ：http://zhifei.online

"""


假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
 

限制：

0 <= 数组长度 <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 解题思路：动态规划

# 动态规划解析：
# 状态定义： 设动态规划列表 dpdp ，dp[i]dp[i] 代表以 prices[i]prices[i] 为结尾的子数组的最大利润（以下简称为 前 ii 日的最大利润 ）。
# 转移方程： 由于题目限定 “买卖该股票一次” ，因此前 ii 日最大利润 dp[i]dp[i] 等于前 i - 1i−1 日最大利润 dp[i-1]dp[i−1] 和第 ii 日卖出的最大利润中的最大值。
# 前 i 日最大利润 = \max(前 (i-1) 日最大利润, 第 i 日价格 - 前 i 日最低价格)
# 前i日最大利润=max(前(i−1)日最大利润,第i日价格−前i日最低价格)
#
# dp[i] = \max(dp[i - 1], prices[i] - \min(prices[0:i]))
# dp[i]=max(dp[i−1],prices[i]−min(prices[0:i]))
#
# 初始状态： dp[0] = 0dp[0]=0 ，即首日利润为 00 ；
# 返回值： dp[n - 1]dp[n−1] ，其中 nn 为 dpdp 列表长度。
#
# 作者：jyd
# 链接：https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/solution/mian-shi-ti-63-gu-piao-de-zui-da-li-run-dong-tai-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def maxProfit(self, prices) -> int:
        cost, profit = float("+inf"), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit


if __name__ == '__main__':
    print(Solution().maxProfit([7, 6, 4, 3, 1]))
