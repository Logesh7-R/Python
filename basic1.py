#type conversion
age = 25
mark = 0.1
stri = ""
print(bool(age))
print(bool(mark))
print(bool(stri))

#Formatted String
name = "Logesh"
age = 20
print(f'hi {name}..your age is {age}')
print('hi {}..your age is {}'.format(name,age))
print('hi {1}..your age is {0}'.format(age,name))
print('hi {name_s}.. your age is {age_s}'.format(age_s=22,name_s="Logi"))
