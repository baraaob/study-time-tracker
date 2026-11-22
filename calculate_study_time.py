import datetime
import os
import json

FILE = "study_data.json"

def load_data():
    if not os.path.exists(FILE):
        return None
    else:
        with open(FILE, mode="r", encoding="utf-8") as read_file:
            return json.load(read_file)

def save_data(data):
    with open(FILE, mode="w", encoding="utf-8") as write_file:
        json.dump(data, write_file, indent=4)

def take_timer():
    return datetime.datetime.now().isoformat(timespec="seconds")

def total_study(start_text, end_text):
    start = datetime.datetime.fromisoformat(start_text)
    end = datetime.datetime.fromisoformat(end_text)
    return int((end - start).total_seconds())

def show_total(total_seconds):
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"\n\n\n➜ Your total study hour is: {hours:02d}:{minutes:02d}:{seconds:02d}")

def new_day():
    return {
        "start_time": 0,
        "end_time": 0,
        "total_study": 0,
        "session_finished": True
    }

def leave():
    exit()


def main():
    data = load_data()
    if data == None:
        data = new_day()

    print("\n\n\nWelcome to Study Time Tracker")

    while True:
        print("\n\n===== Study Tracker Options =====\n")
        print("[1] Start the timer")
        print("[2] Stop the timer")
        print("[3] Total study hours")
        print("[4] New day")
        print("[5] Exit")
        print("\n==================================\n")

        user_input = int(input("Choose what you want and type the number: ").strip())

        if user_input == 1:
            if not data["session_finished"]:
                print("\n\n\n➜ The current session is still active! Please end it before starting a new one.")
            else:
                print("\n\n\n➜ Timer starts now — good luck!")
                data["start_time"] = take_timer()
                data["session_finished"] = False
                save_data(data)
        elif user_input == 2:
            if data["session_finished"]:
                print("\n\n\n➜ This session has already ended! Start a new session to continue.")
            else:
                print("\n\n\n➜ Time's up! — Hope you did your best!")
                data["end_time"] = take_timer()
                data["total_study"] += total_study(data["start_time"], data["end_time"])
                data["session_finished"] = True
                save_data(data)
        elif user_input == 3:
            show_total(data["total_study"])
        elif user_input == 4:
            print("\n\n\n➜ Hi! A new day, a fresh start, and a new session!")
            data = new_day()
            save_data(data)
        elif user_input == 5:
            leave()

if __name__ == "__main__":
    main()