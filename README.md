# LeetCode Solutions

My solutions to LeetCode problems that I worked through on my own to practice
algorithms and problem-solving. Each file contains a working solution with a short
explanation of the approach.

I'm sharing these to show how I think through algorithmic problems — not just
getting a working answer, but also looking for a more efficient one where possible.

## Problems

### Maximum Unique Subarray (LeetCode 1695)
`maximum_unique_subarray.py`

Find the contiguous subarray with all unique elements that has the largest sum.
I included **two approaches**: a first straightforward version that builds each
candidate subarray, and an optimized **sliding-window** version that runs in linear
time O(n). Keeping both shows the step from "a solution that works" to "a solution
that scales."

### Add Two Numbers (LeetCode 2)
`add_two_numbers.py`

Add two numbers represented as linked lists (digits stored in reverse order),
returning the result as a linked list. I solved it by walking through both lists
at once, adding digit by digit and carrying over — the same way you add numbers by
hand. The file includes small helpers to build and print linked lists for testing.

### Three Taps / Buckets Puzzle
`three_taps_puzzle.py`

Not a LeetCode problem, but a puzzle we were given in high school that I enjoyed
solving. Three taps each fill a tank in a given time on their own; the goal is to
find how long it takes when all three run together. I solved it by simulating the
filling in small time steps until the tank is full, then converting the result into
minutes and seconds.

## Technologies

Python 3 (standard library only).
