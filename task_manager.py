import json
import os
from datetime import datetime

TASK_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return[]
    with open(TASK_FILE,"r") as file:
        try:
           return json.load(file)
        except json.JSONDecodeError:
            return[]         
def save_tasks(tasks):
    with open(TASK_FILE,"w") as file:
        json.dump(tasks,file,indent=4)

def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks)+1
    task ={
        "id":task_id,
            "description":description,
                "status":"todo",
                "createdAt":datetime.now().isoformat(),
                "updatedAt":datetime.now().isoformat()
    }        
    tasks.append(task)
    save_tasks(tasks)
    print(f"task added successfully (ID:{task_id})")

def update_task(task_id,new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Task updated successfully")
            return
        print("task not found!")
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print("Task deleted successfully")

def mark_in_progress(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Task marked as in progress")
            return
        print("Task not found!")
def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task in tasks:
            task["status"] = "done"
            task["updateAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Task marked as done")
            return
        print("Task not found")
def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task["status"] == status]
    
    if not tasks:
        print("No tasks found.")
        return
    
    for task in tasks:
        print(f"[{task['id']}] {task['description']} - {task['status']} (Updated: {task['updatedAt']})")



