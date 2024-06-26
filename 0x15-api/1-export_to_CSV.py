#!/usr/bin/python3
"""This script exportthe csv format about the task details. 
Using Placeholder Api.
employee_id (int): The ID of the employee."""


import pandas as pd
import requests
import sys


def fetch_employee_data(employee_id):
    """
    Fetches data for a given employee including their user information

    Args:
        employee_id (int): The ID of the employee.

    Returns:
       tuple:
          A tuple containing user data and TODO lis
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()

    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todos_data = todos_response.json()

    return user_data, todos_data


def export_to_CSV(employee_id):
    """
    exports the task information  for a given employe
    Args:
        employee_id (int): The ID of the employee.
    """
    user_data, todos_data = fetch_employee_data(employee_id)
    e_name = user_data.get("username")
    tasks = []
    for task in todos_data:
        single_task = {
                "employee_id": employee_id,
                "e_name": e_name,
                "completed": task.get("completed"),
                "title": task.get("title")
                }
        tasks.append(single_task)
    df = pd.DataFrame(tasks)
    csv_file_path = f'{employee_id}.csv'
    df.to_csv(
            csv_file_path,
            index=False,
            header=False,
            quoting=1,
            escapechar='\\'
            )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
    export_to_CSV(employee_id)
