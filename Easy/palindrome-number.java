class Solution {
    public boolean isPalindrome(int x) {
        int left,reversed=0,temp;    
        temp=x;   
        //reversing the int 
        while(temp>0){    
        left=temp%10;  //getting remainder  
        reversed=(reversed*10)+left;    
        temp=temp/10;    
        }  
        //comparing the reversed int with the original one
        if(x==reversed)    
        return true;    
        else    
        return false;    
    }
}
