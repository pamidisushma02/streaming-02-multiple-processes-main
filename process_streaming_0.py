"""

Streaming Process - port 9999

First we need a fake stream of data. 

We'll use the temperature data from the batch process.

But we need to reverse the order of the rows 
so we can read oldest data first.

Important! We'll stream forever - or until we 
           read the end of the file. 
           Use use Ctrl-C to stop.
           (Hit Control key and c key at the same time.)

Explore more at 
https://wiki.python.org/moin/UdpCommunication

"""

import csv
import socket
import time

host = "localhost"
port = 9999
address_tuple = (host, port)

# use an enumerated type to set the address family to (IPV4) for internet
socket_family = socket.AF_INET 

# use an enumerated type to set the socket type to UDP (datagram)
socket_type = socket.SOCK_DGRAM 

# use the socket constructor to create a socket object we'll call sock
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# read from a file to get some fake data
input_file = open("batchfile_0_farenheit.csv", "r")

# use the built0in sorted() function to get them in chronological order
reversed = sorted(input_file)

# create a csv reader for our comma delimited data
reader = csv.reader(reversed, delimiter=",")

for row in reader:
    # read a row from the file
    Year, Month, Day, Time, TempF = row

    # use an fstring to create a message from our data
    # notice the f before the opening quote for our string?
    fstring_message = f"[{Year}, {Month}, {Day}, {Time}, {TempF}]"
    
    # prepare a binary (1s and 0s) message to stream
    MESSAGE = fstring_message.encode()

    # use the socket sendto() method to send the message
    sock.sendto(MESSAGE, address_tuple)
    print (f"Sent: {MESSAGE} on port {port}.")

    # sleep for a few seconds
    time.sleep(3)
