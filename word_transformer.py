word=str(input("enter a word"))
print(word.lower())
print(len(word)//2)
if len(word)>=5:
    print("it is a long word")
else:
    print("it is a short word")