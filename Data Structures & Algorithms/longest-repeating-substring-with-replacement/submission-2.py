class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start_index = 0
        end_index = start_index + 1
        longest = 0
        skip = k
        next_start = None

        while end_index < len(s):
            if s[start_index] != s[end_index] and skip != 0:
                if next_start is None:
                    next_start = end_index
                skip -= 1
                # longest += 1
                # longest = max(longest, start_index + end_index + 1)
                longest = max(longest, end_index - start_index + 1)
                end_index += 1
            elif s[start_index] == s[end_index]:
                # longest += 1
                # longest = max(longest, start_index + end_index + 1)
                longest = max(longest, end_index - start_index + 1)
                end_index += 1
            else:
                start_index = next_start
                end_index = start_index + 1
                next_start = None
                skip = k
                # longest = 0
        return longest