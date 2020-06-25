# Control statements!

# Done writing the problems! 

# Try to just get as far as you can. You have enough knowledge to at least attempt all of the problems! If you have more time try out the extra challenge!
# If you don't fully understand a problem, just do your best!

# TO DO: 
# (1) Work on Bash_Crawl until you get comfortable with moving around 
# (2) Work on these functions! 

#uncomment functions in main() as you work on them! 
def main():
    print("Make this print out in the shell")

    #Logical operatives
    which_dessert()

    #While vs. For loops
    #cutest_dog()
    #repeat_programming()
    # neverending_song()

    #building 
    #       note - you may want to expand the size of the shell for these   problems! (make it wider)
    #build_4x4()
    #build_wall()
    #build_floor()
    #build_walls_double()
    #build_flat_house()

    #extra challence - build house
    #build_roof()
    #build_house(





#
# logical operatives 
#

#This returns what dessert you should get based on 
#some logical operators
#TO DO: Add at least 4 conditions below and create a logical flow with those
# to figure out what dessert you want to eat. Use each of "and", "or", "not" as least once. 
#Be creative! Feel free to make it as complex as you want

def which_dessert():
    #conditions  
    warm = False 
    something_sweet = False 
    chocolate = False 
    salty = False
    cold = False
    #logic
    result = input("warm?")
    if result == "yes":
      warm = True
    else:
      warm = False
    result1 = input("sweet?")
    if result1 == "yes":
      something_sweet = True
    else:
        something_sweet = False
    result2 = input("chocolate?")
    if result2 == "yes":
      chocolate = True
    else:
      chocolate = False
    result3 = input("salty?")
    if result3 == "yes":
      salty = True
    else:
      salty = False
    result4 = input("cold?")
    if result4 == "yes":
      cold = True
    else:
      cold = False
    if warm and something_sweet:
      if chocolate:
        return "chocolate Ice Cream" 
      else:
        return "vanilla ice cream"
    if warm and salty:
      if chocolate:
        return "sea salt chocolate bar"
      else:
        return "pretzel"
    if something_sweet and chocolate and warm:
      return "chocolate shake"
      if not something_sweet:
        return "pure chocolate"
    if (something_sweet and cold) or (something_sweet and salty) :
      return "Some flavorful pork! But that is not a dessert!"




#
# While vs. For loops 
#

#This is a function that asks the user "Who is the cutest dog?" until they reply with your dog's name 
# TO DO: implement this!
#Do we want a while loop or a for loop?

def cutest_dog():
  ROVER = False
  while (ROVER == False) :
   result = input("Who is the cutest dog?")
   if result == "Rover" :
     ROVER = True
     print("Yes!")

  
	


#This prints out "Programmimg is the best!"" 18 times
# TO DO: implement this!
#Do we want a while loop or a for loop?
def repeat_programming():
  for i in range(18) : 
    print("add code here")

#The song that never ends! 
#TO DO: Change this to print the neverending song 20 times or 
#until the user inputs "Stop this!" - whichever comes first
def neverending_song():
    print("This is the song that never ends, yes it goes on and on my friend. Some people started singing it, not knowing what it was, and they'll continue singing it forever just because...This is the song that never ends, yes it goes on and on my friend. Some people started singing it, not knowing what it was, and they'll continue singing it forever just because...")


#Question to answer: (just type a comment)
#Q: Any ideas for when do we want to use a for loop vs a while loop? (hint: what would happen if you use the opposite type of loop in the functions above?)
#A: 

#
#Let's build some things! 
#

#This builds a 4 by 4 block
#TO DO: clean this code up with some sort of loop 
def build_4x4():
  for i in range(20):
    print("....")
    print("....")
    print("....")
    print("....")

#This builds a wall - a wall is defined as 4 * 20 

# ....
# ....
# ....
# ....
# (but 20 times)

#TO DO: implement this. 
#Tip: how could we use build_4x4() here?
# make sure to avoid repeated code! 
def build_wall(): 
    pass  #remove pass when finished

#Builds a floor - a floor is defined as 58 by 4
#
# ..........................................................
# ..........................................................
# ..........................................................
# ..........................................................
#
# TO DO: (1) implement this! 
# Tip:  build_4x4() doesn't help here - do you see why?
#
# TO DO: (2) Once you have that working, adjust the code so you don't have "........ etc" 58 times, make it easy to switch this code to a floor of a different length
#   Tip:  we can print without a new line (aka print on the same line) with print("string", end ="")
#           ex. print(apple); 
#               print("orange", end = "")
#           prints out "appleorange"

def build_floor():
    pass 


#This builds two walls with a space in between 
# a small version of it is: 
#
# ....                          ....
# ....                          ....                         
# ....                          ....
# ....                          ....
# The final dimensions should be:
# each wall has length of 4  (height of 20) with a space of 50 in between 
#tip: build_wall won't help you much here. Do you see why?
def build_walls_double():
    pass


#builds a  house with a triangle roof! With the dimensions given above
#TO DO: Implement this! This should be less than 5 lines of code
#tip: use the functions you wrote above! a floor looks just like a roof!
def build_house():
    pass

#
# Extra challenge: Build house 
#

#This builds a roof with a base of 58 that goes to a peak 
#TO DO: implement this. Make sure to complete each milestone before moving forwards!
#milestone 1: build a roof with a base of 3. Note the roof will be semi-lopsided (off by the tinest amount - that is ok)
#milestone 2: build an inverted roof with a base of 5 (so upsidedown triangle)
#milestone 3: now use a for loop to build this inverted roof (think about how i is changing and how that helps you use the loop)
#       It might be helpful to first build a lopsided triangle 
#       .....
#       ....
#       ...
#       ..
#       .
#       and then work beyond that
#milestone 4: Now use a for loops to build this roof right side up!
#milestone 5: now build a roof with a base of 58
def build_roof():
    pass


#builds a a house with a triangular roof! With the dimensions given above
#TO DO: Implement this! This should be less than 5 lines of code
#tip: use the functions you wrote above! a floor looks just like a roof!
def build_flat_house():
    pass


#even more time? 
# ideas:
# add a door, window, potted plant
# change the dimensions  of the house 




if __name__ == '__main__':
	main();