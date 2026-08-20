#Modules
def Greet():
    return "Welcome Back!"
#To exculed printing from the second module file use if
if __name__=="__main__":
    print("function call from first",Greet())
    print("function call from first",Greet())
#MATH MODULE
import math
print(math.sqrt(8))
# print(math.issqrt(8))
print(int(math.pow(2,3)))
print(math.factorial(5))
print(math.ceil(5.6)) #rounding up
print(math.floor(5.6)) #rounding down
print(math.fabs(-1.3))
print(math.pi)
print(math.exp(2))
print(math.e) #euler number
print(math.gcd(10,20))
print(math.lcm(10,20))
print(math.trunc(-12.5))
print(math.log(100,10))
#RANDOM MODULE
import random
print(random.random())
#random  integer values btw range
print(random.randint(1,10))
color=['Red','blue','red']
print(random.choice(color))
#prints random floating number
print(random.uniform(1,10))
#ITERTOOLS MODULE
from itertools import count,permutations,combinations
n=[1,2,3,4,5,6,2,4]
c=n.count(2)
print(c)
n=(permutations('abc',2))
print(list(n))
#PLATFORM MODULE
import platform
print(platform.system())
print(platform.version())
print(platform.release())
print(platform.machine())
print(platform.architecture())
print(platform.platform())
print(platform.uname())
#JSON MODULE
import json
d={'name':'raj','age':24}
print(type(d))
s=json.dump(d)
print(s) #string type

