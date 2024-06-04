'''
FilePath: 2521-数组乘积中的不同质因数数目.py
Author: Huang_CJ
Date: 2024-06-04 22:38:45
LastEditTime: 2024-06-04 22:47:08
Copyright: 2024 xxxTech CO.,LTD. All Rights Reserved.
Descripttion: 给你一个正整数数组 nums ，对 nums 所有元素求积之后，找出并返回乘积中 不同质因数 的数目。
'''

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        s = set()
        for x in nums:
            i = 2
            while i * i <= x:
                if x % i == 0:
                    s.add(i)
                    x //= i
                    while x % i == 0:
                        x //= i
                i += 1
            if x > 1 :
                s.add(x)

        return len(s)    

'''
核心思路：遍历每个数，分解质因数，把质因数加到哈希表中。对于一个正整数n，如果其存在质因数p，则n可以表示为n=p*q，其中q为除p外的其他质因数的乘积。因此，我们可以先判断2是否是n的质因数，如果是，则将其保存下来，并将n除以2，继续进行同样的操作，直到n为奇数，然后从3开始，依次判断所有的奇数是否是n的质因数。由于n除以每个质因数后都会变得更小，因此当n不是质数时，分解质因数后得到的所有质因数必然都小于或等于n的平方根。
'''