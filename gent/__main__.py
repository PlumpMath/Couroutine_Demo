import sys

from . import slow_chain
from . import fast_chain

def main():
    args = sys.argv
    nargs = len(args)
    help_msg = """Usages:\n
               $ python -m gent slow -- Demonstrate a chain of blocking functions\n
               $ python -m gent fast -- Demonstrate a chain of non-blocking coroutines\n
               """
    if nargs != 2:
        print(help_msg)
        sys.exit(1)
    
    op = args[1]

    if op == 'slow':
        slow_chain.slow_function_chain()
    elif op == 'fast':
        fast_chain.fast_function_chain()
    else:
        print(help_msg)
        sys.exit(1)

if __name__ == '__main__':
    main()
    
