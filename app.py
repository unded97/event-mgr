import datetime as dt


currentDateTime = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
 
eventID = 4  #change this to 1 after removing the built-in events


#Built-in Events
event1 = {
    "name":"Python Workshop",
    "date":dt.date(2026, 9, 26).strftime("%d/%m/%Y"),
    "time":dt.time(10, 0, 0).strftime("%H:%M:%S"),
    "venue":"School"
}
event2 = {
    "name":"Python Workshop2",
    "date":dt.date(2026, 9, 27).strftime("%d/%m/%Y"),
    "time":dt.time(10, 0, 0).strftime("%H:%M:%S"),
    "venue":"School"
}
event3 = {
    "name":"Python Workshop3",
    "date":dt.date(2026, 9, 25).strftime("%d/%m/%Y"),
    "time":dt.time(10, 0, 0).strftime("%H:%M:%S"),
    "venue":"School"
}

#Add New Event
eventContainer = [event1, event2, event3]


Events = {
    1: eventContainer[0], #change the numbers to eventID variable after removing the built-in events
    2: eventContainer[1],
    3: eventContainer[2]
}
for eventID in Events:
    updateEvent = Events[eventID]

def addEvent():
    eventName = input("Enter the name of the event: ")
    eventDate = dt.date.strptime((input("Enter the date of the event (dd/mm/yyyy): ")), "%d/%m/%Y").strftime("%d/%m/%Y")
    eventTime = dt.time.strptime((input("Enter the time of the event (HH:MM:SS): ")), "%H:%M:%S").strftime("%H:%M:%S")
    eventVenue = input("Enter the venue of the event: ")

    newEvent = {
    "name": eventName,
    "date": eventDate,
    "time": eventTime,
    "venue": eventVenue
 }
    eventContainer.append(newEvent)
    eventContainer.sort(key=lambda x: (x["date"], x["time"]))
    global eventID
    eventID+=1
    global Events
    Events = {eventID: eventContainer}
    displayEvents()



#Display Events
def displayEvents():
        print("Today's date and time: \n", currentDateTime)
        print("Events:")
        print("  Passed Events:")
        for i in range(len(eventContainer)):
            if dt.datetime.strptime(eventContainer[i]["date"], "%d/%m/%Y") < dt.datetime.strptime(currentDateTime.split()[0], "%d/%m/%Y"):
                print(f"    - {eventContainer[i]['name']} ({eventContainer[i]['date']} at {eventContainer[i]['time']})")
        '''for event_key, event in Events.items():
            if dt.datetime.strptime(event["date"], "%d/%m/%Y") < dt.datetime.strptime(currentDateTime.split()[0], "%d/%m/%Y"):
                print(f"    - {event['name']} ({event['date']} at {event['time']})")'''
        print("  Upcoming Events:")
        for i in range(len(eventContainer)):
            if dt.datetime.strptime(eventContainer[i]["date"], "%d/%m/%Y") >= dt.datetime.strptime(currentDateTime.split()[0], "%d/%m/%Y"):
                print(f"    - {eventContainer[i]['name']} ({eventContainer[i]['date']} at {eventContainer[i]['time']})")
        '''for event_key, event in Events.items():
            if dt.datetime.strptime(event["date"], "%d/%m/%Y") >= dt.datetime.strptime(currentDateTime.split()[0], "%d/%m/%Y"):
                print(f"    - {event['name']} ({event['date']} at {event['time']})")'''

#Display Menu
def displayMenu():
    print("\nMenu:")
    print("1. Add Event")
    print("2. Display Events")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    match choice:
        case "1": addEvent()
        case "2": displayEvents()
        case "3": exit()
        case _: print("Invalid choice. Please try again.")


while True:
    displayMenu()