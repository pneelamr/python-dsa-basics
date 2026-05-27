# Minimum Platforms: Find the minimum number of railway platforms needed given train arrival and departure times.
# Sort arrivals and departures separately; use two pointers to count how many trains overlap at any moment.
# The answer is the maximum number of trains present simultaneously at the station.

# Time: O(n log n) — dominated by sorting the two arrays
# Space: O(n) — sorted copies of arrivals and departures
def minimum_platforms(arrivals, departures):
    arr = sorted(arrivals)
    dep = sorted(departures)
    n = len(arr)
    platforms = 0
    max_platforms = 0
    i = 0
    j = 0
    while i < n and j < n:
        if arr[i] <= dep[j]:
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1
    return max_platforms

# Time: O(n log n) — sorting 2n events; scan is O(n)
# Space: O(n) — events list of size 2n
def max_overlapping_intervals(intervals):
    events = []
    for start, end in intervals:
        events.append((start, 1))
        events.append((end, -1))
    events.sort(key=lambda e: (e[0], e[1]))
    current = 0
    max_overlap = 0
    for _, delta in events:
        current += delta
        max_overlap = max(max_overlap, current)
    return max_overlap
