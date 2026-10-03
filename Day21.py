from dataclasses import dataclass
from collections import deque

@dataclass
class Task:
    name: str
    priority: int
    completed: bool = False

task1 = Task("Learn Python", 1)

print(task1)
print(task1.name)
print(task1.priority)
print(task1.completed)

tasks = []

task1 = Task("Learn Python", 1)
task2 = Task("Complete Assignment", 2)
task3 = Task("Go for a Walk", 3)

tasks.append(task1)
tasks.append(task2)
tasks.append(task3)

print(tasks)

def display_tasks(tasks):
    print("========================")
    print("TASK SCHEDULER")
    print("========================")

    for task in tasks:
        status = "Completed" if task.completed else "Pending"

        print(f"Task: {task.name}")
        print(f"Priority: {task.priority}")
        print(f"Status: {status}")
        print("------------------------")

display_tasks(tasks)

def complete_task(tasks, task_name):
    for task in tasks:
        if task.name == task_name:
            task.completed = True
            print(f"{task_name} marked as completed!")
            return

    print("Task not found.")

complete_task(tasks, "Learn Python")

display_tasks(tasks)

def add_task(tasks, name, priority):
    task = Task(name, priority)
    tasks.append(task)
    print(f"{name} added successfully!")

add_task(tasks, "Practice SQL", 2)

display_tasks(tasks)

def sort_by_priority(tasks):
    return sorted(tasks, key=lambda task: task.priority)

sorted_tasks = sort_by_priority(tasks)

display_tasks(sorted_tasks)

def get_next_task(tasks):
    pending_tasks = [task for task in tasks if not task.completed]

    if not pending_tasks:
        print("No pending tasks!")
        return

    next_task = min(pending_tasks, key=lambda task: task.priority)

    print("NEXT TASK")
    print(f"Task: {next_task.name}")
    print(f"Priority: {next_task.priority}")


get_next_task(tasks)

def complete_next_task(tasks):
    pending_tasks = [task for task in tasks if not task.completed]

    if not pending_tasks:
        print("No pending tasks!")
        return

    next_task = min(pending_tasks, key=lambda task: task.priority)

    next_task.completed = True

    print(f"Completed: {next_task.name}")

complete_next_task(tasks)
get_next_task(tasks)

sorted_tasks = sorted(
    [task for task in tasks if not task.completed],
    key=lambda task: task.priority
)

task_queue = deque(sorted_tasks)

print("TASK QUEUE")
print(task_queue)

next_task = task_queue.popleft()

print("PROCESSING TASK")
print(f"Task: {next_task.name}")
print(f"Priority: {next_task.priority}")

next_task.completed = True

print(f"{next_task.name} marked as completed!")
print("REMAINING TASKS")
print(task_queue)
def run_scheduler(tasks):
    pending_tasks = [
        task for task in tasks
        if not task.completed
    ]

    sorted_tasks = sorted(
        pending_tasks,
        key=lambda task: task.priority
    )

    task_queue = deque(sorted_tasks)

    print("========================")
    print("RUNNING TASK SCHEDULER")
    print("========================")

    while task_queue:
        task = task_queue.popleft()

        print(f"Processing: {task.name}")
        print(f"Priority: {task.priority}")

        task.completed = True

        print(f"{task.name} completed!")
        print("------------------------")

    print("All pending tasks completed!")
run_scheduler(tasks)

display_tasks(tasks)