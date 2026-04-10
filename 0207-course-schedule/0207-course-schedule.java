class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {

        int[] indegree = new int[numCourses];
        List<List<Integer>> adj = new LinkedList<>();

        for(int i=0;i<numCourses;i++){
            adj.add(new LinkedList<>());
        }

        for(int[] cur_arr:prerequisites){
            adj.get(cur_arr[1]).add(cur_arr[0]);
            indegree[cur_arr[0]]++;
        }

        Queue<Integer> q = new LinkedList<>();
        int numCourses_completed = 0;
        for(int i=0;i<numCourses;i++){
            if(indegree[i] == 0) q.offer(i);
        }

        while(!q.isEmpty()){
            int cur_q = q.poll();
            numCourses_completed++;
            for(int n:adj.get(cur_q)){
                indegree[n]--;
                if(indegree[n] == 0){
                    q.offer(n);
                }
            }
        }

        return numCourses==numCourses_completed;
    }
}