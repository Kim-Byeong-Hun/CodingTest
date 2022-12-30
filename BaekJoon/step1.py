# 2557번
print('Hello World!')
print('Hello World!', end='\n', sep=' ')
print('Hello', end=' ')
print('World', '!', sep='')

# 1000번
a = list(map(int, input().split()))
print(sum(a))

# 1001번
a = list(map(int, input().split()))
print(a[0]-a[1])

# 10998번
a = list(map(int, input().split()))
print(a[0] * a[1])

# 1008번
a = list(map(int, input().split()))
print(a[0] / a[1])

# 10869번
a = list(map(int, input().split()))
print(a[0] + a[1])
print(a[0] - a[1])
print(a[0] * a[1])
print(a[0] // a[1])
print(a[0] % a[1])

# 10926번
a = input()
print(a + '??!')

# 18108번
a = int(input())
print(a-543)

# 3003번
a = list(map(int, input().split()))
print(str(1-a[0])+' '+str(1-a[1])+' '+str(2-a[2])+' '+str(2-a[3])+' '+str(2-a[4])+' '+str(8-a[5]))
b = [1,1,2,2,2,8]
for a1,b1 in zip(a,b):
    print(a1 - b1, end=' ')

# 10430번
a,b,c = map(int, input().split())
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)

# 2588번
a = int(input())
b = int(input())
print(a*int(str(b)[2]))
print(a*int(str(b)[1]))
print(a*int(str(b)[0]))
print(a*b)

# 10171번
print('\\    /\\')
print(" )  ( ')")
print('(  /  )')
print(' \(__)|')

# 10172번
print('|\_/|')
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\\__|')

# 25083번
print('         ,r\'"7')
print("r`-_   ,'  ,/")
print(' \. ". L_r\'')
print('   `~\/')
print('      |')
print('      |')