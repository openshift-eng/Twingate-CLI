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


#Twingate-CLI

logintenat = os.environ["TG_TENANT"]
loginapi = os.environ["TG_API"]


loginoutput = subprocess.check_output('python3 ./tgcli.py auth login -t ' + logintenat + ' -a ' + loginapi, shell=True)
session = loginoutput.decode("utf-8").split(":")[1].strip()
#print(f"Session created: {session}")

datainputjson = ["python3", "./tgcli.py", "-s", session, "user", "list"]
subprocess.call(datainputjson, stdout=subprocess.DEVNULL)
output = subprocess.check_output(datainputjson, encoding='UTF-8')

json_data = json.loads(output)
#json_data = json.loads(output.decode("utf-8"))

# Print the JSON data
#print(json.dumps(json_data, indent=4))


def check_timestamp(timestamp):
    created_at = datetime.datetime.fromisoformat(timestamp)

    # Convert the timestamp to UTC if it's not already in UTC
    if created_at.tzinfo is None:
        created_at = created_at.replace(tzinfo=datetime.timezone.utc)

    time_diff = datetime.datetime.now(datetime.timezone.utc) - created_at
    seconds_diff = time_diff.total_seconds()

    #return seconds_diff > 24 * 60 * 60
    return seconds_diff > 30 * 24 * 60 * 60

# Loop through each element in the outer list
for element in json_data:
  for item in element: 
    # Access the nested "node" dictionary
    node = item["node"]
    #print(element)
    ## Extract and print the "createdAt" value
    createdat = node["createdAt"]
    id = node["id"]
    email = node["email"]
    state = node["state"]
    #print(f"createdAt: {createdat} {id} {email} {state}")

    #timestamp = datainputjson
    timestamp = createdat 
    #print(f"{timestamp} what time is it")

    if check_timestamp(timestamp):
      # Run your task here
      #print("Timestamp is over 30 days old. Running task...")
      if state == "PENDING":
        print("DELETE Account pending to long")
        print(f"createdAt: {createdat} {id} {email} {state}")
        #time.sleep(10)
        removeuser = ["python3", "./tgcli.py", "-s", session, "user", "delete", "-i", id]
        subprocess.call(removeuser)
        print(removeuser)

    else:
      #print("Timestamp is not over 24 hours old. Skipping task.")
      print("Timestamp is not over 30 days old. Skipping task.")
      print(f"createdAt: {createdat} {email} {state}")


animals = ['BlueFly', 'BlackEel', 'RedBoa', 'BlackBat', 'BlackBoa', 'OrangeFox', 'OrangeApe', 'GreenApe', 'WhiteApe', 'PurpleElk', 'RedCow', 'GreenFox', 'YellowFox', 'PinkBoa', 'YellowElk', 'PinkFox', 'GreenBoa', 'RedBat', 'PurpleApe', 'OrangeBat', 'YellowEel', 'OrangeYak', 'RedDog', 'PinkEel', 'PurpleBat', 'OrangeElk', 'BlueBoa', 'OrangeEel', 'GreenCat', 'WhiteDog', 'OrangeCat', 'BlueCat', 'YellowCat', 'GreenCow', 'BlackYak', 'RedCat', 'WhiteFox']

# Print the list
#for animal in animals:
#   subprocess.call(["python3", "./tgcli.py", "auth", "logout", "-s", animal])

subprocess.call(["python3", "./tgcli.py", "auth", "logout", "-s", session])


