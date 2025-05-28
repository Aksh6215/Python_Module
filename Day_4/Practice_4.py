# zip() function
'''
name = ["Manjeet", "Nikhil", "Shanbhavi", "Astha"]
roll_no = [4,1,3,2]
marks = [40, 50, 60, 70]

mapped = list(zip(name, roll_no, marks))
print(mapped, sep = "\n")
'''

# file handling (Reading a text file)
'''
file1 = open("C:\\Users\\rohit\\OneDrive\\Desktop\\important.txt", "r")
if file1:
    print("File opened successfully")

contents = file1.read()     # you can also directly read the entire file without putting it in any other variable
print(contents)     # when you read the full file it will take your pointer to the end of that file

print(file1.tell())     # tell that where your pointer is cuurrently pointing
file1.seek(0)   # take you to that specific position
print(file1.tell())
# print(file1.read())

if file1:
    for i in file1:
        print(i, end=" ")

file1.close()
'''

# File Handling (Writing in a text file)
'''
file = open("C:\\Users\\rohit\\OneDrive\\Desktop\\file.txt", "w")

if file:
    name = input("Enter your name: ")
    city = input("Enter your city: ")
    college = input("Enter your college name: ")
    file.write(name)
    file.write(city)
    file.write(college)

file = open("C:\\Users\\rohit\\OneDrive\\Desktop\\file.txt", "r")
print(file.read())
file.close()
'''
'''
file = open("C:\\Users\\rohit\\OneDrive\\Desktop\\file.txt", "w")
for i in range(0,3):
    data = input("Enter data: ")
    file.write(data + "\n")

file = open("C:\\Users\\rohit\\OneDrive\\Desktop\\file.txt", "r")
print(file.read())
'''
'''
x,y,z = 43,54,67
S = 'Spam'
D = {'a': 1, 'b': 2}
L = [1,2,3]
T = (10,100,20)

F = open("datafile.txt", "w")
F.write(S +"\n")
F.write('%s')
F.write
'''

# use of with clause in file handling -> in this we not need to close the file it will automatically close it
'''
with open("file.txt", "w") as f:
    f.write('first line\n')
    f.write('second line\n')
    f.write('third line\n')

with open("file.txt", "r") as f:
    content = f.readlines()

for i in content:
    print(i)
'''

'''
list = ["Abc","ayz","dfg","poi"]

with open("file.txt", "w") as f:
    f.writelines(str(list))

with open("file.txt", "r") as f:
    content = f.readlines()

for i in content:
    print(i +"\n")
'''


'''
with open("C:\\Users\\rohit\\Downloads\\signup image.png", "rb") as file:
    print(file.read())
print("Here starts the another ")
with open("C:\\Users\\rohit\\Downloads\\signup image.png", "rb") as f1:
    with open("C:\\Users\\rohit\\Downloads\\1430603_6964.jpg", "wb") as f2:     # Copying image
        f2.write(f1.read())
'''


# Exception Handling

file = open("C:\\Users\\rohit\\OneDrive\\Desktop\\practical.txt", "w")
file.write("hello how are you")
