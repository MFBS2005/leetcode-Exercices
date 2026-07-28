"""
Maximum Unique Subarray (LeetCode 1695)
========================================
Given an array of positive integers, find the contiguous subarray with all unique
elements that has the largest possible sum, and return that sum.

I solved this problem in two steps. First I wrote a straightforward version that
builds each candidate subarray directly. Then I rewrote it as a more efficient
sliding-window solution that runs in linear time.

Author: Mohamed Farouk Ben Salem
"""


# --------------------------------------------------------------------------
# First approach: build each candidate subarray starting from every index.
# For each starting index i, extend as long as the next value hasn't been seen
# yet in the current subarray, keeping the sum. Keep the best sum found.
# --------------------------------------------------------------------------
class SolutionNaive:
    def maximumUniqueSubarray(self, nums):
        x = 0
        lfinal = []
        for i in range(len(nums)):
            l1 = []
            l1.append(nums[i])
            s = nums[i]
            j = i
            while j != len(nums)-1 and nums[j+1] not in l1:
                s += nums[j+1]
                l1.append(nums[j+1])
                j += 1
            else:
                if s > x:
                    x = s
                    lfinal = l1
        return x


# --------------------------------------------------------------------------
# Optimized approach: sliding window in O(n).
# Move a "right" pointer across the array. If the value is already in the
# window, shrink from the left until it's unique again, updating the running
# sum. Track the maximum sum seen.
# --------------------------------------------------------------------------
class Solution:
    def maximumUniqueSubarray(self, nums):
        seen = set()
        left = 0
        max_sum = 0
        curr_sum = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
            seen.add(nums[right])
            curr_sum += nums[right]
            max_sum = max(max_sum, curr_sum)
        return max_sum


if __name__ == "__main__":
    nums = [5, 2, 1, 2, 5, 2, 1, 2, 5]

    print("Naive approach:   ", SolutionNaive().maximumUniqueSubarray(nums))
    print("Sliding window:   ", Solution().maximumUniqueSubarray(nums))
