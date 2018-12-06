import os # module called as operating system

myfolder = os.getcwd() # get current working directory
print(myfolder)

# file1 = open("data.csv", "w") # filename and filemode, w ==> write
# file1.write("Line 2 in a file\n")
# file1.close()

# file2 = open("data.csv", "a") # filename and filemode a ==> append
# file2.write("Line 3 in a file\n")
# file2.close()

# file3 = open("data.csv", "r") # filename and filemode r ==> read, default is read mode in python
# content = file3.readlines()   # /readlines() returns as list
# print(content)
# file3.close()

# file4 = open("data.csv", "r")
# content = file4.read()  # .read() returns as strings
# print(content)
# file4.close()

count = 0
file5 = open("data.csv", "r")
line = file5.readline()      # readline() reads only first line and returns as string
while line:
    print(line.strip())     # strip() is removing that \n (line break)
    count += 1
    line = file5.readline()
#
# print("Number of,  lines is %d" %(count))
file5.close()
#
# if not os.path.isdir("testfolder"):             # checking if the folder exist or not
#     os.mkdir("testfolder")                      # it creates a folder
# os.chdir("testfolder")                          # changing directory
# file6 = open("data2.csv", "w+")                 # filename, write and read
# file6.write("File inside a folder")             # write a file
# print("Now printing the content from the file") # print
# file6.seek(0)                                   # seek(0):- position the cursor at the beginning of the file
# content = file6.read()
# print(content)
# os.chdir(myfolder)                              # changing directory back to myfolder

#   if we don't want to use seek() then close() file and open() again. so that cursor is at beginning.