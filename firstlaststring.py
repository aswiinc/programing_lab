word=input("enter the string")



first=word[0]
last=word[-1]

word=last+word[1:-1]+first

print("after exchanging charecter",word)
