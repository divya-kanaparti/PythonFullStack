start=int(input())
end=int(input())
count=0
for n in range(start,end+1):
     if n > 1:
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            print(n)
            count+=1
print("Count:",count)