# File capitalizer

import os
import time

print("WELCOME TO FILECAPITALIZER!\nBy ShubhamProgmer - https://github.com/ShubhamProgmer\n\n-> Used to capitalize the first letter of any file in a directory.\n-> You can provide or create a txt file of files not to touch.\n-> You can give any one extention to ignore all the files of that extention.\n")

def readingFile(txtFile):
	print("\nReading file...(Please wait), --Ignore if chosen option \'3\'")
	f = open(txtFile)	
	time.sleep(1)
	content = f.read()
	f.close()
	z = open(txtFile, "a")
	z.write(f"\n{txtFile}")
	z.close()
	print("File reading completed...")
	global finalList
	finalList = content.split("\n")
	print()
	
def createFinal():
	global fileToChange
	fileToChange = (os.listdir(direc)) 
	for files in fileToChange:
		if files in finalList:
			fileToChange.remove(files)
		
def finalOperation(formateName):
	print()
	print("Doing Task...")
	time.sleep(1)
	for names in fileToChange:
		if formateName in names:
			pass
		else:
			b = str(names[0].upper()) + names[1:len(names)]
			os.rename(names, names+'.temp')
			os.rename(names+'.temp', b)
	print("Task done!\nYou can delete \'Test.txt\' or provided text file manually from chosen directory. --Ignore if chosen option \'3\'")

while True:				
	while True:				
		direc = input("Please enter the directory location: ")
		try:
			os.chdir(direc)
			break
		except Exception as e:
			print("Directory not found!")
			continue

	while True:
		choice1 = input("\nGive input \'1\' if you have a txt file containing file names not to touch\nGive input \'2\' if you want to create one\nGive input \'3\' if you dont want to provide txt file!:\n")
		
		
		if choice1 == "1":
			txtFile = input("Please enter the name of txt file: ")
			try:
				readingFile(txtFile)
				createFinal()
				formateName = input("Please enter the extention of file not to touch! (including \'.\'), (enter \'NULL\' if none): ")
				finalOperation(formateName)
				break
			except Exception as a:
				print("File not found! ")
				print()
				continue
				
		
		elif choice1 == "2":
			print()
			print("Creating a text file named \'Test.txt..'")
			j = open("Test.txt", "w")
			j.close()
			txtFile = "Test.txt"
			print("Please enter the names of files NOT TO TOUCH (along with extention) and enter \'quit\' to exit\n")
			while True:
				j = open("Test.txt", "a")
				m = input()
				if m == "quit":
					j.close()
					break
				else:
					j.write(f"\n{m}")
			print()
			readingFile(txtFile)
			createFinal()
			formateName = input("Please enter the extention of file not to touch! (including \'.\'), (enter \'NULL\' if none): ")
			finalOperation(formateName)
			
		
		elif choice1 == "3":
			r = open("Test.txt", "w")
			r.close()
			txtFile = "Test.txt"
			readingFile(txtFile)
			createFinal()
			formateName = input("Please enter the extention of file not to touch! (including \'.\'), (enter \'NULL\' if none): ")
			finalOperation(formateName)
			os.remove("Test.txt")
		
		
		else:
			print("Please enter a valid option!")
			continue
		break
		
	
	print()
	lalchi = input("Do you want to use it again? (y/n): ")
	print()
	while True:
		if lalchi == "y":
			break
		elif lalchi == "n":
			print("Thank you for using FileCapitalizer!\nExiting....")
			time.sleep(3)
			exit()
		else:
			print("Please enter a valid option! (\'y\' for YES and \'n\' for NO)")
			continue
	continue
		