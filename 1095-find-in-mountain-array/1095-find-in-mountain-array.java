/**
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index) {}
 *     public int length() {}
 * }
 */
 
class Solution {
    public int findInMountainArray(int target, MountainArray mountainArr) {
        int n = mountainArr.length();
        int left = 0;
        int right = n-1;

        while(left<right){
            int mid = left + (right-left)/2;
            if(mountainArr.get(mid) < mountainArr.get(mid+1))
                left = mid+1;
            else
                right = mid;
        }
        int peak = left;
        int res = bs(mountainArr,target,0,peak,true);
        if(res != -1){
            return res;
        }
        return bs(mountainArr,target,peak+1,n-1,false);
    }

    static int bs(MountainArray mountainArr,int target,int l,int r,boolean a){
        while(l<=r){
            int mid = l+(r-l)/2;
            int val = mountainArr.get(mid);

            if(val == target)
                return mid;
            if(a){
                if(val<target)
                    l = mid+1;
                else
                    r = mid - 1;
            }else{
                if(val > target){
                    l = mid + 1;
                }else{
                    r = mid - 1;
                }
            }
        }
        return -1;
    }
}