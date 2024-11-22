class KthLargest

    def binary_insert(num)
        left = 0
        right = @top_scores.length - 1
        while left <= right
            middle = (left + right) / 2
            val = @top_scores[middle]
            if num == val
                @top_scores.insert(middle, num)
                while @top_scores.length > @k
                    @top_scores.shift
                end
                return
            elsif num < val
                right = middle - 1
            else
                left = middle + 1
            end
        end

        @top_scores.insert(left, num)
        while @top_scores.length > @k
            @top_scores.shift
        end
    end

=begin
    :type k: Integer
    :type nums: Integer[]
=end
    def initialize(k, nums)
        @k = k
        @top_scores = nums.sort.pop(k)
    end


=begin
    :type val: Integer
    :rtype: Integer
=end
    def add(val)
        binary_insert(val)
        return @top_scores[0]
    end


end

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest.new(k, nums)
# param_1 = obj.add(val)
