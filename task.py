class Task:
    def __init__(self, name, total_runtime):
        self.name = name
        self.total_runtime = total_runtime
        self.remaining_runtime = total_runtime

    def run(self, time_slice):
        if self.remaining_runtime <= time_slice:
            print(f"{self.name} ran for {self.remaining_runtime} time units and is now complete.")
            self.remaining_runtime = 0
        else:
            print(f"{self.name} ran for {time_slice} time units. {self.remaining_runtime - time_slice} time units remaining.")
            self.remaining_runtime -= time_slice

    def is_completed(self):
        return self.remaining_runtime == 0