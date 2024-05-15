#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@File    ：q2.py
@Author  ：Muratjan
@Date    ：2024/5/15
"""
"""
题目描述:每输入一个字符串， 检查括号是否匹配。 如果只有左括号没有右括号， 我们就在它下面标一个x， 如果只有右括号， 我们就在它下面标一个问号。
输入:字符串s (1 <= len(s) <= 1000)
输出:字符串以及s下面的标记
思路：
    1. 创建两个数组stack和markers， stack用于存储左括号的索引， markers用于存储标记,markers初始化为' '长度为字符串s的长度
    2. 遍历字符串， 遇到左括号入栈， 遇到右括号出栈， 如果栈为空， 则标记为问号,"?"
    3. 遍历结束后， 如果栈不为空， 则标记为"x"
    4. 返回字符串和标记
"""


def check_brackets(input_string):
    # 创建两数组
    stack = []
    markers = [' '] * len(input_string)
    for i, char in enumerate(input_string):
        # 遇到左括号入栈
        if char == '(':
            # 入栈，将左括号的索引入栈
            stack.append(i)
        # 遇到右括号出栈或者标记为问号
        elif char == ')':
            if stack:
                stack.pop()
            else:
                # 栈为空， 标记为问号
                markers[i] = '?'
    while stack:
        markers[stack.pop()] = 'x'
    return input_string + '\n' + ''.join(markers)


if __name__ == "__main__":
    # 测试用例
    inputs = [
        # 题中测试开始
        "bge)))))))))",
        "((IIII))))))",
        "()()()()(uuu",
        "))))UUUU((()",
        # 题中测试结束，开始自己的测试
        "((((ddsda))))",
        "(((aa)))",
        "(((((((aa"
    ]

    for input_string in inputs:
        print(check_brackets(input_string))
        print()  # 添加空行以分隔输出
