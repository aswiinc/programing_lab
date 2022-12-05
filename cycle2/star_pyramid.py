def pyramid():
    

    row=int(input("enter no: of rows"))

    for i in range(row):
        for j in range(i+1):
            print("*" ,end=" ")
        print("\n")

    for k in range(row,1,-1):
        for e in range(k-1):
            print("*" ,end=" ")
        print("\n")

pyramid()
