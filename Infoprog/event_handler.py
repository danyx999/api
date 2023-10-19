from global_variables import GlobalVariables
from event import Event


class EventHandler:
    def CreateEventFromString(event: str):
        eventParts = event.split(f"{GlobalVariables.Separator}")
        return Event(eventParts[0], eventParts[1], eventParts[2], eventParts[3])

    def CreateEventStrToFile(self, events: list[Event]) -> str:
        return "\n".join([event.CreateEventStr() for event in events])

    def CreateEventsFromFile(self, events: str) -> list[Event]:
        return [
            EventHandler.CreateEventFromString(event) for event in events.split("\n")
        ]
