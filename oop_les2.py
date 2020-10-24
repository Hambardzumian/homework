# class Text():  # karanq grenq def__init__(self,age) u 10rd toxum grenq Text(568)

# 	def __init__(self):
# 		self.name = input("tell smthing\n")


# 	def printing(self):
# 		print(self.name)

# my_object = Text()
# my_object.printing()
# ##########
# class tringle:
# 	def __init__(self, a, b, c):
# 		self.a = a
# 		self.b = b
# 		self.c = c

# 	def paragic(self):
# 		p = self.a + self.b + self.c	
# 		print(p)
# erankyun = tringle(6,7,8)		
# erankyun.paragic()
 
import random
d = {}
n_d = {}
class task:
	def __init__(self,):
 		self.word = input("Tell me word")

	def	dictionary(self):
 		for i in self.word: 
 			d[i] = random.randint(1,10)
 		print(d)

 	
	def dublicate(self):
		for key, value in d.items():
			if value not in n_d.values():
				n_d[key] = value
		print(n_d)

	def max_3(self):
		list_ = list(n_d.values())	
		a = list_.sort()  
		print(list_[-1],list_[-2],list_[-3])


example = task()
example.dictionary() 	
example.dublicate()
example.max_3()

