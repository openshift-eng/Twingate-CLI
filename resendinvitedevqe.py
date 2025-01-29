#!/usr/bin/env python3

import csv
import subprocess
import os
import random
import string
import re
import secrets
import json
import argparse
import time
import datetime
from datetime import datetime

#Twingate-CLI

logintenat = os.environ["TG_TENANT"]
loginapi = os.environ["TG_API"]


loginoutput = subprocess.check_output('python3 ./tgcli.py auth login -t ' + logintenat + ' -a ' + loginapi, shell=True)
session = loginoutput.decode("utf-8").split(":")[1].strip()
print(session)

filename = "username.csv"
with open(filename, 'r') as f:
  reader = csv.reader(f)
  for row in reader:
    newUserUsername = row[0]
    newUserEmail = row[1]
    newGroup = row[2]
    newFirst = row[3]
    newLast = row[4]
    print(f"First name:{newFirst}, Last name:{newLast}, Email:{newUserEmail}")
    command = ["python3", "./tgcli.py", "-s", session, "user", "create", "-e", newUserEmail, "-r", "MEMBER", "-s", "true", "-f", newFirst, "-l", newLast]
    subprocess.call(command)

    datainput = ["python3", "./tgcli.py", "-s", session, "group", "list"]

    data = subprocess.check_output(datainput, encoding='UTF-8')


    with open("group.txt", "w") as f:

      # Write the variable to the file
      f.write(str(data))

    # Close the file
    f.close()

    # Load the JSON file.
    with open("group.txt", "r") as f:
      data0 = json.load(f)
    f.close()


    netname = "IBMC-devqe"

    for node in data0[0]:
      if node['node']['name'] == netname:
        # Print the node
        print(node['node']['id'])
        groupnodeid = node['node']['id']



    datainput = ["python3", "./tgcli.py", "-s", session, "user", "list"]

    data = subprocess.check_output(datainput, encoding='UTF-8')


    with open("email.txt", "w") as f:

      # Write the variable to the file
      f.write(str(data))

    # Close the file
    f.close()

    # Load the JSON file.
    with open("email.txt", "r") as f:
      data0 = json.load(f)
    f.close()


    email = newUserEmail.replace(" ", "")
    print(email)
    for node in data0[0]:
      if node['node']['email'] == email:
        # Print the node
        print(node['node']['id'])
        emailnodeid = node['node']['id']


    command2 = ["python3", "./tgcli.py", "-s", session, "group", "addUsers", "-g", groupnodeid, "-u", emailnodeid]
    subprocess.call(command2)



command3 = ["python3", "./tgcli.py", "auth", "logout", "-s", session]
subprocess.call(command3)
os.remove("group.txt")
os.remove("email.txt")



#animals = ['BlueFly', 'BlackEel', 'RedBoa', 'BlackBat', 'BlackBoa', 'OrangeFox', 'OrangeApe', 'GreenApe', 'WhiteApe', 'PurpleElk', 'RedCow', 'GreenFox', 'YellowFox', 'PinkBoa', 'YellowElk', 'PinkFox', 'GreenBoa', 'RedBat', 'PurpleApe', 'OrangeBat', 'YellowEel', 'OrangeYak', 'RedDog', 'PinkEel', 'PurpleBat', 'OrangeElk', 'BlueBoa', 'OrangeEel', 'GreenCat', 'WhiteDog', 'OrangeCat', 'BlueCat', 'YellowCat', 'GreenCow', 'BlackYak', 'RedCat', 'WhiteFox']

# Print the list
#for animal in animals:
#   subprocess.call(["python3", "./tgcli.py", "auth", "logout", "-s", animal])

