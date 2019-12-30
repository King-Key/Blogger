#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    		: 2019-12-30 11:15:00
# @Author  		: King-Key
# @E-mail  		: guo_wang_113@163.com
# @BlogLink     : kingkey.club
# @Version 		: 1.0

# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/two-sum


def twoSum(nums,target):
    hashMap={}
    for index,num1 in enumerate(nums):
        num2=target-num1
        if num2 in hashMap:
            return [hashMap[num2],index]
        hashMap[num1]=index
    return None

if __name__=="__main__":
	nums=[2,7,9,15]
	target=9
	print(twoSum(nums,target))