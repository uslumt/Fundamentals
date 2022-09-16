def convert_to_binary(width, height, pixels):

    collected_event = np.full(( max(width) + 1, max(height) + 1 ), 0, dtype=int)
    coordinates = list(zip(width, height))
    rows, cols = zip(*coordinates)
    collected_event[rows, cols] = pixels
    
    return collected_event
