
# Print intro
print("Hello! My name is Lauren")
age = 20
print("I am " + str(age), "years old.")

#conversation w/ computer
name = input("what is your name? ")
print("Hello! "+ name + ". Nice to meet you!")

#dog age
age_str = input("How old is your dog? ")
dog_years = float(age_str) * 7
print("Dog years: ", dog_years)


#object w/ similar color
color = input("choose a color! ")

if color == "yellow":
	print("Gold is also yellow")
elif color == "red":
	print("roses are also red")
elif color == "green":
	print("grass is also green")
else: 
	print("color isn't entered yet")


