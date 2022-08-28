//Using the greedy aproach
class Solution {
    public int maxProfit(int[] prices) {
        int max_profit = 0;
        int buy_price=prices[0];
        for (int i=1 ; i < prices.length ;i++){
            if (prices[i]<buy_price){
                buy_price=prices[i];
            }
            if (prices[i]-buy_price>max_profit){
                max_profit=prices[i]-buy_price;
            }
        }
        return max_profit;
    }
}
