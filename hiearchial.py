class parent:
	def drive(self):
		print("i can drive")
class child1(parent):
	def cook(self):
		print("i can cook")
class child2(parent):
	def code(self):
		print("i can code")
ob=child1()
ob.drive()
ob.cook()
ob1=child2()
ob1.drive()
ob1.code()