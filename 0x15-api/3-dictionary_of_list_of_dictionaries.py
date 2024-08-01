#!/usr/bin/python3
"""
Write a script that returns information about an employee using
this [REST API]('https://jsonplaceholder.typicode.com/')
"""

import json
import requests


def gather_data():
    '''
    Function that returns information about an employee using
    the REST API
    '''

    # Define the endpoint for the API
    endpoint_user = 'users'
    endpoint_todos = 'todos'

    # Define the base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Define the URL for the user endpoint
    url = '{}{}'.format(base_url, endpoint_user)
    # Define the URL for the todos endpoint
    url_todos = '{}{}'.format(base_url, endpoint_todos)

    # Make a GET request to the API
    user_response = requests.get(url)
    todos_response = requests.get(url_todos)

    # Store the response in a variable
    employees = user_response.json()
    todos = todos_response.json()
    allEmployeesTasks = {}

    for employee in employees:
        employeeName = employee.get('username')
        employeeId = employee.get('id')
        employeeTasks = []
        for task in todos:
            task['task'] = task['title']
            task['username'] = employeeName
            filterKeys = ["task", "completed", "username"]
            task = {key: task[key] for key in filterKeys}
            employeeTasks.append(task)
        allEmployeesTasks[employeeName] = employeeTasks

    with open("todo_all_employees.json", 'w') as file:
        jsonObj = json.dumps({str(employeeId): allEmployeesTasks})
        file.write(jsonObj)


if __name__ == "__main__":
    gather_data()
