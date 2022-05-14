class father:
	def drive(self):
		print("i can drive")
class mother:
	def cook(self):
		print("i can cook")
class child(father,mother):
	def code(self):
		print("i can code")
ob=child()
ob.drive()
ob.cook()
ob.code()