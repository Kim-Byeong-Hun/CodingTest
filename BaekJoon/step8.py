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

# 11653번
n = int(input())
div_n = 2
while n >= 2:
    if n%div_n == 0:
        print(div_n)
        n //= div_n
    else:
        div_n += 1

# 1929번
import math
m,n = map(int, input().split())

num_list = [True] * (n+1)

for i in range(2, int(math.sqrt(n))+1):
    if num_list[i] == True:
        for j in range(i*2, n+1, i):
            num_list[j] = False

for i in range(m, n+1):
    if i == 0 or i == 1:
        continue
    if num_list[i] == True:
        print(i)

# 4948번
import math
while True:
    n = int(input())
    if n == 0:
        break

    num_list = [True] * (2*n+2)
    num_list[0] = False
    num_list[1] = False

    for i in range(2, int(math.sqrt(2*n+1))+1):
        if num_list[i] == True:
            for j in range(i*2, 2*n+2, i):
                num_list[j] = False
    
    sosu = 0
    for i in range(n+1, 2*n+1):
        if num_list[i] == True:
            sosu += 1
    print(sosu)

# 9020번
import math
T = int(input())

sosu_list = []
num_list = [True] * (10001)

for i in range(2, int(math.sqrt(10000))+1):
    if num_list[i] == True:
        for j in range(i*2, 10001, i):
            num_list[j] = False
    
for i in range(2, 10001):
    if num_list[i] == True:
        sosu_list.append(i)

for _ in range(T):
    n = int(input())
    
    gold_list = []
    for num in sosu_list:
        for num2 in sosu_list:
            if n == (num + num2):
                gold = [num, num2]
                gold_list.append(gold)

    gold_list2 = gold_list[:len(gold_list)//2]

    for num in gold_list2[-1]:
        print(num, end=' ')
    print()
    