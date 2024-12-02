# @param {String} sentence
# @param {String} search_word
# @return {Integer}
def is_prefix_of_word(sentence, search_word)
    words = []
    words = sentence.split(" ")
    words.each_with_index do |word, index|
        if word.index(search_word) == 0
            return index + 1
        end
    end

    return -1

end
