word=input("enter the word")
word=list(word)

for i in range(1,len(word)):
    if(word[0]==word[i]):
        word[i]="$"

word = ''.join(word)

print(word)
