input_val = 2789475


def multiply(x):
    length = len(str(x))
    if length < 3:
        print("This integer is not long enough!")
    else:
        list = [int(a) for a in str(x)]
        result1 = 1
        for i in list:
            result1 *= i
        return result1


def match_logic(x, y):
    list1 = list(str(x))
    list2 = list(str(y))
    a = [int(i) for i in list1 if i in list2]
    return (sorted(set(a)))


####### Matching #######
#

def matching(func):
    print("before executing random!")
    return func

 
@matching
def random():
    print("random executing...")
    x = multiply(input_val)
    y = match_logic(input_val, x)
    return x, y

# random = matching(random)
print(random())

# print(multiply(input_val))
# print(match_logic(input_val,multiply(input_val)),"\n")
