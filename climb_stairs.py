class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initialize the base cases
        one_step_before = 2
        two_steps_before = 1
        
        # For each step from 3 to n, calculate the number of ways
        for i in range(3, n + 1):
            current = one_step_before + two_steps_before
            # Update the values for the next iteration
            two_steps_before = one_step_before
            one_step_before = current
        
        return one_step_before
