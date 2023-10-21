from event import Event
from event_checker import EventChecker
from event_handler import EventHandler
from global_variables import GlobalVariables

# from exceptions import


class Menu:
    def GetDate() -> str:
        isDate = False
        while not isDate:
            date = input("Enter date of event (using format DD.MM.YYYY): ")
            isDate = EventChecker.CheckDate(date)

        return date

    def GetTime(timeText: str) -> str:
        isTime = False
        while not isTime:
            time = input(f"Enter {timeText} time of event (using format HH:MM): ")
            isTime = EventChecker.CheckTime(time)

        return time

    def GetText() -> str:
        isText = False
        while not isText:
            text = input(
                f"Enter text for your event (must to be shorter than {GlobalVariables.MaxTextLength} characters): "
            )
            isText = EventChecker.CheckTextLength(text)

        return text

    def PrintEventsSortedByDate(events: list[Event]) -> None:
        for event in events:
            print(event.CreateEventStr())
        return events

    def PrintSearchedEvents(events: list[Event]) -> None:
        searchedDate = Menu.GetDate()
        searchedEvents = EventHandler.CreateSearchedDateList(events, searchedDate)
        print(f"Events for the date {searchedDate} are:")
        for event in searchedEvents:
            print(event.CreateEventStr())
        return events

    def CreateNewEvent(events: list[Event]) -> list[Event]:
        starTime = Menu.GetTime("start")
        endTime = Menu.GetTime("end")
        isCorrect = False
        while not isCorrect:
            isCorrect = EventChecker.CompareTimes(starTime, endTime)
            if not isCorrect:
                choice = input("Enter which time to correct (1 - start, 2 - end): ")
                if choice in "1":
                    starTime = Menu.GetTime("start")
                elif choice in "2":
                    endTime = Menu.GetTime("end")
        date = Menu.GetDate()
        text = Menu.GetText()
        events.append(Event(starTime, endTime, date, text))
        with open(GlobalVariables.FilePath, "w") as f:
            f.write(EventHandler.CreateEventStrToFile(events))

        return events


def main() -> None:
    with open(GlobalVariables.FilePath, "r") as f:
        events = EventHandler.CreateEventsFromFile(f.read())
    menu = {
        "1": Menu.PrintEventsSortedByDate,
        "2": Menu.PrintSearchedEvents,
        "3": Menu.CreateNewEvent,
    }
    while True:
        print(
            "Choose from the following:\n1 - Write out records\n2 - Search for records by date\n3 - Add new record\n0 - Exit"
        )
        chosenOption = input("Enter your choice: ")
        chosenFunction = menu.get(chosenOption)
        if chosenFunction:
            events = chosenFunction(events)
        elif chosenOption == "0":
            print("Goodbye, have a nice day")
            break


main()
