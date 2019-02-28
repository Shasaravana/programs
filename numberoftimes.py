#Number of Times
def notimes(arr,x):
    count=0
    for i in arr:
        if i==x:
            count+=1
    return count

arr=[1,2,3,4,5,2]

print(notimes(arr,2))