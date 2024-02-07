from datetime import datetime
from event import Event
from event_handler import EventHandler
from global_variables import GlobalVariables


class EventEditor:
    def HandleEdit(
        EventList: list[Event], eventNumber: int, editMode: str, changes: str
    ) -> list[Event]:
        eventToEdit = EventList.pop(eventNumber)
        match editMode:
            case "1":
                editedEvent = EventEditor.EditStartTime(eventToEdit, changes)
            case "2":
                editedEvent = EventEditor.EditEndTime(eventToEdit, changes)
            case "3":
                editedEvent = EventEditor.EditDate(eventToEdit, changes)
            case "4":
                editedEvent = EventEditor.EditNote(eventToEdit, changes)

        EventList.append(editedEvent)

        return EventHandler.SortEventsByDate(EventList)

    def EditStartTime(eventToEdit: Event, startTime: str) -> Event:
        eventToEdit.StartTime = datetime.strptime(startTime, GlobalVariables.TimeFormat)
        return eventToEdit

    def EditEndTime(eventToEdit: Event, endTime: str) -> Event:
        eventToEdit.EndTime = datetime.strptime(endTime, GlobalVariables.TimeFormat)
        return eventToEdit

    def EditDate(eventToEdit: Event, date: str) -> Event:
        eventToEdit.Date = datetime.strptime(date, GlobalVariables.DateFormat)
        return eventToEdit

    def EditNote(eventToEdit: Event, note: str) -> Event:
        eventToEdit.Text = note
        return eventToEdit
