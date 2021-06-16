#!/usr/bin/python3

import requests
import csv
import sys

def save_tasks_to_csv(employeeId):
    username = ''
    all_tasks = []

    userRes = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employeeId))
    todosRes = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(employeeId))

    username =  userRes.json().get('username')
    tododsJson = todosRes.json()

    for task in tododsJson:
        taskrow = []
        taskrow.append(employeeId)
        taskrow.append(username)
        taskrow.append(task.get("completed"))
        taskrow.append(task.get("title"))

        all_tasks.append(taskrow)

    with open("{}.csv".format(employeeId), 'w') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(all_tasks)

    return 0

if __name__ == "__main__":
    save_tasks_to_csv(sys.argv[1])