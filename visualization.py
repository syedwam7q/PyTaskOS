def visualize_task_queue(task_queue):
    print("\nCurrent Task Queue:")
    for task in task_queue:
        print(f"Task: {task.name}, Remaining Runtime: {task.remaining_runtime}")
    print()