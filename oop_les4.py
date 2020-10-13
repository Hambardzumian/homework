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
