class Solution {
    public int numIslands(char[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int count = 0;

        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(grid[i][j] == '1'){
                    count++;
                    Traverse4Dir(grid,rows,cols,i,j);
                }
            }
        }
        return count;
    }
    static void Traverse4Dir(char[][] grid,int rows,int cols,int i,int j){
        if(i<0 || i>=rows || j<0 || j>=cols || grid[i][j] == '0') return;
        grid[i][j] = '0';
        Traverse4Dir(grid,rows,cols,i,j+1);
        Traverse4Dir(grid,rows,cols,i+1,j);
        Traverse4Dir(grid,rows,cols,i,j-1);
        Traverse4Dir(grid,rows,cols,i-1,j);
    }
}