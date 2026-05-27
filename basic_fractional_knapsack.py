# Fractional Knapsack: Greedy knapsack where items can be split to fill remaining capacity.
# Sort items by value-to-weight ratio (value/weight) in descending order; take as much of the highest-ratio item as capacity allows.
# Unlike 0/1 knapsack, the greedy approach is optimal here because fractional items are allowed.

# Time: O(n log n) — dominated by sorting; the greedy fill loop is O(n)
# Space: O(n) — sorted copy of items list
def fractional_knapsack(items, capacity):
    sorted_items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0.0
    remaining = capacity
    for weight, value in sorted_items:
        if remaining <= 0:
            break
        take = min(weight, remaining)
        total_value += take * (value / weight)
        remaining -= take
    return total_value
