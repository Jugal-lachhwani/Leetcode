class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        index = -1
        for i in range(len(arr)-1,0,-1):
            if arr[i] > arr[i-1]:
                index = i-1
                break
        if index == -1:
            return arr.reverse()
        for i in range(len(arr)-1,index,-1):
            if arr[i] > arr[index]:
                arr[i],arr[index] = arr[index],arr[i]
                break
        arr[index + 1:] = reversed(arr[index + 1:])
        return arr
            