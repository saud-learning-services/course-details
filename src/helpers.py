
## Functions I seem to use over and over

from canvasapi import Canvas
import getpass
import sys
import pandas as pd
import re
import ast
from interface import shut_down


def _create_csv(df, output_name):
    print(df.head())
    while True:
        confirmation = input("Your csv will be called: {}\nDo you want to generate this csv from with the data above? (y/n): ".format(output_name))
        
        if confirmation == "y":
            df.to_csv(output_name, index=False)
            print("\n{} created.\nBye!".format(output_name))
            break
        elif confirmation =="n":
            shut_down("\nCsv not created. You can run the script again or exit for no further action.\n")
            break
        else:
            print("Please enter 'y' to accept or 'n' to exit\n")
            continue


def _confirm_strict(msg, to_return=None):
    confirm = input(
        f'{msg} [y/n]: \n')

    if confirm == 'y' or confirm == 'Y':
        return(to_return)
    elif confirm == 'n' or confirm == 'N':
        shut_down('Exiting...')
    else:
        shut_down('ERROR: Only accepted values are y and n')   


