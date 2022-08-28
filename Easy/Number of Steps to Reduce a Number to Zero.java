class Solution {
    public int numberOfSteps(int num) {
        int number_of_steps=0;
        while (num!=0){
            if(num%2==0){
                num/=2;
            } else num--;
            number_of_steps++;
        }
        return number_of_steps;
    }
}
