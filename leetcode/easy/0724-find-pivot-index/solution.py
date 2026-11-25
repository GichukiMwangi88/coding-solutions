class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum = 0 # initialize the left_sum to 0, starting leftmost index
        right_sum = sum(nums) # store the sum of the list of nums

        # Iterate through the array
        for i in range(len(nums)):
            # Update the right_sum by subtracting the current num
            # at index i
            right_sum -= nums[i]

            # Check if left_sum is equal to right_sum
            if left_sum == right_sum:
                return i # return the location of that index

            # Update the left_sum as you move to the right
            left_sum += nums[i]

        return -1 # if no pivot index is found

       


        