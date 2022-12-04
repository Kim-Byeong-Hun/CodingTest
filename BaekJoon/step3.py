# 2739번
a = int(input())
for i in range(9):
    print(str(a)+' * '+str(i+1)+' = '+str(a*(i+1)))

# 10950번
a = int(input())
for i in range(a):
    b,c = map(int, input().split())
    print(b+c)

# 8393번
a = int(input())
b = 0
for i in range(1,a+1):
    b += i
print(b)

# 25304번
x = int(input())
n = int(input())
a = 0
for i in range(n):
    b,c = map(int, input().split())
    a += b*c
if a == x:
    print('Yes')
else:
    print('No')

# 15552번
import sys
a = int(input())
for i in range(a):
    b,c = map(int, sys.stdin.readline().rstrip().split())
    print(b+c)
# input은 prompt message 값을 인자로 받기 때문에 prompt message값을 반환하고, strip을 삭제한 값을 반환하기 때문에 느림
# 반면 sys.stdin.readline은 prompt message값을 인수로 받지 않고, strip을 그대로 출력하기 때문에 빠름
# 대신 strip을 출력하기 때문에 rstrip()함수를 사용해서 개행문자를 삭제시켜야하는 소요가 있다.

# 11021번
import sys
a = int(sys.stdin.readline().rstrip())
for i in range(1, a+1):
    b,c = map(int, sys.stdin.readline().rstrip().split())
    print('Case #%d: %d' % (i, b+c))

# 11022번
import sys
a = int(sys.stdin.readline().rstrip())
for i in range(1, a+1):
    b,c = map(int, sys.stdin.readline().rstrip().split())
    print('Case #%d: %d + %d = %d' % (i, b, c, b+c))

# 2438번
a = int(input())
for i in range(1, a+1):
    print('*' * i)

# 2439번
a = int(input())
for i in range(1, a+1):
    print(' ' * (a-i), end='')
    print('*' * i)

# 10952번
import sys
while True:
    a,b = map(int,sys.stdin.readline().rstrip().split())
    if a==b==0:
        break
    print(a+b)

# 10951번 (예외처리 문제)
import sys
while True:
    try:
        a,b = map(int, sys.stdin.readline().rstrip().split())
        if a <= 0 or b >= 10:
            raise Exception()
        print(a+b)
    except:
        break

# 1110번
a = input()
b = 0
i = []
if int(a) < 10:
    a = '0' + a

while True:
    if len(i) == 0:
        i += [a[-1] + str(int(a[0]) + int(a[1]))]
    else:
        i += [i[b-1][-1] + str(int(i[b-1][0]) + int(i[b-1][1]))]

    if a == i[-1]:
        print(len(i))
        break
    b += 1

# i에 결과를 넣자
# i의 길이를 출력하면되겠네
# i의 마지막 

