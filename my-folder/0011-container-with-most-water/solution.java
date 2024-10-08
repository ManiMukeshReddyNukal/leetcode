import static java.lang.Math.max;

class Solution {
    public int maxArea(int[] height) {
        int maxarea=0;
        int l = 0;
        int r = height.length-1;
        while (l<r){
            maxarea=Math.max(Math.min(height[l],height[r])*(r-l),maxarea);
            if (height[l]<height[r]){
                l++;
            }
            else{
                r--;
            }
        }
        return maxarea;
    }
}
