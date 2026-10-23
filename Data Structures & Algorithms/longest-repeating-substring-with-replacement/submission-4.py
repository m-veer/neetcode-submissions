class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        hashmap = {}
        left_pointer = 0
        right_pointer = 0

        while right_pointer < len(s):
            if s[right_pointer] not in hashmap:
                hashmap[s[right_pointer]] = 1
            else:
                hashmap[s[right_pointer]] = hashmap[s[right_pointer]] + 1
            
            window_length = right_pointer - left_pointer + 1
            if window_length - max(hashmap.values()) > k:
                # Invalid window
                hashmap[s[left_pointer]] = hashmap[s[left_pointer]] - 1
                hashmap[s[right_pointer]] = hashmap[s[right_pointer]] - 1
                left_pointer += 1
            else:
                longest = max(longest, window_length)
                right_pointer += 1
        return longest