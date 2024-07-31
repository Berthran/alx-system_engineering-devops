#!/usr/bin/python3
"""
Write a script that returns information about an employee using
this [REST API]('https://jsonplaceholder.typicode.com/')
"""

import requests
import sys


def gather_data():
    '''
    Function that returns information about an employee using
    the REST API
    '''
    # Accept ID parameter from the command line and store it in a variable
    if (len(sys.argv) != 2):
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)
    else:
        employee_id = sys.argv[1]

    # Define the endpoint for the API
    endpoint_user = 'users'
    endpoint_todos = 'todos'

    # Define the base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Define the URL for the user endpoint
    url = '{}{}/{}'.format(base_url, endpoint_user, employee_id)
    # Define the URL for the todos endpoint
    url_todos = '{}{}'.format(base_url, endpoint_todos)

    # Make a GET request to the API
    user_response = requests.get(url)
    todos_response = requests.get(url_todos)

    # Store the response in a variable
    employee = user_response.json()
    name = employee.get('name')
    todos = todos_response.json()
    completedTasks = 0
    totTasks = 0
    tasksCompleted = []

    for task in todos:
        if task.get('userId') == int(employee_id):
            totTasks += 1
            if task.get('completed'):
                completedTasks += 1
                tasksCompleted.append(task.get('title'))

    print(f"Employee {name} is done with tasks({completedTasks}/{totTasks}):")
    print("\n".join("\t {}".format(task) for task in tasksCompleted))


if __name__ == "__main__":
    gather_data()
