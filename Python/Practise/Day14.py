#Patterns
#star patterns
#1)
r=4
for i in range(r,0,-1):
    for k in range(r-i):
        print(" ",end=" ")
    for j in range(i):
        print('*',end=" ")
    print()
print("------------------------------------------------")
#2)
for i in range(1,r+1):
    for k in range(r-i):
        print(" ",end=" ")
    for j in range((i*2)-1):
        print('*',end=" ")
    print()
print("------------------------------------------------")
#3)
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()
print("------------------------------------------------")
#4)
for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
print("------------------------------------------------")
#5)
n=5
for i in range(1,6):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

#Number Patterns
count=1
for i in range(1,5):
    for j in range(1,i+1):
        print(count,end=" ")
        count+=1
    print()
print("------------------------------------------------")
#2)
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print("------------------------------------------------")
#3)
n=5
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()
print("-----------------------------------------------")
#Hallow Sphere
n=5
for i in range(5):
    for j in range(5):
        if i==n//2 or j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("------------------------------------------------")
#2)
for i in range(5):
    for j in range(5):
        if i==j  or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("---------------------------------------------------")
#3)
for i in range(5):
    for j in range(5):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("---------------------------------------------------")
#4)
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==i or j==1 or i==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("---------------------------------------------------")
#5)
n=5
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(1,2*i):
        if j==1 or j==2*i-1 or i==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()