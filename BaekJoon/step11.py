# 10872번
a = int(input()) # 재귀 미사용
b = 1
while a > 0:
    b = a * b
    a -= 1
print(b)


a = int(input()) # 재귀사용
def factorial(n):
    if n==1:
        return 1
    elif n==0:
        return 1
    return n * factorial(n-1)
print(factorial(a))


# 10870번
a = int(input())  # a >= 2

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    result = fibonacci(n-1) + fibonacci(n-2)

    return result

print(fibonacci(a))

# 25501번
t = int(input())
cnt = [0] # 리스트는 ID가 변하지 않기 때문에 전역변수로 간주됨. 그래서 함수안에서 리스트 값을 변경 가능
def recursion(s, l, r):
    cnt[0] += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)
        
def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for i in range(t):
    cnt = [0]
    print(isPalindrome(input()), end=' ')
    print(cnt[0])

# 24060번 ☆☆☆☆☆☆☆☆☆☆☆☆☆☆

# 2447번 ☆☆☆☆☆☆☆☆☆☆☆☆☆
a = int(input())

def star10(n):
    if n < 3:
        return 0
    if n >= 3:
        print('***' * int(n/3))
        print(('*' + ' ' + '*') * int(n/3))
        print('***' * int(n/3))
    star10(n-3)

star10(3)

# 11729번 ☆☆☆☆☆☆☆☆☆☆☆☆☆
a = int(input())
b = [0]
def hanoi_tower(n):
    b[0] += 1
    if n == 0:
        return 0
    
