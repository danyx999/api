from datetime import datetime
from global_variables import GlobalVariables
from event import Event


class EventHandler:
    @staticmethod
    def CreateEventFromString(event: str) -> Event:
        eventParts = event.split(f"{GlobalVariables.Separator}")
        return Event(eventParts[0], eventParts[1], eventParts[2], eventParts[3])

    @staticmethod
    def CreateEventStrToFile(events: list[Event]) -> str:
        sortedEvents: list[Event] = EventHandler.SortEventsByDate(events)
        return "\n".join([event.CreateEventStr() for event in sortedEvents])

    @staticmethod
    def CreateEventsFromFile(events: str) -> list[Event]:
        if len(events) == 0:
            return []
        return EventHandler.SortEventsByDate(
            [EventHandler.CreateEventFromString(event) for event in events.split("\n")]
        )

    @staticmethod
    def SortEventsByDate(events: list[Event]) -> list[Event]:
        return sorted(events, key=lambda e: e.Date)

    @staticmethod
    def CreateSearchedDateList(events: list[Event], searchedDate: str) -> list[Event]:
        searchedDates: list[Event] = []
        date = datetime.strptime(searchedDate, GlobalVariables.DateFormat)
        for event in events:
            if event.Date == date:
                searchedDates.append(event)

        return EventHandler.SortEventsByStartTime(searchedDates)

    @staticmethod
    def SortEventsByStartTime(events: list[Event]) -> list[Event]:
        return sorted(events, key=lambda e: e.StartTime)
