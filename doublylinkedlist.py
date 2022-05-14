class Node:
	def __init__(self,data):
		self.data=data
		self.prev=None 
		self.next=None 
class Linkedlist:
	def __init__(self):
		self.head=None 
	def display():
		temp=llist.head
		while(temp):
			print(temp.data)
			temp=temp.next
llist=Linkedlist() 
llist.head=Node(10)
second=Node(20)
third=Node(30)
four=Node(40) 
llist.head.next=second
second.prev=llist.head 
second.next=third
third.prev=second
third.next=four 
four.prev=third 
Linkedlist.display()