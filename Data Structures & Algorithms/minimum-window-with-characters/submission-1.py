class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < 2:
            return s == t

        left_pointer = 0
        output = ""
        t_counter = Counter(t)
        s_counter = {}

        if len(s) < 2:
            while s[left_pointer] not in t:
                left_pointer += 1
        right_pointer = left_pointer

        while right_pointer < len(s):
            if s[right_pointer] in t and not s[right_pointer] in s_counter:
                # Add the character to hashmap with count, if character is present in t and not in s counter
                s_counter[s[right_pointer]] = 1
            elif s[right_pointer] in t and s[right_pointer] in s_counter:
                # If character is already present in the hashmap, increase it's count by 1
                s_counter[s[right_pointer]] = s_counter[s[right_pointer]] + 1
            right_pointer += 1

            if s_counter.keys() == t_counter.keys() and min(s_counter.values()) > 0:
                window = s[left_pointer: right_pointer]
                if not output or len(window) < len(output):
                    output = window
                if s[left_pointer] in t:
                    s_counter[s[left_pointer]] = s_counter[s[left_pointer]] - 1
                if s[right_pointer - 1] in t:
                    s_counter[s[right_pointer - 1]] = s_counter[s[right_pointer - 1]] - 1
                left_pointer = left_pointer + 1
                right_pointer -= 1
        return output