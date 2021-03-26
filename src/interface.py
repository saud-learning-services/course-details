
import getpass
from canvasapi import Canvas
from termcolor import cprint
import sys


def print_error(msg):
    """ Prints the error message without shutting down the script
    Args:
        msg (string): Message to print before continuing execution
    """
    cprint(f'\n{msg}\n', 'yellow')

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

def confirm_strict(msg, to_return=None):

    while True:
        confirm = input(f'{msg} [Y/N]: \n')
        confirm_upper = confirm.upper()
        
        if confirm_upper not in ('Y', "N"): 
            print('Invalid entry, please enter Y or N')
            continue
        
        else:
            if confirm_upper == 'Y':
                return(to_return)
            elif confirm_upper == 'N':
                shut_down('Exiting...')
            break

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

    confirm_strict('Would you like to continue using the above information?')
        

def _create_csv(df, output_name):
    print(df.head())
    while True:
        confirmation = input("Your csv will be called: {}\nDo you want to generate this csv from with the data above? (y/n): ".format(output_name))
        
        if confirmation.upper() == "Y":
            df.to_csv(output_name, index=False)
            print("\n{} created.\nBye!".format(output_name))
            break
        elif confirmation.upper() =="N":
            shut_down("\nCsv not created. You can run the script again or exit for no further action.\n")
            break
        else:
            print("Please enter 'Y' to accept or 'N' to exit\n")
            continue