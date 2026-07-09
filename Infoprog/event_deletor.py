from event import Event

class EventDeletor:
    @staticmethod
    def DeleteEvent(events: list[Event], eventNum: int) -> list[Event]:
        events.pop(eventNum)

        return events
