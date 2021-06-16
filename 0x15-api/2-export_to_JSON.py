#!/usr/bin/python3
""" """
import json
import requests
import sys


def export_to_JSON(employeeId):
    username = ''
    user_dict = {}
    user = "https://jsonplaceholder.typicode.com/users/"
    todo = "https://jsonplaceholder.typicode.com/users/"
    userRes = requests.get('{}{}'.format(user, employeeId))
    todosRes = requests.get('{}{}/todos'.format(todo, employeeId))

    username = userRes.json().get('username')
    todosJson = todosRes.json()

    user_dict[employeeId] = []

    for task in todosJson:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["username"] = username
        task_dict["completed"] = task.get('completed')

        user_dict[employeeId].append(task_dict)

    with open("{}.json".format(employeeId), 'w') as jsonFile:
        json.dump(user_dict, jsonFile)

    return 0

if __name__ == "__main__":
    export_to_JSON(sys.argv[1])
