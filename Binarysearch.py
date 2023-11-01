def bin(arr,low,high,key):
    if low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return True
        elif arr[mid]>key:
            return bin(arr,low,mid-1,key)
        else:
            return bin(arr,mid+1,high,key)
    return -1
arr=[1,2,4,6,8,100,120,200,300]
h=bin(arr,0,len(arr)-1,6)
print(h)
