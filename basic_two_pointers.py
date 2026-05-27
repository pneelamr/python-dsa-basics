# Two Pointers: Technique using two index pointers to solve array/string problems in O(n) instead of O(n²).
# Pointers either converge from both ends (sorted sum problems) or move in the same direction (partitioning).
# Common uses: two-sum on sorted arrays, three-sum, container with most water, trapping rain water.

# Time: O(n) — single left-right pass over sorted array
# Space: O(1) — no extra storage beyond two index variables
def two_sum_sorted(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return (left, right)
        elif s < target:
            left += 1
        else:
            right -= 1
    return None

# Time: O(n^2) — outer loop O(n) with inner two-pointer scan O(n); sorting is O(n log n)
# Space: O(n) — sorted copy and output list
def three_sum(arr):
    arr = sorted(arr)
    n = len(arr)
    result = []
    for i in range(n - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        left = i + 1
        right = n - 1
        while left < right:
            s = arr[i] + arr[left] + arr[right]
            if s == 0:
                result.append([arr[i], arr[left], arr[right]])
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    return result

# Time: O(n) — single left-right converging pass
# Space: O(1) — only two pointer variables
def container_with_most_water(heights):
    left = 0
    right = len(heights) - 1
    max_water = 0
    while left < right:
        water = min(heights[left], heights[right]) * (right - left)
        max_water = max(max_water, water)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_water

# Time: O(n) — single left-right pass; each element visited once
# Space: O(1) — only pointer and running-sum variables
def trap_rain_water(heights):
    if not heights:
        return 0
    left = 0
    right = len(heights) - 1
    left_max = 0
    right_max = 0
    water = 0
    while left < right:
        if heights[left] < heights[right]:
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                water += left_max - heights[left]
            left += 1
        else:
            if heights[right] >= right_max:
                right_max = heights[right]
            else:
                water += right_max - heights[right]
            right -= 1
    return water
