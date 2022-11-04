year=2022
year2=int(input("enter future year"))

for i in range(year,year2):
    if (i % 400 == 0) and (i % 100 == 0):
        print(i)
    elif (i % 4 == 0) and (i % 100 != 0):
        print(i)
