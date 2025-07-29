# 1. Write a python program to display a user entered name followed by Good 
# Afternoon using input () function. 
# name = input("Enter your name: ")
# print("good afternoon " + name + "!")



#2. Write a program to fill in a letter template given below with name and date.
# Name = input("Enter your name: ")
# date = (input("enter date: (dd/mm/yy)"))

# letter = '''  
# Dear <|Name|>, 
# You are selected! 
# <|Date|> 
# '''

# letter = letter.replace("<|Name|>", Name)
# letter = letter.replace("<|Date|>", date)

# print(letter)



# 3. Write a program to detect double space in a string.
# str = input("Enter string: ")
# if "  " in str:
#     print("double space detected")
# else:
#     print("double space not detected")



# 4. Replace the double space from problem 3 with single spaces. 
# str = input("Enter string: ")
# str = str.replace("  ", " ")
# print(str)


# 5. Write a program to format the following letter using escape sequence characters. 
letter = "Dear Harry,\n \tthis python course is nice.\nThanks!"
print(letter)