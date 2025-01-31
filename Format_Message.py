import json
from datetime import datetime, timedelta


def get_Weekday(current,due):

    delta = due - current

    weekday_number = (current.weekday() + delta.days) % 7

    weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    weekday_name = weekday_names[weekday_number]

    return weekday_name

def get_Assignments(taskNum):
    final_Message = ""

    with open('simple_rows.json', 'r') as file:
        # Load the JSON data from the file
        Json_File = json.load(file)


    This_Week = []

    current = datetime.now()
    current_date_formatted = current.strftime("%Y-%m-%d")
    current_date = datetime.strptime(current_date_formatted, '%Y-%m-%d')

    days_until_sunday = (6 - current.weekday()) % 7
    nearest_sunday = current + timedelta(days=days_until_sunday)

    for task in Json_File:
        if task["Status"] == True:
            continue

        date = datetime.strptime(task["Due_Date"], '%Y-%m-%d')

        if date <= nearest_sunday and date >= current_date:
            This_Week.append(task)

    This_Week = sorted(This_Week, key=lambda x: x["Due_Date"])

    if taskNum == 0:
        final_Message += "Good morning baby! Here are your assignments that you have left to do this week:\n"
    else:
        final_Message += "Here are your assignments that you have left to do this week:\n"

    for x in This_Week:
        date = datetime.strptime(x["Due_Date"], '%Y-%m-%d')
        weekday = get_Weekday(current_date, date)
        if date == current_date:
            weekday = "Today"


        final_Message += ("\n\nYou have "+ x["Assignment"]+ " for "+ x["Class"]+ " due "+ weekday)




    return final_Message