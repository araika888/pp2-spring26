#1
def my_function1(fname):
    print(fname + " Refsnes")

my_function1("Emil")
my_function1("Tobias")
my_function1("Linus")

#2
def func(uni):
    print("I study at university " + uni)

uni = "KBTU"
func(uni)

#3
def my_function2(name): # name is a parameter
    print("Hello", name)

my_function2("Arai") # "Arai" is an argument

#4
def my_function33(fname, lname):
    print(fname + " " + lname)

my_function33("Emil", "Refsnes")

#5
def my_function(country = "Norway"):
    print("I am from", country)

my_function("Sweden")
my_function("Kazakhstan")
my_function()
my_function("Brazil")