class Solution:
    def generateRow(self, row:int) -> List[int]:
        ans = 1
        arr = [1]
        for i in range(1,row):
            ans = (ans*(row-i))//i
            arr.append(ans)
        return arr
    def getRow(self, rowIndex: int) -> List[int]:
        result = self.generateRow(rowIndex+1)
        return result