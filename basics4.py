print('h'=='H')
print('Ii'>='Hi')
print('a2'>'A2')
a = list(range(5))
# print(a)

def check(s):
    print(s)
    print(a)
check(1)

b = a
b[0]=10
print(a,b)
a[1]=20
print(a,b)
print(a is b)

# print(dir(a))
c = a.copy()
a[0]=11
print(a,c)
print(a is c)

p = 5
q = p
print(p,q)
print(p is q)
p = 10
print(p is q)
print(p,q)
