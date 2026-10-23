class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Instead of keeping a Counter for every iteration, can I keep on updating a hashmap and when same as s1, return True
        if len(s2) < len(s1):
            return False

        left_pointer = 0
        right_pointer = 0

        s1_hashmap = Counter(s1)
        s2_hashmap = {}

        while right_pointer < len(s2):
            if s2[right_pointer] not in s2_hashmap:
                s2_hashmap[s2[right_pointer]] = 1
            else:
                s2_hashmap[s2[right_pointer]] = s2_hashmap[s2[right_pointer]] + 1

            if s2_hashmap == s1_hashmap:
                return True
            if right_pointer - left_pointer + 1 == len(s1):
                s2_hashmap[s2[left_pointer]] = s2_hashmap[s2[left_pointer]] - 1
                if s2_hashmap[s2[left_pointer]] == 0:
                    del s2_hashmap[s2[left_pointer]]
                left_pointer += 1

            right_pointer += 1
        return False