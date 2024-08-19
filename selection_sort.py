arr = [2,6,4,7,1,9,0]
print(arr)
for i in range(len(arr)-1):
    min = i
    for j in range(i +1, len(arr)):
          if arr[min] > arr[j]:
            min = j
            aux = arr[i]
            arr[i] = arr[min]  
            arr[min]= aux
print(arr)