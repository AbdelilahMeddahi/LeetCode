class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int plus = 0;
        int minus = 0;
        for (int i = 0; i<operations.length; i++){
            if (operations[i].equals("++X") || operations[i].equals("X++")  ){
                plus++;
            } else if (operations[i].equals("--X") || operations[i].equals("X--")  ){
                minus++;
            };
        }
        return plus-minus;
    }
}
