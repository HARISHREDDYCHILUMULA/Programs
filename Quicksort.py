def quick(arr,left,right):
    if left<right:
        partition_pos=partition(arr,left,right)
        quick(arr,left,partition_pos-1)
        quick(arr,partition_pos+1,right)
def partition(arr,left,right):
    i=left
    j=right-1
    pivot=arr[right]
    while i<j:
        while arr[i]<pivot and i<right:
            i+=1
        while arr[j]>=pivot and j>left:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[i],arr[right]=arr[right],arr[i]
    return i
arr=[234,54,2,23,5432,41,34,53,654,7]
quick(arr,0,len(arr)-1)
print(arr)
