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
	def search():
		print("enter search element3")
		key=int(input())
		count=1
		temp=llist.head
		while(temp):
			if temp.data==key:
				print(count)
				break
			else:
				count=count+1
				temp=temp.next
llist=Linkedlist() 
llist.head=Node(1)
second=Node(2)
third=Node(3)
four=Node(4)
llist.head.next=second
second.next=third
third.next=four 
Linkedlist.display()
Linkedlist.search()
