class Rectangle:
    def __init__(self):
        self.__length=int(input("enter length of rectangle"))
        self.__breadth=int(input("enter breadth of rectangle"))
    def findarea(self):
        self.area=self.__length*self.__breadth
        return self.area
	
    def __lt__(self,other):
        if(self.findarea() < other.findarea()):
            print("area of rectangle two is greater")
        else:
            print("area of rectangle one is greater")

ob1 = Rectangle()
print(f"area of rectangle one is {ob1.findarea()}")
ob2 = Rectangle()
print(f"area of rectangle two is {ob2.findarea()}")
ob1<ob2
