# 1712번
a = list(map(int, input().split()))
if a[1] >= a[2]:
    print(-1)
else:
    print(int(a[0]/(a[2]-a[1]))+1)

# 2292번
a = int(input())
b = 1
c = 1
while a > c:
    c += b * 6 
    b += 1
print(b)

# 1193번
a = int(input())

def search_fraction(x):
    line = 0 # 1 2 3 4
    max_num = 0 # 1 3 6 10                 -> 1,2,3--- 씩 늘어나는 숫자 만들기 위한 방법!(구조 이해하기)
    while max_num < x:
        line += 1               #라인을 찾기 위해
        max_num += line         #라인에서의 최대값을 찾기 위해

    gap = max_num - x # 10 - 10 = 0
    if line % 2 == 0: # 4 % 2 = 0
        top = line - gap # 4 - 0 = 4
        under = gap + 1 # 0 + 1 = 1
    else:
        top = gap + 1
        under = line - gap

    print('%d/%d' % (top, under))

search_fraction(a)

# 2869번 
import math
a,b,v = map(int, input().split())

day_up = a - b
all_diff = v - a


if all_diff + a > v:
    int(math.ceil(v/day_up))
else:
    int(math.ceil(v/day_up))


# 수학적인 사고는 아직 부족하기 때문에 우선 다른 문제 진행하고 수학적으로 막히면 기본수학문제 많이 풀기