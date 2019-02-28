#number of mode returns
def mode(arr):
    count=0
    countmax=0
    mode=0
    for i in arr:
        count=0
        for j in arr:
            if(i==j):
                count+=1

        if(count>countmax):
            countmax>count
            mode=i

    return mode

arr=[1,2,3,4,5,3,2,2,4,5,2]
print(mode(arr))