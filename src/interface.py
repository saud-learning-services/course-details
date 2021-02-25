"""
GROUP CSV: interface & utl
authors:
@markoprodanovic
last edit:
September 24, 2020
"""

import getpass
from canvasapi import Canvas
from termcolor import cprint
import sys


def print_error(msg):
    """ Prints the error message without shutting down the script
    Args:
        msg (string): Message to print before continuing execution
    """
    cprint(f'\n{msg}\n', 'red')

def print_success(msg):
    """ Prints the success message without shutting down the script
    Args:
        msg (string): Message to print before continuing execution
    """
    cprint(f'\n{msg}\n', 'green')

def shut_down(msg):
    """ Shuts down the script.
    Args:
        msg (string): Message to print before printing 'Shutting down...' 
                      and exiting the script.
    """
    cprint(f'\n{msg}\n', 'red')
    print('Shutting down...')
    sys.exit()


def _prompt_for_confirmation(user_name, course_name):
    """Prints user inputs to screen and asks user to confirm. Shuts down if user inputs
    anything other than 'Y' or 'y'. Returns otherwise.
    Args:
        user_name (string): name of user (aka. holder of token)
        course_name (string): name of course returned from Canvas
    Returns:
        None -- returns only if user confirms
    """
    cprint('\nConfirmation:', 'blue')
    print(f'USER:  {user_name}')
    print(f'COURSE:  {course_name}')
    print('\n')

    confirm = input(
    'Would you like to continue using the above information? [y/n]: \n')

    if confirm == 'y' or confirm == 'Y':
        return
    elif confirm == 'n' or confirm == 'N':
        shut_down('Exiting...')
    else:
        shut_down('ERROR: Only accepted values are y and n')            