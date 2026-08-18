#Recursion
#factorial
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input())
r=fact(5)
print(r)
#2)Fibbonacci
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-2)+fibo(n-1)
n=int(input("Enter num:"))
res=fibo(n)
print(res)
