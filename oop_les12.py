import os
base_dir = os.getcwd()

print("we are now in  {}".format(base_dir))
os.chdir("/Users/USER/Desktop/homework/Current_work_dir")

try:
	a = input("Do you want to delete the contents of the file \n for yes writw y, for no write n ")
	if a == "y":
		path = F"{os.getcwd()}/dir1"
		os.rmdir(path)
		path = F"{os.getcwd()}/dir2"
		os.rmdir(path)
		path = F"{os.getcwd()}/dir3"
		os.rmdir(path)
		path = F"{os.getcwd()}/dir4"
		os.rmdir(path)
		path = F"{os.getcwd()}my.txt"
		os.remove(path)
		
	if a == "n":
		print("We did deleted the contents of the file")
	else:
		raise Exception(" for yes writw y, for no write n")	
except Exception as error:
	print(error)		

print("thank you !!!")		
