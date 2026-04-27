def trailingZeroes(n):
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count
n = 13
print(trailingZeroes(n))