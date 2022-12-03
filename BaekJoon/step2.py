# 1330번
a,b = map(int, input().split())
if a<b:
    print('<')
elif a>b:
    print('>')
else:
    print('==')

# 9498번
a = int(input())
if 90<=a<=100:
    print('A')
elif 80<=a<=89:
    print('B')
elif 70<=a<=79:
    print('C')
elif 60<=a<=69:
    print('D')
else:
    print('F')

# 2753번
a = int(input())
if (a%4 == 0 and a%100 != 0) or (a%400 == 0):
    print('1')
else:
    print('0')

# 14681번
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
else:
    print('4')

# 2884번 모듈로 풀기(백준에서는 런타임오류)
import datetime
h,m = map(int, input().split())
h_r = ''
m_r = 0
h_r = str(datetime.timedelta(hours=h, minutes=m) - datetime.timedelta(minutes=45)).split(':')[0]
m_r = int(str(datetime.timedelta(hours=h, minutes=m) - datetime.timedelta(minutes=45)).split(':')[1])
if len(h_r) >= 3:
    print(h_r.split(' ')[2] + ' ' + m_r)
else:
    print(h_r + ' ' + str(m_r))

# 2884번
h,m = map(int, input().split())
a = h*60
b = a+m-45
if b < 0:
    b += 1440
    print(str(b//60) + ' ' + str(b%60))
else:
    print(str(b//60) + ' ' + str(b%60))


24 * 60