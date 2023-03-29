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
a = int(input())
b = ''
if len(str(a)) < 2:
    b = '0' + str(a)
else:
    b = str(a)
c = [b]
while True:
    d = int(b[0]) + int(b[1])
    e = b[1]+str(d)[-1]
    c += [e]
    if c[0] == c[-1]:
        break
    else:
        if len(e) < 2:
            b = '0' + e
        else:
            b = e
print(len(c)-1)

# 25314번
n = int(input())
print(('long ' * (n//4)) + 'int')