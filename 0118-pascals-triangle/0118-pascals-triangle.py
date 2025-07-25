class Solution:
    def generateRow(self, row:int) -> List[int]:
        ans = 1
        arr = [1]
        for i in range(1,row):
            ans = (ans*(row-i))//i
            arr.append(ans)
        return arr
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(1,numRows+1):
            result.append(self.generateRow(i))
        return result
            