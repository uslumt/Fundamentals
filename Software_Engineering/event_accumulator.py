from array import array
import numpy as np
import inspect

def convert_to_binary(width , height, pixel):
        for i in inspect.getfullargspec(convert_to_binary).args: 
            indx = inspect.getfullargspec(convert_to_binary).args.index(i)
            i_ = inspect.getfullargspec(convert_to_binary).args.__getitem__(indx)
            i = eval(i_)
            assert isinstance(i, (list, array, str, np.ndarray)),f"Type of {i_} list or array expected, got: {type(i)}" 

        collected_event = np.full((len((width)),len((height))), 0, dtype=int)
        coordinates = list(zip(width, height))
        rows, cols = zip(*coordinates)
        collected_event[rows, cols] = pixel
        
        return collected_event
