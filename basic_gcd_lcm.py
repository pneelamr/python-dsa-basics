# GCD & LCM: Euclidean algorithm computes the Greatest Common Divisor using repeated modulo division.
# LCM (Least Common Multiple) = a * b // GCD(a, b), avoiding overflow.
# Extended Euclidean algorithm additionally finds integers x, y satisfying ax + by = GCD(a, b).

# Time: O(log min(a, b)) — number of modulo steps is bounded by Fibonacci sequence growth
# Space: O(1) — iterative; only two variables swapped per step
def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a % b
    return a

# Time: O(log min(a, b)) — uses gcd which runs in O(log min(a,b))
# Space: O(1) — single division and multiplication
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a) * abs(b) // gcd(a, b)

# Time: O(log min(a, b)) — same number of steps as the standard Euclidean algorithm
# Space: O(log min(a, b)) — recursion stack depth equals the number of Euclidean steps
def gcd_extended(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = gcd_extended(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

# Time: O(n log M) — n-1 gcd calls where M is the maximum value in nums
# Space: O(1) — iterative reduction over the list
def gcd_multiple(nums):
    if not nums:
        return 0
    result = nums[0]
    for num in nums[1:]:
        result = gcd(result, num)
    return result
