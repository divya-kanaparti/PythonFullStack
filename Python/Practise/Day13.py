#1)Reverse number
n=int(input("Enter num:"))
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print(rev)
print("----------------------------------")
#2)Find factors
n2=int(input("Enter num:"))
for i in range(1,n2+1):
    if n2%i==0:
        print(i)
print("----------------------------------")
#3)Prime no
n3=4
count=0
for i in range(1,n3+1):
    if n3%i==0:
        count=count+1
print(count)
if count==2:
    print("Prime")
else:
    print("not prime")
print("----------------------------------")
#4)Count of even digits
n=123456
count=0
while n>0:
    r=n%10
    if r%2==0:
        count+=1
    n=n//10
print(count)
print("----------------------------------")
#5)Factorial
n=5
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
print("----------------------------------")
#6)sum of all numbers
sum=0
l=[1,2,3,4]
for i in range(len(l)):
    sum=l[i]+sum
print(sum)
print("----------------------------------")
#7)Reverse the list
s=[1,2,3,4,5,6]
n=[]
for i in range(len(s)-1,-1,-1):
    n.append(s[i])
print(n)
print("----------------------------------")

#8)Sum of prime digit
n=123456
sum=0
while n>0:
    r=n%10
    if r>1:
        count=0
        for i in range(1,r+1):
            if r%i==0:
                count+=1
        if count==2:
            sum+=digit
    n=n//10
print(sum)
print("----------------------------------")
#9)Middle digit
a=int(input("Enter num"))
middle=(a//10)%10
print(middle)