class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int maxpile=0;
        for(int pile: piles){
            maxpile=Math.max(maxpile,pile);// ceil returns the smallest integer value greater than or equal to the argument
        }// used double so fractional part can be rounded up correctly
        int l=0;
        int r=maxpile;
        int res=r;
        while(l<=r){
            int k=l+(r-l)/2;
            int totaltime=0;
            for(int t:piles){
                totaltime+=Math.ceil((double)t/k);
            }
            if(totaltime<=h){
                res=k;//updating the result(res)
                r=k-1;
            }else{
                l=k+1;
            }
        }
        return res;
    }
}
