class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # To keep a track of the key and indexes
        mappings = {}

        # The start of the sliding window
        left_pointer = 0

        # The longest length
        length = 0

        # Iterate over the input string and use the interating index as the right_pointer
        for right_pointer in range(len(s)):
            # If the character is already present in the mappings then update the left pointer
            if s[right_pointer] in mappings:
                left_pointer = max(mappings[s[right_pointer]] + 1, left_pointer)

            # Update the dictionary with the updated index
            mappings[s[right_pointer]] = right_pointer

            # Update the length with the maximum length
            length = max(right_pointer - left_pointer + 1, length)
        return length