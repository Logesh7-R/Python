#Exception handling
t = (1,2,3)
try:
    print(1)
    t[0] = 11 # if error ,then jumps to exception part
    print(2)
except SyntaxError:
    print(SyntaxError)
except:
    print("Caught it")

#List Comprehension
a = [x for x in range(5)]
print(a)
b = [x for x in range(5) if x%2==0]
print(b)
c = [x if x%2==0 else -1 for x in range(5)]
print(c)

# check = int(input("Enter digit:"))
# print("even" if check%2==0 else "odd")

#Zip
for i,j in zip(range(10),range(1,6)):
    print(i,j)

zip_list = [(i,j) for i,j in zip(range(10),range(1,6))]
print(zip_list)

zip_dict = {i:j for i,j in zip(range(10),range(1,6))}
print(zip_dict)

#ASCII and Character conversion
ascii = 65
val = chr(ascii)
print(ascii,val)

ch = 'Z'
asc = ord(ch)
print(ch,asc)
