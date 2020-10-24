# class Store:
# 	def presentation(self):
# 		return "This store sells equipments"
# class ClothesStore:
# 	def presentation(self):
# 		return "This store sells clothes"

# class Shoes(ClothesStore):
# 	def presentation(self):
# 		b = super().presentation()

# 		return b, "This shoe is for kids"


# shoe_1 = Shoes()
# print(shoe_1.presentation())
# a = Store()
# b = ClothesStore()
# print(a.presentation())
# print(b.presentation())			
# class Store:
# 	def __init__(self,text):
# 		self.text = text
# 	def presentation(self):
# 		return self.text


# class NewStore(Store):
# 	def __init__(self,text,type_):
# 		super().__init__(text)
# 		self.type_ = type_
# 	def presentation(self):
# 		presentation = F"{super().presentation()}and its type is{self.type_}"
# 		return presentation	

# little_store = NewStore("Hi we are saturn we sell cellphones","phone-seller")
# print(little_store.presentation())		

# class ClothesStore:
# 	def presentation(self):
# 		return "This store sells  clothes not"

# class Shoes(ClothesStore):
# 	def presentation(self):
# 		b = super().presentation()

# 		if "not" in b:
# 			b += "))))"

# 		return b	
# shoe_1 = Shoes()
# print(shoe_1.presentation())


# class Store:
# 	def __init__(self, text):
# 		self.text = text
# 	def presentation(self):
# 		return self.text
	

# 	def set_text(self,new_text):
# 		try:
# 			if new_text.isalpha():
# 				self.text = new_text
# 		except:
# 			print("wrong value")	

# new_store = Store("Saturn")
# print(new_store.text)
# new_store.text = 5
# print(new_store.text)