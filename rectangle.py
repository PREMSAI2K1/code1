class rectangle:
	def __init__(self,width,height):
		self.width=width
		self.height=height 
	def display(self):
		print(self.width,self.height)

class rectangleArea(rectangle):
	def read_input(self,width,height):
		self.width=width
		self.height=height 
	def display(self):
		super.__display__()
		print(self.width*self.height)
ob=rectangleArea(5,4)
ob.display()