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
# v = (a-b)*(n-1) + a
# v = an-bn+b
# v = (a-b)n+b
import math
A,B,V = map(int, input().split())
print(math.ceil((V-B)/(A-B)))

# 10250번
# 전체호수 =  (N - (H * N/H의 내림):층 * 100) + (N/H의 올림 : 호수)
import math
T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    print(((N - (H * (math.floor(N/H)))) * 100) + math.ceil(N/H))

# 2775번
# k층의 n(n<=14)호에는 몇명(a명)살까? 

T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())

    f0 = [f for f in range(1, 15)]
    for j in range(k):
        fn = []
        for l in range(n):
            fn.append(sum(f0[:l+1]))
        f0 = fn.copy()
    print(f0[-1])

# 2839번 
N = int(input())
count = 0
while N >= 0:
    if N % 5 == 0:  # 5의 배수이면
        count += (N // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(count)
        break
    N -= 3  
    count += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else:
    print(-1)

# 10757번
a,b = map(int, input().split())
print(a+b)