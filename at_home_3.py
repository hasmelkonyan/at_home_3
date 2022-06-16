def contain(data, val):
    """is the list contains val item?"""
    if val in data:
        return True
    return False


def pop(data, i=None):
    """ this function deletes the item with the specified index և returns the deleted item, and if the index is not
    specified, it deletes the last item
    """
    deleted_item = None
    if i is None:
        data.remove(data[-1])
    else:
        deleted_item = data[i]
        data.remove(data[i])
    return deleted_item


def remove_all(data, value):
    """this function deletes items equal to the specified value
    """
    new_data = []
    for each in range(len(data)):
        if data[each] != value:
            new_data.append(data[each])
    return new_data


def reverse(data):
    """this function returns reversed data list
    """
    return data[::-1]


def min(data):
    """this function returned the smallest item from data list
    """
    min_index = 0
    for each in range(1, len(data)):
        if data[each] < data[min_index]:
            min_index = each
    return data[min_index]


def max(data):
    """this function returned the biggest item from data list
    """
    max_index = 0
    for each in range(1, len(data)):
        if data[each] > data[max_index]:
            max_index = each
    return data[max_index]