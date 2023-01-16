"""

In this example, 
three processes are working with the same table 
in a shared database. 
The processes are not synchronized,
so they can interfere with each other.

Run the app several times and notice the 
orders that events occur. 
Is the order predictable?

Modify the code to make each task take longer. 
When the task duration is 3 (seconds),
we'll typically got concurrency errors as mutliple processes
try to access the database at the same time.


"""

# import helfpul libraries first (free code!)

import sqlite3
import time
import multiprocessing
import os
import datetime
import platform
import sys


# define global variables

task_duration = 3 # TODO: increase this to 3 and see what happens

dbname = "shared.db"

# define a multi-line string to communicate with the user
success_message ="""
SUCCESS! All processes are done.
Now - increase the task duration (representing 
      the time the task has the database 
      tied up during an insert statement).
How well do the multiple, concurrent processes share a database 
when each task can take more time? 
How can we let multiple processes share a resource
without interfering with each other?
"""

# define another multi-line f-string to
# display useful information at the start of the program
# f-strings make it easy to insert variables into strings
info_message = f"""

STARTING UP.............................
It's {datetime.date.today()} at {datetime.datetime.now().strftime("%I:%M %p")}

This file is running on:    {os.name} {platform.system()} {platform.release()}
The Python version is:      {platform.python_version()}
 
The Python interpreter is at: 
 {sys.executable}

"""


# define helpful functions (bits of reusable code)

def create_table():
    # create a database connection
    conn = sqlite3.connect(dbname)
    # create a cursor to execute statements
    cur = conn.cursor()
    # create valid SQL statement
    sql = "CREATE TABLE pets (id INTEGER PRIMARY KEY, name TEXT, breed TEXT)"
    # call cursor.execute() to create a table
    cur.execute(sql)
    # commit the transaction
    conn.commit()
    # close the connection
    conn.close()

def drop_table():
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS pets")
    conn.commit()
    conn.close()

def insert_pet(process, name, breed):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    sql = f"INSERT INTO pets (name, breed) VALUES ('{name}', '{breed}');"
    print(f"{process} getting ready to insert {name} the {breed}.")
    cur.execute(sql)
    print(f"{process} ADDED {name} the {breed}.")
    time.sleep(task_duration)
    conn.commit()
    conn.close()

def process_one():
    insert_pet("P1","Ace", "Dog")
    insert_pet("P1", "Buddy", "Dog")

def process_two():
    insert_pet("P2", "Cooper", "Rabbit")
    insert_pet("P2","Dufus", "Dog")

def process_three():
    insert_pet("P3","Emma", "Rabbit")
    insert_pet("P3","Felix", "Cat")

def recreate_database():
    drop_table()
    print("DELETED tabble pets.")
    create_table()
    print("CREATED table pets.")
    print()


# The earlier parts of the code were used to 
# import content and define some variables and functions. 

# In Python programs, you'll typically find the main flow of execution
# at the bottom of the file.

# The line below says "if this file is the file being executed"
# That is, if it's not been imported, then run the code below.

# This is a common pattern in Python programs.

if __name__ == "__main__":

    # print some helepful information
    print(info_message)

    # start over with a clean database
    recreate_database()

    # define several processes
    # to represent several users
    # accessing the same resource
    p1 = multiprocessing.Process(target=process_one)
    p2 = multiprocessing.Process(target=process_two)
    p3 = multiprocessing.Process(target=process_three)
    
    # start each process
    p1.start()
    p2.start()
    p3.start()
       
    # wait for a processes to finish and rejoin the flow of execution
    p1.join()
    p2.join()
    p3.join()
    
    # if the task duration is 0, then show the success message
    if task_duration == 0:
        print(success_message)
   
