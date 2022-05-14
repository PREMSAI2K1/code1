class parent():
	def cook(self):
		print("i know cook")
class child(parent):
	def oops(self):
		print("i know inheritance") 
ob=child()
ob.cook()
ob.oops()		