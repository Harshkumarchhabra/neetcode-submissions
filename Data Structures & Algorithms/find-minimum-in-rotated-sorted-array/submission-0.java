class Solution {
    public int findMin(int[] nums) {
        int left=0;
        int right=nums.length-1;
        while(left<right){
          int mid=left+(right-left)/2;
          if(nums[mid]>nums[right]){
            left=mid+1;
          }else{
            right=mid;
          }
        }
        return nums[left];
    }
}
//brute force approach:
// int minm=0;
// for(int i=1;i<nums.length;i++){
//   if(nums[minm]>nums[i]){
//     minm=i;
//   }
// }
// return nums[minm];
