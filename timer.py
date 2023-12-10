import time
import keyboard
import os
from datetime import datetime


def get_hours_and_min(accumulated_time):
    hours = int(accumulated_time // 3600)
    minutes = int((accumulated_time % 3600) // 60)
    return f"{hours} hours and {minutes} minutes"


def get_date_and_time():
    current_time = datetime.now()
    return current_time.strftime("%Y-%m-%d %H:%M:%S")


class TimerApp:
    def __init__(self):
        self.running = False
        self.time_at_start = 0
        self.time_at_end = 0
        self.time_list = []
        self.accumulated_time = sum(self.time_list)
        self.formatted_time = get_hours_and_min(self.accumulated_time)
        self.file_path = None
        self.update_file_path()

    def update_file_path(self):
        current_date = datetime.now().strftime("%Y-%m-%d")
        filename = f"{current_date}.txt"
        get_dir = os.path.dirname(os.path.realpath(__file__))
        self.file_path = os.path.join(get_dir, "logs", filename)

    def toggle_timer(self):
        if self.running:
            # Stop the timer
            self.running = False
            self.time_at_end = time.time()
            self.time_list.append(self.time_at_start - self.time_at_end)
            self.log_time_stop(self.formatted_time)
            print(f"Timer stopped at {get_date_and_time()} | Total time: {self.formatted_time}")
        else:
            # Start the timer
            self.running = True
            self.time_at_start = time.time()
            self.log_time_stop(self.formatted_time)
            print(f"Timer started at {get_date_and_time()}")

    def new_session(self):
        if self.running:
            self.toggle_timer()
        print("\n--- Starting a new timer session ---\n")
        self.time_list.clear()

    def rollback_time(self):
        # Rollback the time by the last time entry added
        self.time_list.remove(self.time_list[-1])
        self.log_rollback(self.formatted_time)
        print(f"Time removed | New total time: {self.formatted_time}")

    def log_time_start(self):
        with open(self.file_path, "a") as file:
            file.write(f"Timer started at {get_date_and_time()}")

    def log_time_stop(self, formatted_time):
        with open(self.file_path, "a") as file:
            file.write(f"Timer stopped at {get_date_and_time()} | Total time: {formatted_time}")

    def log_rollback(self, formatted_time):
        with open(self.file_path, "a") as file:
            file.write(f"Time removed | Total time: {formatted_time}\n")

    def log_session(self):
        with open(self.file_path, "a") as file:
            file.write("\n--- New Timer Session ---\n")

    def run(self):
        print(
            "Press F8 to start/stop the timer\n"
            "Press shift+F8 to start a new timer session in this window\n"
            "Press shift+F9 to rollback last addition to total time\n"
            "-----"
        )

        keyboard.add_hotkey('F8', self.toggle_timer)
        keyboard.add_hotkey('shift+f8', self.new_session)
        keyboard.add_hotkey('shift+f9', self.rollback_time)

        # Keeps the program running.
        while True:
            time.sleep(1)


if __name__ == "__main__":
    app = TimerApp()
    app.run()