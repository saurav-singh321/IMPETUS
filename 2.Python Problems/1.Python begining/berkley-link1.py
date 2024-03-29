# https://ischoolonline.berkeley.edu/blog/python-practice-problems/
# 1. Fly Swatting: Debugging and String Formatting Exercise
import math
def problem_one():
    capitals = {"Maryland": "Annapolis",
                "California": "Sacramento",
                "New York": "Albany",
                "Utah": "Salt Lake City",
                "Alabama": "Montgomery"
                }
    for state, city in capitals.items():
        print(f"The capital of {state} is {city}.")

problem_one()

# 2. That’s a Wrap: Functions and Wrapped Functions Exercise
from functools import lru_cache


input_val = int(input("Enter value: "))

@lru_cache(maxsize=2)
def multiply(x):
    length = len(str(x))
    if length < 3:
        print("This integer is not long enough!")
    elif length >= 3:
        list = [int(a) for a in str(x)]
        result1 = 1
        for i in list:
            result1 *= i
        print('multiplication: ', result1)
        return result1

@lru_cache(maxsize=2)
def match_logic(x, y):

    list1 = list(str(x))
    list2 = list(str(y))
    a = [int(i) for i in list1 if i in list2]
    return sorted(set(a))

###### Matching #######

def matching(random):
    print("before executing random")
    return random



@matching
def random():
    x = multiply(input_val)
    y = match_logic(input_val,x)
    return x,y

print(multiply(input_val))
print(match_logic(input_val,141120))
print(random())


# 3. Show Me the Money: Data Types and Arithmetic Exercise
USD = float(input("Input a value to convert from $USD: "))
EUR = round(USD*0.94, 2)
JPY = round(USD*130.09, 2)
MXN = round(USD*19.76, 2)
final = f"{USD} USD = {EUR} EUR = {JPY} JPY = {MXN} MXN"
print(final)


# 4.  What’s in a Name: String Slicing and If/Else Statements Exercise
name = input("Enter one word name: ").lower()
reverse = name[::-1]
print(reverse.capitalize(), "\nPalindrome") if name == reverse else print(reverse.capitalize())
# without slicing
reverse = ""
for i in name:
    reverse = i+reverse
print(reverse.capitalize(), "\nPalindrome") if name == reverse else print(reverse.capitalize())


# 5. Adventures in Loops: “For” Loops and List Comprehensions Exercise
text = "Alice was beginning to get very tired of sitting \
by her sister on the bank, and of having nothing to do: \
once or twice she had peeped into the book her sister \
was reading, but it had no pictures or conversations in \
it, 'and what is the use of a book,' thought Alice, \
'without pictures or conversations?'"

a = text.split(" ")
# using one liner
letter = [print(i[0:], end=" ") if (len(i) < 2) else print(''.join(sorted(i[1:].lower())), end=" ") for i in a]
# normally
print("\n")
for i in a:
    if len(i) < 2:
        print(i[0:], end=" ")
    else:
        letter = i[1:].lower()
        letter = ''.join(sorted(letter))
        print(letter, end=" ")

# 6. The Drones You’re Looking For: Classes and Objects
class Drone:
    ascend_count = 0
    __altitude = 0

    def __init__(self, altitude=0):
        self.__altitude = altitude
        self.alt_vali()


    def alt_vali(self):
        if self.__altitude < 0:
            raise ValueError

    @property
    def altitude(self):
        return self.fly()

    @altitude.setter
    def altitude(self, set_alt):
        self.__altitude = set_alt
        self.alt_vali()

    def ascend(self, set_asc):
        self.__altitude += set_asc
        self.ascend_count += 1
        return self.__altitude, self.ascend_count

    def fly(self):
        return "The Drone is flying at {} feet".format(self.__altitude)


d1 = Drone(100)
print(d1.fly())

d1.altitude = 200
print(d1.fly())

print(d1.ascend(100))
d1.fly()
print(d1.ascend_count)

# 7. Top of the Class: Dictionaries and “While” Loops Exercise
import math
class Gradebook:
    gradebook = {}
    grade_list = []

    def add_student(self):
        self.student_name = input("Enter student name: ")
        print(f"A new student - {self.student_name}! Adding them to the gradebook...")
        grade = input("Enter list of grade seperated by comma with no space: ")
        a = grade.split(",")  # it will convert to list
        self.grade_list = [float(i) for i in a]
        print('New entry complete!')
        return self.grade_list

    def add_grades(self):
        add_grade = input("Enter Grades you want to add: ")
        list1 = add_grade.split(",")
        [self.grade_list.append(float(i)) for i in list1]
        Gradebook.gradebook.update({self.student_name: self.grade_list})
        return self.grade_list

    def view_gradebook(self):
        return f"Gradebook - {Gradebook.gradebook}"

    def calculate_average(self):
        average = [{key: round(sum(value)/len(value), 2)}
                   for key, value in Gradebook.gradebook.items()]
        return average

    def input(self):
        while(True):
            print("1 - Add a student \n2 - Add grades \n3 - View Gradebook \n4 - Calculates Average \n5 - Quit")
            ask = input("what task would you like to complete: ")
            input_dict = {str(1): print(self.add_student()),
                          str(2): print(self.add_grades()),
                          str(3): print(self.view_gradebook()),
                          str(4): print(self.calculate_average()),
                          str(5): print("End of program")
                         }
            if ask  in input_dict.keys():
                print("Please enter any number from above")
            else:
                input_dict[ask]
            # ask = input("what task would you like to complete: ")
            # if ask == str(1):
            #     print(self.add_student())
            #     continue
            # elif ask == str(2):
            #     print(self.add_grades())
            #     continue
            # elif ask == str(3):
            #     print(self.view_gradebook())
            #     continue
            # elif ask == str(4):
            #     print(self.calculate_average())
            #     continue
            # elif ask == str(5):
            #     print("End of program")
            #     break
            # else:
            #     print("Please enter any number from above")
            #     continue


saurav = Gradebook()
saurav.input()
