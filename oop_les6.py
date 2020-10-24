class Country:
	def __init__(self,cname,continent):
		self.cname = cname
		self.continent = continent
	def presentation(self):
		print(F"{self.cname} is a country in {self.continent}")	

class Brand:
	def __init__(self,brand_name,start_date):
		self.brand_name = brand_name
		self.start_date = start_date
	def brand_presentation(self):
		print(F"{self.brand_name} start date is {self.start_date}")

class Season:
	def __init__(self,seson_name, temperature):
		self.seson_name = seson_name
		self.temperature =temperature
	def seson_presentation(self):
		print(F"In {self.seson_name} temperature is {self.temperature}")	


class product(Country, Brand, Season):
	def __init__(self,name,type_,price,quantiti,cname,brand_name,seson_name,continent,start_date,temperature):
		self.name = name
		self.type_ = type_  
		self.price = price
		self.quantiti = quantiti
		Country.__init__(self,cname,continent)
		Brand.__init__(self,brand_name,start_date)
		Season.__init__(self,seson_name,temperature)
	def pr_present(self):
		print(F"Product name {self.name}")
		print(F"Country {self.cname}")
		print(f"Brand {self.brand_name}")
		print(F"Price {self.price}")
		print(F"Quantiti {self.quantiti}")
	

	def discount(self,precent):
		n_price = self.price -(self.price * precent) /100
		print(F"Product price with {precent} precent is {n_price}")


	def numb_quantiti(self):
		if self.seson_name == "summer" or self.seson_name == "winter":
			self.quantiti += 0.5 * self.quantiti
		print("The avaible quantiti of a product", self.quantiti)

Germany = Country("Germany","Europe")		
Adidas = Brand("Adidas",1949)
summer = Season("summer",35)
Yezzy = product("Adidas","Yezzy",500,2500,"Germany","Adidas","summer","Europe",1949,35)

Germany.presentation()
Adidas.brand_presentation()
summer.seson_presentation()
print("")

Yezzy.pr_present()
print("")

Yezzy.discount(30)
Yezzy.numb_quantiti()

			
									