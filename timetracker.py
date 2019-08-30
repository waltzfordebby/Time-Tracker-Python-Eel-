import json
import time
from datetime import datetime

import eel

eel.init("web")

# Date and Time Variables
current_hour = time.strftime("%I").lstrip("0")
period = time.strftime("%p")
conflicting_time = ["12", "1", "2", "3", "4", "5"]

# Color variables
day_bg_color = "#7289da"
day_font_color = "#ffffff"
night_bg_color = "#2c2f33"
night_font_color = "#ffffff"


def set_value_day_night(day_value, night_value):
    if "AM" in period:
        if current_hour in conflicting_time:
            return night_value
        return day_value
    elif "PM" in period:
        if current_hour in conflicting_time:
            return day_value
        return night_value


@eel.expose
def get_time():
    current_time = datetime.now().strftime("%I:%M:%S %p").lstrip("0")
    return set_value_day_night(
        f'<i class="fas fa-sun"></i> {current_time}',
        f'<i class="fas fa-moon"></i> {current_time}',
    )


@eel.expose
def get_date():
    return datetime.now().strftime("%A, %d %B %Y")


@eel.expose
def get_bg_color():
    return set_value_day_night(day_bg_color, night_bg_color)


@eel.expose
def get_font_color():
    return set_value_day_night(day_font_color, night_font_color)

@eel.expose
def get_button_color():
    return set_value_day_night(night_bg_color, day_bg_color)


eel.start("main.html", size=(600, 500))

        