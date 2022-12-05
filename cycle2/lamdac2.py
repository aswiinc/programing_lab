def square():
    a=int(input("enter side of square"))
    l1=lambda x:a*a
    print("Area of square is",l1(a))
square()
def rect():
        a=int(input("enter length of rectangle"))
        b=int(input("enter breadth of rectangle"))
        l2=lambda a,b:a*b
        print("Area of Rectangle is",l2(a,b))
rect()
def tri():
        a=int(input("enter base of triangle"))
        h=int(input("enter height of triangle"))
        l3=lambda a,h:0.5*a*h
        print("Area of triangle is",l3(a,h))
tri()
        

