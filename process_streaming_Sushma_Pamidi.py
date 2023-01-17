"""

Streaming Process - port 9999

We'll use the driver response data 


"""

import csv
import socket
import time
import sys
import subprocess

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
input_file = open("driverresponse.csv", "r")

# Declare a variable to hold the output file name
output_file_name = "out9.txt"

output_file = open(output_file_name, "w", newline='')


# use the built0in sorted() function to get them in chronological order
#reversed = sorted(input_file)

# create a csv reader for our comma delimited data
reader = csv.reader(input_file, delimiter=",")


# create a csv writer for our comma delimited data
writer = csv.writer(output_file, delimiter=",")

header = next(reader)
header_list = ["Sno","State","Region","Alcintake","Overspeed"]
writer.writerow(header_list)

for row in reader:
    # read a row from the file
    Sno, State, Region, Alcintake, Overspeed = row

    # use an fstring to create a message from our data
    # notice the f before the opening quote for our string?
    fstring_message = f"[{Sno}, {State}, {Region}, {Alcintake}, {Overspeed}]"
    
    # prepare a binary (1s and 0s) message to stream
    MESSAGE = fstring_message.encode()

    # use the socket sendto() method to send the message
    sock.sendto(MESSAGE, address_tuple)
    
    writer.writerow([Sno, State, Region, Alcintake, Overspeed])

    print (f"Sent: {MESSAGE} on port {port}.")
   
    # sleep for a few seconds
    time.sleep(1)


output_file.close()
input_file.close()