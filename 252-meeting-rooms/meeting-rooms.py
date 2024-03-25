class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # sort the meetings by starting time  
        intervals.sort()
      
        for i in range(len(intervals) - 1):
            # Check that each meeting ends before the next one starts
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True
