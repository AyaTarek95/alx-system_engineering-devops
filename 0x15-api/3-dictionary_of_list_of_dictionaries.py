#!/usr/bin/python3
""" export data in the JSON format
File name must be: todo_all_employees.json
"""

import json
import requests

if __name__ == "__main__":

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todos_list = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos_list = todos_list.json()
    all_todos = {}

    for user in users:
        tasks = []
        for task in todos_list:
            if task.get('userId') == user.get('id'):
                tasks_dict = {"username": user.get('username'),
                              "task": task.get('title'),
                              "completed": task.get('completed')}
                tasks.append(tasks_dict)
        all_todos[user.get('id')] = tasks

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(all_todos, f)
