
# ask why 13 is printing in numbers
fp = open("c:\\Users\\admin\\Desktop\Impetus\Programs\Python Problems\\5.Python file handling\\lab05_pre-lab.txt")
total = 0
letters = ''
other =''
for line in fp:
    for ch in line:
        if ch.isdigit():
            total += int(ch)
        elif ch.isalpha():
            letters += ch
        else:
            other+=ch
            # 
print( total )    # Line 1
print( letters )  # Line 2
print(other)
fp.close()