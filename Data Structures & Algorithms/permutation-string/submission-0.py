class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        left_pointer = 0
        right_pointer = len(s1) - 1

        s1 = Counter(s1)

        while right_pointer < len(s2):
            window = s2[left_pointer: right_pointer + 1]
            if s1 == Counter(window):
                return True
            left_pointer += 1
            right_pointer += 1

        return False