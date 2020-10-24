import json
with open("py_file.txt") as file:
	read_value = file.read()
print(read_value)
######################	
	# for line in file:
	# 	print(line)

########################


with open("sample_json.json","r") as file2:
	data = json.load(file2)
print(data)
print(type(data))	
print("\n",data["items"][0])	
################ 
# read_value += "\n today is 10/22/2020"
# with open("py_file.txt","a") as file:
# 	file.write(read_value)


######################

