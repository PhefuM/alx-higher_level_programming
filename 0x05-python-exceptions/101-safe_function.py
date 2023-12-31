#!/usr/bin/python3

def safe_function(fct, *args):
    import sys
    try:
        res = fct(*args)
    except Exception as ax:
        sys.stderr.write("Exception: {}\n".foramt(ax))
        res = None
    return (res)
