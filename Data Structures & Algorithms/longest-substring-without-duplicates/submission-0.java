class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> map=new HashMap<>();
        int start=0;
        int max=0;
        for(int end=0;end<s.length();end++){
          char curr=s.charAt(end);
          if(map.containsKey(curr)){
            start=Math.max(start,map.get(curr)+1);
          }
          map.put(curr,end);
          max=Math.max(max,end-start+1);
        }
        return max;
    }
}
