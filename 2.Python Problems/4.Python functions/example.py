# Part A
def convert_to_minutes(num_hours):
    minutes = num_hours * 60
    return minutes


def convert_to_seconds(num_hours):
    minutes = convert_to_minutes(num_hours)
    seconds = minutes * 60
    return seconds


seconds = convert_to_seconds(1)
print(seconds)


# Part B
def leap_year(string):
    if int(string) % 400 == 0 and int(string) % 100 == 0:
        return True
    elif int(string) % 4 == 0 and int(string) % 100 != 0:
        return True
    else:
        return False

# one liner
def leap_year(string):
    return True if (int(string) % 400 == 0 and int(string) % 100 == 0) or (int(string) % 4 == 0 and int(string) % 100 != 0) else False


print(leap_year("1900"))


# Part C 
# Write a function rotate(s,n) that has one string parameter s followed by a positive integer
# parameter n. It returns a rotated string such that the last n characters have been moved to the
# beginning. If the string is empty or a single character, the function should simply return the string
# unchanged. Assume that n is less than or equal to the length of s and that n is a positive integer.
# For example:
# rotate('abcdefgh',3) returns 'fghabcde'
# (Optional challenge: write the function to handle n larger than the length of s.)

# ask
s = input("type something: ")
n = int(input("type how many shifts: "))

def rotate(s, n):
    if s == "" or len(s) == 1:
        return s
    else:
        for index,item in enumerate(s):
            pass
            

        # m = ""
        # for i in s:
            # a = ord(i) + n
            # m += chr(a) - n
        # print(m)

# print(rotate(s, n))


# Part D
even_count = []
odd_count = []
zero_count = []

def digit_count(s):
    s = str(s).split('.')[0]
    s = str(s)
    for i in s:
        if int(i) == 0:
            zero_count.append(int(i))
        elif int(i) % 2 == 0:
            even_count.append(int(i))
        if int(i) % 2 == 1:
            odd_count.append(int(i))
    return len(even_count), len(odd_count), len(zero_count)

print(digit_count(1234567890123))


# Part E
def isdigit(s):
    if(s.isdigit()):
        return True
    else:
        return False

def float_check(s):
    if(s.count('.') == 1):
        return True
    else:
        return False

# one liner
def isdigit(s):
    return True if(s.isdigit()) else False


def float_check(s):
    return True if(s.count('.') == 1) else False


print(isdigit("hello"))
print(float_check("1234.."))
