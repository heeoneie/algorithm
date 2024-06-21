import sys
from itertools import combinations

input = sys.stdin.readline
l,c = map(int, input().split())
s = sorted(input().rstrip().split())
vowels = ['a', 'e', 'i', 'o', 'u']
def is_valid(password):
    vowel_count = sum(1 for char in password if char in vowels)
    consonant_count = len(password) - vowel_count
    return vowel_count >= 1 and consonant_count >= 2

all_combinations = combinations(s, l)
valid_combinations = [''.join(combination) for combination in all_combinations if is_valid(combination)]

for valid_combination in valid_combinations:
    print(valid_combination)