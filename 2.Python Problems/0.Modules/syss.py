import sys

#stdin
for line in sys.stdin: 
    if line.rstrip() == 'q': 
        break
    print(f'Input : {line}') 
  
#stdout
sys.stdout.write('My name is Saurav singh\n')

#stderr
sys.stderr.write("This is a error")

#argv

def main(arg):
    if len(arg) == 3:
        return arg[2]
    else:
        sys.exit("exit")

print(main(sys.argv))


