
dict={}
val = str.lower(input("enter a string"))
for i in val:
    if(dict.get(i)):
          dict[i]+=1
    else:
        dict[i]=1
print(dict)      
