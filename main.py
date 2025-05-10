from task_scheduler import Scheduler
from task import Task

def main():
    # Create a scheduler
    scheduler = Scheduler()

    # Create some tasks
    task1 = Task("Task 1", 5)  # Task with runtime of 5 units
    task2 = Task("Task 2", 3)  # Task with runtime of 3 units
    task3 = Task("Task 3", 8)  # Task with runtime of 8 units

    # Add tasks to the scheduler
    scheduler.add_task(task1)
    scheduler.add_task(task2)
    scheduler.add_task(task3)

    # Run the scheduler
    scheduler.run()

if __name__ == "__main__":
    main()