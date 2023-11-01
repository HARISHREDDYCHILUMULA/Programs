arr=[23,54,63,2,543,7,1]
for i in range(1,len(arr)):
    j=i-1
    key=arr[i]
    while j>=0 and key<arr[j]:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
print(arr)
