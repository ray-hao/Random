# @param {Integer[][]} matrix
# @return {Integer}
def max_matrix_sum(matrix)
    num_negatives = 0
    smallest_abs = 1/0.0
    sum = 0
    matrix.each do |row|
        row.each do |cell|
            if cell < 0
                num_negatives += 1
            end
            smallest_abs = [smallest_abs, cell.abs].min
            sum += cell.abs
        end
    end

    if num_negatives % 2 == 0
        return sum
    else
        return sum - 2 * smallest_abs
    end

end
