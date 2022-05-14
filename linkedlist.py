class Node:
	def __init__(self,data):
		self.data=data
		self.next=None 
class Linkedlist:
	def __init__(self):
		self.head=None 
	def display():
		temp=llist.head
		while(temp):
			print(temp.data)
			temp=temp.next 
	def insertatbegin():
		print("new node inserted")
		four=Node(4)
		four.next=llist.head 
		llist.head=four 
		Linkedlist.display()
	def insertatend():
		print("insertat end")
		five=Node(5)
		temp=llist.head
		while(temp.next!=None):
			temp=temp.next 
		temp.next=five 
		Linkedlist.display() 
	def delfirstnode():
		print("deleted node")
		llist.head=llist.head.next
		Linkedlist.display() 
	def dellastnode():
		print("last node deleted")
		temp=llist.head 
		while(temp.next.next!=None):
			temp=temp.next 
		temp.next=None 
		Linkedlist.display() 
	def insertatposition():
		print("insert at position")
		six=Node(6)
		pos=int(input())
		if pos==1:
			six.next=llist.head 
			llist.head=six 
			Linkedlist.display()
		else:
			temp=llist.head
			for i in range(1,pos-2+1):
				temp=temp.next 
			six.next=temp.next 
			temp.next=six 
			Linkedlist.display()



llist=Linkedlist()
llist.head=Node(1)
second=Node(2)
third=Node(3)
llist.head.next=second
second.next=third 
Linkedlist.display()
Linkedlist.insertatbegin()
Linkedlist.insertatend()
Linkedlist.delfirstnode()
Linkedlist.dellastnode()
Linkedlist.insertatposition()
