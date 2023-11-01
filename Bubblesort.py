arr=[23,54,63,2,543,7,1]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr)
