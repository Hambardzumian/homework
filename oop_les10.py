import random

class house_temp:
	current1 = random.randint(1,40)
	current2 = random.randint(1,40)
	current3 = random.randint(1,40)
	current4 = random.randint(1,40)


	def __init__(self,fin1, fin2,fin3,fin4):
		self.fin1 = fin1
		self.fin2 = fin2
		self.fin3 = fin3
		self.fin4 = fin4

	def __del__(self):
		print("Object is succesfully deleted")	


	def display(self):
		print(f"Room1:\t Current temperature  {self.current1}, final temperature {self.fin1}")
		print(f"Room2:\t Current temperature  {self.current2}, final temperature {self.fin2}")
		print(f"Room3:\t Current temperature  {self.current3}, final temperature {self.fin3}")
		print(f"Room4:\t Current temperature  {self.current4}, final temperature {self.fin4}")


	def fixation(self):
		list1 = [self.current1,self.current2,self.current3,self.current4]
		list2 = [self.fin1,self.fin2,self.fin3,self.fin4]

		for i in range(0,4):
			if list1[i] != list2[i]:
				list1[i] = (int(list1[i]) + 2 * int(list2[i]))/3


		self.current1 = int(list1[0] + 0.5)
		self.current2 = int(list1[1] + 0.5)
		self.current3 = int(list1[2] + 0.5)
		self.current4 = int(list1[3] + 0.5)

		self.display()
		print("")


	def changes(self):
		list1 = [self.current1,self.current2,self.current3,self.current4]
		list2 = [self.fin1,self.fin2,self.fin3,self.fin4]
		amount = 0

		for i in range(0,4):
			if list1[i] == list2[i]:
				amount += 1

		print(amount, "houses have normal temperatures")		
	
	def __bool__(self):
		if self.current1 == self.fin1:
			check = True
		else:
			check = False
		return check	
		
a = house_temp(22,35,27,18)	
a.display()
print(" ")	
a.fixation()
a.changes()
print(bool(a))
a.fixation()
a.changes()
a.fixation()
a.changes()
a.fixation()
a.changes()