class Solution:
    def quicksort(self,arr,low,high):
        if low < high:
            mid = self.partition(arr,low,high)
            self.quicksort(arr, low, mid - 1)
            self.quicksort(arr, mid + 1, high)

    def partition(self,arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1

    def sortColors(self, nums: List[int]) -> None:
        self.quicksort(nums, 0, len(nums)-1)