#1-1
#The user inputs their weight and the program returns what their weight would be on another planet

# Milestone 1: Make sure this works first before moving on! The user inputs their weight and the program returns what their weight is on the moon. You will have to look up how your weight changes when your are on another planet. 

# Milestone 2: (If you have time) The user inputs their weight and some planet and the program returns what their weight on that planet is. 

# Beyond: Really excited by this program? Add your own spin! What do you think it needs? Some inspiration: What else would be different on different planets? What is their survival changes on that other planet? 

#!!!!! Having trouble running this? run main above and follow the instructions! Let me know if you have any questions! 

#auto indent : https://www.tutorialspoint.com/online_python_formatter.htm

def main():
	#write code here
	print("weight-converter ")
	result = input("what is your weight?")
	weight = int(result)
	print(weight)
	result = input("what planet would you like to know your weight on?")
	if result == "moon" :
		weight_mult = 0.165
	elif result == "venus" : 
		weight_mult = 0.9
	elif result == "saturn" :
		weight_mult = 1.07
	elif result == "neptune" :
		weight_mult = 1.10
	elif result == "mars" :
		weight_mult = 0.379
	elif result == "mercury" :
		weight_mult = 0.376
	elif result == "jupiter" :
		weight_mult =  2.4
	elif result == "uranus" : 
		weight_mult = 0.86

	weight = weight * weight_mult
  print(weight)

  

#write any helper functions here

#this just runs the main function above when we run this file as a script
if __name__ == '__main__':
	main();