#If 2array are same return True
def arrsame(a,b):
    if len(a)==len(b):
        for i in range(0,len(0)):
            if not(a[i]==b[i]):
                return False

            else:     
                return False
    return True 

a=[1,2,3,5]
b=[1,2,3,4,5]   
print(arrsame(a,b))