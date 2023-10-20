from datetime import datetime
from global_variables import GlobalVariables
from event import Event


class EventHandler:
    def CreateEventFromString(event: str) -> Event:
        eventParts = event.split(f"{GlobalVariables.Separator}")
        return Event(eventParts[0], eventParts[1], eventParts[2], eventParts[3])

    def CreateEventStrToFile(self, events: list[Event]) -> str:
        return "\n".join([event.CreateEventStr() for event in events])

    def CreateEventsFromFile(self, events: str) -> list[Event]:
        return [
            EventHandler.CreateEventFromString(event) for event in events.split("\n")
        ]

    def SortEventsByDate(events: list[Event]) -> list[Event]:
        return sorted(events, key=lambda e: e.Date)

    def CreateSearchedDateList(events: list[Event], searchedDate: str) -> list[Event]:
        searchedDates = []
        date = datetime.strptime(searchedDate, GlobalVariables.DateFormat)
        for event in events:
            if event.Date == date:
                searchedDates.append(event)

        return EventHandler.SortEventsByStartTime(searchedDates)

    def SortEventsByStartTime(events: list[Event]) -> list[Event]:
        return sorted(events, key=lambda e: e.StartTime)
