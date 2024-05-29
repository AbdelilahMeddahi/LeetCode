class Solution:
    def numSteps(self, s: str) -> int:
        # If the binary string represents 1, no steps are needed.
        if s == "1":
            return 0
        count = 0
        # Convert the binary string to an integer
        number = int(s, 2)
        while number != 1:
            if number % 2 == 0:
                # Even number: divide by 2
                number //= 2
            else:
                # Odd number: add 1
                number += 1
            count += 1
        return count
