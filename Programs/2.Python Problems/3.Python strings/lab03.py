VOWELS = "aeiou"
list = []
[list.append(VOWELS[i]) for i in range(len(VOWELS))]
print(list)
b = ""
j = 0

while(True):
    word = input("Enter a word ('quit' to quit): ")
    if word == "quit":
        break
    if word[0] in list:
        print(word+"way")
    else:
        for i in word:
            if i not in list:
                b+=i
                j+=1
            else:
                break
        new = word[j:]+b+"ay"
        print(new)
        j=0    #to reset the value after one value is printed
        b=""
    
    
    


# """The program will repeatedly prompt the user to enter a word. First convert the word to lower case. The
# word will be converted to Pig Latin using the following rules:
# a) If the word begins with a vowel, append “way” to the end of the word.
# b) If the word begins with a consonant, remove all consonants from the beginning of the word
# and append them to the end of the word. Then, append “ay” to the end of the word.
# For example:
# "dog" becomes "ogday"
# "scratch" becomes "atchscray"
# "is" becomes "isway"
# "apple" becomes "appleway"
# "Hello" becomes "ellohay"
# "a" becomes "away"
# The program will halt when the user enters “quit” (any combination of lower and upper case letters, such
# as “QUIT”, “Quit” or “qUIt”).
# Suggestions:
# a) Use .lower() to change the word to lower case.
# b) How do you find the position of the first vowel? I like using enumerate(word) as in
# for i,ch in enumerate(word)
# where ch is each character in the word and i is the character’s index (position).
# c) Use slicing to isolate the first letter of each word.
# d) Use slicing and concatenation to form the equivalent Pig Latin words.
# e) Use the in operator and the string "aeiou" to test for vowels.
# Good practice: define a constant VOWELS = "aeiou" """
# 
# vowels = ['a', 'e', 'i', 'o', 'u']
# ch = input("Enter your string: ")
# b = ""
# count = 0
# for i in ch:
    # if i not in vowels:
        # b = b+i
        # count += 1
    # else:
        # break
# print(b)
# new_string = ch[count:]+b
# print(new_string)
