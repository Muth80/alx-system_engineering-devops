#!/usr/bin/python3

import requests
import sys
import json

def export_employee_tasks_to_json(user_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')
    if response.status_code != 200:
        print(f"Failed to fetch data for user with ID: {user_id}")
        return

    tasks = response.json()
    employee_tasks = {user_id: []}

    for task in tasks:
        task_data = {
            "task": task['title'],
            "completed": task['completed'],
            "username": task['userId']
        }
        employee_tasks[user_id].append(task_data)

    with open(f"{user_id}.json", "w") as json_file:
        json.dump(employee_tasks, json_file, indent=2)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Please provide a user ID.")
    else:
        user_id = sys.argv[1]
        export_employee_tasks_to_json(user_id)

