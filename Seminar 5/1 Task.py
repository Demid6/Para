"""
1 если нет повторяющихся символов, а если есть то 0
"""

words = input()
n = set(words)
if len(n)<len(words):
    print("0")
else:
    print("1")

