from event import Event
from event_checker import EventChecker
from event_handler import EventHandler
from global_variables import GlobalVariables
from event_editor import EventEditor
from event_deletor import EventDeletor

from exceptions import (
    TextIsLongerThanMaxTextLengthException,
    StartTimeIsLaterThanEndTimeException,
    IncorrectDateException,
    IncorrectTimeException,
    IncorrectOptionException,
    IncorrectModeException,
)


class Menu:
    def GetDate() -> str:
        isDate = False
        while not isDate:
            try:
                date = input("Enter date of event (using format DD.MM.YYYY): ")
                isDate = EventChecker.CheckDate(date)
                if not isDate:
                    raise IncorrectDateException
            except IncorrectDateException as e:
                print(e.Text)

        return date

    def GetText() -> str:
        isText = False
        while not isText:
            try:
                text = input(
                    f"Enter text for your event (must to be shorter than {GlobalVariables.MaxTextLength} characters): "
                )
                isText = EventChecker.CheckTextLength(text)
                if not isText:
                    raise TextIsLongerThanMaxTextLengthException
            except TextIsLongerThanMaxTextLengthException as e:
                print(e.Text)

        return text

    def GetStartTime() -> str:
        isTime = False
        while not isTime:
            try:
                time = input(f"Enter start time of event (using format HH:MM): ")
                isTime = EventChecker.CheckTime(time)
                if not isTime:
                    raise IncorrectTimeException
            except IncorrectTimeException as e:
                print(e.Text)

        return time

    def GetEndTime() -> str:
        isTime = False
        while not isTime:
            try:
                time = input(f"Enter end time of event (using format HH:MM): ")
                isTime = EventChecker.CheckTime(time)
                if not isTime:
                    raise IncorrectTimeException
            except IncorrectTimeException as e:
                print(e.Text)

        return time

    def CorrectTimes_CreateNewEvent(startTime: str, endTime: str) -> tuple[str, str]:
        isCorrect = False
        while not isCorrect:
            choice = input("Enter which time to correct (1 - start, 2 - end): ")
            if choice in "1":
                startTime = Menu.GetStartTime()
            elif choice in "2":
                endTime = Menu.GetEndTime()
            isCorrect = Menu.CheckTimes(startTime, endTime)

        return startTime, endTime

    def CorrectTimes_EditEvent(startTime: str, endTime: str, mode: str) -> str:
        isCorrect = False
        while not isCorrect:
            if mode in "1":
                startTime = Menu.GetStartTime()
            elif mode in "2":
                endTime = Menu.GetEndTime()
            isCorrect = Menu.CheckTimes(startTime, endTime)

        if mode in "1":
            return startTime
        else:
            return endTime

        return startTime, endTime

    def CheckTimes(startTime: str, endTime: str) -> bool:
        try:
            isCorrect = EventChecker.CompareTimes(startTime, endTime)
            if not isCorrect:
                raise StartTimeIsLaterThanEndTimeException
            return True
        except StartTimeIsLaterThanEndTimeException as e:
            print(e.Text)
            return False

    def CheckEventNumber(eventLength: int, eventNumber: str) -> None:
        if not str(eventNumber).isnumeric():
            return False
        elif int(eventNumber) - 1 >= eventLength:
            return False
        else:
            return True

    def PrintEventsSortedByDate(events: list[Event]) -> None:
        for number, event in enumerate(events):
            print(f"{number + 1}-{event.CreateEventStr()}")
        return events

    def PrintSearchedEvents(events: list[Event]) -> None:
        searchedDate = Menu.GetDate()
        searchedEvents = EventHandler.CreateSearchedDateList(events, searchedDate)
        if len(searchedEvents) > 0:
            print(f"Events for the date {searchedDate} are:")
            for number, event in enumerate(searchedEvents):
                print(f"{number + 1}-{event.CreateEventStr()}")
        else:
            print(f"There are no dates recorded for the date {searchedDate}")

        return events

    def CreateNewEvent(events: list[Event]) -> list[Event]:
        startTime = Menu.GetStartTime()
        endTime = Menu.GetEndTime()
        if not Menu.CheckTimes(startTime, endTime):
            startTime, endTime = Menu.CorrectTimes_CreateNewEvent(startTime, endTime)
        date = Menu.GetDate()
        text = Menu.GetText()
        events.append(Event(startTime, endTime, date, text))
        Menu.SaveToFile(events)

        return events

    def EditEvent(events: list[Event]) -> list[Event]:
        isEventNumber = False
        while True:
            eventNumberToEdit = input("Enter the number of event to edit: ")
            isEventNumber = Menu.CheckEventNumber(len(events), eventNumberToEdit)
            if not isEventNumber:
                print("Incorrectly entered event number")
            else:
                break

        eventNumberToEdit = int(eventNumberToEdit) - 1
        print(f"Currently editing: {events[eventNumberToEdit].CreateEventStr()}")
        print(
            "Choose what to edit:\n1 - Start time\n2 - End time\n3 - Date\n4 - Note\n0 - Exit"
        )
        isCorrect = False
        isTime = True
        while not isCorrect:
            try:
                mode = input("Enter your choice: ")
                if mode in "1":
                    changes = Menu.GetStartTime()
                    isTime = Menu.CheckTimes(
                        changes,
                        events[eventNumberToEdit].EndTime.strftime(
                            GlobalVariables.TimeFormat
                        ),
                    )
                    isCorrect = True
                elif mode in "2":
                    changes = Menu.GetEndTime()
                    isTime = Menu.CheckTimes(
                        events[eventNumberToEdit].StartTime.strftime(
                            GlobalVariables.TimeFormat
                        ),
                        changes,
                    )
                    isCorrect = True
                elif mode in "3":
                    changes = Menu.GetDate()
                    isCorrect = True
                elif mode in "4":
                    changes = Menu.GetText()
                    isCorrect = True
                elif mode in "0":
                    return events
                else:
                    raise IncorrectModeException
            except IncorrectModeException as e:
                print(e.Text)

        if (not isTime) and (mode == "1"):
            changes = Menu.CorrectTimes_EditEvent(
                changes,
                events[eventNumberToEdit].EndTime.strftime(GlobalVariables.TimeFormat),
                mode,
            )
        elif (not isTime) and (mode == "2"):
            changes = Menu.CorrectTimes_EditEvent(
                events[eventNumberToEdit].StartTime.strftime(
                    GlobalVariables.TimeFormat
                ),
                changes,
                mode,
            )
        events = EventEditor.HandleEdit(events, eventNumberToEdit, mode, changes)
        print("Edit successfully completed")
        Menu.SaveToFile(events)

        return events

    def DeleteEvent(events: list[Event]) -> list[Event]:
        pass

    def SaveToFile(events: list[Event]) -> None:
        with open(GlobalVariables.FilePath, "w") as f:
            f.write(EventHandler.CreateEventStrToFile(events))


def main() -> None:
    with open(GlobalVariables.FilePath, "r") as f:
        events = EventHandler.CreateEventsFromFile(f.read())
    menu = {
        "1": Menu.PrintEventsSortedByDate,
        "2": Menu.PrintSearchedEvents,
        "3": Menu.CreateNewEvent,
        "4": Menu.EditEvent,
        "5": Menu.DeleteEvent,
    }
    while True:
        try:
            print(
                "Choose from the following:\n1 - Write out events\n2 - Search for events by date\n3 - Add new event\n4 - Edit event\n5 - Delete Event\n0 - Exit"
            )
            chosenOption = input("Enter your choice: ")
            chosenFunction = menu.get(chosenOption)
            if chosenFunction:
                events = chosenFunction(events)
            elif chosenOption == "0":
                print("Goodbye, have a nice day!")
                break
            else:
                raise IncorrectOptionException
        except IncorrectOptionException as e:
            print(e.Text)


main()
