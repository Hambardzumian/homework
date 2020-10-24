
class Students(object):
	def __init__(self,grade):
		self.__grade = grade
	
	# def __str__(self):
	# 	return "this is a object of students and its grade is {} ".format(self.__grade)	
	# def __int__(self):
	# 	return int(self.__grade)
	# def __bool__(self):

	# 	if self.grade > 10:
	# 		check = True
	# 	else:
	# 		check = False
	# 	return check		

		
	def __repr__(self):
		return "class student {}".format(self.__grade)	
	# def __del__(self):
	# 	print(self, "Object is succesfully deleted")
	def get_grade(self):
		return self.__grade
	def set_grade(self,new_grade):
		self.__grade = new_grade


	def __eq__(self,other):
		check =  type(self.__grade) == type(other)			
		return check	
a = Students(10.5)
print(a == 5)
dict_ = {1:a}
print(dict_)
# print(int(a))
# print(bool(a))
# a = Students(11)
# print(str(a))
# del a

# b = Students(50)

# print(a.get_grade())
# a.__grade = 5
# print(a.get_grade())
# a.set_grade(9)
# print(a.get_grade()) 