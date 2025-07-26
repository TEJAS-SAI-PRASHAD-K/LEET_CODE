class Solution:
    def left(self,nums: List[int], target: int):
        left = 0
        right = len(nums)-1
        temp = -1
        while(left <= right):
            mid = (left + right)//2
            if(nums[mid] == target):
                temp = mid
                right = mid-1
            elif(nums[mid] < target):
                left = mid + 1
            else:
                right = mid - 1
        return temp
    def right(self,nums: List[int], target: int):
        left = 0
        right = len(nums)-1
        temp = -1
        while(left <= right):
            mid = (left + right)//2
            if(nums[mid] == target):
                temp = mid
                left = mid + 1
            elif(nums[mid] < target):
                left = mid + 1
            else:
                right = mid - 1
        return temp
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [self.left(nums,target),self.right(nums,target)]
        return result
