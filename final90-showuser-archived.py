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
#print(f"Session created: {session}")

datainputjson = ["python3", "./tgcli.py", "-s", session, "device", "list"]
subprocess.call(datainputjson, stdout=subprocess.DEVNULL)
output = subprocess.check_output(datainputjson, encoding='UTF-8')

json_data = json.loads(output)
#json_data = json.loads(output.decode("utf-8"))

# Print the JSON data
#print(json.dumps(json_data, indent=4))

def parse_args():
    """
    Parses command-line arguments using argparse.

    Returns:
        Namespace: An object containing the parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Remove INACTIVE users with 'enable' flag")
    parser.add_argument("--enable", action="store_true", help="Enable a specific feature")
    return parser.parse_args()

args = parse_args()

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
    #createdat = node["createdAt"]
    id = node["id"]
    email = node["user"]["email"]
    state = node["activeState"]
    slogin = node["lastSuccessfulLoginAt"]
    #print(f"ID: {id} {email} {state} {slogin}")

    if state == "ARCHIVED":
      print(f"ID: {id} EMAIL: {email} STATE: {state} DATE: {slogin}")
      #print(id, email ,state, slogin)

      print(f"#############################")

    if state == "ACTIVE":
      print(f"ID: {id} EMAIL: {email} STATE: {state} DATE: {slogin}")
      #print(id, email ,state, slogin)

      print(f"*****************************")


print("DONE")

from datetime import datetime, timedelta, timezone

def get_newest_record_per_email(json_data):
    """
    Finds the newest record for each unique email address in the given JSON data.

    Args:
        json_data: A list of dictionaries, where each dictionary represents a record.

    Returns:
        A list of dictionaries containing the newest record for each email address.
    """

    newest_records = {}
    days_ago = datetime.now(timezone.utc) - timedelta(days=90) 

    for element in json_data:
        for item in element:
            node = item["node"]
            id = node["id"]
            email = node["user"]["email"]
            state = node["activeState"]
            slogin = node["lastSuccessfulLoginAt"]

            if state == "ARCHIVED":
                try:
                    date = datetime.fromisoformat(slogin)
                except ValueError:
                    print(f"Invalid date format for email: {email}")
                    continue

                # Initialize record with default values for new emails
                if email not in newest_records:
                    newest_records[email] = {'ID': id, 'EMAIL': email, 'STATE': state, 'DATE': date}
                elif date > newest_records[email]['DATE']:
                    newest_records[email] = {'ID': id, 'EMAIL': email, 'STATE': state, 'DATE': date}

            if state == "ACTIVE":
                try:
                    date = datetime.fromisoformat(slogin)
                except ValueError:
                    print(f"Invalid date format for email: {email}")
                    continue

                # Initialize record with default values for new emails
                if email not in newest_records:
                    newest_records[email] = {'ID': id, 'EMAIL': email, 'STATE': state, 'DATE': date}
                elif date > newest_records[email]['DATE']:
                    newest_records[email] = {'ID': id, 'EMAIL': email, 'STATE': state, 'DATE': date}


    # Filter out records newer than 90 days
    filtered_records = [record for record in newest_records.values() if record['DATE'] < days_ago] 

    return filtered_records


newest_records = get_newest_record_per_email(json_data)

for record in newest_records:
    print(f"ID: {record['ID']}, EMAIL: {record['EMAIL']}, STATE: {record['STATE']}, DATE: {record['DATE']}")


    print(f"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    if args.enable: 
      print("DELETE Account NOT ACTIVE")
      print(f"ID: {record['ID']}, EMAIL: {record['EMAIL']}, STATE: {record['STATE']}, DATE: {record['DATE']}")
      time.sleep(10)
      removeuser = ["python3", "./tgcli.py", "-s", session, "user", "delete", "-i", {record['ID']}]
      subprocess.call(removeuser)
      print(removeuser)
      print("@@@@@ user removed @@@@@")




print("COMPLETED")

animals = ['BlueFly', 'BlackEel', 'RedBoa', 'BlackBat', 'BlackBoa', 'OrangeFox', 'OrangeApe', 'GreenApe', 'WhiteApe', 'PurpleElk', 'RedCow', 'GreenFox', 'YellowFox', 'PinkBoa', 'YellowElk', 'PinkFox', 'GreenBoa', 'RedBat', 'PurpleApe', 'OrangeBat', 'YellowEel', 'OrangeYak', 'RedDog', 'PinkEel', 'PurpleBat', 'OrangeElk', 'BlueBoa', 'OrangeEel', 'GreenCat', 'WhiteDog', 'OrangeCat', 'BlueCat', 'YellowCat', 'GreenCow', 'BlackYak', 'RedCat', 'WhiteFox']

# Print the list
#for animal in animals:
#   subprocess.call(["python3", "./tgcli.py", "auth", "logout", "-s", animal])

subprocess.call(["python3", "./tgcli.py", "auth", "logout", "-s", session])


