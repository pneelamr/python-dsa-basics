# Job Sequencing: Greedy algorithm scheduling jobs with deadlines to maximize total profit.
# Sort jobs by profit descending; assign each job to the latest available time slot before its deadline.
# If no slot is free before the deadline, the job is skipped — ensuring high-profit jobs get scheduled first.

# Time: O(n^2) — for each of n jobs, scan up to max_deadline slots; O(n log n) sort is dominated
# Space: O(n) — slot array of size max_deadline plus output list
def job_sequencing(jobs):
    sorted_jobs = sorted(jobs, key=lambda j: j[2], reverse=True)
    max_deadline = max(j[1] for j in jobs) if jobs else 0
    slots = [None] * (max_deadline + 1)
    scheduled = []
    total_profit = 0
    for job_id, deadline, profit in sorted_jobs:
        for t in range(min(deadline, max_deadline), 0, -1):
            if slots[t] is None:
                slots[t] = job_id
                scheduled.append(job_id)
                total_profit += profit
                break
    return scheduled, total_profit
