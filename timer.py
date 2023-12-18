import time
import keyboard
import os
from datetime import datetime


class TimerApp:
    def __init__(self):
        self.running = False
        self.time_at_start = 0
        self.time_at_stop = 0
        self.time_list = []
        self.accumulated_time = 0
        self.formatted_time = ""

    def toggle_timer(self):
        if self.running:
            # Stop the timer
            self.running = False
            self.time_at_stop = time.time()
            self.time_list.append(self.time_at_stop - self.time_at_start)
            self.update_time()
            log_time_stop(self.formatted_time)
        else:
            # Start the timer
            self.running = True
            self.time_at_start = time.time()
            log_time_start()

    def new_session(self):
        if self.running:
            self.toggle_timer()
        self.time_list.clear()
        log_session()


    def rollback_time(self):
        if self.running:
            self.toggle_timer()
        self.time_list.remove(self.time_list[-1])
        self.update_time()
        log_rollback(self.formatted_time)

    def edit_time(self):
        if self.running:
            self.toggle_timer()
        new_time = input("Enter new total time in minutes: ")
        try:
            self.time_list.clear()
            self.time_list.append(float(new_time) * 60)
            self.update_time()
            log_edit(self.formatted_time)
        except ValueError:
            print("Invalid input. Please enter a number.")

    def update_time(self):
        self.accumulated_time = sum(self.time_list)
        self.formatted_time = get_hours_and_min(self.accumulated_time)

    def run(self):
        print(
            "Press F8 to start/stop the timer\n"
            "Press shift+F7 to enter a new total time\n"
            "Press shift+F8 to undo the last addition to total time\n"
            "Press shift+F9 to start a new timer session in this window\n"
            "-----"
        )

        # Edit hotkey strings to suit your needs, be mindful of OS and application hotkeys
        # https://github.com/boppreh/keyboard#api
        keyboard.add_hotkey('F8', self.toggle_timer)
        keyboard.add_hotkey('shift+f7', self.edit_time)
        keyboard.add_hotkey('shift+f8', self.rollback_time)
        keyboard.add_hotkey('shift+f9', self.new_session)

        # Keeps the program running.
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.time_at_stop = time.time()
            self.time_list.append(self.time_at_stop - self.time_at_start)
            self.update_time()
            log_time_stop(self.formatted_time)


def log_time_start():
    with open(file_path, "a") as file:
        file.write(f"Timer started at {get_date_and_time()}\n")
    print(f"Timer started at {get_date_and_time()}")


def log_time_stop(formatted_time):
    with open(file_path, "a") as file:
        file.write(f"Timer stopped at {get_date_and_time()} | Total time: {formatted_time}\n")
    print(f"Timer stopped at {get_date_and_time()} | Total time: {formatted_time}")


def log_rollback(formatted_time):
    with open(file_path, "a") as file:
        file.write(f"Time removed | Total time: {formatted_time}\n")
    print(f"Time removed | Total time: {formatted_time}")


def log_session():
    with open(file_path, "a") as file:
        file.write("\n--- Started a new timer session ---\n")
    print("\n--- Started a new timer session ---\n")


def log_edit(formatted_time):
    with open(file_path, "a") as file:
        file.write(f"Timer edited at {get_date_and_time()} | Total time: {formatted_time}")
    print(f"Timer edited at {get_date_and_time()} | Total time: {formatted_time}")


def get_hours_and_min(accumulated_time):
    hours = int(accumulated_time // 3600)
    minutes = int(round((accumulated_time % 3600) / 60))
    return f"{hours} hours and {minutes} minutes"


def get_date_and_time():
    current_time = datetime.now()
    return current_time.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    current_date = datetime.now().strftime("%Y-%m-%d")
    filename = f"{current_date}.txt"
    get_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(get_dir, "logs", filename)
    app = TimerApp()
    app.run()
