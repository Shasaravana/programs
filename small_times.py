#count the smallest number
def small(a):
    small=a[0]
    for i in a:
        if(i<small):
            small=i

    return small

def times(x):
    count=0
    

a=[2,6,8,1]
print(small(a))
def lenofarr(arr):
    count=0
    for _ in arr:
        count+=1
    return count