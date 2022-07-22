


def a_(data):
    print(data)
    for i in range (0,len(data)):
        
        dat = data[i].split()
        print(dat)
        if dat[0] in dct :
            dct[dat[0]].add(dat[1])
        else:
            dct[dat[0]] = {dat[1]}
file = open('demo.txt','r')
data = file.readlines()
dct={}
a_(data)
print(dct)