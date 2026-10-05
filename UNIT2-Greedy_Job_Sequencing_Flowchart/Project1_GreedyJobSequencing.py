"""
===========================================================================
  Greedy Job Sequencing with Deadlines and Profits
  -------------------------------------------------
  Course  : Design and Analysis of Algorithms (DAA-538)
  Author  : Student
  Date    : October 2026
===========================================================================

PROBLEM STATEMENT
-----------------
Given a set of jobs where each job has an ID, a deadline, and a profit,
the goal is to schedule jobs on a single machine to maximize total profit.
Each job takes exactly one unit of time, and a job must finish on or
before its deadline.

APPROACH  (Greedy Strategy)
---------------------------
1. Sort all jobs in descending order of profit.
2. Find the maximum deadline among all jobs to determine the number of
   available time slots.
3. Create an array of time slots, initially all empty.
4. For each job (in sorted order), try to place it in the latest
   available slot on or before its deadline.
5. If a slot is found, schedule the job there; otherwise, reject it.

This greedy choice is optimal because prioritizing higher-profit jobs
ensures we never pass up a more profitable job for a less profitable one.
===========================================================================
"""


# ─────────────────────────────────────────────────────────────
# Helper function: input validation
# ─────────────────────────────────────────────────────────────

def validate_jobs(jobs):
    """
    Validate that every job has:
      - A non-empty string ID
      - A positive integer deadline (>= 1)
      - A non-negative numeric profit

    Parameters
    ----------
    jobs : list of tuples  – [(job_id, deadline, profit), ...]

    Returns
    -------
    bool – True if all jobs are valid

    Raises
    ------
    ValueError – with a descriptive message if any job is invalid
    """
    if not jobs:
        raise ValueError("Job list cannot be empty.")

    for idx, job in enumerate(jobs):
        job_id, deadline, profit = job

        # Job ID must be a non-empty string
        if not isinstance(job_id, str) or job_id.strip() == "":
            raise ValueError(
                f"Job at index {idx}: ID must be a non-empty string. "
                f"Got: {job_id!r}"
            )

        # Deadline must be a positive integer
        if not isinstance(deadline, int) or deadline < 1:
            raise ValueError(
                f"Job '{job_id}': Deadline must be a positive integer (>= 1). "
                f"Got: {deadline!r}"
            )

        # Profit must be a non-negative number (int or float)
        if not isinstance(profit, (int, float)) or profit < 0:
            raise ValueError(
                f"Job '{job_id}': Profit must be a non-negative number. "
                f"Got: {profit!r}"
            )

    return True


# ─────────────────────────────────────────────────────────────
# Core algorithm
# ─────────────────────────────────────────────────────────────

def greedy_job_sequencing(jobs):
    """
    Schedule jobs to maximize total profit using the Greedy approach.

    Parameters
    ----------
    jobs : list of tuples
        Each tuple is (job_id: str, deadline: int, profit: number).

    Returns
    -------
    scheduled_jobs : list of tuples – jobs that were scheduled
    rejected_jobs  : list of tuples – jobs that could not be scheduled
    total_profit   : int/float      – sum of profits of scheduled jobs
    slot_assignment : list           – shows which job occupies each slot

    Example
    -------
    >>> jobs = [("J1",2,100), ("J2",1,19), ("J3",2,27), ("J4",1,25), ("J5",3,15)]
    >>> scheduled, rejected, profit, slots = greedy_job_sequencing(jobs)
    >>> profit
    142
    """

    # Step 0: Validate input
    validate_jobs(jobs)

    # Step 1: Sort jobs in DESCENDING order of profit
    #         If two jobs have the same profit, the one listed first stays first.
    sorted_jobs = sorted(jobs, key=lambda j: j[2], reverse=True)

    # Step 2: Find the maximum deadline to know how many time slots we need
    max_deadline = max(job[1] for job in sorted_jobs)

    # Step 3: Initialize time slots
    #         Index 0 is unused; slots 1..max_deadline represent time units.
    #         None means the slot is empty / available.
    slots = [None] * (max_deadline + 1)  # slots[0] is a dummy

    # Lists to track scheduled and rejected jobs
    scheduled_jobs = []
    rejected_jobs = []

    # Step 4: Try to schedule each job (highest profit first)
    for job in sorted_jobs:
        job_id, deadline, profit = job

        # Try to place this job in the latest available slot
        # on or before its deadline.
        placed = False
        for slot in range(min(deadline, max_deadline), 0, -1):
            if slots[slot] is None:          # Slot is free
                slots[slot] = job            # Assign job to this slot
                scheduled_jobs.append(job)
                placed = True
                break                        # Move to the next job

        if not placed:
            # No valid slot was found → reject this job
            rejected_jobs.append(job)

    # Step 5: Calculate total profit of all scheduled jobs
    total_profit = sum(job[2] for job in scheduled_jobs)

    # Build a readable slot-assignment list (slot number → job ID)
    slot_assignment = []
    for i in range(1, max_deadline + 1):
        if slots[i] is not None:
            slot_assignment.append((i, slots[i][0]))
        else:
            slot_assignment.append((i, "Empty"))

    return scheduled_jobs, rejected_jobs, total_profit, slot_assignment


# ─────────────────────────────────────────────────────────────
# Display helper
# ─────────────────────────────────────────────────────────────

def display_results(scheduled, rejected, total_profit, slot_assignment):
    """Pretty-print the scheduling results."""

    print("\n" + "=" * 55)
    print("   GREEDY JOB SEQUENCING – RESULTS")
    print("=" * 55)

    # Slot assignment table
    print("\n  Time-Slot Assignment:")
    print("  " + "-" * 30)
    print(f"  {'Slot':<8} {'Job ID':<10}")
    print("  " + "-" * 30)
    for slot_num, job_id in slot_assignment:
        print(f"  {slot_num:<8} {job_id:<10}")
    print("  " + "-" * 30)

    # Scheduled jobs
    print("\n  Scheduled Jobs:")
    print("  " + "-" * 40)
    print(f"  {'Job':<8} {'Deadline':<10} {'Profit':<10}")
    print("  " + "-" * 40)
    for job_id, deadline, profit in scheduled:
        print(f"  {job_id:<8} {deadline:<10} {profit:<10}")
    print("  " + "-" * 40)

    # Rejected jobs
    if rejected:
        print("\n  Rejected Jobs:")
        print("  " + "-" * 40)
        print(f"  {'Job':<8} {'Deadline':<10} {'Profit':<10}")
        print("  " + "-" * 40)
        for job_id, deadline, profit in rejected:
            print(f"  {job_id:<8} {deadline:<10} {profit:<10}")
        print("  " + "-" * 40)
    else:
        print("\n  No jobs were rejected. All jobs scheduled!")

    # Total profit
    print(f"\n  ★  Maximum Total Profit: {total_profit}")
    print("=" * 55)


# ─────────────────────────────────────────────────────────────
# Custom-input mode
# ─────────────────────────────────────────────────────────────

def get_custom_jobs():
    """
    Interactively collect job data from the user.
    Validates each entry before accepting it.
    """
    jobs = []
    print("\n--- Enter Job Details (type 'done' as Job ID to finish) ---\n")

    while True:
        job_id = input("  Job ID (e.g. J1): ").strip()
        if job_id.lower() == "done":
            if not jobs:
                print("  ⚠  You must enter at least one job.\n")
                continue
            break

        # Read and validate deadline
        try:
            deadline = int(input("  Deadline (positive integer): ").strip())
            if deadline < 1:
                raise ValueError
        except ValueError:
            print("  ✖  Invalid deadline. Must be a positive integer.\n")
            continue

        # Read and validate profit
        try:
            profit = float(input("  Profit  (non-negative number): ").strip())
            if profit < 0:
                raise ValueError
            # Use int if whole number for cleaner display
            if profit == int(profit):
                profit = int(profit)
        except ValueError:
            print("  ✖  Invalid profit. Must be a non-negative number.\n")
            continue

        jobs.append((job_id, deadline, profit))
        print(f"  ✔  Added {job_id}  (Deadline={deadline}, Profit={profit})\n")

    return jobs


# ─────────────────────────────────────────────────────────────
# Main program
# ─────────────────────────────────────────────────────────────

def main():
    """Entry point: choose sample data or custom input."""

    print("\n" + "=" * 55)
    print("   GREEDY JOB SEQUENCING WITH DEADLINES AND PROFITS")
    print("=" * 55)

    # ── Sample dataset (from the assignment) ──
    sample_jobs = [
        ("J1", 2, 100),   # Job J1 – deadline 2, profit 100
        ("J2", 1,  19),   # Job J2 – deadline 1, profit  19
        ("J3", 2,  27),   # Job J3 – deadline 2, profit  27
        ("J4", 1,  25),   # Job J4 – deadline 1, profit  25
        ("J5", 3,  15),   # Job J5 – deadline 3, profit  15
    ]

    print("\nChoose an option:")
    print("  1. Run with sample dataset")
    print("  2. Enter custom jobs")

    choice = input("\nYour choice (1 or 2): ").strip()

    if choice == "2":
        jobs = get_custom_jobs()
    else:
        jobs = sample_jobs
        print("\nUsing sample dataset:")
        print("  Job   Deadline   Profit")
        print("  " + "-" * 30)
        for jid, dl, pr in jobs:
            print(f"  {jid:<6} {dl:<10} {pr}")

    # Run the greedy algorithm
    scheduled, rejected, total_profit, slot_assignment = greedy_job_sequencing(jobs)

    # Display results
    display_results(scheduled, rejected, total_profit, slot_assignment)


# ─────────────────────────────────────────────────────────────
# Run the program when this file is executed directly
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
