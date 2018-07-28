from vehicle import Vehicle

class car(Vehicle):

	ac = "off"
	steering_wheel = "steady"
	seat_belt = "unlocked"
	audio_player = "off"

	def __init__(self, ac, steering_wheel, seat_belt, audio_player,no_of_wheels, speed, weight, mileage, color):
	self.ac = ac
	self.steering_wheel = steering_wheel
	self.seat_belt = seat_belt
	self.audio_player = audio_player
	super().__init__(no_of_wheels, speed, weight, mileage, color)

	def drift(self):
		print("Car's drifting")
	
	def deploy_airbags(self):
		print("Airbags has been deployed")

