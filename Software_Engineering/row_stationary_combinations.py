import numpy as np

def rs_map (k, n, m):
    output_row_index = np.array(list(i for i in range(1, k+1)))
    kernel_row_index = np.array(list(i for i in range(1, n+1)))
    input_row_index = np.array([np.arange(1, m+1)[i:i+n] for i in range(m - n + 1)])
    
    pe_map = []
    for i in range (0, len(output_row_index)) :
        pe_map.append(np.array([output_row_index[i], kernel_row_index, input_row_index[i]], dtype=object))
    return(pe_map)
  
print(rs_map(3, 3, 5))
