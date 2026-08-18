#Generators
def square(l):
    for i in l:
        return i*i
n=[1,2,3,4,5]
r=square(n)
print(r)
#Output:1

def square(l):
    k=[]
    for i in l:
        k.append(i*i)
    return k
n=[1,2,3,4,5]
r=square(n)
print(r)
#Output:[1,4,9,16,25]

def my_gen():
    yield "first"
m=my_gen
print(m) #object adress
# print(next(m))

def numbers():
    for i in range(1,6):
        yield i
n=numbers()
for val in range(1,6):
    print(val)

#LIST COMPREHENSION
l=[i for i in range(1,6)]
print(l)
#2)square
l=[i*i for i in range(1,6)]
print(l)
#3)even
l=[i for i in range(1,6) if i%2==0]
print(l)
#4)printuppercase
name=['raMesh','Harish','manIsha']
l1=[i.upper() for i in name]
print(l1)

prices=[5000,9000,3000,1000]
p=[p for p in prices if p>2000]
print(p)
#Stocks
stock=[1,3,0,9,10,0]
l2=[index for index,value in enumerate(stock) if not value]
print(l2)

products=[('laptop',50000),('mobile',40000),('tab',10000)]
l3=[product[0] for product in products if product[1]>20000]
print(l3)

pinfo=[
    {'name':'laptop','price':50000,'stock':2},
    {'name':'mobile','price':30000,'stock':0},
    {'name':'tab','price':10000,'stock':4}
]
l4=[{p['name']:p['price']*0.9} for p in pinfo if p['stock']>0]
print(l4)