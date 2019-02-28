#Find if A contains X
def findX(arr,x):
    flag=False
    for i in arr:
        if(arr[i]==x):
            flag=True
        return flag
arr=[1,2,3,4,5,6]
print(findX(arr,8))