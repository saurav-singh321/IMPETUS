import shutil   
src = r"C:\Users\admin\Desktop\Impetus\Programs\2.Python Problems\1.Python begining\shutill.py"
dest = r"C:\Users\admin\Desktop\Impetus\destination.txt"

src1 = r"C:\Users\admin\Desktop\Impetus\Programs\2.Python Problems\1.Python begining"
dest1 = r"C:\Users\admin\Desktop\Impetus\destination1"

#copies the file to another file
shutil.copyfile(src,dest)

#copies the file and permissions to another file
shutil.copy(src,dest)

#copies the file and metadata to another file
shutil.copy2(src,dest)

#copies the enitire folder to another folder
shutil.copytree(src1,dest1)

#removes the enitire folder
shutil.rmtree(dest1)