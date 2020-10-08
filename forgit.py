# import itertools

# a = {'1':['a','b'], '2':['c','d'], '3':['e','f']}
# list1 = a['1']
# list2 = a['2']
# list3 = a['3']
# b = list(itertools.product(list1,list2,list3))
# print(b)
# s = ""
# for i in b:
# 	for j in i:
# 		s +=j
# 	print(s)
# 	s = ""	



####################
######################

import random
computer_number = random.randint(1000,9999)
cows = 0
bools = 0

while True:
	try:
		usernumber = input('Tell me a number\t')
		if not usernumber.isdigit():
			raise Exception("Tell me a number")
		if int(usernumber) < 1000 or int(usernumber) > 9999:
			raise Exception("Tell me 4-digit number")
		break
	except Exception as e:
		print(e)
print("\t\t\t",computer_number)
a = str(computer_number)
computer_list = [a[0],a[1],a[2],a[3]]
b = str(usernumber)		
user_list = [b[0],b[1],b[2],b[3]]
for i in range(4):
	if a[i] == b[i]:
		cows +=1
	elif user_list[i] in computer_list:
		bools +=1
print("cows\t", f"{cows}")	
print("bools\t", f"{bools}")			

				