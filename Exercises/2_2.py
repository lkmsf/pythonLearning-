#All about functions! 

def main(): 

    #(a) Return vs. Print
    #print_name1()
    #print_name2()

    #(d) Parmeters
    #affirm()
    #parm_mys_code()

    #(c) Writing good functions
    #add_nums(2,2)

    #(d) Decomposing a big problem into smaller steps 
    #build_house(10)
    #build_house(3)

    

#(a) Return vs. Print
def print_name1():
    print(MY_NAME)

def print_name2():
    return MY_NAME 

#(b) parmeters
def affirm():
    print("Lauren" + "you are amazing!")
    print("Lauren" + "is wonderful, just wonderful")
    print("Watch out world! " + "Lauren" + "is coming")
    print("Lauren" + "deserves a million dollars.")
    print("Lauren" + "is really great at python!")

def parm_mystery(a, b):
    print("a is " + str(a))
    print("b is " + str(b))

def parm_mys_code():
    parm_mystery(1,1)
    # parm_mystery(1,5)
    # c = 10 
    # d = 15
    # parm_mystery(c,d)
    # a = 2
    # b = 6
    # parm_mystery(a,b)
    # parm_mystery(b, a)


#(c) Writing good functions

#a good function should do “one conceptual thing.”
#TO DO: Fix this! 
def add_nums(a, b):
    print("added is:", a+b)
    print("subtracted is:", a-b)

#a good function should have a descriptive name
#TO DO: Fix these! 
def does_something(x):
    b = x * x
    return b

#(d) Decomposing a big problem into smaller steps 
#TO DO How should we decompose this problem? 

# a house has a floor, 2 walls, and a flat roof 
# the floor has length "width" and the height is 
# half of "width" rounded down.
# ex. a house with width 5
# -----
# |   |
# |   |
# -----    
# a house with width 6
# ------
# |    |
# |    |
# |    |
# ------

def build_house(width):
    pass 


if __name__ == '__main__':
	main()