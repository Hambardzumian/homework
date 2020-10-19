class hotel:
	def __init__(self,name,place,mid_room_price,lux_room_price):
		self.name = name
		self.place = place
		self.mid_room_price = mid_room_price
		self.lux_room_price = lux_room_price
	def presentation(self):
		print(F"HOTEL\n Name {self.name} \n Place {self.place} \n Rooms middle and lux \n room price {self.mid_room_price} (mid)  and {self.lux_room_price} (lux)")	

	def sale_hotel(self,prescent1,prescent2):
		sale_price1 = (prescent1 / 100) * 85 
		sale_price2 = (prescent2 / 100) * 70	
		print(sale_price1,"Dram  ---", "15%""sale for middle room" )
		print(sale_price2,"Dram  ---", "30%""sale for lux room" )

class taxi:
	def __init__(self,name_t,car_type,price_for_tour ):
		self.name_t= name_t
		self.car_type = car_type
		self.price_for_tour = price_for_tour
	
	def sale_taxi(self,prescent):
		new_price = (prescent / 100) * 75
		print(new_price,"Dram  ---",  "25%""-sale for Taxi")		
	def tpresentation(self):
		print(F"TAXI \nName car {self.name_t} \n type of car {self.car_type} \n Price for trip {self.price_for_tour}")

class tour:
	def __init__(self,name_u,price_lux,price_mid):
		self.name_u = name_u
		self.price_lux = price_lux
		self.price_mid = price_mid
		
	def upresentation(self):
		print(F"TOUR\n Name {self.name_u}\n Price lux {self.price_lux} and mid {self.price_mid}")


class all_price_for_tour(hotel,taxi,tour):
	def __init__(self,tour_price,mid_room_price,lux_room_price,price_for_tour,price_lux,price_mid):
		self.tour_price = tour_price
		hotel.__init__(self,mid_room_price,lux_room_price)
		taxi.__init__(self,price_for_tour)
		tour.__init__(self,price_lux,price_mid)
	def all_price_types(self):
		a = (self.lux_room_price + self.price_for_tour + self.price_lux)/100 * 90
		print(a,"10%","sale for lux tour")
		b = (self.mid_room_price + self.price_mid + self.price_for_tour)/100 * 95	
		print(b,"5%","sale for mid room")		
	
# All_price = all_price_for_tour(500000000,200000,300000,100000,50000,30000)
Mercedes_Benz = taxi("Mercedes_Benz","S600",100000)
Mariott = hotel("Mariott","Erevan",200000,300000)
Gegard = tour("Gegard Tour",50000,30000)

Mercedes_Benz.tpresentation()
Mariott.presentation()
Gegard.upresentation()
print("Salees %")
Mercedes_Benz.sale_taxi(100000)
Mariott.sale_hotel(200000,300000)
# All_price.all_price_types()



#50 u 61 toxer@ baceluc chgidem incha linum chem karum uxxem u tenc falsa berum 

