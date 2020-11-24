#! python3
# mapIt.py - launches a map in the browsser using an adderess from the command line or clipboard

# webbrowser takes a URL and opens it in a new tab
# sys module provides information about constants, functions and methods of the Python interpreter.
# also used for reading the potential command line arguments.
import webbrowser,sys

if len(sys.argv) > 1:
    #get address from command line
    # The sys.argv variable stores a list of the program’s filename and command line arguments.
    # You don’t want the program name in this string, so instead of sys.argv, you should pass sys.argv[1:] to chop off the first element of the array.
    # The final string that this expression evaluates to is stored in the address variable.
    address = ''.join(sys.argv[1:])

# TODO: get address from clipboard

mapit 870 Valencia St, San Francisco, CA 94110