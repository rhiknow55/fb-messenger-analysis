import json
from datetime import datetime
import pytz
import os

from nltk.tokenize import TweetTokenizer
tokenizer = TweetTokenizer()

import helper
import visualizer as vz

MESSAGES_DIRECTORY = "messages/"

participants = []

starting_date = datetime(2019, 3, 26).astimezone(pytz.timezone('US/Pacific'))
ending_date = datetime(2020, 3, 26).astimezone(pytz.timezone('US/Pacific'))
num_days = (ending_date - starting_date).days
dailymessagecounts = []
dailymessagecounts_initialized = False

def main():

    message_files = os.listdir(MESSAGES_DIRECTORY)
    for filename in message_files:
        with open(MESSAGES_DIRECTORY + filename) as f:
            data = json.load(f)

        participants = data["participants"]
        messages = data["messages"]

        init_daily_message_counts(participants)

        for message in messages:
            process_message(message)

    # Finally plot
    vz.year_messages_plot(dailymessagecounts)


#
def process_message(message):
    timestamp = message["timestamp_ms"]
    name = message["sender_name"]

    count_message(timestamp, name)

    if "content" in message.keys():
        process_content(message["content"])

# Message Content Analyze
def process_content(content):
    i = 0

# Daily Message Counter
def init_daily_message_counts(participants):
    global dailymessagecounts_initialized
    if dailymessagecounts_initialized:
        return

    for i in range(num_days):
        obj = {}
        for person in participants:
            name = person["name"]
            obj[name] = 0 # Start off both people at 0 messages

        dailymessagecounts.append(obj)

    dailymessagecounts_initialized = True


def count_message(timestamp, name):
    days = helper.days_since_start(timestamp)

    dailymessagecounts[days - 1][name] += 1


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
