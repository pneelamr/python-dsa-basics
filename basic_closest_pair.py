# Closest Pair of Points: Divide-and-conquer algorithm finding the two closest points in O(n log n).
# Split points by x-coordinate median; recursively find closest pair in each half; check the strip of width 2d around the dividing line.
# The strip check is O(n) because each point compares against at most 7 others due to geometric packing arguments.

import math

# Time: O(1) — single arithmetic operation on two coordinate pairs
# Space: O(1) — no extra storage
def euclidean_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def _closest_rec(pts_x, pts_y):
    n = len(pts_x)
    if n <= 3:
        best_d = float('inf')
        best_p1 = pts_x[0]
        best_p2 = pts_x[1] if n > 1 else pts_x[0]
        for i in range(n):
            for j in range(i + 1, n):
                d = euclidean_dist(pts_x[i], pts_x[j])
                if d < best_d:
                    best_d = d
                    best_p1 = pts_x[i]
                    best_p2 = pts_x[j]
        return best_d, best_p1, best_p2

    mid = n // 2
    mid_point = pts_x[mid]
    left_x = pts_x[:mid]
    right_x = pts_x[mid:]
    left_set = set(map(tuple, left_x))
    left_y = [p for p in pts_y if tuple(p) in left_set]
    right_y = [p for p in pts_y if tuple(p) not in left_set]

    d1, p1a, p1b = _closest_rec(left_x, left_y)
    d2, p2a, p2b = _closest_rec(right_x, right_y)

    if d1 < d2:
        d, pa, pb = d1, p1a, p1b
    else:
        d, pa, pb = d2, p2a, p2b

    strip = [p for p in pts_y if abs(p[0] - mid_point[0]) < d]
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < d:
            sd = euclidean_dist(strip[i], strip[j])
            if sd < d:
                d = sd
                pa = strip[i]
                pb = strip[j]
            j += 1

    return d, pa, pb

# Time: O(n log n) — recurrence T(n)=2T(n/2)+O(n); n log n sort dominates setup
# Space: O(n log n) — O(n) per recursion level across O(log n) levels
def closest_pair(points):
    if len(points) < 2:
        return (0.0, points[0], points[0]) if points else (0.0, None, None)
    pts_x = sorted(points, key=lambda p: p[0])
    pts_y = sorted(points, key=lambda p: p[1])
    return _closest_rec(pts_x, pts_y)
