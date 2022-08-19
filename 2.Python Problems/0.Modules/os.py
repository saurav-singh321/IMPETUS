# import os
# #get the current directory
# print(os.getcwd())

# #will change the current directory
# os.chdir("C:\\Users\\admin\\Desktop\\Impetus")
# print(os.getcwd())

# #get all the list of folders
# print(os.listdir())

# #make new directory
# # one = os.mkdir("Programs2") #will create only folder 
# # two = os.makedirs("Programs3/hello") # will create subfolder also
# # print(os.listdir())

# # #remove the directory
# # one = os.rmdir("Programs2") #will remove only folder 
# # two = os.removedirs("Programs3/hello") # will remove subfolder also
# # print(os.listdir())

# # rename folder
# ren = os.rename('list.txt','lists.txt')
# print(os.listdir())

# #get the information of file+
# ren = os.stat('lists.txt')
# print(ren)

# #get the directory tree
# # os.walk() yeilds 3 things at a time - current path, directories in that path and files in that path
# for dirpath,dirname,dirfile in os.walk("C:\\Users\\admin\\Desktop\\Impetus"):
#     print("current path - ",dirpath)
#     print("directories - ",dirname)
#     print("files - ",dirfile)


# #get path
# os.environ.get('lists.txt')
# b = os.path.join("C:\\Users\\admin\Desktop\Impetus","hello")
# print(b)



for i in range(10):
    x = float(input("Enter: "))
    a = round(float(x),2)
    print(a)
