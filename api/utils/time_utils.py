from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%H:%M")

def get_current_day():
    return datetime.now().strftime("%a")  # Returns abbreviated weekday name (Mon, Tue, etc.)
