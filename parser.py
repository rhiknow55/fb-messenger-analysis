import json
from datetime import datetime
import pytz

import helper

filename = "files/test.json"
participants = []

starting_date = datetime(2019, 3, 26).astimezone(pytz.timezone('US/Pacific'))
ending_date = datetime(2020, 3, 26).astimezone(pytz.timezone('US/Pacific'))
num_days = (ending_date - starting_date).days
dailymessagecounts = []


def main():
    with open(filename) as f:
        data = json.load(f)

    participants = data["participants"]
    print(participants)
    messages = data["messages"]

    init_daily_message_counts(participants)

    for message in messages:
        count_message(message)

    print(dailymessagecounts)

# Daily Message Counter
def init_daily_message_counts(participants):
    for i in range(num_days):
        obj = {}
        for person in participants:
            name = person["name"]
            obj[name] = 0 # Start off both people at 0 messages

        dailymessagecounts.append(obj)


def count_message(message):
    name = message["sender_name"]
    timestamp = message["timestamp_ms"]
    days = helper.days_since_start(timestamp)

    dailymessagecounts[days - 1][name] += 1



print(helper.days_since_start(1584673042479))
print(helper.year_and_month(359))

# Overall Message Counter
def overall_message_counts(participants):
    counts = {}
    for person in participants:
        name = person["name"]
        counts[name] = 0

    for day in dailymessagecounts:
        for name in day.keys():
            counts[name] += day[name]

    return counts


if __name__ == "__main__":
    main()
    print("Finished running fb message parser!")
