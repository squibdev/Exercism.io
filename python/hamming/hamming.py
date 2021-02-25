def distance(strand_a, strand_b):
    
    difference_count = 0

    if len(strand_a) != len(strand_b):
        raise ValueError("The two strands should be equal length.")

    i = 0
    for ch in strand_a:
        if ch != strand_b[i]:
            difference_count += 1
        i+= 1

    return difference_count