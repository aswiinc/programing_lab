class publisher:
	def __init__(self):
		self.name=input("Enter the name of thr Publisher : ")
	def display(self):
		print(f"Name of the author is {self.name}")
class book(publisher):
	def __init__(self):
		self.title=input("Enter the title of the book : ")
		self.author=input("Enter the name of the author : ")		
		super().__init__()
	def display(self):
		print(f"Name of the book is {self.title} ")
		print(f"Name of the author is {self.author} ")
class python(book):
	def __init__(self):
		super().__init__()
		self.price=input(f"Enter the price of the book : ")
		self.pages=input(f"Enter the number of pages : ")
	def display(self):
		super().display()
		print(f"The price of the book is {self.price}")
		print(f"The number of pages is {self.pages}")
obj=python()
obj.display()
		
