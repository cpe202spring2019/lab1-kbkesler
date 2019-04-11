
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    max_num = 0
    if (int_list == None):
	    raise ValueError
    if (int_list == []):
	    return None
    max_num = int_list[0]
    for i in int_list:
        if i > max_num:
            max_num = i
    return max_num

def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if (int_list == None):
        raise ValueError
    if (int_list == []):
        return int_list
    return [int_list[-1]] + reverse_rec(int_list[:-1])

def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    mid = (high - low)//2
    if (int_list == None):
        raise ValueError
    if (int_list == []):
        return None
        quit()
    if (target == int_list[mid]):
        return mid
    if (target > int_list[mid]): 
	    return mid + 1 + bin_search(target, low, len(int_list)//2, int_list[mid+1:]) 
    if (target < int_list[mid]):
        return bin_search(target, low, len(int_list)//2, int_list[:mid])
