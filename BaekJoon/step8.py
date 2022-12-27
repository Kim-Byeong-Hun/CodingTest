# 1978번
n = int(input())
num_list = list(map(int, input().split()))
for num in num_list:
    is_sosu = 0
    if num == 1:
        n -= 1
    for i in range(1, num):
        if num%i == 0:
            is_sosu += 1
    if is_sosu >= 2:
        n -= 1
print(n)

# 2581번
import math
m = int(input())
n = int(input())
num_list = [i for i in range(m, n+1)]
sosu = []
def sosu_func(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    if n == 1:
        return False
    else:
        return True

for num in num_list:
    if sosu_func(num) == True:
        sosu.append(num)

if len(sosu) == 0:
    print(-1)
else:
    print(sum(sosu))
    print(min(sosu))