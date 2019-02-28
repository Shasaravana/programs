#array more than once
def once(arr,x):
    flag=False
    count=0
    for i in arr:
        if i==x:
            count+=1
            if count>1:
                return True

    return flag

arr=[1,2,3,4,5,1]
print(once(arr,2))