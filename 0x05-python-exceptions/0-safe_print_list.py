def safe_print_list(my_list=[], x=0):
    """Print x elements f a list.

    Args:
        my_list (list): The list to prit elements from.
        x (int): THe number of elements of my_list to print,

    Returns:
           The number of elements printed.
    """
    ret = 0
    for i range(x):
        try:
            print("{}".format(my_list[i], end="")
            ret += 1
        except IndexError:
            break
        print("")
        return (ret)
