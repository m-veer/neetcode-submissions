class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start_index = 0
        end_index = start_index + 1
        longest = 0
        skip = k

        while end_index < len(s):
            if s[start_index] != s[end_index] and skip != 0:
                skip -= 1
                longest = max(longest, start_index + end_index + 1)
            elif s[start_index] == s[end_index]:
                longest += 1
            end_index += 1
        return longest + 1