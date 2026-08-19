class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        hashset = set(nums)
        max_sequence = 0

        for n in hashset:

            # Only start from the end of a sequence
            if n + 1 not in hashset:
                current_sequence = 0
                value = n

                # Walk backwards through the sequence
                while value in hashset:
                    current_sequence += 1
                    value -= 1

                max_sequence = max(max_sequence, current_sequence)

        return max_sequence