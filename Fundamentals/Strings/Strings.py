String_one = "s"
print(String_one)

print("--------------------Creating a String---------------------")
String_two = "sumanth"
String_three = 'Naveen'

print(String_two)
print(String_three)

print("--------------------Multi-line Strings---------------------")
String_four = '''If we need a string to span multiple lines then
we can use triple quotes (”’ or “””).
'''
print(String_four)

String_five = """If we need a string 
to span multiple lines
then
we can use triple quotes (”’ or “””) """

print(String_five)

print("--------------------Accessing characters in Python String---------------------")

string_six = "I'm learning python"
print(string_six.__len__(), string_six[18], string_six[5])

print("--------------------String Slicing---------------------")
String_seven = "Hello, Python!"
s7 = String_seven[0:6]
print(s7)

print("--------------------Retrieve All Characters---------------------")
# Get the entire string
s7 = String_seven[:]
s8 = String_seven[::]
print(s7)
print(s8)

# Get All Characters Before or After a Specific Position
String_eight = "My name is sumanth,I'm a Devops Engineer"

# Characters from index 2 to the end
s9 = String_eight[2:]
print(s9)

# Characters from the start up to index 10 (exclusive)
s10 = String_eight[:10]
print(s10)

# Get Characters at Specific Intervals
string_nine = "abcdefghojklmnop"
s11 = string_nine[::2]
print(s11)

# Reverse a string
print(string_nine[::-1])

String_ten = "naveen"
# String_ten[0]="N"

#     String_ten[0]="N"
#     ~~~~~~~~~~^^^
# TypeError: 'str' object does not support item assignment
print(String_ten)
s12 = "N" + String_ten[1:]
print(s12)

print("--------------------Common String Methods---------------------")
# Common String Methods

#replace
string_eleven = "I love Java Programming"
s13 = string_eleven.replace("I love Java Programming", "I love python Programming")
print(s13)

# len()
s14 = len(string_eleven)
print(s14)

# upper() and lower():
print(s13.upper())
print(s13.lower())

# strip() and replace()
String_twelve = "  python  programming"
print("length of String_twelve: ", len(String_twelve))
s14 = String_twelve.strip()
print(" after stripe the length of s14: ", len(s14))
print(s14)
print(String_twelve.replace("programming", "Programs"))

string_thirteen = "Sumanth"
string_fourteen = "Parashuram "

String_fifteen = string_thirteen + "." + string_fourteen
print(String_fifteen * 5)

print("--------------------Formatting Strings---------------------")

# Using f-strings

string_sixteen = "sumanth"
print(f"My name is {string_sixteen} and {string_sixteen} learning python")

name = "pradeep"
age = 26
company = "Enadava"

English = 80
Science = 90
Maths = 70
print(f" my name is {name} and I'm  {age} year old and I'm working in {company} company. ")
print(f"the {name} total marks is {English + Science + Maths} out of 300")

# Python String format() Method

print(" the {} total marks is {} out of 300".format(name, English + Science + Maths))
print("My name is {} and I'm working as {} in {} company".format("sumanth", "Devops Engineer", "Endava"))

print("--------------------Using in for String Membership Testing---------------------")
# Using in for String Membership Testing

String_seventeen="python is  easy to learn"
print("python" in String_seventeen)
print("java" in String_seventeen)
