class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Edge cases
        if x == 0: return 0
        if n == 0: return 1
        
        # Helper function to perform the quick exponentiation that reduces the number of multiplications
        def alt_power(base: float, exponent: int) -> float:
            result = 1.0
            # Continue multiplying the base until the exponent is zero
            while exponent:
                # If exponent is odd, multiply the result by the base
                if exponent % 2 != 0:
                    result *= base
                # Square the base (equivalent to base = pow(base, 2))
                base *= base
                # Dividing by 2
                exponent = exponent//2
            return result 

        # If n is non-negative, call helper function with x and n directly.
        # Otherwise, calculate the reciprocal of the positive power.
        return alt_power(x, n) if n >= 0 else 1 / alt_power(x, -n)
