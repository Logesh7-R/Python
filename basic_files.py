#Creating File
with open('file1.txt','w') as f: # w - write file 
    f.write("Heelloo\nFile 1\n")
    f.write("Thank You")
with open('file1.txt','w') as f: # here file1.txt get killed and created with new content
    f.write("Heelloo\nFile 2\n")
    f.write("Thank You")

# Appending File
with open('file1.txt','a') as f:
    f.write("\nHere we are appending contents")
    f.write("\nBye..")

#Reading File
with open('file1.txt','r') as f:
    #print(f.read()) technique 1
    #print(f.readlines()) technique 2
    for lines in f:
        print(lines.rstrip()) #Here rstrip will remove newline characters.

# x - create file if not exist or return error
# with open('file1.txt','x') as f: 
#     f.write("Heelloo\nFile 1\n")
#     f.write("Thank You")

#To remove file (os.remove(File_name))
import os
os.remove('file1.txt')

#To check if file exists
if(os.path.exists('file1.txt')):
    os.remove('file1.txt')
else:
    print("No such file exist")    
