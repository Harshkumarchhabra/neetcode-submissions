class Solution {
    public int maxProfit(int[] prices) {
        int minPrice=prices[0];
        int maxProfit=0;
        for(int i=1;i<prices.length;i++){
          minPrice=Math.min(minPrice,prices[i]);
          int potentialProfit=prices[i]-minPrice;
          maxProfit=Math.max(maxProfit,potentialProfit);
        }
        return maxProfit;
    }
}
