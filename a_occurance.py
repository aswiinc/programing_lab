line_of_text = input("Enter a line of text : ")

name_list = line_of_text.split(" ")


name2 = {'a':0}

for name in name_list :
    name=list(name)
    for letter in name :
        if(letter=='a'):
            name2[letter]+=1

print(name2)
   
