"""Study Time Tracker: start and stop a timer, and save total study time to a JSON file."""

import datetime
import json
from pathlib import Path

# Keep the data file with the script, no matter where it is.
FILE = Path(__file__).with_name("data.json")


def load_data():
    """Load the saved study data from the JSON file.

    Return None if the file is missing, damaged, or not a dictionary.
    Missing keys are filled in from the defaults, and a total_study or
    session_finished value of the wrong type is replaced by its default.
    """
    
    if not FILE.exists():
        return None

    try:
        with FILE.open(mode="r", encoding="utf-8") as read_file:
            loaded_data = json.load(read_file)
    except json.decoder.JSONDecodeError:
        print("\n\n\n\n➜ Warning: the data file is damaged. Starting fresh.")
        return None

    if not isinstance(loaded_data, dict):
        return None

    defaults = new_day()
    for key, value in defaults.items():
        if key not in loaded_data:
            loaded_data[key] = value

    if type(loaded_data["total_study"]) is not int:
        print("\n\n\n➜ Warning: total study was invalid. Resetting it.")
        loaded_data["total_study"] = defaults["total_study"]

    if type(loaded_data["session_finished"]) is not bool:
        print("\n\n\n➜ Warning: session status was invalid. Resetting it.")
        loaded_data["session_finished"] = defaults["session_finished"]

    return loaded_data


def save_data(data):
    """Overwrite the data file with the current data."""
    with FILE.open(mode="w", encoding="utf-8") as write_file:
        json.dump(data, write_file, indent=4)


def current_time_text():
    """Return the current time as ISO-formatted text."""
    # JSON cannot store datetime objects, so timestamps are stored as text.
    return datetime.datetime.now().isoformat(timespec="seconds")


def parse_iso_timestamp(timestamp_text):
    """Parse an ISO-formatted timestamp into a datetime."""
    return datetime.datetime.fromisoformat(timestamp_text)


def session_length(start_text, end_text):
    """Return elapsed seconds between two ISO-formatted timestamp strings."""
    start = parse_iso_timestamp(start_text)
    end = parse_iso_timestamp(end_text)
    return int((end - start).total_seconds())


def reset_session(data):
    """Reset the session while preserving the accumulated study time."""
    data["start_time"] = None
    data["session_finished"] = True


def format_time(duration_seconds):
    """Return a duration in seconds as hh:mm:ss text."""
    hours, remainder = divmod(duration_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def show_total(total_seconds, session_finished):
    """Display the total study time and warn if a session is still running."""
    formatted_time = format_time(total_seconds)
    print(f"\n\n\n➜ Your total study hours are: {formatted_time}")
    if not session_finished:
        print("\n➜ There is a running session, so this total does not include it yet.")


def show_session_summary(start_text, end_text, session_seconds):
    """Display a session's start time, end time, and duration."""
    start = parse_iso_timestamp(start_text).strftime("%I:%M %p")
    end = parse_iso_timestamp(end_text).strftime("%I:%M %p")
    print("\n\n=========== session summary ===========")
    print(f"\n➜ Your session started at {start}")
    print(f"\n➜ Your session ended at {end}")
    print(f"\n➜ You studied {format_time(session_seconds)}")
    print("\n======================================")


def new_day():
    """Return a fresh study-tracker state."""
    return {
        "start_time": None,
        "end_time": None,
        "total_study": 0,
        "session_finished": True
    }


def main():
    data = load_data()
    # Start with default data on the first run if the file isn't there.
    if data is None:
        data = new_day()

    print("\n\n\nWelcome to Study Time Tracker")

    while True:
        print("\n\n===== Study Tracker Options =====\n")
        print("[1] Start the timer")
        print("[2] Stop the timer")
        print("[3] Reset the session")
        print("[4] Total study hours")
        print("[5] New day")
        print("[6] Exit")
        print("\n==================================\n")

        try:
            user_input = int(input("Choose what you want and type the number: ").strip())
        except ValueError:
            print("\n\n\n➜ Please type a number, not letters.")
            continue

        # session_finished prevents starting two sessions at once,
        # and stopping a session that never started
        if user_input == 1:
            if not data["session_finished"]:
                print("\n\n\n➜ The current session is still active! Please end it before starting a new one.")
            else:
                print("\n\n\n➜ Timer starts now — good luck!")
                data["start_time"] = current_time_text()
                data["session_finished"] = False
                save_data(data)
        elif user_input == 2:
            if data["session_finished"]:
                print("\n\n\n➜ This session has already ended! Start a new session to continue.")
            else:
                print("\n\n\n➜ Time's up! — Hope you did your best!")
                data["end_time"] = current_time_text()
                session_seconds = session_length(data["start_time"], data["end_time"])
                data["total_study"] += session_seconds
                data["session_finished"] = True
                save_data(data)
                show_session_summary(data["start_time"], data["end_time"], session_seconds)
        elif user_input == 3:
            if data["session_finished"]:
                print("\n\n\n➜ No session is running, so there is nothing to reset.")
            else:
                print("\n\n\n➜ Session reset successfully! Good luck with the next one!")
                reset_session(data)
                save_data(data)
        elif user_input == 4:
            show_total(data["total_study"] ,data["session_finished"])
        elif user_input == 5:
            print("\n\n\n➜ Hi! A new day, a fresh start, and a new session!")
            # Discards all data, even a session that is still running.
            data = new_day()
            save_data(data)
        elif user_input == 6:
            print("\n\n\n➜ Program closed successfully!")
            break
        else:
            print("\n\n\n➜ Please choose a number from the list.")


if __name__ == "__main__":
    main()