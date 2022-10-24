import time
# algorithm for generating a sequence from triangulating a matrix of dots without overlap of connections

def getSequence(n, x, y):
    #print("following sequence is for " + str(n) + " dots")

    #set values for number of rows and columns
    num_rows = x
    num_cols = y

    #each sequence is a set of subsequences alternating between a straight line sequence and a zigzag sequence
    #to know when the algorithm is done generating the whole sequence set counters for number of times each subsequence is parsed through
    straight_counter = 0
    zigzag_counter = 0

    sequence = []
    #append the starting value of the sequence which will always be 1 (top left corner of the net)
    sequence.append(1)

    #toggle the type of pattern being used to generate a sub-sequence
    #if 0 --> straight pattern
    #if 1 --> zigzag pattern
    toggle_pattern_type = 0
    
    #most recent value added to the sequence will be curr_val
    curr_val = sequence[0]

    #loop this process until the straight pattern sequence has been used num_cols times 
    # and the zigzag pattern sequence has been used num_cols - 1 times
    
    #outline for different sub-sequences is laid out in sub-sequence-outline.jpg file
    while straight_counter < num_cols and zigzag_counter <= num_cols - 1:
        #process for generating a straight pattern sub-sequence
        if toggle_pattern_type == 0:
            i = 0
            #straight pattern is repeated num_rows - 1 times
            while i < num_rows - 1:
                #adding value is num_cols
                curr_val += num_cols
                sequence.append(curr_val)
                i += 1
            straight_counter += 1
            #toggle pattern type, zig-zag pattern always follows straight pattern
            toggle_pattern_type = 1
        #process for generating a zig-zag pattern sub-sequence
            #has two steps: 
            # [1] subtract a value (to get diagonal dot value) [2] add a value (to get neighboring dot value)
        elif toggle_pattern_type == 1:
            #first add one to the last value generated by the straight pattern
            curr_val += 1
            sequence.append(curr_val)
            i = 0
            #zig-zag pattern will repeat num_rows - 1 times
            while i < num_rows - 1:
                # subtract value is previous number in the sequence minus num_cols + 1
                curr_val = curr_val - (num_cols + 1)
                sequence.append(curr_val)
                # add value is previous number in the sequence plus one
                curr_val += 1
                sequence.append(curr_val)
                i += 1
            zigzag_counter += 1
            #toggle to pattern type, straight pattern always follows a zigzag pattern
            toggle_pattern_type = 0
    
    #print(sequence)
    #length = len(sequence)
    #print("Length of sequence:" + str(length))
    #return length
    return sequence

start = time.time()
print(getSequence(12, 4, 3))
end = time.time()

print(end - start)