#!/usr/bin/python3

import json
import requests
import sys


def fetch_employee_data(employee_id):
    # (Same as before)
    # ... (code from the previous script)


def write_to_json(employee_id, user_data, todos_data):
    employee_name = user_data["username"]
    file_name = f"{employee_id}.json"

    tasks_data = []
    for task in todos_data:
        task_info = {
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name,
        }
        tasks_data.append(task_info)

    user_tasks_data = {str(employee_id): tasks_data}

    with open(file_name, "w") as file:
        json.dump(user_tasks_data, file)


def display_todo_progress(employee_id):
    # (Same as before)
    # ... (code from the previous script)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_data, todos_data = fetch_employee_data(employee_id)
    display_todo_progress(employee_id)
    write_to_json(employee_id, user_data, todos_data)

