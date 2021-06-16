#!/usr/bin/python3
"""
export data in csvformat
"""
import requests
import csv
import sys


def save_tasks_to_csv(employeeId):
    """employee tasks save"""
    username = ''
    all_tasks = []
    user = "https://jsonplaceholder.typicode.com/users/"
    todo = "https://jsonplaceholder.typicode.com/users/"
    userRes = requests.get('{}{}'.format(user, employeeId))
    todosRes = requests.get('{}{}/todos'.format(todo, employeeId))

    username = userRes.json().get('username')
    tododsJson = todosRes.json()

    for task in tododsJson:
        taskrow = []
        taskrow.append(employeeId)
        taskrow.append(username)
        taskrow.append(task.get("completed"))
        taskrow.append(task.get("title"))

        all_tasks.append(taskrow)
        all_tasks.sort()

    with open("{}.csv".format(employeeId), 'w') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(all_tasks)

    return 0

if __name__ == "__main__":
    save_tasks_to_csv(sys.argv[1])
