#Part 1 - get comfortable with the terminal! 
#       - interactive python! 
#Part 2 - work through some functions! 

MY_NAME = "Ben"
MY_AGE = 13

def main():

    #(a) logical operators
    #print("I should climb: ", should_I_climb())
    #print("I should swim: ", should_I_swim())
  


    #(b) While vs For Loop 
    #print_age_alot1()
    #print_age_alot2()
    tell_joke()




#(a) logical operators
def should_I_climb():
    RAINING = False 
    WITH_FRIEND = True 
    def should_I_climb():
        if(not RAINING and WITH_FRIEND):
            return True
        else:
            return False 

def should_I_swim():
    NAUSEA = False
    LIFEGUARD = False
    SHARK = False
    AT_FRIENDS_POOL = False
    def should_I_swim():
    if(not NAUSEA and not SHARK and (LIFEGUARD or AT_FRIENDS_POOL)):
        return True
    else :
        return False



#(b) While vs For Loop 
def print_age_alot1():
    for i in range(11):
        print(i)


def print_age_alot2():
    i = 0
    while i <= 10:
        print(i)
        i += 1

#(1) how could we change this to keep going forever
#(2) How could we keep going until the user tells us to stop?
def tell_joke():
    #annoying_joke = True
    
    result = ""
    while (result != "stop it!") :
        input("Knock Knock ")
        result = input("banana ")
        #if result == "stop it!" :
          #annoying_joke = False
    input("Knock Knock ")
    input("orange ")
    print("orange you glad I didn't say banana!")


if __name__ == '__main__':
	main()