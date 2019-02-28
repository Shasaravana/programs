#Smallest Number Using Array
def SmallArr(arr):
    x=arr[0]
    for i in arr:
        if(i<x):
            x=i
    return x

arr=[8,9,11    ,5,10,12]
print(SmallArr(arr))



