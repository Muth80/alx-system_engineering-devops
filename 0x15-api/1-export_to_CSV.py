#!/usr/bin/python3

import csv
import requests
import sys


def fetch_employee_data(employee_id):
    # (Same as before)
    # ... (code from the previous script)


def write_to_csv(employee_id, user_data, todos_data):
    employee_name = user_data["username"]
    file_name = f"{employee_id}.csv"

    with open(file_name, mode="w", newline="") as file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for task in todos_data:
            writer.writerow(
                {
                    "USER_ID": employee_id,
                    "USERNAME": employee_name,
                    "TASK_COMPLETED_STATUS": str(task["completed"]),
                    "TASK_TITLE": task["title"],
                }
            )


def display_todo_progress(employee_id):
    # (Same as before)
    # ... (code from the previous script)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_data, todos_data = fetch_employee_data(employee_id)
    display_todo_progress(employee_id)
    write_to_csv(employee_id, user_data, todos_data)

