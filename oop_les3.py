

################
1xndir
class Circle:
	def __init__(self,radius):
		self.radius = radius
	def paragic(self):
		p = 2* 3.14 * int(self.radius)	
		print(p)

	def area(self):
		s = 3.14 * int(self.radius)**2
		print(s)

Circle = Circle(1)
Circle.paragic()
Circle.area()	
##############################
2 xndir






#3rd xndir



class Person :
	def __init__(self,age,country):
		self.age = age
		self.country = country
class Student:
	def __init__(self,weigth,heigth,age,country):
		self.weigth = weigth
		self.heigth	= heigth
		Person.__init__(self,age, country)

Jane = Student("70kg","165sm" ,22,"Armenia" )
print(Jane.weigth)		 		
print(Jane.age)		
print(Jane.country)		
print(Jane.heigth)