# The knows API is already defined for you.
# @param {Integer} person a
# @param {Integer} person b
# @return {Boolean} whether a knows b
# def knows(a, b)

# @param {Integer} n
# @return {Integer}
def find_celebrity(n)
    
    # start arbitrarily at person 0, check if they know each other person.
    # if they don't know the person, move onto the next, cuz the one they
    # don't know is definitely not the celebrity
    # if they know the person, move the ptr to the person, since they
    # are in contention to be the celebrity. 

    candidate = 0
    current = 1
    possibilities = []

    while current < n
        if knows(candidate, current)
            possibilities.push(current)
        end
        current += 1
    end

    if possibilities.length == 0
        (1...n).each do |other|
            if not knows(other, 0)
                return -1
            end
        end

        return 0
    else
        current = possibilities[0]

        (1..n - 1).each do |other|
            if knows(current, other)
                current = other
            end
        end

        (0..n - 1).each do |person|
            if person == current
                next
            else
                if not knows(person, current) or knows(current, person)
                    return -1
                end
            end
        end

        return current

    end

end
