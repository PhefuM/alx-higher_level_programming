#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
<<<<<<< HEAD
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
=======
    num_elements = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            num_elements += 1
        except IndexError:
            break
    print("")
    return num_elements
>>>>>>> 8d33ee3a5980b373df7978a6a6308a82cc1443ea
