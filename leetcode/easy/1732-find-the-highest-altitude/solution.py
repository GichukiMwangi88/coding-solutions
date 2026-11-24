class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        # gain array is net gain of altitude between points
        start_alt = 0 # Starting altitude
        max_alt = 0 # maximum change in altitude

        # Iterate the altitude gain array, adding each gain 
        # to start_alt to get the change in altitude
        # Compare the current change with current altitude,
        # then return the max altitude.
        for change in gain:
            start_alt += change
            max_alt = max(max_alt, start_alt)

        return max_alt

        
            
        