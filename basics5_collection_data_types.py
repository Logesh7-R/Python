# List
l = list(range(10))
print(l)
l.insert(0,10)
print(l)
b = list(range(11,16))
l.append(b)
print(l)
l.extend(b)
l.extend(b)
print(l)
print(l.count(1))
l.remove(11)
print(l)

# Dictionary
d = {"a":"alpha","b":"beta","g":"gamma"}
del d["a"]
print(d)
d["t"] = "theta"
print(d)
for key in d.keys():
    print(key,d[key])

#String
name = "Logesh"
age = 25
st1 = f"hi!.. I am {name} and my age is {age}"
st2 = "hi!.. I am {0} and {0} age is {1}".format(name,age)
print(st1,st2)
#name[0] = "y" #Erroe becoz strings are immutable

#Tuple
t = ()
t+=(1,2,"orange")  #adding values to tuple is by add new tuple to it
print(t)
#Tuples are immutable

#set
a = set()
stri = "hiiiii....! good MorniNg@@!"
a = set(stri)
print(a)
#removes dublicate

lis = [1,2,3,4]
print(lis,lis==sorted(lis))
lis[0]=10
print(lis,lis==sorted(lis))
