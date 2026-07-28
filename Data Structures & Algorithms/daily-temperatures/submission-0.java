class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n=temperatures.length;
        Stack<Integer> stack=new Stack<>();
        int [] result =new int [n];
        for(int i=0;i<n;i++){
            while(!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]){
                int prevday=stack.pop();
                result[prevday]=i-prevday;
            }
            stack.push(i);
        }
        return result;
         
    }
}

        // int n=temperatures.length;
        // int [] result =new int [n];
        // for(int i=0;i<n;i++){
        //     for(int j=i+1;j<n;j++){
        //         if(temperatures[j]>temperatures[i]){
        //             result[i]=j-i;
        //             break;
        //         }
        //     }
        // }
        // return result;
