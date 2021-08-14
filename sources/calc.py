'''
The 'calc' library contains the 'add2' function that takes 2 values and adds
them together. If either value is a string (or both of them are) 'add2' ensures
they are both strings, thereby resulting in a concatenated result.
NOTE: If a value submitted to the 'add2' function is a float, it must be done so
in quotes (i.e. as a string).
'''

# If 'value' is not an integer, convert it to a float and failing that, a string.
def conv(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return str(value)

# The 'add2' function itself
def add2(arg1, arg2, arg3, arg4, arg5):
    # Convert 'arg1' and 'arg2' to their appropriate types
    arg1conv = conv(arg1)
    arg2conv = conv(arg2)
    arg3conv = conv(arg3)
    arg4conv = conv(arg4)
    arg5conv = conv(arg5)
    # If either 'arg1' or 'arg2' is a string, ensure they're both strings.
    if isinstance(arg1conv, str) or isinstance(arg2conv, str) or isinstance(arg3conv, str) or isinstance(arg4conv, str) or isinstance(arg5conv, str):
        arg1conv = str(arg1conv)
        arg2conv = str(arg2conv)
        arg3conv = str(arg3conv)
        arg4conv = str(arg4conv)
        arg5conv = str(arg5conv)
    return arg1conv + arg2conv + arg3conv + arg4conv + arg5conv
