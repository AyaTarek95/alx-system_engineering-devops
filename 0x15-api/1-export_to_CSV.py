#!/usr/bin/python3
"""export data in the CSV format
File name: USER_ID.csv
"""

import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emplyee_id = sys.argv[1]

    emplyee_todo = requests.get(f"{url}/users/{sys.argv[1]}/todos")
    emplyee_name = requests.get(f"{url}/users/{sys.argv[1]}")

    emplyee_todo = emplyee_todo.json()
    emplyee_name = emplyee_name.json()['username']

    completed_tasks = 0

    for task in emplyee_todo:
        if task['completed']:
            completed_tasks += 1

    csv_filename = emplyee_id + ".csv"

    with open(csv_filename, 'w', newline='') as file:
        file_writting = csv.writer(file, delimiter=",", quoting=csv.QUOTE_ALL)

        for line in emplyee_todo:
            file_writting.writerow([emplyee_id, emplyee_name,
                                    line.get('completed'), line.get('title')])
