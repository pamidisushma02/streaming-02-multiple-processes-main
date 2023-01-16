"""
This file provides standard information to
help with debugging. 

This file is named:   about.py
This module is named: about

It uses a built-in attribute representing the file name:

    print(get_header(__file__))

To learn more, search:

    builtin attributes python

"""

# imports (all of these are from the standard library)

import datetime
import os
import platform
import sys

# declare program constants
# sometimes, data is kept in a folder named 'data'
# in this repo, data is in the same directory as the source code

data_folder = ""
divider = "=============================================================="

# define helper functions


def get_source_directory_path():
    """Returns the absolute path to this source directory."""
    dir = os.path.dirname(os.path.abspath(__file__))
    return dir


def get_data_directory_path():
    """Returns the absolute path to the data directory."""
    datapath = os.sep.join([os.getcwd(), data_folder])
    return datapath


def get_data_file_path(fn):
    """Return the absolute path to a data file given just the file name (fn)."""
    dir = get_data_directory_path()
    fullPath = os.sep.join([dir, fn])
    return fullPath


def get_header(fn):
    """This function prints helpful information about a file."""
    return f"""

{divider}
{divider}

 Welcome! 

 It's {datetime.date.today()} at {datetime.datetime.now().strftime("%I:%M %p")}

 This file is running on:    {os.name} {platform.system()} {platform.release()}
 
 The Python version is:      {platform.python_version()}
 
 The Python interpreter is at: 
 {sys.executable}

 The active environment should be either conda OR pip (one should be None):

     Active conda env is: {os.environ.get('CONDA_DEFAULT_ENV') }
     Active pip env is:   {os.environ.get('PIP_DEFAULT_ENV')}
 
 The path to the active virtual environment is:

 {sys.prefix}
 
 The Current Working Directory (CWD) where this command was launched is:

 {os.getcwd()}
 
 The absolute path to the data directory is:

 {get_data_directory_path()}
 
 The absolute path to this source directory is:

 {get_source_directory_path()}
 
 The absolute path to this file is:

 {fn}
 
{divider}
{divider}

"""


# -------------------------------------------------------------
# Call some functions and execute code!

# Call our print_header() function on this file to test it
# Python provides a built-in attribute representing the file name
# two underscores on each side of the word 'file'
print(get_header(__file__))

print_to_file = True

if print_to_file:
    # print to a file named about.txt
    fn = "about.txt"
    with open(fn, "w") as f:
        f.write(get_header(__file__))
