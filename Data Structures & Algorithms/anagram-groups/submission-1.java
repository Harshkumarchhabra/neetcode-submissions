class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> Amap = new HashMap<>();
        for(String str: strs){
            char[] chars=str.toCharArray();
            Arrays.sort(chars);
            String sortedStr=new String(chars);
            if(!Amap.containsKey(sortedStr)){
                Amap.put(sortedStr, new ArrayList<>());
            }
            Amap.get(sortedStr).add(str);
        }
        return new ArrayList<>(Amap.values());
    }
}
