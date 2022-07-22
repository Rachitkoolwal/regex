list = input("enter a number") 
list = list.split()
if list[0] == 'add':
    add_=0
    for i in range(1 , len(list)):
      
       add_+= int(list[i])
    print(add_)
elif list[0] == 'multi':
    for i in range(1,len(list)):
        multi_=1
        mutli_*= int(list[1])
        print(multi_)
