class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m , n = len(matrix), len(matrix[0])
        i,j = 0,0
        UP,DOWN,RIGHT,LEFT = 0,1,2,3

        direction = RIGHT
        up_wall = 0
        right_wall = n
        down_wall = m
        left_wall = -1

        while(len(res) != m*n):
            if direction == RIGHT:
                while j < right_wall:
                    res.append(matrix[i][j])
                    j += 1
                i,j = i+1,j-1
                right_wall -= 1
                direction = DOWN
            elif direction == DOWN:
                while i < down_wall:
                    res.append(matrix[i][j])
                    i += 1
                i, j = i -1, j-1
                down_wall -= 1
                direction = LEFT
            elif direction == LEFT:
                while j > left_wall:
                    res.append(matrix[i][j])
                    j-= 1
                i, j = i-1, j+1
                left_wall += 1
                direction = UP
            else:
                while i > up_wall:
                    res.append(matrix[i][j])
                    i -= 1
                i, j = i+1, j+1
                up_wall += 1
                direction = RIGHT
        return res