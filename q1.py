#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@File    ：q1.py
@Author  ：Muratjan
@Date    ：2024/5/15
"""
"""
问题描述：A subsequence of a string is a new string that is formed from the original string by deleting
some (can be none) of the characters without disturbing the relative positions of the remaining
characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
Given two strings source and target, return the minimum number of subsequences of source
such that their concatenation equals target. If the task is impossible, return -1.

输入：source = "abc", target = "abcbc"
输出：2


解题思路：
    1. 从source的第一个字符开始，依次匹配target的字符，如果匹配成功，source和target的指针都向后移动一位
    2. 如果source的指针到达末尾，但是target的指针没有到达末尾，说明source中没有足够的字符来匹配target，返回-1
    3. 如果target的指针到达末尾，说明source中的字符足够匹配target，返回匹配的次数
"""


def min_subsequences(source, target):
    source_len, target_len = len(source), len(target)
    source_i, target_i, subsequences_count = 0, 0, 0
    # 从source的第一个字符开始，依次匹配target的字符
    while target_i < target_len:
        # 记录当前target的索引
        current_target_i = target_i
        while target_i < target_len and source_i < source_len:
            # 如果匹配成功，source和target的指针都向后移动一位
            if source[source_i] == target[target_i]:
                target_i += 1
            source_i += 1
        # 如果source的指针到达末尾，但是target的指针没有到达末尾，返回-1
        if current_target_i == target_i:
            return -1
        subsequences_count += 1
        source_i = 0
    return subsequences_count


if __name__ == '__main__':
    # 测试案例（题干）
    print(min_subsequences("abc", "abcbc"))
    print(min_subsequences("abc", "acdbc"))
    print(min_subsequences("xyz", "xzyxz"))
    # 测试案例（自己构造）
    print(min_subsequences("abc", "abc"))
    print(min_subsequences("abc", "abababbc"))
