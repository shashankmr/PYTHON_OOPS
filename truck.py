from vehicle import Vehicle

class truck(Vehicle):
	
	max_load = 0
	speed_limit = 20

	def __init__(self, max_load, speed_limit,no_of_wheels, speed, weight, mileage, color):
		self.max_load = max_load
		self.speed_limit = speed_limit
		super().__init__(no_of_wheels, speed, weight, mileage, color)

	def load(self):
		print("Truck is loaded")
	
	def unload(self):
		print("Truck is unloaded")



	
