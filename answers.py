# Question 1:
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
# Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.
# Example 1:
# Input: source = "abc", target = "abcbc"Output: 2
# Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
# Example 2:
# Input: source = "abc", target = "acdbc"
# Output: -1
# Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
# Example 3:
# Input: source = "xyz", target = "xzyxz"
# Output: 3
# Explanation: The target string can be constructed as follows "xz" + "y" + "xz".

def minSubsequence(source, target):
    count = 0
    left = 0
    right = 0

    while right < len(target):
        if target[right] not in source:
            return - 1

        if source[left] == target[right]:
            left += 1
            right += 1
        else:
            left += 1
        
        if left == len(source):
            count += 1
            left = 0
    
    return count

print("Question 1:")
print(minSubsequence("abc", "abcbc"))
print(minSubsequence("abc", "acdbc"))
print(minSubsequence("xyz", "xzyxz"))

# Question 2:
# 每输入一个字符串，检查括号是否匹配。如果只有左括号没有右括号，我们就在它下面标一个 x，如果只有右括号，我们就在它下面标一个问号。每行为单独测试用例。
# 样例输入:
# bge))))))))) 
# ((IIII)))))) 
# ()()()()(uuu 
# ))))UUUU((() 
# 样例输出: 
# bge)))))))))
#    ?????????
# ((IIII)))))) 
#         ????
# ()()()()(uuu 
#         x
# ))))UUUU((() 
# ????    xx  

def validParentheses(string):
    stack = []
    length = len(string)
    result = " " * length

    for ii in range(length):
        if string[ii] == "(":
            stack.append(ii)
        elif string[ii] == ")":
            if not stack:
                result = result[:ii] + "?" + result[ii+1:]
            else:
                stack.pop()

    for index in stack:
        result = result[:index] + "x" + result[index+1:]

    return result

print("Question 2:")
print(validParentheses("bge)))))))))"))
print(validParentheses("((IIII))))))"))
print(validParentheses("()()()()(uuu")) 
print(validParentheses("))))UUUU((()"))

# Question 3:
# 定义一个多重集合 S 的权值 val(S)为 Mean(S)-Median(S)。
# 其中 Mean(S):S 所有数字的平均数 Median(S): S 的中位数，即若 S 从小到大排序为 s[0],s[1],...,s[k-1]，则中位数的定义以 https://en.wikipedia.org/wiki/Median 为准。
# 给定一个长度为 n 的非负整数序列 a[0],a[1],..,a[n-1]，对于所有 2^n 个子序列，求出最大权值的子序列的权值。
# 要求时间复杂度 为 O(n^2) 及以下。 Sample input: n=4 a =[1,3,5,9]; Sample output: 1.333...。
from itertools import combinations
from statistics import mean, median

def maxValue(n, a):
    max_value = float('-inf')
    
    for ii in range(1, n+1):
        for subseq in combinations(a, ii):
            subseq_mean = mean(subseq)
            subseq_median = median(subseq)
            val = subseq_mean - subseq_median
            if val > max_value:
                max_value = val
    
    return max_value

print("Question 3:")
print(maxValue(4, [1, 3, 5, 9]))
