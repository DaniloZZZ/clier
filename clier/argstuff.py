"""Arguments parsing, validation and conversion"""

import inspect

def convert_annotated_args(func, args):
    anames = inspect.getfullargspec(func).args
    new_args = []
    #TODO: this is not an optimal way. If anames is {} were still running
    for arg, argname in zip(args, anames):
        ann = func.__annotations__.get(argname)
        if ann:
            # Ignore annotations that are not types
            if isinstance(ann, type):
                #TODO: print some good error if annotation isnt callable or type
                arg = ann(arg)
        new_args.append(arg)

    return new_args

def parse_command(comm):
    """
    Parse a string to command name and arguments.

    :param comm: A string consisting 1 or more words separated by spaces and an optional json as the last word 
    :return: 2-tuple: command name, args list
    """
    # Just perform a command without args
    if ' ' not in comm:
        return comm, []
    else:
        words = comm.split(' ')
        words = [w for w in words if w is not '']
        method_name = words.pop(0)
        return method_name, words

