class Dog:
	# my class definition goes here
	def __init__(self, fur_color, size, name):
		self.fur_color = fur_color # set my fur color as the input fur color
		self.size = size # set my size
		self.name = name # set my name

	def walk(self): # go for a walk
		print(self.name + " is going for a walk!")

	def return_size(self): # return my size
		return self.size

	def bark_num_times(self, num): # bark num times
		for i in range(num):
			print("Bark!")

# creating an instance of Dog called sasha
sasha = Dog("cocker spaniel", 10, "Sasha")
sasha.walk()
print(sasha.return_size())
print(sasha.size)
print(sasha.name)

sasha.bark_num_times(20)

# print("Hello!")