def fibb(n):
     n1,n2=0,1
     count=0
     while count<n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
     return


limit=int(input("enter the limit"))


if limit<0:
    print("negative number")
elif limit==1:
    print(0)
else:
    fibb(limit)
