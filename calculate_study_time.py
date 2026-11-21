import datetime
start = 0
end = 0
totoal_seconds = 0
hours = 0
minutes = 0
seconds = 0

def start_timer():
    return datetime.datetime.now()

def stop_timer():
    return datetime.datetime.now()

def calculate_total(start, end):
    return end - start

def show_total(hours, minutes, seconds):
    print(f"Total study is -> {hours:02d}:{minutes:02d}:{seconds:02d}")

def start_new_day():
    global start
    global end
    global totoal_seconds
    global hours
    global minutes
    global seconds
    start = 0
    end = 0
    hours = 0
    minutes = 0
    seconds = 0


def quit():
    exit()

while True:
    print('''

Welcome to Study Time Tracker

---------------------------
[1] Start the timer
[2] Stop the timer
[3] Total study hour
[4] New day
[5] Exit
---------------------------
    ''')

    user_input = int(input("Chouse what you want and type the number: "))

    if user_input == 1:
        start = start_timer()
    elif user_input == 2:
        end = stop_timer()
        totoal_seconds = int(calculate_total(start,end).total_seconds())
        hours = totoal_seconds // 3600
        minutes = (totoal_seconds % 3600) // 60
        seconds = totoal_seconds % 60
    elif user_input == 3:
        show_total(hours, minutes, seconds)
    elif user_input == 4:
        start_new_day()
    elif user_input == 5:
        quit()