n=int(input())
rev=0
print(int(str(n)[::-1]))
while n>0:
    digit=n%10
    rev= rev *10+ digit
    n=n//10
print(rev)
