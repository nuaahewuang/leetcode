'''
FilePath: 2280-表示一个折线图的最少线段数.py
Author: Huang_CJ
Date: 2024-06-03 13:45:44
LastEditTime: 2024-06-03 13:51:58
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一个二维整数数组 stockPrices ，其中 stockPrices[i] = [dayi, pricei] 表示股票在 dayi 的价格为 pricei 。折线图 是一个二维平面上的若干个点组成的图，横坐标表示日期，纵坐标表示价格，折线图由相邻的点连接而成。
'''

class Solution(object):
    def minimumLines(self, stockPrices):
        """
        :type stockPrices: List[List[int]]
        :rtype: int
        """
        stockPrices.sort()
        n = len(stockPrices)
        if n <= 2:
            return n - 1

        res = 1
        for i in range(2, n):
        # 遍历相邻点对，并判断线段是否可以合并
            dx0 = stockPrices[i-1][0] - stockPrices[i-2][0]
            dy0 = stockPrices[i-1][1] - stockPrices[i-2][1]
            dx1 = stockPrices[i][0] - stockPrices[i-1][0]
            dy1 = stockPrices[i][1] - stockPrices[i-1][1]
            if dx0 * dy1 != dy0 * dx1:
                res += 1
        
        return res

'''
核心思想：首先将折线图的点按照横坐标升序排列，排序后数组 stockPrices 中的相邻格点连成的线段即组成了折线图。
用 n 来表示折线图的点数，并用 res 统计表示折线图所需的最少线段数。当 n≤2 时，折线图的表示方式唯一，即需要 n−1 条线段表示。当 n>2 时，我们可以从左至右遍历每一对相邻的点对，并判断该点对组成的折线是否可以与前面相邻的折线（如有）合并，进而计算最少的线段数。
细节：在比较斜率 dy0/dx0 与 dy1/dx1 时，为了避免浮点数的精度造成误差，我们可以对两边进行通分，即判断 dx0 × dy1 与 dx1 × dy0 是否相等。
'''