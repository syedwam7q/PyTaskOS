from collections import deque

class Scheduler:
    def __init__(self, time_slice=2):
        self.time_slice = time_slice  # Time slice for round-robin scheduling
        self.task_queue = deque()    # Queue to hold tasks

    def add_task(self, task):
        self.task_queue.append(task)

    def run(self):
        print("Starting Scheduler...")
        while self.task_queue:
            current_task = self.task_queue.popleft()
            print(f"Running {current_task.name} for {self.time_slice} time units.")
            current_task.run(self.time_slice)

            if not current_task.is_completed():
                print(f"{current_task.name} is not completed. Adding back to the queue.")
                self.task_queue.append(current_task)
            else:
                print(f"{current_task.name} has completed execution.")
        print("All tasks are completed!")