#!/usr/bin/python3
""" export data in the JSON format
in a file named :
    USER_ID.json
"""

import json
import requests
import sys

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    emplyee_id = sys.argv[1]

    emplyee_todo = requests.get(f"{url}users/{sys.argv[1]}/todos")
    emplyee_name = requests.get(f"{url}users/{sys.argv[1]}")

    emplyee_todo = emplyee_todo.json()
    emplyee_name = emplyee_name.json()['username']

    total_tasks = []
    updated_user = {}

    for tasks in emplyee_todo:
        total_tasks.append(
               {
                   "task": tasks.get('title'),
                   "completed": tasks.get('completed'),
                   "username": emplyee_name,
                })

    updated_user[emplyee_id] = total_tasks
    json_filename = emplyee_id + ".json"

    with open(json_filename, 'w') as f:
        json.dump(updated_user, f)
