SEGFAULT = 0
BADOUTPUT = 1
RETVALUE = 2
TIMEOUT = 3

class Test:
    def __init__(self, name, category):
        self.name = name
        self.age = age

class Category:
    def __init__(self, name, category):
        self.name = name
        self.age = age



my_cat = Category("Solving - Error Handling", None)
my_test = Test("Bad Carac", my_cat)
my_test.addtest("Only X", "Checking with map...")
my_test.error("Only X", SEGFAULT, expected="LOL", got="")
