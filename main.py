
########################################################
########################################################
# Are you trying to open an exercise or challenge? 
# open a folder to the left and find the file you want
# need help running a file? press play above!
########################################################
########################################################

 
def main():
	#this is code to remind how to open a file
	print("running main- did you mean to run a different file?")

	print() # print blank line
	set_up_shell()

	print() # print blank line
	set_up_folder()

	print() # print blank line
	set_up_file()



def set_up_shell():
	shell_question = 'Do you see at least "~/tutoringben" (not ">") on the \n right or bottom window? (y/n) '
	
	shell_completed = (valid_input(shell_question, ['y', 'n']) == 'y'); 

	if not shell_completed:
		#step is not completed
		shell_instructions = get_os_instruction()
		print("Shell isn't quite set up yet")
		instruct(shell_question, shell_instructions)

	print("Yay! The shell is open!")

def get_os_instruction():
	os = valid_input("Are you on mac or pc? ", ["mac", "pc"])
	if os == "mac":
		instructions = "\n (1) Press Cmd+Shift+P or F1 \n"
	else:
		instructions = "\n (1) Press Ctrl+Shift+P or F1 \n"

	instructions += ' (2) Now type in "open shell" and select that option \n'

	return instructions


def set_up_folder():
	folder_to_open = valid_input("Which folder is the file you want to run in? ", ["Exercises", "Challenges"])

	folder_question = 'Do you see "~/tutoringben/' + folder_to_open + ' $" in the terminal? '

	folder_completed = (valid_input(folder_question, ['y', 'n']) == 'y'); 


	if not folder_completed:
		#step is not completed

		#are we in the wrong folder?
		wrong_folder_question = 'Is it blank after "~/tutoringben" besides "$"? '
		in_right_folder = valid_input(wrong_folder_question, ['y', 'n']) 

		if(in_right_folder == "n"):
			wrong_folder_instruction = '\nRun the command "cd .." in the terminal. (This just exits the current folder) \n'
			instruct(wrong_folder_question, wrong_folder_instruction)
			print("\nWe still aren't in the right folder")

		#open the right file
		folder_instructions = '\nRun the command "cd ' + folder_to_open + '\\" in the terminal. (cd stands for change directory)\n'

		instruct(folder_question, folder_instructions)

	print("Whew! Correct folder is open!")

def set_up_file():
	correct_file = 'n'
	while correct_file == 'n':
		file_to_open = input("What file do you what to open? ")
		correct_file = valid_input("Is " + file_to_open + " the correct file? ", ['y', 'n'])


	file_question = 'Have you tried the "Python3 ' + file_to_open + '" command in the shell? ' 

	file_completed = (valid_input(file_question, ['y', 'n']) == 'y')

	if not file_completed:
		#step is not completed
		file_instructions =  'Run the command "python3 ' + file_to_open + '" in the shell and press enter'
		
		instruct(file_question, file_instructions)

	print("Yay! We can run the file")



#this function prompts the user with a question and forces the user to
#with a valid answer and return the answer
def valid_input(prompt, options):
	result = input(prompt)
	#prompt until valid response
	while result not in options:
		#look up the function join - really cool 
		result = input("Please enter " + ' or '.join(options) + '. ')
	return result 


#givees instructions until give question is valid
def instruct(question, instructions):
	print("That's ok! We'll get it")
	print(instructions)

	answer = valid_input(question, ['y', 'n'])
	while answer == 'n':
		print("\nLet's try again!")
		print(instructions)
		answer = valid_input(question, ['y', 'n'])



#this just runs the main function above when we run this file as a script
if __name__ == '__main__':
	main();