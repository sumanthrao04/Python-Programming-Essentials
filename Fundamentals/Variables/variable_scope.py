print("---------------Python local variable ----------------------")


def local_variable():
    local_valiable = "hey I'm a local variable"
    print(local_valiable)


local_variable()

# Can a local variable be used outside a function?
# got the below error
# NameError: name 'local_valiable' is not defined. Did you mean: 'local_variable'?
# print(local_valiable)

print("---------------Python Global Variables ----------------------")
# Python Global Variables

golabl_variable = "Hey I'm a global variable"


def gobal_variable():
    print("global variable Inside a function ", golabl_variable)


gobal_variable()
print(golabl_variable)

# Why do we use Local and Global variables in Python?
print("---------------Why do we use Local and Global variables in Python? ----------------------")


def global_or_local_values():
    global_or_local_value = " I'm a  global_or_local_value from inside the function"
    print(global_or_local_value)


global_or_local_values()

global_or_local_value = "I'm a  global_or_local_value from outside the function"
print(global_or_local_value)
global_or_local_values()

# To change the gobal value of a variable from inside the function
print("---------------To change the gobal value of a variable from inside the function ----------------------")

globalKey = 1


def a():
    print("inside a function a()", globalKey)


def b():
    globalKey = 10
    print("inside a function b()", globalKey)


def c():
    global globalKey
    globalKey = 100
    print("inside function C()", globalKey)

print(globalKey)
a()
print(globalKey)
b()
print(globalKey)
c()
print(globalKey)
