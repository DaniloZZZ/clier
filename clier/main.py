import time
from clier.argstuff import parse_command, convert_annotated_args

COMMANDS = { }

def _help():
    """Print help info about commands"""
    for fname, f in COMMANDS.items():
        docstr = f.__doc__
        info = fname
        if docstr:
            info += ':\t' + docstr
        print(info)

COMMANDS['help'] = _help

def command(func):
    """Just a decorator for `add_func()`"""
    add_command(func)
    return func

def add_command(func):
    """
    Add a command to the cli.

    Use help to list all commands
    """
    global COMMANDS
    COMMANDS[func.__name__] = func

def start():
    """
    Starts the interactive cli
    """
    try:
        input_loop()
    except KeyboardInterrupt:
        print("Bye")
        return
    except EOFError:
        print("Done")
        return

# Input-related methods
# --------

def input_loop():
    """
    This runs in a thread and polls input, then parses
    arguments and executes method.
    Prints to stderr if there was an error
    """
    while True:
        command = input()
        method_name, args = parse_command(command)
        method = COMMANDS.get(method_name)
        args = convert_annotated_args(method, args)
        if method is None:
            print(f"Command `{method_name}` not found. Type help to display available commands.")
            continue
        try:
            method( *args )
        except Exception as e:
            # TODO: construct a special exception to catch in main loop
            raise Exception("Error executing:", str(e))
        time.sleep(0)
