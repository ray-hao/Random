# @param {Integer[][]} intervals
# @return {Boolean}
def can_attend_meetings(intervals)
    intervals = intervals.sort_by {|interval| interval[0]}
    prev_end = -1
    intervals.each do |interval|
        startTime, endTime = interval[0], interval[1]
        if (prev_end > startTime)
            return false 
        end
        prev_end = endTime
    end

    return true
end
