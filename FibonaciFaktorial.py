def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
def fibo(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
def fibonaciOrFactorial(n, elements, p):
    sum = 0
    if(p == 1):
        for i in range(len(elements)):
           sum += fibo(elements[i]) 
    if(p == 2):
         for i in range(len(elements)):
           sum += factorial(elements[i]) 
    return sum

# print(fibonaciOrFactorial(int(input()), list(map(int, input().split())), int(input())))


# n = int(input())
# k = list(map(int, input().split()))
# p = int(input())


# 1 fibonaci
# 2 faktorial 

n = 5
k = [1, 2, 3, 4, 5]
p = 1
print(fibonaciOrFactorial(n, k, p))
