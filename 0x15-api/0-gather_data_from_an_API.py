#!/usr/bin/python3

import requests
import sys


def fetch_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = f"{base_url}users/{employee_id}"
    todos_url = f"{base_url}todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    return user_data, todos_data


def display_todo_progress(employee_id):
    user_data, todos_data = fetch_employee_data(employee_id)

    employee_name = user_data["name"]
    total_tasks = len(todos_data)
    done_tasks = sum(task["completed"] for task in todos_data)

    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in todos_data:
        if task["completed"]:
            print("\t", task["title"])


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    display_todo_progress(employee_id)

