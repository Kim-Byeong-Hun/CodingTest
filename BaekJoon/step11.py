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