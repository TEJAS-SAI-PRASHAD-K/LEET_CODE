class Solution {
    public int maxProfit(int[] prices) {
        int max_price = 0;
        int x = prices[0];
        for(int i=1;i<prices.length;i++){
            if(prices[i]<x){
                x = prices[i];
            }else if(prices[i] - x > max_price){max_price = prices[i] - x;}
        }
        return max_price;
    }
}