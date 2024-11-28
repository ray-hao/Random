def rearrange_barcodes(barcodes)
    max_heap = MaxHeap.new()
    barcode_counter = Hash.new { |h, k| h[k] = 0 }    
    barcodes.each do |barcode|
        barcode_counter[barcode] += 1
    end

    barcode_counter.each_key do |barcode_num|
        max_heap.push(barcode_counter[barcode_num], [barcode_counter[barcode_num], barcode_num])
    end

    retval = []

    while retval.length != barcodes.length do

        largest = max_heap.pop
        num, code = largest

        if retval.length == 0 or retval[-1] != code
            retval.push(code)
            if num - 1 > 0
                max_heap.push(num - 1, [num - 1, code])
            end
        else
            second_largest = max_heap.pop
            second_num, second_code = second_largest

            retval.push(second_code)
            if second_num - 1 > 0
                max_heap.push(second_num - 1, [second_num - 1, second_code])
            end
            max_heap.push(num, [num, code])
        end
    end

    return retval
end
