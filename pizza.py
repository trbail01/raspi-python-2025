# Define a pizza class
class Pizza:
	def __init__(self,size,crust,toppings):
		self.size = size # e.g. 'Small','Medium','Large'
		self.crust = crust # e.g. 'Thin','Hand Tossed'
		self.toppings = toppings # list of toppings
		
	def add_toppings(self,topping):
		self.toppings.append(topping)
		print(f"{topping} added")
		
	def remove_topping(self,topping):
		if topping in self.toppings:
			self.toppings.remove(topping)
			print(f"{topping} removed")
		else:
			print(f"{topping} not found on pizza")
			
	def describe(self):
		print(f"Pizza size:{self.size}")
		print(f"Crust type:{self.crust}")
		print(f"Toppings:{','.join(self.toppings) if self.toppings else 'No toppings'}")
