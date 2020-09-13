"""
BOJ 나머지(remainder) problem
"""

__author__ = 'hanayong'

from sys import stdin

nums = list(map(int, stdin.readline().split()))

print((nums[0] + nums[1]) % nums[2])
print((nums[0] % nums[2] + nums[1] % nums[2]) % nums[2])
print((nums[0] * nums[1]) % nums[2])
print(((nums[0] % nums[2]) * (nums[1] % nums[2])) % nums[2])
