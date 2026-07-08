class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_pointer = 0
        right_pointer = 1

        highest_output = 0
    
        while right_pointer < len(prices):
            if prices[left_pointer] < prices[right_pointer]:
                output = prices[right_pointer] - prices[left_pointer]
                highest_output = output if output > highest_output else highest_output
            else:
                left_pointer = right_pointer
            right_pointer += 1
        return highest_output