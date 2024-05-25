import sys
input = sys.stdin.readline

words = input().rstrip()
searh_word = input().rstrip()
words = words.replace(searh_word, '-')
print(words.count('-'))