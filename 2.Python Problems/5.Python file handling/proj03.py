def open_file():
    while True:
        try:
            name = input('enter file name')
            fp = open( f"c:\\Users\\admin\Desktop\Impetus\Programs\Python Problems\\5.Python file handling\{name}")
        except(FileNotFoundError):
            print('File not found')
            continue
        return fp
    
def find_min_percent():
    fp = open("c:\\Users\\admin\Desktop\Impetus\Programs\Python Problems\\5.Python file handling\proj03.txt")
    for line in fp:
        print(line)
    return line 
def find_max_percent(line):
    '''Find the max percent change in the line; return the value and the index.'''
    pass # replace this line with your code

def find_gdp(line, index):
    '''Use the index fo find the gdp value in the line; return the value'''
    pass # replace this line with your code

        
def display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp):
    '''Display values; convert billions to trillions first.'''    
    pass # replace this line with your code

def main():                    
    # print(open_file())
    str = 'c:\\Users\\admin\Desktop\Impetus\Programs\Python Problems\\5.Python file handling\proj03.txt'
    print(find_min_percent())

# Calls the 'main' function only when you execute within Spyder (or console)
# Do not modify the next two lines.
if __name__ == "__main__":
    main()
