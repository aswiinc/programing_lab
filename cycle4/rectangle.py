class rectangle:
	
	def __init__(self,a,b):
		self.length=a
		self.breadth=b
		self.area()
		self.perimeter()
	def area(self):
		self.area1=self.length*self.breadth
		
	def perimeter(self):
		self.perimeter1=2*(self.length+self.breadth)
		
l1=int(input("Enter the length of rectangle 1: "))
b1=int(input("Enter the breadth of rectangle 1: "))
l2=int(input("Enter the length of rectangle 2: "))
b2=int(input("Enter the breadth of rectangle 2: "))
r1=rectangle(l1,b1)
r2=rectangle(l2,b2)
print(f"\nArea of Rectangle one is: {r1.area1}\n Area of Rectangle 2 is: {r2.area1}")
if(r1.area1>r2.area1):
	print("Rectangle 1 is larger")
else:
	print("Rectangle 2 is larger") 
