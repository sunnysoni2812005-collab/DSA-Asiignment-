import math

def find_gcd(nums):
    return math.gcd(min(nums), max(nums))

print(find_gcd([2, 5, 6, 9, 10]))