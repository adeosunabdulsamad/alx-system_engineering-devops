#!/usr/bin/python3
"""
This script retrieves and displays the TODO list progress for a given employee
using the JSONPlaceholder API.
"""


import requests
import sys


def fetch_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()

    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todos_data = todos_response.json()

    return user_data, todos_data


def display_todo_progress(employee_id):
    user_data, todos_data = fetch_employee_data(employee_id)
    e_name = user_data.get("name")
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed")]
    len_done = len(done_tasks)
    print(f"Employee {e_name} is done with tasks({len_done}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

display_todo_progress(employee_id)
