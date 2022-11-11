wrd1 = input("Enter 1st word : ")
wrd2 = input("Enter 2nd word : ")

new_word = wrd1.replace(wrd1[0],wrd2[0])+" "+wrd2.replace(wrd2[0],wrd1[0])

print("After swapping charecters : ",new_word)
