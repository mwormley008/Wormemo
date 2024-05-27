from datetime import date
import os

def make_todays_file():
    today_file_name = f"{date.today()}"
    if not os.path.exists(today_file_name):
        os.makedirs(today_file_name) 
