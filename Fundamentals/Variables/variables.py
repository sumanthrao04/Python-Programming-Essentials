print("---------------Variable ----------------------")
# Variable 'x' stores the integer value 10
x = 5
# Variable 'name' stores the string "Sumanth"
name = "Sumanth"
print(x, name)

# Id() in Python
print(id(x))
print(id(name))

# Dynamic Typing
# Python variables are dynamically typed, meaning the same variable can hold different types of values during execution.
print("---------------immutable Objects----------------------")

#immutable
first_name = "Sumanth"
print(first_name)
print(id(first_name))
first_name = "Naveen"
print(first_name)
print(id(first_name))
first_name = 2
print(first_name)
print(id(first_name))

print("---------------immutable Objects----------------------")
#Immutable Objects
a = 10
print(id(a))  # Let's say this prints: 140724431551192
a = 20
print(id(a))  # This will print a different id: 140724431551512

print("---------------iMutable Objects----------------------")
#Mutable Objects
a = [1, 2, 3]
print(id(a))  # Let's say this prints: 2178064109952
a.append(4)
print(id(a))  # The id remains the same

print("---------------Reassignment----------------------")
#Reassignment
# If you directly assign a new value to a variable (even for mutable objects), the variable is pointing to a different object, and the id() will change.
a = [1, 2, 3]
print(id(a))  # Some ID for list a
a = [4, 5, 6]  # Reassign to a new list
print(id(a))  # This will print a new ID since it's a different object

print("---------------#Optimization (Interning)----------------------")
#Optimization (Interning)
# For certain types of objects, like small integers (in the range of -5 to 256) or short strings, Python may reuse the same object across different parts of the program (this is called interning). This can result in the same id() even if you're working with seemingly different values in some cases.
a = 256
print(id(a))  # Let's say this prints: 140724431559064
a = 256
print(id(a))  # The id may remain the same due to interning

# Multiple Assignments
# Assigning the Same Value
print("---------------Assigning the Same Value----------------------")

intial_value = middle_value = final_value = 100
print(intial_value)
print(middle_value)
print(final_value)

print("---------------Assigning Different Values----------------------")

# Assigning Different Values
diffrent_intial_value, diffrent_middle_value, diffrent_Final_value = "intialvalue", 200, "finalvalue"
print(diffrent_intial_value)
print(diffrent_middle_value)
print(diffrent_Final_value)

print("---------------Casting a Variable----------------------")
# Casting a Variable
s = "10"
n = int(5)
print(type(n))

x = 100
y = str(x)
print(type(y))

print("---------------getting the Type of Variable----------------------")
# Getting the Type of Variable
interger_value = 150
float_value = 3.12
string_value = "this is a string"
boolean_value=True
tupple_vaulue=('sumanth','Renuka')
list_value=[1,'2',3]
dictionary_value={"name":"sumanth","age": 25}

print(type(interger_value))
print(type(float_value))
print(type(string_value))
print(type(boolean_value))
print(type(tupple_vaulue))
print(type(list_value))
print(type(dictionary_value))


# Delete a Variable Using del Keyword
print("---------------Delete a Variable Using del Keyword----------------------")
del_vaule=500
print(del_vaule)
del del_vaule
#print(del_vaule)

