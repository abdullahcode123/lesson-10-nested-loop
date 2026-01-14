str=input("Enter your word: ")
char=input("Enter your character: ")
i=0
coun=0
while (i<len(str)):
    if(str[i]==char):
        coun=coun+1
    i=i+1
print("the total num of time ",char,"has occured= ",coun)