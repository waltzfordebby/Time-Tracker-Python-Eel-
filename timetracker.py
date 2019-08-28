import json
import time
from datetime import datetime

import eel

eel.init("web")

current_hour = time.strftime("%I").lstrip("0")
period = time.strftime("%p")
conflicting_time = ["12", "1", "2", "3", "4", "5"]


@eel.expose
def get_time():
    current_time = datetime.now().strftime("%I:%M:%S %p").lstrip("0")
    if "AM" in period:
        if current_hour in conflicting_time:
            return f'<i class="fas fa-moon"></i> {current_time}'
        return f'<i class="fas fa-sun"></i> {datetime.now().strftime("%I:%M:%S %p").lstrip("0")}'
    elif "PM" in period:
        if current_hour in conflicting_time:
            return f'<i class="fas fa-sun"></i> {current_time}'
        return f'<i class="fas fa-moon"></i> {current_time}'


@eel.expose
def get_date():
    return datetime.now().strftime("%A, %d %B %Y")

@eel.expose
def set_bg_color():
    current_time = datetime.now().strftime("%I:%M:%S %p").lstrip("0")
    if "AM" in period:
        if current_hour in conflicting_time:
            return "#000000"
        return "#87CEEB"
    elif "PM" in period:
        if current_hour in conflicting_time:
            return "#87CEEB"
        return "#000000"


eel.start("main.html", size=(600, 500))

