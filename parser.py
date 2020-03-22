import json

filename = "files/test.json"
participants = []
counts = {}

def main():
    with open(filename) as f:
        data = json.load(f)

    participants = data["participants"]
    messages = data["messages"]

    init_counts(participants)

    for message in messages:
        count_message(message)

    print(counts)



def init_counts(participants):
    for person in participants:
        name = person["name"]
        counts[name] = 0

def count_message(message):
    name = message["sender_name"]
    counts[name] += 1

if __name__ == "__main__":
    main()
    print("Finished running fb message parser!")
