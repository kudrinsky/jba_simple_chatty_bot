n = abs(int(input()))
r = abs(int(input()))
count = 0
while r < n:
    count += 1
    n = n / 2
print(count * 12)