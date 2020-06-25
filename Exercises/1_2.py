#Functions! 

def main():
	print_hello()
	#cutest_dog()

	#string_indexing()
	#test_string_indexing()

	#reverse_string("apple")


	#shift_by_1("Gh\x1fAdm")

#how could we simplify this with decomposition? 

def print_hello():
	print_H() 
	print() 
	print_E()
	print()
	print_L()
	print()
	print_L()
	print()
	print_O() 


def print_H():
    print("|   |")
    print("|   |")
    print("|---|")
    print("|   |")
    print("|   |")
	
def print_E():
	print("_____")
	print("|    ")
	print("|--- ")
	print("|    ")
	print("|____")
	
def print_L():
	print("|")
	print("|")
	print("|")
	print("|____")

def print_O():
    print("_____")
    print("|   |")
    print("|   |")
    print("|___|")



##Didn't get to below

#make a function that asks the user "Who is the cutest dog?"until they reply with your dog's name 
def cutest_dog():
	print("Shasha is the best dog")

#return the max of 3 numbers 

################################
#           Strings 
################################

def string_indexing():
	s = "Python is the best"
	print("s : " + s)
	print("s[0] : " + s[0])
	print("s[0:3] : " + s[0:3])
	print("s[0:] : " + s[0:])
	print("s[-1] :" + s[-1])
	print("s[0:::2] : " +  s[0:6:2])

def test_string_indexing():
	s = "When life gives you lemons, make lemonade"

	print(s[4] + ": answer")
	print(s[-1] + ": answer")

	print("a :", s[:]) 

	print(s[4] + ": answer")
	print(s[:4] + ": answer")

	print("lemons :" +  s[:]) 

	print(s[:25] + s[27:-3] + "answer")


#reverse a string 
def reverse_string(s):
	return s


#remove every e in a string
def remove_es(str):
	return str

#casear cipher - shift every character by 1 (if have time)
#how would we ignore punctuation? 
#right now we aren't wrapping around the alphabet ex. z doesn't do to a
def shift_by_1(s):
	return str


if __name__ == '__main__':
	main();