//Hey, for this problem it's based on the 'Kadane Algorithm'
class Solution {
    public int maxSubArray(int[] nums) {
        int max_so_far = Integer.MIN_VALUE;
        int line_max = 0;
        if (nums.length==1){
            return nums[0];
        } else for (int i =0;i<nums.length;i++){
            line_max += nums[i];
            if(max_so_far < line_max){
                max_so_far = line_max;
            }
            if(line_max < 0){
                line_max = 0;
            }
        }
        return max_so_far;
    }
}
