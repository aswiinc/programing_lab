def longest():
    a=[(item) for item in input("Enter elements to list:").split()]
    longestt=len(max(a,key=len))
    print(longestt)

longest()

