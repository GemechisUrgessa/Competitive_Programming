class Solution: 
    def select(self, arr, i):
        pass
    
    def selectionSort(self, arr,n):
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if(arr[i]>arr[j]):
                    arr[j],arr[i]=arr[i],arr[j]
        return arr

